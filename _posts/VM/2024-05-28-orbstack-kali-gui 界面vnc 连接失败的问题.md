---

---

## 问题

安装的是 xfce4 桌面, vnc 使用 tigervnc

```bash
$ vncserver

New Xtigervnc server 'ka-intel:1 (zorch)' on port 5901 for display :1.
Use xtigervncviewer -SecurityTypes VncAuth -passwd /tmp/tigervnc._8ZLKL/passwd :1 to connect to the VNC server.


=================== tail /home/zorch/.vnc/ka-intel:1.log ===================
/usr/bin/startxfce4: X server already running on display :1
[mi] mieq: warning: overriding existing handler (nil) with 0x555555730de0 for event 2
[mi] mieq: warning: overriding existing handler (nil) with 0x555555730de0 for event 3
MESA: error: ZINK: failed to choose pdev
glx: failed to create drisw screen
/usr/bin/iceauth:  creating new authority file /run/user/501/ICEauthority
dbus-update-activation-environment: warning: error sending to systemd: org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
gpg-agent: a gpg-agent is already running - not starting a new one
assertion failed [rem_idx != -1]: Unable to find existing allocation for shared memory segment to unmap
(VMAllocationTracker.cpp:745 remove_shared_mem)

============================================================================

Session startup via '/home/zorch/.vnc/xstartup' exited with status 1!

Maybe try something simple first, e.g.,
	tigervncserver -xstartup /usr/bin/xterm
The X session exited with status 1!
The Xtigervnc server died with signal 5!
Cleaning stale X11 lock '/tmp/.X1-lock'!
Cleaning stale X11 lock '/tmp/.X11-unix/X1'!
```

看了一些文章提到升级 MacOS 到 14.5,  还是报错. 仅可以执行下面的 xterm 命令:

```
tigervncserver -xstartup /usr/bin/xterm
```

试了 ubuntu, 还是不行. 感觉还是 Rosetta 的 bug, 看来暂时还是只能用命令行版本的 Linux. 

并且使用 xrbp 也闪退, 不理解为什么 了. 