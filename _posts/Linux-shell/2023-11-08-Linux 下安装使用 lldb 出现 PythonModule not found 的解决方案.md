---
categories: [Linux-Shell]
tags: C++ lldb
---

# 写在前面

在 archlinux 和 Ubuntu 上都遇到了这个问题, 后来看 issue 解决 了



# 解决



>   [ModuleNotFoundError: No module named 'lldb.embedded_interpreter' · Issue #55575 · llvm/llvm-project](https://github.com/llvm/llvm-project/issues/55575#issuecomment-1247426995);





```bash
apt install python3-lldb-14
ln -s /usr/lib/llvm-14/lib/python3.10/dist-packages/lldb/* /usr/lib/python3/dist-packages/lldb/
```

