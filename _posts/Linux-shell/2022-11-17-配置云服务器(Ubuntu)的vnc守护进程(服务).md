---
categories: [Linux-Shell]
tags: Ubuntu Server
---

# 写在前面

之前配置过了基于Ubuntu的阿里云服务器, 并且通过vnc远程查看UI界面, 但是美中不足的一点就是每次开启ssh会话都要重新输入`vncserver -kill :1`和`vncserver -geometry 1920x1080 :1`, 很不方便.

查看Google发现有人也遇到了这个问题, 并且给出了创建`systemd`服务的解决方案[^1], 下面来看看这是如何配置和实现的. 

# 方法

>   下面我的操作均在`root`用户下. 所以家目录为`/root`.

## 安装

首先需要安装vnc的服务端, 这里我已经安装过了, 用的是`vnc4server`, (需要通过`aptitude`以及换源安装), 当然如果直接用`apt`的话可以安装`tightvncserver`, 这里就不赘述了. 

可以通过`vncserver`检查一下安装情况, 然后输入密码并确认密码, 之后连接的话需要用到的.

```bash
You will require a password to access your desktops.

Password:
Verify:
```

然后就是配置守护进程了. 在此之前你应该已经开启了对应的端口`5900`以及`5901`, 并打开了对应的防火墙. 具体方法看我之前的文章.

先kill掉进程, 方便后序操作:

```bash
vncserver -kill :1
```



## vnc配置文件

修改一下配置文件, 在此之前先备份:

```bash
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
```

修改

```bash
vi ~/.vnc/xstartup
```

改为:

```bash
#!/bin/sh

export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP="GNOME-Flashback:GNOME"
export XDG_MENU_PREFIX="gnome-flashback-"
gnome-session --session=gnome-flashback-metacity --disable-acceleration-check &
# vncconfig &
```

最后一行据说是开启剪贴板的,但事实上并没有用, 我就注释掉了. 

修改访问权限:

```bash
chmod +x ~/.vnc/xstartup
```

## 服务配置

先创建一个文件:

```bash
cd /etc/systemd/system/
vi vncserver@1.service 
```

写入如下内容:(当然也可以用非root用户, 我这里为省事用`/root`)

```bash
[Unit]
Description=Start VNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=root
WorkingDirectory=/root

PIDFile=/root/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

这里跟[^1]中的内容有出入, 因为里面是访问本地网络中的Ubuntu, 而我们这里需要访问公网IP上的, 就不能加`-localhost`选项, 否则就算创建成功也连不上...(小坑)

简单解释一下就是创建有网络连接时候启动的服务, 启动之前先kill掉打开的vnc进程, 然后开启一个1920x1080的窗口, 最后在服务结束之后kill掉vnc后台服务.

最后就是启动服务并设置开机启动, 三条命令一套完成:

```bash
sudo systemctl daemon-reload
sudo systemctl enable vncserver@1.service
sudo systemctl start vncserver@1
```

看一下状态:

```bash
sudo systemctl status vncserver@1
```

绿点点就对了:

```bash
● vncserver@1.service - Start VNC server at startup
     Loaded: loaded (/etc/systemd/system/vncserver@1.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2022-11-16 19:06:14 CST; 1 day 1h ago
   Main PID: 890 (Xvnc4)
      Tasks: 223 (limit: 4432)
     Memory: 387.7M
     CGroup: /system.slice/system-vncserver.slice/vncserver@1.service
             ├─ 890 Xvnc4 :1 -desktop xxx:1 (root) -auth /root/.Xauthority -geometry 1920x1080 -depth 24 -rfb>
             ├─1174 /usr/libexec/gnome-session-binary --builtin --session=gnome-flashback-metacity --disable-acceleration-check
             ├─1203 dbus-launch --exit-with-session /usr/libexec/gnome-session-binary --builtin --session=gnome-flashback-metacit>
             ├─1211 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --session
             ├─1371 /usr/libexec/gvfsd
             ├─1392 /usr/libexec/gvfsd-fuse /root/.cache/gvfs -f -o big_writes
             ├─1431 /usr/bin/gnome-keyring-daemon --start --components=ssh
             ├─1496 /usr/libexec/gsd-smartcard
             ├─1498 /usr/lib/gnome-flashback/gnome-flashback-clipboard
             ├─1500 /usr/libexec/gsd-housekeeping
             ├─1503 /usr/libexec/gsd-power
             ├─1508 gnome-flashback
```

这样的话不管是重启服务器还是重新开启一个ssh会话, 只要服务器在运行, 就能丝滑连接vnc服务并查看图形化界面, 还是很方便的. 

# ref

[^1]:[How to Install and Configure VNC on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04);