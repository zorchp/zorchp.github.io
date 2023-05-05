---
categories: [Python]
tags: Python MacOS Tips
---

# 写在前面

之前写过一篇关于用Charles抓包下载钉钉直播回放视频的方法, 那会还是可以直接通过`FFmpeg`下载`m3u8`链接并且直接合并的, 但是现在直接上`FFmpeg`会出现403, 所以还是用别的方法来做吧. 

后来发现抓包找到的m3u8不是加密视频流, 那就直接下载ts文件然后合并即可. 



# 抓包

## Charles代理



1.   `Proxy -> macOS Proxy` 菜单开启代理

2.   `Proxy -> Proxy Settings` 菜单，对代理进行配置，需要开启 `HTTP` 代理——选择 `Use HTTP proxy`。

3.   安装 Charles 根证书，选择 `Help -> SSL Proxying -> Install Charles Root Certificate` 即可完成安装

     >   未出现可自行打开 Mac 系统自带软件——钥匙串访问  ，如果证书显示不被信任，则双击进行设置，设置为始终信任

4.   设置 SSL 代理，选择 `Proxy -> SSL Proxying Settings` 菜单，出现如下界面后，选中 `Enable SSL Proxying`，然后添加一个代理规则，Host 设置为 `*`，由于是抓取 HTTPS 协议请求，Port 设置为 `443`。

>   之后每次打开Charles抓包都需要开启SSL代理和MacOS系统代理. 
>
>   然后用完之后记得关掉系统代理. 

## 钉钉部分

点击视频, 找到直播回放, 点开, 向后拖拽一下进度条, 然后就可以回到Charles界面查看情况了. 

一般来说就是要找:

```bash
https://dtliving-sz.dingtalk.com
```

开头的网址, 点进去之后有一个m3u8文件, 点`Contents`, 复制全部内容(m3u8实际上是一个文本文件). 

类似下面这样:

```c
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:1
#EXT-X-TARGETDURATION:33
#EXTINF:32.000,
xxx/1.ts?auth_key=xxx
...
```

保存为`aa.m3u8`, 在python脚本的同级目录下. 

# Python脚本



```python
import requests, os, re, time


def crawl(url):
    r = requests.get(url).content
    return r


base_url = "https://dtliving-sz.dingtalk.com/live_hp/"


def get_url():
    url_list = []
    with open("aa.m3u8", "r") as f:
        s = f.readlines()
    for i in s:
        if re.match(r".*?ts.*?", i):
            url_list.append(base_url + i)

    return url_list


def download():
    urls = get_url()
    for i, url in enumerate(urls):
        with open(f"{i + 1}.ts", "wb") as f:
            f.write(crawl(url[:-1]))  # 去掉换行符
        print(i, "ok")
        # time.sleep(1)


# 整合文件名, 方便FFmpeg合并
def parse_filename():
    base_path = os.getcwd()
    urls = get_url()
    with open("file.txt", "w+") as f:
        for i in range(1, 1 + len(urls)):
            path = f"file '{base_path}/{i}.ts'\n"
            print(path)
            f.write(path)


if __name__ == "__main__":
    download()
    print("download finished...")
    parse_filename()
```



# FFmpeg合并

```bash
ffmpeg -f concat -safe 0 -i file.txt -c copy a.mp4
```

如果下载的可执行文件, 还需要使用`./`前缀来执行, 如果提示需要移至废纸篓, 那就去`安全性与隐私`那里点击仍要打开. 

可以写在一个Python脚本中:

```python
import requests, os, re, time


def crawl(url):
    r = requests.get(url).content
    return r


base_url = "https://dtliving-sz.dingtalk.com/live_hp/"


def get_url():
    url_list = []
    with open("aa.m3u8", "r") as f:
        s = f.readlines()
    for i in s:
        if re.match(r".*?ts.*?", i):
            url_list.append(base_url + i)

    return url_list


def output_url():
    base_url = "https://dtliving-sz.dingtalk.com/live_hp/"

    url_lst = get_url()
    with open("urls.txt", "w+") as f:
        for i, itm in enumerate(url_lst):
            url = base_url + itm
            print(i, url)
            f.write(url)


def download():
    urls = get_url()
    for i, url in enumerate(urls):
        with open(f"{i+1}.ts", "wb") as f:
            f.write(crawl(url[:-1]))
        print(i, "ok")
        # time.sleep(1)


def parse_filename():
    base_path = os.getcwd()
    with open("file.txt", "w+") as f:
        for i in range(1, 10):
            path = f"file '{base_path}/{i}.ts'\n"
            print(path)
            f.write(path)


def merge_ts(video_name):
    cmd = f"./ffmpeg -f concat -safe 0 -i file.txt -c copy {video_name}.mp4"
    os.system(cmd)


if __name__ == "__main__":
    download()
    print("download success!")
    print()
    parse_filename()
    merge_ts("a")
    print("merge success!")
    os.remove("file.txt")
```



# 结语

一开始使用`requests`怎么也下不下来, 反而一句`curl`就搞定了, 我还以为是Python的requests有某些限制, 后来才发现原来是行尾的换行符导致url解析出问题了... 还是要细心啊. 

>   视频加密技术在不断更新, 解密技术也在不断提高, 真的是道高一尺魔高一丈啊. 技术也正是这样一点点发展起来的. 