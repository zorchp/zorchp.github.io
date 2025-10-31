---
categories: [Python]
tags: Python
---

## 写在前面

## 背景

总要发一些结果文件(通常是文本文件) 给 PM. 但是每次都要

- 拉取文件到 Mac
- IM软件发给同事

比较麻烦. 并且每次要保存一份副本. 

此时可以在物理机启动一个 httpserver, 然后每次共享链接即可 (内网开放端口在 8000-9000)

## 方法

> ref: [python http.server网页打开txt乱码问题解决_txt导入网页变乱码-CSDN博客](https://blog.csdn.net/li281037846/article/details/129202574)

```bash
nohup python3 -c from http.server import test, SimpleHTTPRequestHandler as RH; RH.extensions_map={k:v+';charset=UTF-8' for k,v in RH.extensions_map.items()};RH.extensions_map['.txt']='text/plain; charset=utf-8'; test(HandlerClass=RH, port=8225) &>>/dev/null &
```

使 httpserver 的中文文件在浏览器显示正常. 

端口 8000-9000 (公司内需要)

后缀需要是 txt 的. 

```python
from http.server import test, SimpleHTTPRequestHandler as RH
RH.extensions_map = {k: v+';charset=UTF-8' for k,
                     v in RH.extensions_map.items()}
RH.extensions_map['.txt'] = 'text/plain; charset=utf-8'
test(HandlerClass=RH, port=8225)

```

本质是源码里面写死了指定扩展. 



![img](https://cdn.jsdelivr.net/gh/zorchp/blogimage@main//imageDownloadAddress.jpeg)



## 使用

```bash
http://example.com:8225/ref.txt
```



## 带密码方式

```bash
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, quote
import os
import html
import sys

ACCESS_KEY = "file_test"

class KeyProtectedHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        self._key = params.get('key', [None])[0]
        if self._key != ACCESS_KEY:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Forbidden: invalid key')
            return
        self.path = parsed_url.path  # 清理 query 参数，仅保留路径
        return super().do_GET()

    def list_directory(self, path):
        try:
            entries = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        entries.sort()
        r = []
        displaypath = html.escape(self.path)
        r.append(f'<html><title>Index of {displaypath}</title>')
        r.append(f'<body><h2>Index of {displaypath}</h2><hr><ul>')
        for name in entries:
            fullname = os.path.join(path, name)
            displayname = name
            linkname = quote(name)
            if os.path.isdir(fullname):
                displayname += "/"
                linkname += "/"
            r.append(f'<li><a href="{linkname}?key={quote(self._key)}">{html.escape(displayname)}</a></li>')
        r.append('</ul><hr></body></html>')
        encoded = '\n'.join(r).encode('utf-8', 'surrogateescape')
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def end_headers(self):
        # 强制为 UTF-8 文本
        if self.path.endswith(".txt"):
            self.send_header("Content-Type", "text/plain; charset=utf-8")
        super().end_headers()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} port')
        exit(-2)
    port = int(sys.argv[1])
    server = HTTPServer(('0.0.0.0', port), KeyProtectedHandler)
    print(f"Serving on http://localhost:{port}")
    server.serve_forever()
```

使用

```bash
nohup python3 http.file.passwd.py 8226 &
```

## 优化版本

> 支持多线程

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, quote
import os
import html
import sys
import socket
from socketserver import ThreadingMixIn
import threading
import time

ACCESS_KEY = "audio_file_test"

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """多线程HTTP服务器"""
    daemon_threads = True
    timeout = 10  # 减少超时时间
    request_queue_size = 100  # 增加队列大小

class KeyProtectedHandler(SimpleHTTPRequestHandler):
    # 优化缓冲区设置
    buffer_size = 64 * 1024  # 64KB 缓冲区，避免过大导致内存问题
    
    # 禁用日志以减少I/O阻塞
    def log_request(self, code='-', size='-'):
        pass
    
    def log_message(self, format, *args):
        # 只记录错误，减少I/O
        if not ('200' in format or '304' in format):
            print(f"{self.address_string()} - {format % args}")

    def do_GET(self):
        start_time = time.time()
        try:
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)
            self._key = params.get('key', [None])[0]
            
            if self._key != ACCESS_KEY:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b'Forbidden: invalid key')
                return
                
            self.path = parsed_url.path
            super().do_GET()
            
        except BrokenPipeError:
            pass
        except Exception as e:
            print(f"Error handling request: {e}")
        finally:
            # 记录处理时间用于调试
            elapsed = time.time() - start_time
            if elapsed > 1.0:  # 只记录慢请求
                print(f"Slow request: {self.path} took {elapsed:.2f}s")

    def send_head(self):
        """完全重写 send_head 方法以优化性能"""
        path = self.translate_path(self.path)
        
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # 重定向到以/结尾的URL
                self.send_response(301)
                self.send_header("Location", self.path + "/" + f"?key={quote(self._key)}")
                self.end_headers()
                return None
            return self.list_directory(path)
        
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None
        
        fs = os.fstat(f.fileno())
        file_size = fs.st_size
        
        # 检查If-Modified-Since头
        if "If-Modified-Since" in self.headers:
            import email.utils
            header_time = email.utils.parsedate_to_datetime(self.headers["If-Modified-Since"])
            file_time = email.utils.parsedate_to_datetime(self.date_time_string(fs.st_mtime))
            if file_time <= header_time:
                f.close()
                self.send_response(304)
                self.end_headers()
                return None
        
        # 支持范围请求（断点续传）
        range_header = self.headers.get('Range')
        if range_header:
            try:
                self.send_response(206)
                self.send_header("Content-Type", self.guess_type(path))
                self.send_header("Accept-Ranges", "bytes")
                
                # 解析范围请求
                import re
                range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
                if range_match:
                    start = int(range_match.group(1))
                    end = int(range_match.group(2)) if range_match.group(2) else file_size - 1
                    content_length = end - start + 1
                    
                    self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
                    self.send_header("Content-Length", str(content_length))
                    self.end_headers()
                    
                    f.seek(start)
                    return RangeFileWrapper(f, start, end)
            except:
                f.close()
                raise
        
        # 普通文件请求
        self.send_response(200)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Length", str(file_size))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def end_headers(self):
        """优化HTTP头部"""
        # 缓存控制
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        
        # 性能优化头部
        self.send_header("Connection", "close")  # 禁用持久连接
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        
        # 设置正确的MIME类型
        if self.path.endswith(".wav"):
            self.send_header("Content-Type", "audio/wav")
        elif self.path.endswith(".mp3"):
            self.send_header("Content-Type", "audio/mpeg")
        elif self.path.endswith((".txt", ".log", ".wer", ".ref")):
            self.send_header("Content-Type", "text/plain; charset=utf-8")
        elif self.path.endswith((".html", ".htm")):
            self.send_header("Content-Type", "text/html; charset=utf-8")
        
        super().end_headers()

    def copyfile(self, source, outputfile):
        """优化的文件复制方法"""
        try:
            # 使用更小的缓冲区但更频繁的写入
            buffer_size = 8192  # 8KB 缓冲区
            
            if hasattr(source, 'read'):
                # 普通文件对象
                while True:
                    buf = source.read(buffer_size)
                    if not buf:
                        break
                    try:
                        outputfile.write(buf)
                        outputfile.flush()  # 强制立即发送
                    except (BrokenPipeError, ConnectionResetError):
                        break
            else:
                # 范围请求包装器
                for chunk in source:
                    try:
                        outputfile.write(chunk)
                        outputfile.flush()
                    except (BrokenPipeError, ConnectionResetError):
                        break
        except (ConnectionResetError, BrokenPipeError):
            pass
        finally:
            if hasattr(source, 'close'):
                source.close()

    def list_directory(self, path):
        """极简目录列表"""
        try:
            entries = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
            
        entries.sort()
        
        # 极简HTML，减少数据传输
        html_parts = ['<!DOCTYPE html><html><head><meta charset="utf-8">']
        html_parts.append('<title>Index of {}</title>'.format(html.escape(self.path)))
        html_parts.append('<style>body{font-family: sans-serif; margin: 20px;} ul{list-style: none; padding: 0;} li{margin: 5px 0;} a{text-decoration: none;}</style>')
        html_parts.append('</head><body><h2>Index of {}</h2><ul>'.format(html.escape(self.path)))
        
        # 父目录链接
        if self.path != "/":
            html_parts.append('<li><a href="../?key={}">↩ Parent Directory</a></li>'.format(quote(self._key)))
        
        for name in entries:
            fullname = os.path.join(path, name)
            is_dir = os.path.isdir(fullname)
            displayname = name + ("/" if is_dir else "")
            linkname = quote(name) + ("/" if is_dir else "")
            
            html_parts.append('<li><a href="{}?key={}">{}</a></li>'.format(
                linkname, quote(self._key), html.escape(displayname)))
            
        html_parts.append('</ul></body></html>')
        
        encoded = ''.join(html_parts).encode('utf-8')
        
        try:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
        except (BrokenPipeError, ConnectionResetError):
            pass
        return None

