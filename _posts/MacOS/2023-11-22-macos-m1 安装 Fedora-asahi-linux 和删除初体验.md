---

---

# 写在前面



# 安装

```bash
curl https://fedora-asahi-remix.org/install | sh
```

按照流程一步一步来就行, 最后分区也是通过指导程序完成的, 基本上都是属于比较傻瓜的操作. 

不过全英文还是有点不太舒服, 需要字斟句酌. 

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/macos-asahi-fedora-install-steps.jpg" alt="asahi" style="zoom:50%;" />

# 体验

就是Linux 的味道, 开机之后打开的就是 Linux 桌面, 我安装的是 kde 桌面, 但是不想花时间折腾了, 并且安装一个输入法都要折腾好久, 感觉太浪费时间. 

直接 MacOS 或者直接 Linux 命令行界面他不香吗?

>   跑分也没测试, 理论上来说 Linux 肯定要更快吧, 因为没有夹带私货(不像 Mac 和 win 那样需要很大一部分空间来运行自己的系统)

# 卸载

>   [[M1运行Linux\][全网首发]卸载来啦 M1卸载Asahi Linux教程 手把手教你卸载_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV173411H7ja/?vd_source=0c1bebd4c4b9a0a90051ca715b0b2491);

先从终端里面查看一下磁盘挂载点情况:

```bash
diskutil list
```

然后在磁盘实用工具中删除一个大约500MB 的分区, 我这里没有执行参考视频中的其他操作, 抹去并合并那个 Linux 的引导分区就可以了, 可能因为不是纯的 asahi-Linux 吧..