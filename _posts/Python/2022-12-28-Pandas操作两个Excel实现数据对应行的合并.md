---
categories: [Python]
tags: Python Pandas Excel
---

# 写在前面

最近有朋友问我怎么把一个Excel工作表中的数据按照对应的匹配规则放到另外一个表中, 要求是两个对应的列要相同, 具体来看就是`sheet1`中数据比较多, `sheet2`中只含有两列, 这两列包含了年份和行业信息, 这两个表的`header`(pandas中的术语, 表示表头或者列名)都是相同的, 所以关键点就是让表1中的数据与表2中的数据建立对应即可, 然后注意一下选取过的数据就不能选了这个条件. 

>   当然可能会有直接使用Pandas内置高级函数的方法来做, 但是毕竟不是主要研究数据分析了, 能用就行..

为了数据安全, 这里就不放截图了. 

# 主要思路

因为要填充表2, 那么当然要遍历表二的每一行, 针对这每一行给出的列标信息, 然后遍历表1中满足条件的行, 填入表二之后`break`即可, 因为可能会出现重复遍历, 这里用到了哈希表的方法, 并且哈希表也有两种实现, 

-   一种是给表1新添加一个列, 这个列可以是布尔值或者全`0`列, 表示没有遍历过(`unused`), 然后在满足条件的行添加到表二之后, 将对应值设置为`1`即可, 这样可以在之后的遍历过程中忽略掉已添加的数据.
-   另一种方法就是使用哈希表存储表一中遍历过的行的索引, 思路跟上面是一样的, 但是不会对原始数据进行增删. 



# 代码

代码部分我给出了两个版本, 一种是我首先想到的, 不借助pandas内置函数, 将数据转换为列表来完成, 这样虽然好想当然之后还要手动处理表头, 比较麻烦, 代码如下:

```python
import pandas as pd

df1 = pd.read_excel('data.xlsx', sheet_name='Sheet1', header=0).values.tolist()
df2 = pd.read_excel('data.xlsx', sheet_name='Sheet2', header=0).values.tolist()
for i in range(len(df1)):
    df1[i].append(0)

for i, item in enumerate(df2):
    for j in range(len(df1)):
        if df1[j][-1] == 0 and df1[j][0] == item[0] and df1[j][2] == item[2]:
            df2[i] = df1[j]
            df1[j][-1] = 1
            break
df2 = pd.DataFrame(df2)
print(df2)

with pd.ExcelWriter("data.xlsx", mode='a', engine='openpyxl') as writer:
    df2.to_excel(writer, sheet_name="Sheet3")

```



另一种用到了pandas内置的行遍历方法和索引等方法, 对`Dataframe`这种pandas内置的原生数据结构支持比较好, 但是不用的话就总忘..

```python
import pandas as pd
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df1 = pd.read_excel('data.xlsx', sheet_name='Sheet1', header=0)
df2 = pd.read_excel('data.xlsx', sheet_name='Sheet2', header=0)
# 标记是否匹配过
used = set()

for idx2, row2 in df2.iterrows():
    tmp = df1[(df1['所属行业'] == row2['所属行业']) & (df1['新年份'] == row2['新年份'])]
    for idx1, row1 in tmp.iterrows():
        if idx1 not in used:
            df2.iloc[idx2, :] = row1
            used.add(idx1)
            break

df2.set_index('所属行业', inplace=True)
print(df2)

with pd.ExcelWriter("data.xlsx", mode='a', engine='openpyxl') as writer:
    df2.to_excel(writer, sheet_name="Sheet4")

```



