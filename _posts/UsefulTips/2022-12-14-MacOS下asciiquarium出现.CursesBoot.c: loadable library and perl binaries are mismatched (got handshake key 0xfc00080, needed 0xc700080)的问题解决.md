---
categories: [Tips]
tags: Debug Perl
---

# 问题

>   m1Mac brew

一个终端养鱼程序(Perl):`ASCIIQuarium`, [https://github.com/cmatsuoka/asciiquarium](https://github.com/cmatsuoka/asciiquarium);

在使用`brew`安装之后报错了:

```lua
./CursesBoot.c: loadable library and perl binaries are mismatched (got handshake key 0xfc00080, needed 0xc700080)
```

然后网上找一圈也没有解决方案, 后来发现重新从源构建就好了:

```bash
brew reinstall asciiquarium --build-from-source
```

完美:

![截屏2022-12-14 18.35.03](https://s2.loli.net/2022/12/14/joQtxBEr5fs8vli.jpg)