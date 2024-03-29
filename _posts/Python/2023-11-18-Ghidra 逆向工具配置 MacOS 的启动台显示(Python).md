---
categories: [Python]
tags: Python Ghidra
---

# 写在前面

通过 ghidra 工具, 但是只能用命令行启动, 不太舒服, 写个脚本生成 MacOS 的 app 格式并导入启动台.

不算复杂, 主要是解析包的一些元信息还有裁剪软件图标(通过 MacOS 自带的 API)

# 脚本

{% raw %}

```python
#!/opt/homebrew/bin/python3

import os
import re
import subprocess as sp  # for get command return value(stdout)

base_path = "/Applications"
app_name = "Ghidra"
exec_file = "ghidraRun"

target_path = f"{base_path}/{app_name}.app/Contents"

if not os.path.exists(target_path):
    print(f"[INFO] {target_path} not exists, creating...")
    cmd = f"mkdir -p {target_path}/{{MacOS,Resources}}"
    os.system(cmd)

""" target layout
.
└── Contents
    ├── Info.plist
    ├── MacOS
    │   └── ghidraRun -> /opt/homebrew/bin/ghidraRun
    └── Resources
        └── logo.icns
"""

# 0. get meta Info
_, brew_prefix = sp.getstatusoutput("brew --prefix")
_, brew_info = sp.getstatusoutput(f"brew info {app_name}")
if brew_info.find("Not installed") != -1:
    print(f"{app_name} not installed, install...")
    os.system(f"brew install {app_name}")
# print(brew_info)
# exit()
version_num = re.match(r"==> ghidra: (\d+\.\d+[,\.]\d+)[\s,]", brew_info).group(1)
exec_dir = re.findall(r"==> Artifacts\s(.*?)\(Binary", brew_info)[0].strip()
installed_dir = exec_dir[: exec_dir.rfind("/")]
img_file = f"{installed_dir}/docs/images/GHIDRA_1.png"
# print(version_num, exec_dir)
# exit()

# 1. create soft link
src_exec = f"{brew_prefix}/bin/{exec_file}"
print(f"create soft link : {src_exec} => {target_path}/MacOS/{exec_file}")
os.system(f"ln -s {src_exec} {target_path}/MacOS/{exec_file}")

# 2. create icon by using sips
print(f"resize png file {img_file}")
tmp_img_file = "tmp.png"
os.system(f"sips -z 512 512 {img_file} -o {target_path}/{tmp_img_file}")
icns_file = "logo.icns"
print(f"generate icns file {icns_file}")
os.system(
    f"sips -s format icns {target_path}/{tmp_img_file} -o {target_path}/Resources/{icns_file}"
)
os.system(f"rm {target_path}/{tmp_img_file}")


# 3. create Info.plist
info_plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleName</key>
	<string>{app_name}</string>
	<key>CFBundleExecutable</key>
	<string>{exec_file}</string>
	<key>CFBundleIdentifier</key>
	<string>org.{app_name}</string>
	<key>CFBundleDisplayName</key>
	<string>{app_name}</string>
	<key>CFBundleVersion</key>
	<string>{version_num}</string>
	<key>CFBundleIconFile</key>
	<string>{icns_file}</string>
</dict>
</plist>"""

print(f"write info.plist to {target_path}/Info.plist")
with open(f"{target_path}/Info.plist", "w") as f:
    f.write(info_plist)
print("[INFO] done")

```

{% endraw %}


<script src="https://gist.github.com/zorchp/2f5cba673d7d4e92259f286cdc2174da.js"></script>

可以放在任意位置, 执行之后应该就会出现火龙的标志了:

<img src="https://cdn.jsdelivr.net/gh/zorchp/blogimage/%E6%88%AA%E5%B1%8F2023-11-19%2022.20.15.jpg" alt="截屏2023-11-19 22.20.15" style="zoom:50%;" />
