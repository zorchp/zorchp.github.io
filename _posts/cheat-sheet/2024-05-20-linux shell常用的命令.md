---

---

## 查找可执行文件并删除

>   在 git 提交时候用这个删可执行文件比较方便

在当前目录下找权限为 rwxr-xr-x(755)的 norm file 执行删除即可

```bash
find . -perm 755 -type f -exec rm {} \;
```

但是这里要注意, 如果是具有可执行权限的 `build.sh` 之类的文件其实不应该被删除, 此时加上一个排除条件

```bash
find . -perm 755 -type f ! -name "*.sh" -exec rm {} \;
```

或者直接用`-delete` 代替 `-exec rm {} \;` 亦可. 



## mv 当前目录下的所有文件到当前目录下的空目录中

>   测试数据:
>
>   ```bash
>   for i in {1..10};do touch file_$i.txt;done
>   mkdir -p d1/d2
>   for i in {1..3};do touch d1/d1_file_$i.txt;done
>   for i in {1..3};do touch d1/d2/d2_file_$i.txt;done
>   mkdir target
>   git init
>   git add .
>   ```

---

>   如果直接使用 `mv * target` 会报错, 虽然不影响结果, 但是git 的提交看着难受
>
>   如果使用 `git mv * target`, 会报错导致不会向下执行.  

```bash
find . ! -name target ! -name .git -depth 1 -print0 | xargs -0 -I {} git mv {} target/
```

>   上面的命令在 MacOS 下测试通过, 感觉可以用 find 的 exec 来做, 但是MacOS 下的mv没有-t 选项, 导致exec 的+ 不能用, 下面试试 Linux 下

仅针对 mv 可用, git-mv 不行

```bash
find . -maxdepth 1 -mindepth 1 ! -name .git ! -name target -exec mv -t target/ {} +
```

>   最大深度保证 mv 仅在当前目录下执行, 最小深度保证不搜`.` 

这里能用 exec 和`+` 主要是因为 mv 有-t 参数指定了 target, 如果用 git mv就不行了, 因为没有-t. 

所以还是老老实实 xargs:

```bash
find . -maxdepth 1 -mindepth 1 ! -name target ! -name .git -print0 | xargs -0 -I {} git mv {} target/
```

>   注意 MacOS 和 Linux 的一个区别, Mac 里面的 depth 指定一次即可

而且这里不能针对目录执行 git mv, 很奇怪...

```bash
$ git mv d1/ target/d1
fatal: not under version control, source=d1, destination=target/d1
```

但是 MacOS 下没有问题. 莫非是git 版本?MacOS 下 git 为 2.39, Linux 下为 2.40, 有关系吗?