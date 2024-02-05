---
categories: [Linux-Shell]
tags: Tips
---

# 方法

先在mail.qq.com界面找到`设置`, `账户`, 然后开启`IMAP/SMTP`服务, 需要发短信, 然后得到一串密码, 保留. 

进入`http://<公网IP>:10000/settings/user`, 填写QQ邮箱, 一会nextcloud会向这个邮箱发邮件.

然后进入`http://<公网IP>:10000/settings/admin`界面, 设置电子邮件服务器:

| 发送模式   | SMTP          | 加密SSL/TLS    |
| ---------- | ------------- | -------------- |
| 来自地址   | QQ号          | `qq.com`       |
| 认证方法   | 无            | 勾选需要认证   |
| 服务器地址 | `smtp.qq.com` | `465`          |
| 证书       | QQ号          | 刚才复制的密码 |

保存, 测试:

<img src="https://s2.loli.net/2022/12/09/hwO86tiIYsTaSXj.jpg" alt="截屏2022-12-09 16.36.00" style="zoom:50%;" />