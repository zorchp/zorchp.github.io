---
categories: [Tips]
tags: MacOS Tips
---



# 写在前面

最近又有安装brew的需求了, 想起以前已经写过一篇关于如何快速安装`brew`的文章, 但是距今已经有快一年时间, 我有学习到不少关于`brew`的东西, 对这些方法也更加熟练. 下面重新回顾一下在arm架构的macOS上如何快速安装`brew`.



# 主要安装步骤

一台新的macOS, 如果想要安装`brew`, 首先要进行的一步是找到终端并且安装`xcode-select`组件, 可以通过执行
```bash
xcode-select --install
```

进行安装. 这个过程的时间长短视网速而定, 快的话不到半小时就可以完成. 

安装完之后, 先不要着急安装`brew`, 先进入科大镜像站[^1], (清华也可以, 速度都差不多) 这里默认终端为`zsh`, 老版本Mac可以通过
```bash
echo $SHELL
```

查看是不是`zsh`, (不是`zsh`的话那应该就是`bash`了, 网站有类似的命令, 这里不放了) 之后在终端输入下面的命令:
```bash
echo 'export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"' >> ~/.zshrc
```

接下来是`bottles`的镜像切换[^2]:

```bash
echo 'export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"' >> ~/.zshrc
```

以及`core`源[^3]:
```bash
echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> ~/.zshrc
```



输入完上面三条命令, 在终端继续执行:
```bash
source ~/.zshrc
```



然后就可以进入`brew`的官方主页[^4], 复制安装命令:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

这次就会快不少, 安装中根据提示输入密码以及按回车键, 如果失败就`Ctrl+C`多试几次, 在安装完成之后, `brew`应该默认安装到了`/opt/homebrew/`目录下, 这是为了与Rosetta2转译的`brew`进行区分. 但是默认的话系统只会读取`/usr/local/`目录下的`brew`, 这就需要添加环境变量
```bash
echo 'export PATH="/opt/homebrew/bin/:$PATH"' >> ~/.zshrc
```

并且执行刷新命令:
```bash
source ~/.zshrc
```

就可以完美使用`brew`安装软件了. 可以在命令行中输入`brew --version`查看是否成功安装. 
```bash
❯ brew --version
Homebrew 3.4.3-40-gc31d7a0
Homebrew/homebrew-core (git revision 8830b7c95f0; last commit 2022-03-23)
Homebrew/homebrew-cask (git revision 8e475199aa; last commit 2022-03-23)
```



注意这里还有两个`brew`没有安装, 分别是`cask`和`cask-version`. 这里直接使用科大镜像推荐的安装命令[^5][^6]:

```bash
brew tap --custom-remote --force-auto-update homebrew/cask https://mirrors.ustc.edu.cn/homebrew-cask.git
brew tap --custom-remote --force-auto-update homebrew/cask-versions https://mirrors.ustc.edu.cn/homebrew-cask-versions.git
```







# 参考

[^1]:[Homebrew 源使用帮助 — USTC Mirror Help 文档](http://mirrors.ustc.edu.cn/help/brew.git.html);
[^2]:[Homebrew Bottles 源使用帮助 — USTC Mirror Help 文档](http://mirrors.ustc.edu.cn/help/homebrew-bottles.html);
[^3]:[Homebrew Core 源使用帮助 — USTC Mirror Help 文档](http://mirrors.ustc.edu.cn/help/homebrew-core.git.html);
[^4]:[The Missing Package Manager for macOS (or Linux) — Homebrew](https://brew.sh/);
[^5]:[Homebrew Cask 源使用帮助 — USTC Mirror Help 文档](http://mirrors.ustc.edu.cn/help/homebrew-cask.git.html);
[^6]:[Homebrew Cask Versions 源使用帮助 — USTC Mirror Help 文档](http://mirrors.ustc.edu.cn/help/homebrew-cask-versions.git.html);