**漏洞描述**

 泛微e-cology OA action.jsp 存在文件上传漏洞。

**漏洞环境**

Quake语法

```sh
app:"e-office"
```

**漏洞复现**

 构造payload发送请求，获取到响应中的url的值

![图片](%E6%B3%9B%E5%BE%AEe-cology%20OA%20action.jsp%20%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640.png)

拼接请求该url

![图片](%E6%B3%9B%E5%BE%AEe-cology%20OA%20action.jsp%20%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.assets/640-1716346013596-1.png)