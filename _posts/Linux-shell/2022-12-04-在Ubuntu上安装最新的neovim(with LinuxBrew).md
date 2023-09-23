---
categories: [Linux-Shell]
tags: Ubuntu Server Tips Vim
---

# 写在前面

之前一直是在mac上写程序的, 后来有了阿里云服务器, 想把环境都部署到服务器上, (毕竟架构是x86_64, 适配性好), 首先是编辑器, 习惯了nvim, 当然要整上, 直接`apt Install neovim`发现安装的竟然是0.4版本, 太低了... 

后来看Reddit, 大家都在推荐一款包管理器LinuxBrew, 虽然也有说路径混乱等问题的, 但是毕竟在MacOS上成功实践过, 那么就先来安一下这款包管理器吧.

# 安装LinuxBrew

安装倒是不费事, 一行命令:(导入镜像快一些, 随后这三条应该加入到`.bashrc`中)

```bash
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

不过由于homebrew官方的Ruby更新了, 运行科大的镜像时候就会出现404, 我直接从本地下载了一份2.6.8_1版本, 然后sftp到服务器了. 然后执行安装即可. 

安装中可能会出现一些小插曲:

>   fatal: unable to access 'https://github.com/Homebrew/brew/': GnuTLS recv error (-110): The TLS connection was non-properly terminated.

这里的修复莫名其妙, 好像重试一次就可以了... 参考[^1][^2]. ([^2]太过复杂,没有用)

最后就是配置环境变量:

```bash
echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /home/test/.bash_profile
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/test/.bash_profile
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

镜像:

```lua
echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /home/test/.bash_profile
echo 'export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"' >> /home/test/.bash_profile
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
```



# 安装nvim

```bash
brew update
brew install neovim
```

可以看到安装的nvim就是最新版(0.8):

```bash
brew info nvim
==> neovim: stable 0.8.1 (bottled), HEAD
Ambitious Vim-fork focused on extensibility and agility
https://neovim.io/
/home/linuxbrew/.linuxbrew/Cellar/neovim/0.8.1 (1,674 files, 26.7MB) *
  Poured from bottle on 2022-12-04 at 14:08:19
```





# ref

[^1]:[ubuntu - How to fix git error: RPC failed; curl 56 GnuTLS - Stack Overflow](https://stackoverflow.com/questions/38378914/how-to-fix-git-error-rpc-failed-curl-56-gnutls);
[^2]: [[Solution\] Gnutls_handshake() Failed GIT Repository - AWS Codecommit (devopscube.com)](https://devopscube.com/gnutls-handshake-failed-aws-codecommit/);

