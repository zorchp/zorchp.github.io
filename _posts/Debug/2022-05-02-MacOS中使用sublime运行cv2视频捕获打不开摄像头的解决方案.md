---
categories: [Debug]
tags: MacOS Python Debug
---

# 问题

>   环境:
>
>   MacOS12.3.1 Apple silicon
>
>   Python3.9.10 opencv 4.5.5
>
>   sublime text 4

在我使用下面的代码打开摄像头时候, 通过终端(iTerm2)可以完美调用摄像头, 但是通过sublime就不行

```python
import cv2

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

通过对macOS的了解, 我的想法是这个问题主要是因为sublime没有摄像头的权限, 于是就无法打开了. 

# 解决

由于系统偏好设置里面并没有选择摄像头权限的那个菜单, 这时候就只能选择另一种方案, 这里参考了一位大佬的文章[^1], 其实这里主要是通过修改Mac自身的TCC安全数据库来完成的, 但是这样做其实并不好[^2], 应该先对数据库进行一个备份之后再进行修改比较好(这里可以类比在Windows中修改注册表).

具体方案如下, 先查询需要添加权限的app的包名, 这里用到的命令是:

```bash
❯ defaults read /Applications/Sublime\ Text.app/Contents/Info.plist CFBundleIdentifier

com.sublimetext.4
```

得到的包名为`com.sublimetext.4`, 这时候先备份一下数据库, 通过

```bash
❯ cd ~/Library/Application\ Support/com.apple.TCC/

❯ cp TCC.db TCC.db.bak
```



最后进行修改, 这一步需要替换包名称:(这里的命令使用的是macOS11.X的, 12.X也可以用.)

```bash
/usr/bin/sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "REPLACE INTO access VALUES('kTCCServiceCamera','com.sublimetext.4',0,2,0,1,NULL,NULL,NULL,'UNUSED',NULL,0,1608354323);"
```

# 举一反三

对于终端, 由于其已经被赋予了权限, 这里当然直接使用就可, 但是对于像vscode和sublime这样的编辑器, 其调用摄像头的时候不会自己调用系统的权限对话框, 但是jetbrains系列产品就会调用系统对话框, 这也说明这两个轻量级IDE还有值的改进的地方...

<img src="https://s2.loli.net/2022/05/02/nAw35vdGigDJsxl.png" alt="截屏2022-05-02 11.28.57" style="zoom:50%;" />





# 参考

[^1]:[macOS：给 app 添加摄像头权限_afatgoat的博客-CSDN博客_mac 摄像头权限](https://tonyliu2ca.blog.csdn.net/article/details/111403294);
[^2]:[VSCode 终端不允许/请求访问媒体设备的权限 ·问题 #95062 ·微软/vscode (github.com)](https://github.com/microsoft/vscode/issues/95062);