---
categories: [GUI]
tags: C++ OpenGL Debug Config
---

# 写在前面



最近跟着网上的教程学学OpenGL, 但是却倒在了配置环境的第一步, 这个项目需要使用一个名为Simple OpenGL Image Library (SOIL)[^1]的库, 实际上就是对OpenGL接口的进一步封装, 用于添加纹理, 但是不巧的是这个库所使用的Carbon API[^3]在MacOS Catalina已经不支持MacOS的api了[^2], 就在我准备放弃的时候, 一个新的名为`SOIL2`的库[^4]走进我的视线, 竟然还是从O'Reilly中的免费阅读项目中找到的, (这本书还算挺新的, 可以申请免费试看) 有了这个我就直接进入`SOIL2`的官方主页[^5], 然后开始一系列的配置~



但是就是这配置, 却让我折腾了快一天, 最后竟然只是因为`brew`的一个小小的包影响的.. 实在是不应该:cry:.

# 开始配置SOIL2

我这里就演示在macOS(arm64)中配置了, 至于Windows, 有一个很详细的博客, 这里给出地址[（图文）SOIL2环境配置（OpenGL）_凌落星辰的博客-CSDN博客_soil2](https://blog.csdn.net/weixin_44165937/article/details/117261166).

首先就是克隆源码:

```bash
❯ git clone https://github.com/SpartanJ/SOIL2.git
❯ cd SOIL2
❯ ls
CMakeLists.txt bin            make           premake5.lua
LICENSE        cmake          obj            src
README.md      lib            premake4.lua
```

首先要做的是下载一个叫做`premake`的C项目简易构建程序, 这个程序通过读取配置的`lua`脚本然后自动生成`Makefile`, 下面通过`brew`来做.

```bash
❯ brew install premake
```

然后开始构建`Makefile`:

```bash
❯ premake5 gmake
Building configurations...
Running action 'gmake'...
Done (61ms).

```

构建完之后开始通过`make`构建. (下面是构建成功的情况)

```bash
❯ cd make/macosx
❯ make
==== Building soil2-static-lib (debug_x86_64) ====
Linking soil2-static-lib
==== Building soil2-shared-lib (debug_x86_64) ====
Linking soil2-shared-lib
==== Building soil2-test (debug_x86_64) ====
Linking soil2-test
==== Building soil2-perf-test (debug_x86_64) ====
Linking soil2-perf-test

```

## 一个小坑

这里我之前死活过不去, 总是提示`ld: error`, 具体信息如下:

```lua
ld: warning: ignoring file ../../lib/macosx/libsoil2-debug.a, building for macOS-arm64 but attempting to link with file built for unknown-unsupported file format ( 0x21 0x3C 0x61 0x72 0x63 0x68 0x3E 0x0A 0x2F 0x20 0x20 0x20 0x20 0x20 0x20 0x20 )
Undefined symbols for architecture arm64:
  "_SOIL_last_result", referenced from:
      _main in test_SOIL2.o
  "_SOIL_load_OGL_HDR_texture", referenced from:
      _main in test_SOIL2.o
  "_SOIL_load_OGL_cubemap", referenced from:
      _main in test_SOIL2.o
  "_SOIL_load_OGL_single_cubemap", referenced from:
      _main in test_SOIL2.o
  "_SOIL_load_OGL_texture", referenced from:
      _main in test_SOIL2.o
  "_SOIL_version", referenced from:
      _main in test_SOIL2.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[1]: *** [../../bin/soil2-test-debug] Error 1
make: *** [soil2-test] Error 2
```

最重点的报错就是:

```lua
building for macOS-arm64 but attempting to link with file built for unknown-unsupported file format ( 0x21 0x3C 0x61 0x72 0x63 0x68 0x3E 0x0A 0x2F 0x20 0x20 0x20 0x20 0x20 0x20 0x20 )
```

一开始我以为这个包不支持arm, 所以不能安装, 但是后来发现这个包其实是支持arm的, 这样构建出现错误, 但是在`lib/macosx`中其实是有两个链接库的, 放在源码中跑却还是一样的问题:

```lua
Undefined symbols for architecture arm64:
  "_SOIL_load_OGL_texture", referenced from:
      _main in test_SOIL2.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

```

网上各种找资料, 一开始说是不要采用`/opt/homebrew`下的工具链, 而是通过苹果自带的(CommandLineTools或者Xcode)编译工具集进行构建, 例如:

```bash
❯ make -v
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
❯ clang -v
Apple clang version 13.1.6 (clang-1316.0.21.2.5)
Target: arm64-apple-darwin21.4.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin

```

我通过修改`.zshrc`的方式完成了工具链的替换, 但是并没有效果, 该出的问题还是有..

后来一篇文章拯救了我[^6]: 虽然是一篇go语言的文章,但是思路却很有帮助, 就是说Linux文件格式是`ELF`但是mac的是`mach-o`, 出现这个问题主要是安装了一个名叫`binutils`的程序包.....我当时是为了学习汇编(没有Linux下的汇编工具), 才下载了这个包, 没想到这个包对物理机的工具链影响这么大, 以后要引起注意了.

>   是因为mac上面装了binutils，这个工具会改变ar，sanlib（建立静态库符号索引用的）的指向。指向了linux的工具，所以找不到symbol。

于是, 直接执行一条命令:

```bash
❯ brew uninstall binutils
```

这时候再进行构建, 就直接完成了.

## 最后的配置

完成之后, 将项目的`src/SOIL2`目录(其中包含`SOIL2.h`头文件)移动到`/opt/homebrew/include`下, (这里也可以移动到`/usr/local/include`下, 记住位置就好), 将项目的`lib/macosx/libsoil2-debug.*`移动到`/opt/homebrew/lib`下, 在项目的`CMakeLists.txt`件中添加链接库目录, 即可完成安装~

下面附上我的`Cmake`配置, 我不太懂Cmake中的链接部分, 参考了`Stack Overflow`的回答[^7].

```cmake
cmake_minimum_required(VERSION 3.21)
project(OpenGL1)

set(CMAKE_CXX_STANDARD 17)
set(program_SOURCES main.cc
        game.h
        game.cpp)
link_directories("/opt/homebrew/lib")
include_directories("/opt/homebrew/include")

find_library(Cocoa_Library Cocoa)
find_library (
        SOIL2_Library
        NAMES SOIL2 soil2 libsoil2 libsoil2-debug.a  # what to look for
        HINTS "/opt/homebrew/lib" # where to look
        NO_DEFAULT_PATH # do not search system default paths
)
# or more briefly
# find_library (SOIL2_Library SOIL2)
find_library(OpenGl_Library OpenGL)
find_library(GLUT_Library glut)
# check if we found the library
# message(STATUS "SOIL2_Library: [${SOIL2_Library}]")

if (NOT SOIL2_Library)
    message(SEND_ERROR "Did not find lib SOIL2")
endif() # need parenthesis here

add_executable(${PROJECT_NAME} ${program_SOURCES})
target_link_libraries(${PROJECT_NAME} ${Cocoa_Library}
                                      ${SOIL2_Library}
                                      ${OpenGl_Library}
                                      ${GLUT_Library})

```



# Ref

[^1]:[lonesock.net: SOIL (archive.org)](https://web.archive.org/web/20200728145723/http://lonesock.net/soil.html);
[^2]:[opengl - libSOIL.a file is getting ignored on MacOS - Stack Overflow](https://stackoverflow.com/questions/67060284/libsoil-a-file-is-getting-ignored-on-macos);
[^3]:[Carbon (API) - Wikipedia](https://en.wikipedia.org/wiki/Carbon_(API));
[^4]:[Setting up a project to use SOIL on Mac | Learn OpenGL (oreilly.com)](https://learning.oreilly.com/library/view/learn-opengl/9781789340365/88d3a750-00b3-4cf6-80da-3fb96bb3ea3b.xhtml);
[^5]:[SpartanJ/SOIL2: SOIL2 is a tiny C library used primarily for uploading textures into OpenGL. (github.com)](https://github.com/SpartanJ/SOIL2);
[^6]:[cgo调用静态库失败(我的macos版本是：10.15.5) - Go语言中文网 - Golang中文社区 (studygolang.com)](https://studygolang.com/topics/11653);
[^7]:[CMake library not found - Stack Overflow](https://stackoverflow.com/questions/47690827/cmake-library-not-found);
