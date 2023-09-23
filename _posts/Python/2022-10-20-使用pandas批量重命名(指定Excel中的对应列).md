---
categories: [Python]
tags: Python Pandas Excel Tips
---

# 写在前面

今天有个朋友问我有没有一种简单的方法将Excel中的学号和姓名列作为文件名, 批量重命名100个Word文档, 下面是具体的文件, 文件夹中是待修改的Word文档(存在一些比较冗杂的xlsx文件), Excel前两列是学号和姓名信息.

## 文件夹内容



<img src="https://s2.loli.net/2022/10/20/Srz1NmnuixLpIFc.png" style="zoom:50%;" />

可以看到里面的文件名主要的格式为:`<姓名><等级或成绩><成绩><其他信息>.docx`, (忽略其他冗余文件).

## Excel内容

这里不方便给出截图, 以表格形式简单描述:

| 序号 | 学号       | 姓名   | 其他信息 |
| ---- | ---------- | ------ | -------- |
| 1    | 20XXXXXXXX | 张三   | xxx      |
| 2    | 20XXXXXXXX | 王小明 | xxx      |
| 3    | 20XXXXXXXX | 李四   | xxx      |



## 要得到的结果



![WeChat1cef85e16999ad3e1245771ee0211d73](https://s2.loli.net/2022/10/20/eZ8p9mkjBYbuagS.png)

这里的结果就是一个准确的格式:`<学号>+<姓名>.docx`. 



# 思路与分析

不难发现, 主要思路其实就是建立两个文件的映射关系, 先提取Excel全部的姓名列和学号列组成`dict`, 然后遍历文件夹内容找满足名字相等的条目进行修改.

这里面比较麻烦的一点是Word文件名中格式不统一. 一开始我想的是通过正则表达式提取`(<中文>)\w*<其他>`这种类型的内容, 然后丢到Excel里面找匹配, 但是我对中文正则这块还不熟悉, 于是就只能想别的办法. 后来我发现只取名字的前两个就可以完成匹配, (不过这个的前提是`没有前两个字相同的名字的情况`)



# 用到的技术栈(Python)与代码

主要用到三个Python库, 分别是`os`(用于重命名文件), `glob`(用于遍历文件夹下的文件, 以Linux通配符的形式, 相较于`os.walk()`比较方便), 还有就是读取Excel的`Pandas`.

```python
import os
from glob import glob
import pandas as pd


def modify_name():
    df = pd.read_excel("achievement.xlsx",
                       header=0,
                       index_col=0,
                       skiprows=3).iloc[:163, :]
    id1 = df["学号"]
    id1 = pd.Series(id1, dtype="string").apply(lambda x: x[:-2]).tolist()
    name = df["姓名"].tolist()
	# 截取Word文件名前两个字符作为字典的键, 学号加姓名(文件名的目标格式)作为字典的值
    res = {k[:2]: k + "+" + v for k, v in zip(name, id1)}
    return res

# 存放Word文件的目录和文件名
path = "exam_achievement/"
files = glob("exam_achievement/*.docx")

full_files_name = [i.split('/')[-1] for i in files]
# 去掉后缀名便于正则处理(后来发现不用正则的话就没啥用)
pure_files_name = [i.split('.')[0] for i in full_files_name]

name_n_file = {k[:2]: v for k, v in zip(pure_files_name, files)}
modf_name = modify_name()

for item in name_n_file:
    # 满足条件, 改名
    if item in modf_name:
        os.rename(name_n_file[item], path + modf_name[item] + ".docx")
        print((name_n_file[item], path + modf_name[item] + ".docx"), "ok..")

```

