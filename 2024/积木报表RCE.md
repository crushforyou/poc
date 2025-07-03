1、漏洞描述

此接口为积木报表组件自带接口，该接口正常访问会提示没有权限，利用jmLink=YWFhfHxiYmI=可以绕过权限校验。在绕过权限校验后，可在请求体中注入内存马，以获取服务器权限。

2、漏洞路径

/jeecg-boot/jmreport/save?previousPage=xxx&jmLink=YWFhfHxiYmI=