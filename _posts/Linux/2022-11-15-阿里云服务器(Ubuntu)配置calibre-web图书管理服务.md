---
categories: [Linux-Shell]
tags: Leanote Server Tips
---

# 写在前面

这次来配置一个基于calibre电子书管理软件web镜像的电子图书馆, 因为自己本地的电子书太多了, 各个文件夹都有, 显得比较乱糟糟, 有了calibre-web, 这个问题就可以解决了, 主要参考了[^1].

# 预备知识

配置Linux server, 现在已经是轻车熟路了, 但是这次配置的calibre需要一个新的内容, docker. 之前虽然接触过一些, 但是还是不够熟悉, 下面的一步步配置也算是对docker基本命令做一个总结了.

>   docker 安装参考[^5].

先pull一下镜像, 稍后会用到.

```bash
docker pull linuxserver/calibre-web
```



# 服务器配置

## 端口配置

管理界面开启8083/TCP.

参考之前我设置的快捷命令, 直接一步到位:

```bash
addtcp 8083
reufw
```



## 映射目录

```bash
# 存放书
mkdir -p /data/calibre/books
# 配置
mkdir -p /data/calibre/config
```



## 上传calibre数据库文件

将本地主机上的calibre数据库文件`/Users/xxx/Calibre\ 书库/metadata.db`, 上传到Ubuntu服务器, 这里用到了`scp`命令:

```bash
scp ~/Calibre\ 书库/metadata.db root@<公网IP>:/data/caliber/books/
```

然后在Ubuntu的`/data/caliber/books`目录下就有了一个数据库文件

>   数据库可以为空, 即不记录任何书, 后期直接上传即可.

改一下权限:(不然传不上去)

```bash
chmod 777 /data/calibre/*
```

这样的话之后你上传的所有的书都会存放在这个目录的`books/`子目录下.



## docker配置

这里还是比较简单的, 先创建镜像[^2]:

```bash
docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Shanghai \
  -p 8083:8083 \
  -v /data/calibre/books:/books \
  -v /data/calibre/config:/config \
  --restart unless-stopped \
  linuxserver/calibre-web
```

其中:

1.   第一行是用docker的run命令(通过`-d`选项开启后台守护态运行)运行容器.
2.   指定别名.
3.   为容器分配的用户ID
4.   为容器分配的组ID
5.   时区设置
6.   端口转发规则: `外部(主机):内部(容器)`, 之后访问`http://公网IP:8083`时候就可以访问到镜像.
7.   配置路径映射: books存放数据库和书, `外部(服务器主机):内部(容器)`格式.
8.   配置路径映射: config存放配置信息.
9.   重启规则.
10.   所用镜像的名称.

>   不过这样不好改, 还是用docker-compose的yaml配置文件好一些.

查看一下状态:

```bash
$ docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS          PORTS                                       NAMES
c9bcaf90acbb   linuxserver/calibre-web     "/init"                  16 seconds ago   Up 15 seconds   0.0.0.0:8083->8083/tcp, :::8083->8083/tcp   calibre-web
```

这些搞定了之后, 不要着急打开浏览器, 先输入:

```bash
docker logs calibre-web
```

查看一下配置的情况, 如果出现了下面的字样才算是成功配置了:(主要是最后一行)

```lua
[custom-init] No custom services found, skipping...
[migrations] started
[migrations] no migrations found

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[custom-init] No custom files found, skipping...
[ls.io-init] done.
```



## web端配置

输入`<公网IP>:8083`进入webUI, 其中

```bash
用户名:admin
密 码:admin123
```

改一下密码和UI语言(中文)(admin's profile), 以及上传设置(管理权限->编辑基本配置->基本配置->启动上传->保存). 



# 一些可能的问题与解决

## 权限问题

```bash
chmod 777 /data/calibre/books/*
chmod 777 /data/calibre/config/*
```

然后

```bash
docker restart calibre-web
```



## 忘记密码怎么办

邮箱并不会给你发密码, 考虑issue的办法:[^4].

```bash
docker exec -it calibre-web bash
cd /app/calibre-web
python3 cps.py -s admin:admin123
# Password for user 'admin' changed
```



# 小坑

文章[^1]里面说的内容我配置过, 但是成功率很低.. 

至于原因, 一开始我以为是IPv4端口转发没开, 但是事实是阿里云是默认开启的, 并不需要去自己设置. 而且`docker ps`也显示我启动了这个容器.. 后来发现光看`docker ps`并不科学, 因为真正的创建情况不会显示在`docker ps`里面, 这只是一个容器的状态, 至于端口, 容器初始化等情况, 并没有任何提示, 于是才需要用`docker logs calibre-web`看具体的情况.

后来我发现, 应该是镜像里面用到了GitHub 的一些仓库, 然而这些仓库访问特别慢, 需要等很久才能创建成功, 不建议使用, 而且其中提到的[technosoft2000/calibre-web - Docker Image | Docker Hub](https://hub.docker.com/r/technosoft2000/calibre-web)镜像已经一年不更新了, 这里还是推荐用最新的`Linuxserver`下的镜像[^2], 虽然少了电子书转换等功能, 但是不影响基本使用, 可以在之后自行配置服务. 

# ref

[^1]:[【玩转腾讯云】使用轻量应用服务器和calibre-web搭建个人在线图书馆 - 腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1814658);

[^2]:[linuxserver/calibre-web - Docker Image | Docker Hub](https://hub.docker.com/r/linuxserver/calibre-web);

[^3]:[linuxserver/calibre-web - LinuxServer.io](https://docs.linuxserver.io/images/docker-calibre-web);

[^4]:[如何重置密码 ·问题 #750 ·janeczku/calibre-web (github.com)](https://github.com/janeczku/calibre-web/issues/750#issuecomment-950041019);
[^5]:[Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/);