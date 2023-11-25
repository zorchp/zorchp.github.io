---

---



下面演示禁用自动升级的正确姿势。首先关闭Chrome浏览器，然后进入目录“/Library/Google/GoogleSoftwareUpdate”

cd /Library/Google/GoogleSoftwareUpdate

然后删除该目录下的GoogleSoftwareUpdate.bundle即可



-   正确姿势二

可能在有些Mac上发现在“/Library”这个根目录下没有Google目录，那么其实在“~/Library”这个用户目录下也有一个Google目录。在该目录下执行操作同样可以禁用自动更新。请执行以下命令：

cd ~/Library/Google

sudo chown root:wheel GoogleSoftwareUpdate

相当于修改了GoogleSoftwareUpdate这个文件夹的拥有者，而不仅仅是修改了权限，使Google对该文件夹没有写入权限。事实证明这种方式是可行的。重启Chrome完成以后通过“帮助->关于Google Chrome”可以查看结果

>   参考:
>
>   [Mac Chrome浏览器取消自动升级（看这一篇就够了）_mac google浏览器如何关闭更新提示-CSDN博客](https://blog.csdn.net/CHENYUFENG1991/article/details/78568919);



并且因为 Microsoft edge 也是基于 Google 的 chromium 内核开发, 所以也继承了自动更新这一恶心的操作, 禁用的方法跟上面类似, 多找找对应的文件即可. 