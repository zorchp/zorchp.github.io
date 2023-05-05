---
categories: [Tips]
tags: Ubuntu Network
---

# 写在前面

最近看看罗剑锋老师的`透视HTTP协议`, 折腾一下实验环境.

本来是想用mac(arm)来做的, 无奈Openresty的一个lua扩展不给力, 本地编译之后依然不行(表现为服务器错误), 所以就只能借助Intel了, 当然老师也提供了一种思路: 借助dockerfile构建基于arm的镜像实验环境(实在是因为我电脑内存不行, 不然高低折腾一下). 

---

那么下面就开始在阿里云服务器(Ubuntu x86_64)上构建实验环境了.

主要用到的就是:

```lua
Openresty (安装起来比较麻烦, 需要源码编译)
telnet (apt安装即可)
Firefox(或者chromium, Chrome, edge) apt安装
wireshark (apt安装, 但是打不开, 可能是远程的原因)
```



# 准备工作

用于源码构建Openresty:

```bash
sudo apt-get install libpcre3-dev \
    libssl-dev perl make build-essential curl
```

安装Firefox和wireshark[^2]:

```bash
sudo apt install firefox

sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
```





# 安装Openresty

这个算是老大难问题, 放在最后. 参考了[^1],官方的源码构建方法, 这里我比较推荐源码安装, 顺便学一下项目构建方法了.

>   构建的配置参数部分, 参考[^3].
>
>   This module is not built by default, it should be enabled with the `--with-http_v2_module` configuration parameter.

```bash
wget https://openresty.org/download/openresty-1.21.4.1.tar.gz
tar -xvf openresty-1.21.4.1.tar.gz
cd openresty-1.21.4.1/
# 配置信息, 后面的参数一定要加, 不然之后会报错
./configure -j2 --with-http_v2_module
# 编译和链接
make -j2
# 安装
sudo make install
```

添加环境变量:

```bash
vi ~/.bashrc

# 添加:
export PATH=/usr/local/openresty/bin:/usr/local/openresty/nginx/sbin:$PATH

# 然后
source ~/.bashrc
```

查看版本:

```bash
$ resty -V
resty 0.28
nginx version: openresty/1.21.4.1
built by gcc 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)
built with OpenSSL 1.1.1f  31 Mar 2020
TLS SNI support enabled
configure arguments: --prefix=/usr/local/openresty/nginx --with-cc-opt=-O2 --add-module=../ngx_devel_kit-0.3.1 --add-module=../echo-nginx-module-0.62 --add-module=../xss-nginx-module-0.06 --add-module=../ngx_coolkit-0.2 --add-module=../set-misc-nginx-module-0.33 --add-module=../form-input-nginx-module-0.12 --add-module=../encrypted-session-nginx-module-0.09 --add-module=../srcache-nginx-module-0.32 --add-module=../ngx_lua-0.10.21 --add-module=../ngx_lua_upstream-0.07 --add-module=../headers-more-nginx-module-0.33 --add-module=../array-var-nginx-module-0.05 --add-module=../memc-nginx-module-0.19 --add-module=../redis2-nginx-module-0.15 --add-module=../redis-nginx-module-0.3.9 --add-module=../rds-json-nginx-module-0.15 --add-module=../rds-csv-nginx-module-0.09 --add-module=../ngx_stream_lua-0.0.11 --with-ld-opt=-Wl,-rpath,/usr/local/openresty/luajit/lib --with-http_v2_module --with-stream --with-stream_ssl_module --with-stream_ssl_preread_module --with-http_ssl_module
```



# 测试

```bash
~/code/http_study/www$ ./run.sh start
~/code/http_study/www$ ./run.sh list
root      125555       1  0 Jan10 ?        00:00:00 nginx: master process /usr/local/openresty/bin/openresty -c conf/nginx.conf -p /home/zorch/code/http_study/www
nobody    125556  125555  0 Jan10 ?        00:00:00 nginx: worker process
nobody    125557  125555  0 Jan10 ?        00:00:00 nginx: cache manager process
```

完美, 接下来是telnet测试:

在这之前先添加一下`hosts`, 使用:

```bash
sudo vi /etc/hosts

#添加:
127.0.0.1       www.chrono.com
127.0.0.1   	www.metroid.net
127.0.0.1   	origin.io
```

然后就可以测试了:

```bash
~/code/http_study/www$ telnet www.chrono.com 80
Trying 127.0.0.1...
Connected to www.chrono.com.
Escape character is '^]'.
GET /10-1 HTTP/1.1
Host: www.chrono.com

HTTP/1.1 200 OK
Server: openresty/1.21.4.1
Date: Wed, 11 Jan 2023 10:49:39 GMT
Content-Type: text/plain
Connection: keep-alive
content-length: 19

10-1 GET&HEAD test
```

完美~

# ref

[^1]:[OpenResty - Installation](https://openresty.org/en/installation.html#building-from-source);

[^2]:[How to Install and Use Wireshark on Ubuntu Linux? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-install-and-use-wireshark-on-ubuntu-linux/);

[^3]:[Module ngx_http_v2_module (nginx.org)](http://nginx.org/en/docs/http/ngx_http_v2_module.html);