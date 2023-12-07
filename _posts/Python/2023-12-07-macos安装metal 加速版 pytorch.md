---
categories: [Python]
tags: Python MacOS
---

# 写在前面

试试 m3 的 metal 加速效果如何

>   -   Mac computers with Apple silicon or AMD GPUs
>   -   macOS 12.3 or later
>   -   Python 3.7 or later
>   -   Xcode command-line tools: `xcode-select --install` 

# 安装 Python: conda-forge

```bash
brew install miniforge
```



## 镜像

```yaml
channels:
  - defaults
show_channel_urls: true
auto_activate_base: false
ssl-verify: false
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
```

## 安装

开一个新的虚拟环境, 这个是重点, 如果不开的话, 原有的环境会污染 C 库的链接, 所以这一步是必须的

>   [On Mac OS X, import numpy complaining about "Library not loaded: @rpath/libgfortran.3.dylib" · Issue #12970 · numpy/numpy](https://github.com/numpy/numpy/issues/12970);
>
>   这个方案不彻底, 直接卸载 numpy 然后重装不能解决问题...

```bash
conda create -n py3xi python=3.11
conda activate py3xi
# conda update --all -c conda-forge # optional
# 重点: 
conda install pytorch torchvision torchaudio -c pytorch-nightly 
```

然后测试

>   [Accelerated PyTorch training on Mac - Metal - Apple Developer](https://developer.apple.com/metal/pytorch/);

```python
import torch
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")
'''
tensor([1.], device='mps:0')
'''
```

可以在 MacOS 上跑深度学习了. 