---
categories: [Linux-Shell]
tags: Ubuntu Server Linux
---

# 写在前面

最近迷恋上了云服务器的配置, 感觉云服务器能做的事情太多了, 不管是docker还是直接部署, 都是相当方便快捷的, 下面来看看在阿里云服务器配置nextcloud网盘的基本配置方法, 这里参考了一篇文章[^1], 写的相当详细了, 我这里只是做一些补充. 

# 配置前的准备

## 服务器端

### 开端口

阿里云防火墙开启:`10000`, 然后在服务器终端:

```bash
addtcp 10000
reufw
```

>   快捷命令`alias`设置可以看我的leanote那篇博客.

### docker-compose安装

基于Python:(容易)

```bash
sudo pip3 install docker-compose -i https://pypi.mirrors.ustc.edu.cn/simple/
```

效果:

```bash
docker-compose version
docker-compose version 1.29.2, build unknown
docker-py version: <module 'docker.version' from '/usr/local/lib/python3.8/dist-packages/docker/version.py'>
CPython version: 3.8.2
OpenSSL version: OpenSSL 1.1.1f  31 Mar 2020
```



基于命令行(可能需要代理)[^2], 这个是v2, 通过go重新编写.

```bash
ARCH=$(uname -m) && [[ "${ARCH}" == "armv7l" ]] && ARCH="armv7"
sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-${ARCH}" -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```

效果:

```bash
$ docker compose version
Docker Compose version v2.11.2
```

### 新建一些目录

```bash
cd /home/xxx
mkdir docker-compose
mkdir -p /opt/nextcloud
```

### 拉取一些`docker`镜像:

>   会比较慢, 耐心等待, 换源的效果也不明显

```bash
docker pull redis
docker pull mariadb:10.5
docker pull nextcloud
```



## 客户端

play商店搜索nextcloud, 安装. 我上传了一份[nextcloud.apk-Android文档类资源-CSDN文库](https://download.csdn.net/download/qq_41437512/87088923).

Mac:

```bash
brew install nextcloud
```



# 配置

## 服务器端

```bash
cd /home/xxx/docker-compose
vi docker-compose.yaml
```

写入下面的内容:

```yaml
version: '2'

services:
  app:
    container_name: nextcloud_app
    image: nextcloud
    restart: always
    ports:
      - 10000:80
    environment:
      - DATABASE_URL=mysql+pymysql://nextcloud:nextcloud@db/nextcloud
#      - MYSQL_PASSWORD=lyes
#      - MYSQL_DATABASE=nextcloud
#      - MYSQL_USER=nextcloud
#      - MYSQL_HOST=db
      - REDIS_URL=redis://redis:6379
    volumes:
      - /opt/nextcloud/www:/var/www/html
    depends_on:
      - db
      - redis
    networks:
        default:
        internal:

  db:
    container_name: nextcloud_db
    image: mariadb:10.5
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=nextcloud
      - MYSQL_DATABASE=nextcloud
    volumes:
      - /opt/nextcloud/db:/var/lib/mysql
    networks:
        internal:
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW

  redis:
    container_name: nextcloud_redis
    image: redis
    volumes:
      - /opt/nextcloud/redis/data:/data
      - /opt/nextcloud/redis/redis.conf:/etc/redis/redis.conf
    restart: always
    networks:
        internal:
    command: redis-server /etc/redis/redis.conf --appendonly yes

networks:
    default:
    internal:
        internal: true
```

然后启动即可:

```bash
# 以后台方式启动
sudo docker-compose up -d
```



## web端

先进入:

```bash
http://<公网IP>:10000
```

需要修改用户名密码, 以及下面的mariadb数据库的用户名, 密码, 数据库名, 数据库主机名, 这里写成:

```bash
nextcloud
nextcloud
nextcloud
db
```

## Redis缓存

直接使用的话速度比较慢, 这时候可以加上Redis缓存提高速度.

```bash
vi /opt/nextcloud/www/config/config.php
```

到文件倒数第二行, `);`之前, 然后加上:

```php
  'memcache.local' => '\OC\Memcache\Redis',
  'memcache.distributed' => '\OC\Memcache\Redis',
  'memcache.locking' => '\OC\Memcache\Redis',
  'redis' => array(
    'host' => 'redis',
    'port' => 6379,
    'password' => ''
  ),
```



# 后续..

如果nextcloud官方更新了镜像, 可以用下面的命令来更新我们服务器部署的nextcloud:(前提是在你的`docker-compose.yaml`路径下执行)

```bash
sudo docker pull nextcloud

sudo docker-compose down && docker-compose up -d
```

mac端展示:

<img src="https://s2.loli.net/2022/11/19/HiT6AoQzpD8JSxL.jpg" alt="截屏2022-11-19 20.38.38" style="zoom:43%;" />

# ref

[^1]:[Docker部署个人网盘NextCloud - 良月二十's Blog (lyes.host)](https://lyes.host/post/docker部署个人网盘nextcloud/);
[^2]:[Docker Compose - LinuxServer.io](https://docs.linuxserver.io/general/docker-compose#install-option-1-recommended);