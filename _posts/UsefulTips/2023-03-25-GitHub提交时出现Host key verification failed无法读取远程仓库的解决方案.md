---
categories: [Tips]
tags: Git Debug Tips
---

# 问题

今天提交代码时候发现有这样一个问题:

```bash
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s.
Please contact your system administrator.
Add correct host key in ~/.ssh/known_hosts to get rid of this message.
Host key for github.com has changed and you have requested strict checking.
Host key verification failed.

fatal: 无法读取远程仓库
...
```

那么为什么呢?

找了一圈, 发现一篇帖子是最近(两天前写的)由GitHub官方给出的, 如下:

[We updated our RSA SSH host key](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/);

那么, 就用这个方法试试呗:



# 解决方案



1.   ```bash
     ssh-keygen -R github.com
     ```

2.   ```bash
     vi ~/.ssh/known_hosts
     
     # 添加一行:
     github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=
     
     ```

解决了~

重新试试提交:

```bash
git push
Everything up-to-date
```



>   当然, 我之前还试了添加ssh公钥的方法, 并不奏效, 这里也贴出来吧: (熟悉一下操作了)
>
>   >   [测试 SSH 连接 设置 SSH 密钥并将其添加到你在 GitHub.com 上的帐户后，可以测试连接。](https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
>
>   ```bash
>   ssh-keygen -t rsa -C "xxx@gmail.com"
>   
>   cat ~/.ssh/id_rsa.pub
>   
>   # 复制内容到GitHub的ssh界面
>   ```
>
>   



验证一下:

```bash
$ ssh -T git@github.com
Hi Apocaly-pse! You've successfully authenticated, but GitHub does not provide shell access.
```

