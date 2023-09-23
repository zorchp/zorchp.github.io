---
categories: [Tips]
tags: MacOS Linux Server
---

# 写在前面

前几天写了写通过mac远控Windows的一些方法, 下面来看看如何通过frp内网穿透的方法远控mac端, 这里给出通过安卓远控和Windows远控mac两种方式, 加上一些之前内容的补充, 包括一种新的方法给出Windows和服务器端部署开机启动守护进程的方法(Linux通过systemctl, Windows通过开机启动项), 主要参考了[^1].

# 服务器

## 开端口

```bash
addtcp 5900
addtcp 5902
reufw
```

对应管理界面开一下. 

## 开机启动守护进程配置

首先是创建一个文件` vi /lib/systemd/system/frps.service`, 编辑以下内容:

```yaml
[Unit]
Description=Frps
After=syslog.target
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/frps
ExecStart=/opt/frps/frps -c /opt/frps/frps.ini
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

这里主要需要修改的就是`[Service]`项的`WorkingDirectory`以及`ExecStart`键, 其他部分保持不动. 

之前我的配置是通过重定向操作符的方式写入log日志, 不过在`frps.ini`的配置文件里面有一个`log_file`键, 下面更新一下我的`frps.ini`配置:

```ini
[common]
bind_port = 7000
# kcp_bind_port = 7000
dashboard_port = 7500
log_file = /opt/frps/frps.log
# dashboard's username and password are both optional，if not set, default is admin.
dashboard_user = admin
dashboard_pwd = admin
```

对于kcp, 好像因为GFW的原因会导致问题, 所以这里注释掉也无妨. 

然后重载配置, 开启开机启动, 开启服务:

```bash
sudo systemctl daemon-reload       # 重新加载配置
sudo systemctl enable frps.service # 启用 frps 开机启动
sudo systemctl start frps.service  # 启动 frps 服务
systemctl status frps.service      # 查看 frps 服务状态
```

最后状态如下:

```bash
● frps.service - Frps
     Loaded: loaded (/lib/systemd/system/frps.service; enabled; vendor preset: >
     Active: active (running) since Fri 2022-11-11 22:58:05 CST; 2 days ago
   Main PID: 746 (frps)
      Tasks: 5 (limit: 4432)
     Memory: 19.2M
     CGroup: /system.slice/frps.service
             └─746 /opt/frps/frps -c /opt/frps/frps.ini
```

# Mac被控端的配置

这里我的Mac测试系统为`12.6`, m1, 其他系统版本应该也是大同小异的. 

## 基本配置

打开系统偏好设置->共享, 勾选`远程登录`, `远程管理`, 两个界面中的`允许访问`均设置为`所有用户`, 在`远程管理`中有一个`电脑设置`, 这里可选择`vnc`登录时候的密码, 如果设置了, 稍后在远控端就会要求输入设置好的该密码. 

## frpc客户端

```bash
brew install frpc
```

我这里因为是arm, 安装完`frpc`之后路径在`/opt/homebrew/bin`目录下, 这路径稍后会用到. 

默认的配置文件路径在`/opt/homebrew/etc/frp/frpc.ini`, 这个也要用. 

## 配置开机启动项

这里介绍一种新方法, 直接通过`brew services start frpc`即可. 服务管理比较方便, 至于下面的方法仅供参考. 

---



编辑一下`.plist`文件, 其实就是一个xml文件(不知道为什么要用这么反人类的配置)

编辑一下文件`vim ~/Library/LaunchAgents/frpc.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN
http://www.apple.com/DTDs/PropertyList-1.0.dtd >
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>frpc</string>
    <key>ProgramArguments</key>
    <array>
     <string>/opt/homebrew/bin/frpc</string>
         <string>-c</string>
     <string>/opt/homebrew/etc/frp/frpc.ini</string>
    </array>
    <key>KeepAlive</key>
    <true/>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

这里的10行11行和12行就是需要修改的, 改成自己的安装路径. 

其中的`frpc.ini`文件如下:

```ini
[common]
server_addr = <公网IP>
server_port = 7000
; protocol = kcp
log_file = /opt/homebrew/etc/frp/frpc.log

[vnc]
type = tcp
local_ip = 127.0.0.1
local_port = 5900
remote_port = 5902
use_encryption = true
use_compression = true

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
use_encryption = true
use_compression = true

```

下面的vnc是远程桌面需要用到的, ssh是远程会话用到的. 这里要注意mac的防火墙要关闭, 或者只开启指定端口, 这里我直接关闭了(在安全性与隐私那块设置)

最后加载一下使其生效:

```bash
sudo chown root ~/Library/LaunchAgents/frpc.plist
sudo launchctl load -w ~/Library/LaunchAgents/frpc.plist
```

看看是否启动了:

```bash
 ==> ps aux|grep frpc
root             58412   0.0  0.1 409236512  11104   ??  Ss   五03下午   0:11.75 /opt/homebrew/bin/frpc -c /opt/homebrew/etc/frp/frpc.ini
xxx              53991   0.0  0.0 408637584   1808 s000  S+    4:28下午   0:00.00 grep frpc
```



# 安卓/Windows远控端

这个配置比较简单了, 说起来也就是如何使用vnc-viewer这个软件了. 之前我讲了在mac的vnc-viewer上面的使用方法, 安卓端基本一致, 记得前面mac上设置的vnc密码即可. 

>   软件在国内的应用市场应该是没有的, 我在play商店下载的, 有需要的朋友可以私信我获取. 



# 小结

最后完成了上述的所有配置, 就可以愉快地实现设备互联了, 通过一台云服务器就可以完成所有的这些事情, 还是很棒的, 后来我发现在Windows上作为被控端其`frpc`程序总是失效, win10一开始通过cmd的`上次create`的方式, 也还是不行, Win11通过启动项设置:`shell:startup`内的快捷方式倒是可以正常使用, 但是在win10上不行, 由于Windows不作为主力机使用了, 这里我就不详述了. 

此外, 还有一些问题, 例如:

1.   在mac上设置了键映射为`CapsLock->Ctrl`, 但是在通过远控之后, 快捷键就失效了. 
2.   流畅度还可以, 但是通过安卓端的vnc-viewer查看mac桌面时候会出现锯齿形方块.

但是瑕不掩瑜, 这个方法仍然是要比之前的远控软件todesk好, 没有登陆限制, 不会出现信息泄露等情况. 

# ref

[^1]:[macos - 通过 FRP 内网穿透并实现 VNC 远程访问 Mac 桌面_个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000021724321);