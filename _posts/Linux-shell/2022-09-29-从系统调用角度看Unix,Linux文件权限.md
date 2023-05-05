---
categories: [Linux-Shell]
tags: Linux OS Syscall
---

# 写在前面

最近开始看APUE, 其中文件访问权限部分一开始有点不懂, 后来发现就是简单的`chmod`命令的宏形式, 下面简单总结一下, 参考`<sys/stat.h>`. 

# 文件权限



| `st_mode` | 含义         | 八进制值 | 英文注记      |
| --------- | ------------ | -------- | ------------- |
| `S_IRUSR` | 用户读       | 4        | READ `USER`   |
| `S_IWUSR` | 用户写       | 2        | WRITE `USER`  |
| `S_IXUSR` | 用户执行     | 1        | EXEC `USER`   |
| `S_IRGRP` | 组读         | 4        | READ `GROUP`  |
| `S_IWGRP` | 组写         | 2        | WRITE `GROUP` |
| `S_IXGRP` | 组执行       | 1        | EXEC `GROUP`  |
| `S_IROTH` | 其他用户读   | 4        | READ `OTHER`  |
| `S_IWOTH` | 其他用户写   | 2        | WRITE `OTHER` |
| `S_IXOTH` | 其他用户执行 | 1        | EXEC `OTHER`  |

这也对应了我们常见的`chmod 755`, 上面的表格可以分成三组, 每组最大值为7,表示读写执行权限. 下面用C代码来看看具体值:

```c
#include <stdio.h>
#include <sys/stat.h>

/*
S_IRUSR: 使用者读权限, READ USER 4
S_IWUSR: 使用者写权限, WRITE USER 2
S_IRGRP: 组用户读权限, READ GROUP 4
S_IROTH: 其他用户读权限, READ OTHER 4
*/


int main(int argc, char const *argv[]) {
    printf(
        "S_IRUSR, S_IWUSR, S_IRGRP, S_IROTH=%o, %o, %o, %o, (S_IRUSR | S_IWUSR "
        "| S_IRGRP | S_IROTH)=%o\n",
        S_IRUSR, S_IWUSR, S_IRGRP, S_IROTH,
        (S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH));
    return 0;
}
```



结果:

```c
S_IRUSR, S_IWUSR, S_IRGRP, S_IROTH=400, 200, 40, 4, (S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)=644
```

