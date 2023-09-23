---
categories: [Linux-Shell]
tags: Leanote Server Tips
---

# 写在前面

有了服务器, 能做的事情就相当多了, 话不多说, 配置一个云笔记应用先. 检索一遍之后, 发现现在主流的云笔记定制是通过一个叫leanote(中文:蚂蚁笔记)的程序完成的, 虽然要花钱, 但那是对用他们公式的服务器来说的, 自己配置的话不花钱可定制性还特别高, 下面来看看. 服务器配置部分参考[^1],[^2].

# 配置前的准备

## 客户端

mac或安卓端安装一下leanote客户端, 之后要用.

```bash
brew install leanote --cask
```

安卓的话客户端直接在[官方GitHub](https://github.com/leanote/leanote-android/releases)下载. 

>   其实直接在浏览器访问也可以, 但是总觉得应该有一个客户端方便一些.

## 服务器端

服务器端需要通过wget下载, 但是太慢了(因为代理出了一些问题), 这里我先下载到本地, 然后通过`scp`命令上传到Ubuntu服务器端. 

在服务器端我还是将其放在了`/opt/leanote/`目录下, 命令如下:

```bash
# 在物理机:
scp ~/Downloads/leanote-linux-amd64-v2.6.1.bin.tar.gz root@<公网IP>:/opt
# 在服务器:
cd /opt
tar zxvf leanote-linux-amd64-v2.6.1.bin.tar.gz
cd leanote
ls
app  bin  conf  messages  mongodb_backup  public
```

接下来安装一下非关系型数据库MongoDB:

```bash
sudo apt-get install mongodb
```

新建默认的文件夹为数据库位置:

```bash
mkdir -p /data/db
```

开启服务

```bash
sudo systemctl enable mongodb
sudo systemctl start mongodb
sudo systemctl status mongodb
```

状态:

```bash
● mongodb.service - An object/document-oriented database
     Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-11-14 21:38:44 CST; 9min ago
       Docs: man:mongod(1)
   Main PID: 39145 (mongod)
      Tasks: 24 (limit: 4432)
     Memory: 146.9M
     CGroup: /system.slice/mongodb.service
             └─39145 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc/mongodb.conf
```

可以看到配置文件的位置为`/etc/mongodb.conf`, 这个文件之后要更改一下, 加入权限.

# 配置服务器端

## 端口

因为经常需要操作开启和关闭端口, 这里我配置了防火墙端口开放的快捷指令:

```bash
alias addtcp='func_tcp() { firewall-cmd --zone=public --add-port=$1/tcp --permanent && iptables -I INPUT -ptcp --dport $1 -j ACCEPT; };func_tcp'

alias addudp='func_udp() { firewall-cmd --zone=public --add-port=$1/udp --permanent && iptables -I INPUT -pudp --dport $1 -j ACCEPT; };func_udp'

alias reufw="firewall-cmd --reload"

alias port_status='func_port_status() { sudo netstat -tunlp | grep $1 && sudo iptables -L -n --line-numbers | grep $1; }; func_port_status'
```

这样的话需要开启8000端口的TCP访问就直接`addtcp 8000`, 然后`reufw`即可. 

查看端口的开放情况也类似, 例如我这里想查看9000端口的情况:

```bash
$ port_status 9000
tcp6       0      0 :::9000                 :::*                    LISTEN      33083/leanote-linux
12   ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:9000 ctstate NEW,UNTRACKED
```

上面算是一个题外话, 下面步入正题. 

先进入阿里云后台管理界面, 开启端口9000, 然后用上面的命令开启防火墙的TCP/9000端口, 操作完成后进入leanote文件夹. 

## MongoDB数据库的配置

导入初始数据:(路径记得改)

```bash
mongorestore -h localhost -d leanote --dir /opt/leanote/mongodb_backup/leanote_install_data/
```

需要调整一下数据库的内容, 为`leanote`这个数据库配置一下管理员的用户名以及密码[^3], 因为默认的MongoDB安装之后没有用户名密码机制, 不太安全.

首先查看一下MongoDB的版本, `mongo --version`, 显示:

```bash
MongoDB shell version v3.6.8
git version: 8e540c0b6db93ce994cc548f000900bdc740f80a
OpenSSL version: OpenSSL 1.1.1f  31 Mar 2020
allocator: tcmalloc
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64
```

是V3, 那么就通过下面的命令插入用户名以及密码信息:

```sql
# 首先切换到leanote数据库下
> use leanote;
# 添加一个用户root, 密码是abc123
> db.createUser({
    user: 'root',
    pwd: 'abc123',
    roles: [{role: 'dbOwner', db: 'leanote'}]
});
# 测试下是否正确
> db.auth("root", "abc123");
1 # 返回1表示正确
```

用户添加好后, 开启权限验证, 将上面提到的配置文件`/etc/mongodb.conf`中的`auth = true`解注释.

然后重新运行下`mongod`, 如下:

```bash
sudo systemctl restart mongodb
```

>   在mongod的终端按ctrl+c即可退出mongodb.

## leanote配置

`vi /opt/leanote/conf/app.conf`, 然后修改:

```bash
# You Must Change It !! About Security!!
app.secret=xxx
```

在上面还有一条配置为:

```bash
site.url=http://localhost:9000 # or http://x.com:8080, http://www.xx.com:9000
```

这里修改成你的公网IP也可以. 

之后就是数据库的用户名密码:

```bash
db.username=root # if not exists, please leave it blank
db.password=abc123 # if not exists, please leave it blank
```

这时候当你要访问MongoDB数据库, 就需要通过下面的命令来完成:

```bash
mongo -u root -p abc123 --authenticationDatabase leanote
```

否则会报错.

## 配置守护进程

因为在退出终端会话之后进程资源会被回收, 我们将不能通过公网IP访问云笔记, 那么就需要创建一个守护进程(daemon), 在关闭终端之后还能访问该服务, 下面用`systemd`方法来完成守护进程的创建.

```bash
chmod +x /opt/leanote/bin/run.sh
vi /lib/systemd/system/leanote.service
```

写入:

```bash
[Unit]
Description=Leanote
After=syslog.target
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/leanote
ExecStart=/opt/leanote/bin/run.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

最后:

```bash
systemctl daemon-reload 
systemctl start leanote.service 
systemctl enable leanote.service
```

得到:

```bash
Created symlink /etc/systemd/system/multi-user.target.wants/leanote.service → /lib/systemd/system/leanote.service.
```

然后查看状态:

```bash
systemctl status leanote.service 
```

```bash
● leanote.service - Leanote
     Loaded: loaded (/lib/systemd/system/leanote.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-11-27 15:47:10 CST; 22s ago
   Main PID: 2434 (run.sh)
      Tasks: 7 (limit: 4431)
     Memory: 8.3M
     CGroup: /system.slice/leanote.service
             ├─2434 /bin/sh /opt/leanote/bin/run.sh
             └─2440 /opt/leanote/bin/leanote-linux-amd64 -importPath github.com/leanote/leanote
```



查看一下执行情况:

```bash
ps aux |grep leanote
root       33069  0.0  0.0   9572  3256 ?        Ss   10:32   0:00 /usr/bin/bash /opt/leanote/bin/run.sh
root       33083  0.0  0.4  27528 18876 ?        Sl   10:32   0:05 /opt/leanote/bin/leanote-linux-amd64 -importPath github.com/leanote/leanote
root       37336  0.0  0.0   9032   656 pts/1    S+   20:01   0:00 grep --color=auto leanote
```

## 修改网页显示(optional)

这个部分不是非要去改的, 但是毕竟是自用, 注册这个选项也确实不再需要了, 这部分内容也参考了[^1].

```bash
vi /opt/leanote/app/views/home/index.html
# 注释掉下面一行
!<-- <a class="btn btn-default btn-primary" href="/register">{% raw  %}{{msg . "register"}}{% endraw  %}</a> -->
```

然后:

```bash
vi /opt/leanote/app/views/home/login.html
# 注释
<!--
{% raw  %}
<p class="text-muted text-center"><small>{{msg . "hasAcount"}}</small></p>
{{if .openRegister}}
         <a href="/register" class="btn btn-default btn-block">{{msg . "register"}}</a>
         {{msg . "or"}}
 {{end}}
 {% endraw  %}
 -->

```

最后:

```bash
cd /opt/leanote/app/views/home/
mv  register.html register_close.html
```

这样就没有`注册`了.

到这里, 恭喜你, 关于服务器端的配置就告一段落了. 下面在客户端上看看效果.

# 客户端

这里先以网页版为主, 应用程序使用起来跟网页都是一样的.

-   修改一下admin的密码, 在`个人中心`->`账户信息`->`密码` 处进行修改.
-   更改一下头像等信息(optional).

一个示例:

<img src="https://s2.loli.net/2022/11/15/t9PWjJxmsl7X6FU.jpg" style="zoom:40%;" />

# ref

[^1]:[ubuntu20.04蚂蚁笔记(leanote)的使用_yaoyaohyl的博客-CSDN博客_leanote ubuntu](https://blog.csdn.net/yaoyaohyl/article/details/113934344);
[^2]:[Home · leanote/leanote Wiki (github.com)](https://github.com/leanote/leanote/wiki);
[^3]:[QA · leanote/leanote Wiki (github.com)](https://github.com/leanote/leanote/wiki/QA#为mongodb数据库添加用户);
