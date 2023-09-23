---
categories: [Debug]
tags: MacOS R Debug
---

# 问题及解决

>   环境: macOS12.3.1 Apple silicon
>
>   R 4.2.0 with brew (formula)
>
>   RStudio 2022.02.2,485 (with brew cask)



最近室友问我R语言的`xlsx`包安装的问题, 我想着我先在我的电脑上尝试一下, 但是在我用`brew`更新了RStudio之后, 突然出现了一些报错:

```bash
dyld[67146]: terminating because inserted dylib '/opt/homebrew/Cellar/r/4.2.0/lib/R/lib/libR.dylib' could not be loaded: tried: '/opt/homebrew/Cellar/r/4.2.0/lib/R/lib/libR.dylib' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/Users/hep/lib/libR.dylib' (no such file), '/usr/local/lib/libR.dylib' (no such file), '/usr/lib/libR.dylib' (no such file), '/lib/libR.dylib' (no such file), '/var/folders/8g/p4_lzyld1l789585kjmbrvjw0000gn/T/rstudio-fallback-library-path-c4eob3/libR.dylib' (no such file)
dyld[67146]: tried: '/opt/homebrew/Cellar/r/4.2.0/lib/R/lib/libR.dylib' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/Users/hep/lib/libR.dylib' (no such file), '/usr/local/lib/libR.dylib' (no such file), '/usr/lib/libR.dylib' 
```

这里截取了部分报错, 就是在RStudio启动界面出现的, 这里我参考了RStudio 的官方解决方案[^1],

```bash
cd /Applications/Rstudio.app/Contents/MacOS
mv rsession rsession-x86
ln -s rsession-arm64 rsession
# Open RStudio and if it fails then run this:
xattr -r -d com.apple.quarantine /Applications/RStudio.app
```

问题解决~

>   还是arm64 的锅, 重置符号链接就可以了. 遇到问题还是要先看Stack Overflow/github以及软件官网啊!



[^1]:[RStudio and R will not start on Mac M1 OS X Monterey - RStudio IDE - RStudio Community](https://community.rstudio.com/t/rstudio-and-r-will-not-start-on-mac-m1-os-x-monterey/120055/3);

