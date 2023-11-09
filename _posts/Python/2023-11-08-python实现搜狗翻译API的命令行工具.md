---
categories: [Python]
tags: Python
---

# 写在前面



试试找 API, 其实不难, 网址中就给出了, 难就难在解析结果了. 



# Python code

````python
#!/opt/homebrew/Caskroom/miniforge/base/envs/py3x/bin/python3

import sys

import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
user_agent = ua.random
headers = {"User-Agent": user_agent}


def get_content(kwd):
    r = requests.get(f"https://fanyi.sogou.com/text?keyword={kwd}", headers=headers)
    # print(r.text)
    parser = etree.HTMLParser()
    tree = etree.fromstring(r.text, parser)
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


def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: trans <kwd>")
        exit(-1)
    get_content(sys.argv[1])


if __name__ == "__main__":
    main()

````

这里一开始想用浏览器自带的复制 xpath 工具, 但是结果不尽人意, 最后还是老老实实自己写 xpath 了, 很简单, 通过 class 选择或者 id 都行, 尽量找名字比较特殊的, 不会导致重名. 



## 设置软连接

```bash
chmod +x crawl-sogou-trans.py
ln -sf ~/code/py_code/crawl-sogou-trans.py /usr/local/bin/trans
```



# 结果

下面做这样几类测试:

```go
 ==> trans hello
你好

英 [həˈləʊ], 美 [həˈloʊ]

excl. （用于问候、接电话或引起注意）哈罗，喂，你好；（表示惊讶）嘿；（认为别人说了蠢话或没有注意听）喂，嘿
n. “喂”的招呼声；打招呼；问候
v. 说“喂”；打招呼
     
 ==> trans dns
十进位计数制

英 [ˌdiː en ˈes], 美 [ˌdiː en ˈes]

abbr. 域名服务器(Domain Name Server); 十进位计数制(Decimal Number System)
```

