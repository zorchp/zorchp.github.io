---
categories: [Linux-Shell]
tags: Server Ubuntu Wireshark
---

# 写在前面

昨天折腾了一下`透视HTTP协议`这门课的实验环境, 通过阿里云的轻量应用服务器来完成了, 但是还差一步, 那就是wireshark的安装, 虽然通过`apt`安装好了, 但是打不开实在是烦人, 后来经过各种搜索, 我发现问题出在了`tightvnc`上, 这个vnc服务器对qt程序的支持不够好, 那么接下来就来配置一下`tigervnc`, 这里我还用上了xfce4桌面, 感觉比gnome要舒服一些.

>   tigervnc文档感觉不是很全, 但是用起来跟`tightvnc`一样顺手.
>
>   其viewer界面是FLTK开发的, 稍后可以学习一下源码.
>
>   我在Mac端使用了vnc-viewer, 但是不如tigervnc-viewer的给力, vnc-viewer需要一段时间的连接之后才能恢复高画质. 
>
>   不过brew安装的tigervnc-viewer不支持m1, 我在预览版界面[^1]下载的`tigervnc-viewer`的1.13.80版[TigerVNC-1.13.80.dmg (bphinz.com)](http://tigervnc.bphinz.com/nightly/macOS/TigerVNC-1.13.80.dmg)可以在m1Mac上使用. 

[^1]:[tigervnc.bphinz.com/nightly/](http://tigervnc.bphinz.com/nightly/);



# 服务器端的配置

这里的配置也算是一波三折, 一开始我的配置是`tightvnc`+`gnome桌面`, 但是这个组合对于wireshark来说似乎不行, 那么就只能另辟蹊径了, 下面是我的一些参考文章.

>[^2]:[wireshark does not start on TightVNC (headless setup) (#18157) · Issues · Wireshark Foundation / wireshark · GitLab](https://gitlab.com/wireshark/wireshark/-/issues/18157);(指出不要用tightvnc而是使用tigervnc)
>[^3]:[How to Install and Configure VNC on Ubuntu 20.04 | Linuxize](https://linuxize.com/post/how-to-install-and-configure-vnc-on-ubuntu-20-04/);(tigervnc配置)
>[^4]:[解决ubuntu普通用户无权限使用wireshark问题_async7的博客-CSDN博客](https://blog.csdn.net/async7/article/details/104828974);(wireshark的权限问题)
>
>[^5]:[qt - Wireshark crash - Ask Ubuntu](https://askubuntu.com/questions/1026921/wireshark-crash);(wireshark卸载和重装)
>
>

## 第一步:折腾tigervnc

卸载之前的tightvnc:

```bash
sudo apt uninstall tightvnc
```

关闭之前的systemd任务:(如果配置过)

```bash
sudo systemctl stop vncserver@1.service
#修改(如果没有就新建)
sudo vi /etc/systemd/system/vncserver@1.service
```

文件修改为:

```yaml
[Unit]
Description=Start VNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=xxx
WorkingDirectory=/home/xxx/

PIDFile=/home/xxx/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

然后开启一下:

```bash
sudo systemctl daemon-reload
sudo systemctl start vncserver@1
sudo systemctl enable vncserver@1
sudo systemctl status vncserver@1
```

显示:(完美~)

```bash
● vncserver@1.service - Start VNC server at startup
     Loaded: loaded (/etc/systemd/system/vncserver@1.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2023-01-11 23:11:20 CST; 12h ago
   Main PID: 220329 (Xtigervnc)
      Tasks: 147 (limit: 4418)
     Memory: 412.5M
```



用户名(`xxx`)改一下. 

然后安装tigervnc:

```bash
sudo apt install tigervnc-standalone-server
sudo apt install tigervnc-xorg-extension
```

改密码:(密码是六位, 注意之后的是否view-only一定要选`n`)

```bash
vncpasswd
Password:
Verify:
Would you like to enter a view-only password (y/n)? n
```

然后改`~/.vnc/xstartup`配置文件:

```bash
chmod u+x ~/.vnc/xstartup
vi ~/.vnc/xstartup
```

改成:

```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4 
```

改(增加)`~/.vnc/vnc.conf`文件:

>   (用配置文件的好处就是不用每次都更改systemd的配置, systemd还要reload比较麻烦)

```bash
vi ~/.vnc/vnc.conf
#加上:(这里你可以改成自己桌面的分辨率)
$localhost = "no";
$geometry = "1900x1200";
$depth = "24";

1;
```

这上面的选项不知道的话可以通过`vncserver -h`或者`cat /etc/vnc.conf`查看. 



## 第二步: 重新安装wireshark

虽然可能不是必须的, 但是还是重新安装一下保险. (ppa源下载如果比较慢的话可以看我之前的阿里云服务器配置文章, 有加速方法)

```bash
sudo apt-get remove --purge wireshark
sudo apt-get autoremove
sudo apt-get update
sudo apt-get install libcap2-bin wireshark
sudo dpkg-reconfigure wireshark-common#选yes, 使非root用户可以访问
```



更改权限:

```bash
# 创建用户组
sudo groupadd wireshark
# dumpcap加入wireshark用户组
sudo chgrp wireshark /usr/bin/dumpcap
# 增加读写执行权限
sudo chmod 4755 /usr/bin/dumpcap
# 加入用户组
sudo gpasswd -a 你的用户名 wireshark
```

## 第三步: 安装Xfce桌面

安装Xfce桌面:

```bash
sudo apt install xfce4 xfce4-goodies
```





# 演示

用`vnc-viewer`和`tigervnc-viewer`都可以, 可以看到`tigervnc-viewer`还是很丝滑的, 而vnc-viewer就力不从心了(一会才能缓过来):

![截屏2023-01-12 11.09.33](https://s2.loli.net/2023/01/12/6od7eNr8Twx3ulH.jpg)

![截屏2023-01-12 11.10.31](https://s2.loli.net/2023/01/12/ZoFhklOY1fQJI3K.jpg)

然后是wireshark:(这里就用tigervnc了)



![截屏2023-01-12 13.45.27](https://s2.loli.net/2023/01/12/IJlYBf19Ow2Q7EU.jpg)

 相当丝滑.