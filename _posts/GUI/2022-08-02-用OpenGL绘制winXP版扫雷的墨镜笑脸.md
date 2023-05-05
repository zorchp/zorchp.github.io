---
categories: [GUI]
tags: OpenGL Game
---



# 写在前面

最近看看OpenGL的东西, 学了一些基础的语法, 所以用来做点东西, 用基本的点线多边形等来绘制一个Windows XP中经典的游戏扫雷里面的标志性笑脸, 如下图:

![minesweeper-1](https://s2.loli.net/2022/08/03/7XcSlJV1U9QOjqW.gif)

# 思路

这个笑脸有四种形态,分别是初始状态的笑脸, 点击时候的o型嘴, 赢的时候的墨镜脸和输了时候的伤心脸, 下面通过简单的直线和圆来绘制, 都是简单图形, 本质上其实都是点的绘制, 这里我封装了一下函数, 调用会方便一些, 分别是通过`vector<GLint>`表示的点, 这样用`initializer_list`时候会方便很多. 

其次就是一些小细节, 例如圆的绘制中的角度问题(这里就是嘴的绘制), 还有键鼠事件的交互, 我觉得熟悉了这个流程之后, 主要的思路就都放在点的坐标上了, 这里我建议可以通过`Geogebra`这款软件进行草图的绘制, 找到待绘制的点的坐标之后会方便很多.





# 代码(C++)

下面是代码, 这里分成几个部分分别说:

首先是导言区, 导入相应的模块和常量.

```cpp
#include <GL/glut.h>
#include <vector>
//#include <iostream>
#include <cmath>

using namespace std;
const int w = 400, h = 400;

const GLfloat pi = 3.1415926536f;

void init() {
    glClearColor(1, 0, 1, 0);//黑色背景
    glMatrixMode(GL_PROJECTION);//正投影
    glLoadIdentity();
    gluOrtho2D(-w, w, -h, h);
}
```

然后是一些自定义的函数, 分别是画圆画直线和画多边形(这里是四边形)的, 用起来比直接读取点要方便一些. 

```cpp
void drawCircle(GLint x, GLint y, GLint r,
                vector<GLfloat> rgb = {0, 0, 0},
                GLint cir = 2, int mode = GL_POLYGON,
                GLfloat lw = 1,
                const int n = 10000) {
    glColor3f(rgb[0], rgb[1], rgb[2]);
    glLineWidth(lw);
    glBegin(mode);
    for (int i = 0; i < n; i++) {
        glVertex2i(x + r * cos(cir * pi / n * i),
                   y + r * sin(cir * pi / n * i));
    }
    glEnd();
}

void drawLine(vector<GLint> p1, vector<GLint> p2, GLfloat lw = 1,
              vector<GLfloat> rgb = {0, 0, 0},//default:black
              int mode = GL_LINE_STRIP) {
    glColor3f(rgb[0], rgb[1], rgb[2]);
    glLineWidth(lw);
    glBegin(mode);
    glVertex2i(p1[0], p1[1]);
    glVertex2i(p2[0], p2[1]);
    glEnd();
}

void drawPolygon(vector<GLint> p1, vector<GLint> p2,
                 vector<GLint> p3, vector<GLint> p4,
                 vector<GLfloat> rgb = {0, 0, 0},//default:black
                 int mode = GL_POLYGON,
                 GLfloat lw = 1) {
    glColor3f(rgb[0], rgb[1], rgb[2]);
    glLineWidth(lw);
    glBegin(mode);
    glVertex2i(p1[0], p1[1]);
    glVertex2i(p2[0], p2[1]);
    glVertex2i(p3[0], p3[1]);
    glVertex2i(p4[0], p4[1]);
    glEnd();
}
```

最后就是主要的绘制了, 

```cpp
void display() {// 绘制基本的笑脸
    drawCircle(0, 0, 50, {1, 1, 0});//face
    drawCircle(-20, 15, 6);//left eye
    drawCircle(20, 15, 6);//right eye
    drawCircle(0, -10, 20, {0, 0, 0}, -1, GL_LINE_STRIP, 3);//mouth
    glFlush();
}

void openMouth() {//点击时候的张嘴
    drawCircle(-20, 15, 8);//left eye
    drawCircle(20, 15, 8);//right eye
    drawCircle(0, -10, 20, {1, 1, 0}, -1, GL_LINE_STRIP, 3);//cover old mouth
    drawCircle(0, -18, 10, {0, 0, 0}, 2, GL_LINE_STRIP, 3);//mouth
    glFlush();
}

void coolFace() {//赢时候的墨镜表情
    drawPolygon({-40, 25}, {-10, 25}, {-10, 8}, {-40, 8});//left eye
    drawPolygon({40, 25}, {10, 25}, {10, 8}, {40, 8});//right eye
    drawLine({-10, 23}, {10, 23}, 3);//glasses middle
    drawLine({-45, 20}, {-40, 25}, 3);//glasses left
    drawLine({45, 20}, {40, 25}, 3);//glasses right
    glFlush();
}

void dieFace() {//输了时候的伤心脸
    drawCircle(0, 0, 50, {1, 1, 0});//face
    drawLine({-12, 7}, {-28, 23}, 3);
    drawLine({-12, 23}, {-28, 7}, 3);//left eye
    drawLine({12, 7}, {28, 23}, 3);
    drawLine({12, 23}, {28, 7}, 3);//right eye
    drawCircle(0, -10, 20, {0, 0, 0}, 1, GL_LINE_STRIP, 3);//mouth
    glFlush();
}

// 这里是键盘交互, 通过按下q或者esc键实现退出, 按d实现伤心脸, 按w实现墨镜脸
void Key(unsigned char key, int x, int y) {
    switch (key) {
        case 27:
        case 'q':
            exit(0);
        case 'd':
            dieFace();
            break;
        case 'w':
            coolFace();
            break;
    }
}

// 鼠标事件, 点击笑脸变形为O型嘴
void Mouse(int btn, int state, int x, int y) {
    // 如果在圆内, 点击生效
    if (x * x + y * y - w * x - w * y + (w / 2) * w < 50 * 50) {
        if (btn == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
//            cout << x << " " << y << endl;
            openMouth();
        } else {
            display();
        }
    }
}


int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowPosition(200, 200);
    glutInitWindowSize(w, h);
    glutCreateWindow("MineSweeper Smiling Face");
    init();
    glutDisplayFunc(display);
    glutKeyboardFunc(Key);
    glutMouseFunc(Mouse);
    glutMainLoop();
    return 0;
}
```

最后实现结果:

<img src="https://s2.loli.net/2022/08/03/XDSeTwQIdNH3UOc.gif" alt="aa" width=300px; />

顺便附带一下cmake文件:(我的测试环境是Mac, 在Windows中需要配置一下路径)

```lua
cmake_minimum_required(VERSION 3.21)
project(minesweeper-smile)

set(CMAKE_CXX_STANDARD 17)
set(program_SOURCES main.cpp)
link_directories("/opt/homebrew/lib")
include_directories("/opt/homebrew/include")

find_library(Cocoa_Library Cocoa)
find_library(OpenGl_Library OpenGL)
find_library(GLUT_Library glut)
add_executable(${PROJECT_NAME} ${program_SOURCES})
target_link_libraries(${PROJECT_NAME}
        ${Cocoa_Library}
        ${OpenGl_Library}
        ${GLUT_Library}
        )

```

