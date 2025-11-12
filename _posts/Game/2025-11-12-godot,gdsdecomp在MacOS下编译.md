---
tags: Game
categories: Game
---

## 写在前面

用的最新的master 代码

> https://github.com/godotengine/godot.git
>
> https://github.com/GDRETools/gdsdecomp.git



```bash
brew install scons dotnet-sdk
```

需要把`gdsdecomp` 克隆到`modules/gdsdecomp`里面

```bash
 ==> sh misc/scripts/install_vulkan_sdk_macos.sh
  ==> vi modules/gdsdecomp/SCsub +78
  ##env_gdsdecomp.Append(CPPDEFINES=["ENABLE_3_X_SCENE_LOADING"])
scons platform=macos target=template_debug -j4
```









