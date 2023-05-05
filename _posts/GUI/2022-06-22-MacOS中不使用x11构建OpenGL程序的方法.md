---
categories: [GUI]
tags: Debug Tips OpenGL
---

# 写在前面

机缘巧合下, 我读到了下面的这篇文章[^1], 并且开始着手实践. 但是用博客中给出的编译命令并不能得到一样的结果, 编译命令如下:

```bash
c++ square.cpp -lglew -framework opengl -framework glut
./a.out
```

其实主要窗口内的东西都一样, 但是窗口会自动去调用`XQuartz(aka,X11)`框架, 分辨率不高不说, 执行速度也比较慢, 有一种过时的感觉. 后来我不断摸索, 找到了解决方案.

>   这个框架其实就是为了能够在苹果系统上运行Linux的图形界面应用所开发的框架, 有Linux风格是当然的.

# 分析解决

我在谷歌搜索了半天, 只找到一个类似的问题[^2], 同样也是不希望采用`x11`框架来构建程序, 而是采用苹果原生支持的`Cocoa`框架. 这个问题是八年前的了, 只有一个回答, 大意是说不要采用`glut/freeglut`, 而是采用最新的`glfw`, 顺着这个思路往下摸索, 自然想到去`glfw`官网看看. 果不其然, 在这里[^3], 我找到了官方给出的编译命令, 如下:

```bash
cc -o myprog myprog.c -lglfw -framework Cocoa -framework OpenGL -framework IOKit
```

于是, 上面的命令就可以这样来更改:

```bash
cc -o main square.cpp -lglew -framework Cocoa -framework OpenGL -framework glut
```

当然, 如果你用了`GLFW`, 还是要加上相应的依赖链接库(通过`-lglfw`).



# 更新: cmake配置文件

这里贴出来cmake配置文件, 参考了Stack Overflow的一篇回答[^4], 通过`find_library`的方式定位并通过`target_link_libraries`链接macOS中的`framework`, 完整的文件如下:

```cmake
cmake_minimum_required(VERSION 3.21)
project(OpenGL1)

set(CMAKE_CXX_STANDARD 17)

set(program_SOURCES main.cpp)

find_library(Cocoa_Library Cocoa)
find_library(OpenGl_Library OpenGL)
find_library(GLUT_Library glut)


add_executable(${PROJECT_NAME} ${program_SOURCES})
target_link_libraries(${PROJECT_NAME} ${Cocoa_Library}
      								  ${OpenGl_Library}
        							  ${GLUT_Library})



```





# 参考

[^1]:[M1 MacBook OpenGL 配置 - F5的笔记本 (f5soft.site)](https://f5soft.site/zh/notes/2021/0310/);
[^2]:[eclipse - Why does my Freeglut App comes up with XQuartz/X11? - Stack Overflow](https://stackoverflow.com/questions/23430397/why-does-my-freeglut-app-comes-up-with-xquartz-x11/72709205#72709205);
[^3]:[GLFW: Building applications](https://www.glfw.org/docs/latest/build_guide.html);
[^4]:[Why I cannot link the Mac framework file with CMake? - Stack Overflow](https://stackoverflow.com/questions/17070101/why-i-cannot-link-the-mac-framework-file-with-cmake);