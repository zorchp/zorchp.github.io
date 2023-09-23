---
categories: [Tips]
tags: ASM Tips MacOS
---

# 写在前面

学习OS, 不得不学的一门语言就是汇编了, 说起来这种语言应该是除机器语言外最接近计算机底层的语言了, 但是又不失可读性. 下面我在自己的电脑上配置了masm汇编环境, 并且给出了配置文件的使用方法(dosbox-x默认配置文件并不在其官网所述的目录中!) 包括字体的修改, 环境变量的配置等等. 



# 下载安装

`brew`:

```bash
brew install dosbox-x --cask
```

>   至于为什么没有使用dosbox呢? 当时好像是`dosbox-x`最先支持了m1, 并且有更多的功能, 就先体验了(后来发现确实比原版的dosbox要好用一些)



# 配置文件在哪里

关于这个默认的配置文件我找了好久, 因为官网说:

>   ```bash
>   (Windows)  C:\Users\<username>\AppData\Local\DOSBox-X\dosbox-x-<version number>.conf
>   (Linux)    ~/.config/dosbox-x/dosbox-x-<version number>.conf
>   (macOS)    ~/Library/Preferences/DOSBox-X <version number> Preferences
>   ```

但是对应的目录中并没有这个文件...

后来看issue[^1], 发现这是一个bug...

因为默认的dosbox安装路径(在win下)中是有一个`生成配置文件.bat`这样一个批处理文件的, 但是移植过来的`dosb-x`好像去掉了这个文件..

不过, 后来我几经折腾, 找到了这样两个文件:

```bash
/Applications/dosbox-x.app/Contents/Resources/dosbox-x.reference.conf
/Applications/dosbox-x.app/Contents/Resources/dosbox-x.reference.full.conf
```

这不就是配置文件么, 只不过是安装目录中自带的, 先复制一份, 然后就可以进行配置了.

这里我另存了一份此文件在其他目录中, 然后设置了软链接到`/Applications/dosbox-x.app/Contents/MacOS/`目录中, 这样做的目的是同步更改配置文件. 

>   因为每次打开dosbox-x, 默认选取的路径是在`/Applications/dosbox-x.app/Contents/MacOS`中, 将配置文件放进去就OK了. 

这里设置的软链接命令为:

```bash
ln -s ~/code/asm/dosbox-x/dosbox-x.conf /Applications/dosbox-x.app/Contents/MacOS/dosbox-x.conf
```

最后在打开软件的时候选择`/Applications/dosbox-x.app/Contents/MacOS`(默认)即可.



# 修改字体和环境变量

## 字体

默认的字体真的是一言难尽, 虽然保留了DOS时期的经典字体, 但是现在来看实在是不舒服, 官网给出了配置其他字体的方法[^2], 就是将配置文件中的`output`这一项改为`ttf`, 也就是使用TrueType font (TTF)标准字体作为输出.(在配置文件的`[sdl]`段中), 官网显示如下:

![DOSBox-X:TrueType_Font_Default.png (1924×1304)](https://dosbox-x.com/wiki/images/DOSBox-X:TrueType_Font_Default.png)

## 环境变量

之后就是环境变量了, 之所以要设置环境变量, 是因为`masm`, `link`等的汇编工具链在一个文件夹中, 如果不设置环境变量, 那么源代码也必须要在与工具链同级的目录下, 管理起来不太方便. 

这里我的工具链目录为`~/code/asm/dosbox-x/`, 详细信息:

```bash
√  ~/code/asm/dosbox-x
 ==> tree
.
├── CODE
│   ├── TEST.EXE
│   ├── TEST.OBJ
│   └── test.asm
├── DEBUG.EXE
├── EDIT.COM
├── EDIT.INI
├── EXE2BIN.EXE
├── LIB.EXE
├── LINK.EXE
├── MASM.EXE
├── dosbox-x.conf
├── masm.IMg
└── page1.png

1 directory, 13 files
```

其中`code`目录是我在工具链路径下新建的文件夹, 专门用来存放汇编源代码.

具体配置环境变量的方法很简单, 需要先在`[autoexec]`段中写入:

```bash
[autoexec]
# Lines in this section will be run at startup.
# You can put your MOUNT lines here.
mount c: ~/code/asm/dosbox-x/
c:/
cd code
```

然后, 在`[config]`段的`set path`选项后添加`;C:\`, 变成

```bash
[config]
...
set path    = Z:\;Z:\SYSTEM;Z:\BIN;Z:\DOS;Z:\4DOS;Z:\DEBUG;Z:\TEXTUTIL;C:\
```

最后重启`dosbox-x`, 就可以看到:

![截屏2022-10-31 17.46.16](https://s2.loli.net/2022/10/31/znitqVYdvO1U3J7.jpg)

然后就可以用你喜欢的编辑器写汇编了, 在`C:\CODE\`保存源码文件后, 直接在dosbox-x中执行编译(`masm`)和链接(`link`)即可. 



# ref

[^1]: [Can't generate dosbox.conf file [on Mac OS X] · Issue #573 · joncampbell123/dosbox-x (github.com)](https://github.com/joncampbell123/dosbox-x/issues/573);
[^2]:[TrueType font output in DOSBox-X](https://dosbox-x.com/wiki/Guide%3AUsing-TrueType-font-output-in-DOSBox‐X#_truetype_font_output_in_dosbox_x);