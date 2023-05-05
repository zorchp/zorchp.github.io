---
categories: [Debug]
tags: MacOS Debug Tips
---

# 问题

最近想要用之前屡试不爽的方法下载钉钉中的直播回放课程, 但是在命令行执行`ffmpeg`的时候突然出现了一些报错:

```bash
[1]    40344 killed     ffmpeg
```

而且这个问题在之前执行`pip`(`pip`位于`/opt/homebrew/bin/`目录下)的时候也出现了一样的问题.. 被`killed`了... 于是我不得不把终端默认的Python改成系统自带的Python. 

至于为什么会出现上面这么多的问题呢? 我觉得罪魁祸首一定出现在前几天更新的`MacOS12.3`上, 这版新系统中删掉了python2.7支持, 还做了一些其他的改动, 比如clang13, 这些都会导致系统出现不稳定性. 

通过brew重装的方法并不能解决Python的问题, 但是对于ffmpeg还是可以操作一下的. 

# 解决方案

通过下面的命令从源码进行编译安装,就可以解决这个问题. 

```bash
brew tap homebrew-ffmpeg/ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg
```

这时候在终端中输入`ffmpeg`, 就可以得到:

```bash
❯ ffmpeg
ffmpeg version 5.0 Copyright (c) 2000-2022 the FFmpeg developers
  built with Apple clang version 13.1.6 (clang-1316.0.21.2)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/5.0-with-options_2 --enable-shared --cc=clang --host-cflags= --host-ldflags= --enable-gpl --enable-libaom --enable-libdav1d --enable-libmp3lame --enable-libopus --enable-libsnappy --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265 --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-demuxer=dash --enable-opencl --enable-videotoolbox --enable-neon --disable-htmlpages
  libavutil      57. 17.100 / 57. 17.100
  libavcodec     59. 18.100 / 59. 18.100
  libavformat    59. 16.100 / 59. 16.100
  libavdevice    59.  4.100 / 59.  4.100
  libavfilter     8. 24.100 /  8. 24.100
  libswscale      6.  4.100 /  6.  4.100
  libswresample   4.  3.100 /  4.  3.100
  libpostproc    56.  3.100 / 56.  3.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```

