---
tags: LaTeX
categories: LaTeX
---



# 写在前面



本来一直在用 nvim 写 TeX 的, 后来感觉 Ctrl CV 不太舒服就转而用 vscode 了, 配置一下 vscode 的TeX 格式化. 

# 方法

其实主要是配置 perl, 这在插件 `LaTeX Workshop` 的 output 中有所体现.

```c
Can't locate YAML/Tiny.pm in @INC (you may need to install the YAML::Tiny module)
```

这里先看一下perl 是系统自带的还是 brew 的

```bash
which perl
/opt/homebrew/bin/perl
```

如果是 brew 的还要先`pin` 一下版本, 否则之后的 perl 更新了安装的这些组件还要重新安装.

```bash
brew pin perl
```

然后参考了 github 的 issue, 

>   [Beautify error on macOS Sierra: Can't locate YAML/Tiny.pm · Issue #1792 · Glavin001/atom-beautify](https://github.com/Glavin001/atom-beautify/issues/1792#issuecomment-327071117);

需要依次执行下面几个步骤:

```bash
sudo cpan Unicode::GCString
sudo cpan App::cpanminus
sudo cpan YAML::Tiny
sudo perl -MCPAN -e 'install "File::HomeDir"'
```

我执行时候前面没加 sudo, 这时候的默认安装位置为:

```bash
$HOME/.cpan
```

再回到 vscode, 执行 ⌥+⇧+F 即可看到格式化的结果了. 
