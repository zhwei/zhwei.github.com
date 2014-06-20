---
layout: post
title: "使用django框架的reloader重载WSGI app"
date: 2013-09-28 09:22
comments: true
tags: Python
---

使用django框架的autoreload在网站程序代码改动时重载应用。  

一般来说这种方法适用与所有的wsgi app, 这里只说下web.py和bottle

**bottle**

```python
from bottle import run, Bottle

app = Bottle()

def dev_server():
    run(app, host='0.0.0.0', port=8080, debug=True)

if '__main__' == __name__:
    from django.utils import autoreload
    autoreload.main(dev_server)

```

**web.py**

```python
from code import app

def dev_server():
    app.run()

if __name__ == "__main__":
    from django.utils import autoreload
    autoreload.main(dev_server)
```

[http://blog.est.im/post/34342180038](http://blog.est.im/post/34342180038)