class RangeFileWrapper:
    """处理范围请求的文件包装器"""
    def __init__(self, fileobj, start, end):
        self.fileobj = fileobj
        self.start = start
        self.end = end
        self.pos = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos > self.end:
            raise StopIteration
        
        chunk_size = min(8192, self.end - self.pos + 1)
        self.fileobj.seek(self.pos)
        data = self.fileobj.read(chunk_size)
        if not data:
            raise StopIteration
        
        self.pos += len(data)
        return data
    
    def read(self, size=-1):
        if self.pos > self.end:
            return b""
        
        if size == -1:
            size = self.end - self.pos + 1
        else:
            size = min(size, self.end - self.pos + 1)
        
        self.fileobj.seek(self.pos)
        data = self.fileobj.read(size)
        self.pos += len(data)
        return data
    
    def close(self):
        self.fileobj.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} port')
        exit(-2)
    port = int(sys.argv[1])
    
    # 服务器优化配置
    server = ThreadingHTTPServer(('0.0.0.0', port), KeyProtectedHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    print(f"Serving on http://localhost:{port} (Fully optimized)")
    print("Optimizations applied:")
    print("- Reduced buffer size for better flow control")
    print("- Added range request support")
    print("- Minimal logging to reduce I/O")
    print("- Connection closing enforced")
    print("- Flush during file transfer")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()
```

```bash
nohup python3 http.file.server.optim.py 8226 & 
```



搞一个快速生成链接的脚本

```bash
#!/bin/bash

if (($# != 1)); then
    echo "Usage: $0 file_relative_path"
    exit -1
fi

abs_path=$(readlink -f $1)

if [[ "$abs_path" == $HOME/for_pm* ]]; then
    link_prefix="http://$(hostname):8226"
    link_suffix=$(echo $abs_path | sed 's|/home/disk2/pengzongyu/for_pm/||')
else
    echo "Path does not match any known prefix: $abs_path"
    exit
fi

link_passwd="?key=audio_file_test"
echo "$link_prefix/${link_suffix}${link_passwd}" | tee >(copy)
```

copy函数可以看我之前的文章[传送门](../Linux/shell/2025-10-30-shell打通跳板机访问剪贴板.md)实现

