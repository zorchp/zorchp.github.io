
---
categories: [Python]
tags: Python
---

# 写在前面



试试找 API, 其实不难, 网址中就给出了, 难就难在解析结果了. 

```c
# 英译中
https://fanyi.sogou.com/text?keyword=你好&transfrom=auto
# 中译英
https://fanyi.sogou.com/text?keyword=nihao&transfrom=auto
```

替换关键词即可



# 分析html



```html
<!-- 中译英: 你好 -->
<div class="output">
  <p
    id="trans-result"
    class="output-val trans-result-zh2en"
    style="
      white-space: pre-line;
      position: relative;
      height: 76px;
      overflow: hidden;
    "
  >
    <span data-index="0" class="trans-sentence">hello </span>
    <span class="loading" style="display: none"></span>
  </p>
  <p
    id="output-placeholder"
    class="output-val"
    style="
      white-space: pre-line;
      position: absolute;
      left: 0px;
      top: 0px;
      opacity: 0;
      z-index: -1;
      height: auto;
      width: 541px;
    "
  >
    <span class="trans-sentence">hello </span>
  </p>
</div>

<!-- 英译中: nihao -->
<div class="output">
  <p
    id="trans-result"
    class="output-val"
    style="white-space: pre-line; height: 76px; overflow: hidden"
  >
    倪好
  </p>
  <p
    id="output-placeholder"
    class="output-val"
    style="
      white-space: pre-line;
      position: absolute;
      left: 0px;
      top: 0px;
      opacity: 0;
      z-index: -1;
      height: auto;
      width: 541px;
    "
  >
    倪好
  </p>
</div>
```

相同点是 class: output

不同点是内部的值, 

-   中译英在 span 标签内, 需要提取id: trans-result 下 class: trans-sentence 内的元素
-   英译中比较简单, 直接 p 标签走 class: output-val即可



# Python code

````python
#!/opt/homebrew/Caskroom/miniforge/base/envs/py3x/bin/python3

import re
import sys

from urllib.parse import quote # 转换 url 中的特殊字符
import requests
from fake_useragent import UserAgent
from lxml import etree


def get_tree(kwd: str, isEng=True) -> str:
    ua = UserAgent()
    user_agent = ua.random
    headers = {"User-Agent": user_agent}
    pattern = "&transto=zh-CHS"
    r = requests.get(
        f"https://fanyi.sogou.com/text?keyword={kwd}&transfrom=auto{pattern}&model=general",
        headers=headers,
    )
    # print(r.text)
    parser = etree.HTMLParser()
    tree = etree.fromstring(r.text, parser)
    return tree


def eng2chn(kwd):
    tree = get_tree(kwd)
    ans = tree.xpath('//p[@class="output-val"]/text()')
    if ans == []:
        print("no result...")
        return
    print(ans[0])
    print()

    item_wrap = tree.xpath('//div[@class="item-wrap"]')
    if item_wrap == []:
        print("no other info...")
        return

    pronounce = item_wrap[0].xpath('./div[@class="pronounce"]')
    if pronounce == []:
        return
    syms = pronounce[0].xpath('./div[@class="item"]/span/text()')
    print(f"{syms[0]}, {syms[1]}")
    print()

    symbols = item_wrap[0].xpath('./div[@class="item"]/span/text()')
    means = item_wrap[0].xpath('./div[@class="item"]/p/text()')
    for a, b in zip(symbols, means):
        print(f"{a} {b}")


def chn2eng(kwd: str):
    tree = get_tree(kwd)
    t1 = tree.xpath('//*[@class="output"]')
    t2 = t1[0].xpath('./p[@id="trans-result"]')
    ans = t2[0].xpath('./span[@class="trans-sentence"]/text()')
    if ans != []:
        print(ans[0])  # may not work sometimes
    print()
    # get word list :
    t3 = tree.xpath('//*[@class="word-list"]/li')
    for itm in t3:
        word, trans = itm.xpath("./a/text()"), itm.xpath("./span/text()")
        if word != []:
            print(word[0], end="  ")
            if trans != []:
                print(trans[0], end="")
            print()


def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: trans <kwd>")
        exit(-1)
    word = argv[1]
    word = quote(word)
    if re.match(r"[\u4e00-\u9fa5]", word[0]):
        chn2eng(word)
    elif word[0].isalnum():
        eng2chn(argv[1])
    else:
        print("no result...")


if __name__ == "__main__":
    main()

````

这里一开始想用浏览器自带的复制 xpath 工具, 但是结果不尽人意, 最后还是老老实实自己写 xpath 了, 很简单, 通过 class 选择或者 id 都行, 尽量找名字比较特殊的, 不会导致重名. 



## 设置软连接

```bash
chmod +x crawl-sogou-trans.py
ln -sf ~/code/py_code/crawl-sogou-trans.py /usr/local/bin/ts
```



# 结果

下面做这样几类测试:

```c
 ==> ts hello
你好

英 [həˈləʊ], 美 [həˈloʊ]

excl. （用于问候、接电话或引起注意）哈罗，喂，你好；（表示惊讶）嘿；（认为别人说了蠢话或没有注意听）喂，嘿
n. “喂”的招呼声；打招呼；问候
v. 说“喂”；打招呼
     
 ==> ts dns
十进位计数制

英 [ˌdiː en ˈes], 美 [ˌdiː en ˈes]

abbr. 域名服务器(Domain Name Server); 十进位计数制(Decimal Number System)
```

中译英的:

```c
 ==> ts 下降
descend

descend  v.下降；落下；突袭；是…的后裔；堕落到；突然造访；下；下斜；下倾；依次递降
drop  v.使落下；使掉下；投下；落下；掉下；降低；变弱；减少；放弃；中断；停止；卸；输掉；被硬打吊出
fall  v.落下；掉落；跌落；跌倒；摔倒；减少；下降；减弱；沦陷；被攻陷；进入 某种状态；变成；成为；被归类；被排列
decline  v.变小；变少；减少；降低；谢绝；婉言拒绝；下沉；使（名词；代词；形容词）变化词形
go/come down
     
 ==> ts 轨道

rail  n.横条；横杆；横档；栏杆；扶手；铁轨；钢轨；轨道；铁路；冒头；定电位导体轨；秧鸡
railway  n.铁路；铁道；铁路系统；铁道部门；轨道
orbit  n.轨道；范围；眼眶；眼窝；绕轨道运行；电子绕原子核运行的轨道；眼睑
track  n.小道；小径；铁路轨道；线路；足迹；踪迹；车辙；歌曲；音乐；轮距；赛道；跑道
trajectory  n.弹道；轨道；轨迹；常角轨道；轨线
```

这里面每次只能读取前面 5 条, 不过够用了. 

# 一些小问题
1. 长句翻译不一定有效, 需要加上双引号
