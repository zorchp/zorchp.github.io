---

---

## 背景



不知道是不是因为 brew 更新了一些依赖库, conda 在创建环境时候提示:



```python
Error while loading conda entry point: conda-libmamba-solver (dlopen(/opt/homebrew/Caskroom/miniforge/base/lib/python3.10/site-packages/libmambapy/bindings.cpython-310-darwin.so, 0x0002): Library not loaded: @rpath/libarchive.13.dylib
  Referenced from: <87BD792F-0587-3166-8AAF-20CF792B82F9> /opt/homebrew/Caskroom/miniforge/base/lib/libmamba.2.0.0.dylib
  Reason: tried: '/opt/homebrew/Caskroom/miniforge/base/lib/libarchive.13.dylib' (no such file), '/opt/homebrew/Caskroom/miniforge/base/lib/python3.10/site-packages/libmambapy/../../../libarchive.13.dylib' (no such file), '/opt/homebrew/Caskroom/miniforge/base/lib/python3.10/site-packages/libmambapy/../../../libarchive.13.dylib' (no such file), '/opt/homebrew/Caskroom/miniforge/base/bin/../lib/libarchive.13.dylib' (no such file), '/opt/homebrew/Caskroom/miniforge/base/bin/../lib/libarchive.13.dylib' (no such file), '/usr/local/lib/libarchive.13.dylib' (no such file), '/usr/lib/libarchive.13.dylib' (no such file, not in dyld cache))
```



一开始还以为是动态库找不到了, 后来看了一圈博客[^1]发现是一个配置的问题. 

## 解决



```python
conda update --all --override-channels -c conda-forge -n base --solver=classic
conda info -e
```

此时就正常了. 



## ref

[^1]: [libmamba vs classic — conda-libmamba-solver](https://conda.github.io/conda-libmamba-solver/user-guide/libmamba-vs-classic/#should-i-use-conda-libmamba-solver); 

