---
categories: [Tips]
tags: MacOS Alfred Tips
---

# 写在前面

苹果家的应用虽然受众不如ms的广, 但是Apple出品必属精品, 就比如MacOS下的图书app, 英文:iBooks, 但是有一点让人不爽的就是用苹果的图书app打开epub之后, 要是想复制文本, 就会在文本中加上双引号以及`该内容可能受版权保护`之类的文字, 这对于强迫症的我来说实在是不爽, 当然也Google了很多这方面的解决方案, 可是就是不满意, action的方法试了并不奏效, 其他的方法也都大抵如此, 后来成为了Alfred的用户, 突然想到能不能让Alfred这款强大的软件来做这种自动化的事情?

答案是: 有这个方法, 并且也有现成的脚本, 下面来看看. 

>   参考:
>
>   [Workflow: Strip citation from iBooks selection and append to text file? - Discussion & Help - Alfred App Community Forum (alfredforum.com)](https://www.alfredforum.com/topic/9696-workflow-strip-citation-from-ibooks-selection-and-append-to-text-file/#comment-89543);

# 方法1: python脚本



```python
# encoding: utf-8
from __future__ import print_function
import sys

# Fancy quotes
quotes = u'\u201c\u201d'

if len(sys.argv) < 2:
    print('No input', file=sys.stderr)
    sys.exit(1)

text = sys.argv[1].decode('utf-8')

if '\n' in text:
    # Remove last line (citation)
    text = u'\n'.join(text.splitlines()[:-1]).strip()

# Remove surrounding quotes
text = text.rstrip(quotes).lstrip(quotes).strip()

# Output cleaned text
print(text.encode('utf-8'), end='')
```

我试过了, 并不奏效, 稍后我再想一下问题出在哪里. 

# 方法2: osascript脚本

这个有现成的, 我直接拿来主义了, 用着很舒服:

GitHub地址:

[requested-alfred-workflows/Paste from Apple Books.alfredworkflow at master · vitorgalvao/requested-alfred-workflows \(github.com\)](https://github.com/vitorgalvao/requested-alfred-workflows/blob/master/Workflows/Paste from Apple Books.alfredworkflow);

我加上了一个快捷键, 用起来堪称完美. 