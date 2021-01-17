---
comments: true
date: "2013-11-10T00:00:00Z"
tags:
    - Python
title: Pyinstaller打包Python写的windows服务-记录
---

## 由来

最近在写一个服务器监控平台，python开发，前端标准bootstrap，后端Bottle, 数据库mongodb，要写服务器监控肯定少不了客户端了，客户端主要用到了XMLRPCServer, 服务端与客户端通过xml通信，这个在python的标准库里，还是可以信赖的，并且支持http验证，此处不赘言，以后再讲。linux上的客户端很好搞，因为linux自带python解释器，不管版本如何，使用起来还是很好改的， 最头疼的是window下的客户端，以前很少在win下做开发，python环境也是随意搭了一下，正使用的时候还是各种DT。。。

花了一段时间写了一个win下的python程序，不过依赖很多，包括pywin32、wmi，并且python的安装还需要改注册表，作为一个监控，如果还需要在服务器上安装python环境等东西有点得不偿失了。找到了pyinstaller和py2exe，能够将python程序打包成可执行的exe文件，复制到其他机器上可以直接执行，下面进入正题！


## 各种环境安装

+ 安装pywin32、wmi弹框

```
    Python version 2.7 required, which was not found in the registry
```

在注册表中找不到python，使用下面的一个脚本放在c盘根目录执行下就可以, 见[Link](http://www.cnblogs.com/min0208/archive/2012/05/24/2515584.html)

## 程序

```python

    # SmallestService.py
    #
    # A sample demonstrating the smallest possible service written in Python.

    import win32serviceutil
    import win32service
    import win32event

    class SmallestPythonService(win32serviceutil.ServiceFramework):
        _svc_name_ = "SmallestPythonService"
        _svc_display_name_ = "The smallest possible Python Service"
        def __init__(self, args):
            win32serviceutil.ServiceFramework.__init__(self, args)
            # Create an event which we will use to wait on.
            # The "service stop" request will set this event.
            self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

        def SvcStop(self):
            # Before we do anything, tell the SCM we are starting the stop process.
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            # And set my event.
            win32event.SetEvent(self.hWaitStop)

        def SvcDoRun(self):
            # We do nothing other than wait to be stopped!
            win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    if __name__=='__main__':
        win32serviceutil.HandleCommandLine(SmallestPythonService)
```

不过这样写好之后发现，直接运行脚本的确可以正常添加服务，添加的服务也可以正常操作，但是使用pyinstaller打包后的程序并不能正常执行。在pyinstaller的邮件列表找到了一个解决方案。 见 [Link](/archive/2013/windows-service-example-using-pyinstaller.html)

具体细节不明了，需要改动的就是SvcDoRun方法和SvcStop两个方法。

因为RPCServer会一直阻塞线程，这里创建了一个子线程创建RPCServer，使用一个循环条件来控制线程的终结Link，这样不会导致window服务无法停止的问题。 需要在SvcStop方法最后加上所执行的程序的终结方法就可以。
