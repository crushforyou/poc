## 1. 蓝凌EIS智慧协同平台简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

蓝凌智慧协同平台eis集合了非常丰富的模块，满足组织企业在知识、协同、项目管理系统建设等需求

## 2.漏洞描述

蓝凌智慧协同平台eis集合了非常丰富的模块，满足组织企业在知识、协同、项目管理系统建设等需求。蓝凌EIS智慧协同平台DingUsers.aspx接口存在SQL注入漏洞。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

蓝凌EIS智慧协同平台

![蓝凌EIS智慧协同平台DingUsers.aspx接口存在SQL注入漏洞](%E8%93%9D%E5%87%8CEIS%E6%99%BA%E6%85%A7%E5%8D%8F%E5%90%8C%E5%B9%B3%E5%8F%B0DingUsers.aspx%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.assets/640.png)

## 4.fofa查询语句

body="/sc ripts/jquery.landray.common.js" || body="v11_QRcodeBar clr" || title="智慧协同平台"&& body="欢迎登录智慧协同平台"

## 5.漏洞复现

![105ab4a6405555f55137ab2d64997d56](%E8%93%9D%E5%87%8CEIS%E6%99%BA%E6%85%A7%E5%8D%8F%E5%90%8C%E5%B9%B3%E5%8F%B0DingUsers.aspx%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.assets/105ab4a6405555f55137ab2d64997d56.jpg)