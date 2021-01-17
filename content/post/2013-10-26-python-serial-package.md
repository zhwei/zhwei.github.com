---
comments: true
date: "2013-10-26T00:00:00Z"
tags:
    - Python
title: pySerial -- Python的串口通讯模块
---


## 介绍

pySerial  

封装了串口通讯模块，支持Linux、Windows、BSD(可能支持所有支持POSIX的操作系统)，支持Jython(Java)和IconPython(.NET and Mono). 

首页 http://pyserial.sf.net/ 

## 特性

+ 所有平台使用同样的类接口
+ 端口号默认从0开始，程序中不需要知道端口名称
+ 像文件读写一样的API，`read`、`write`（`readline`等也受支持）
+ 所有程序全由Python完成，除了标准库外不依赖其他包，除了pywin32(windows)、JavaComm(Jython). POSIX(Linux, BSD) 只依赖Python标准库。

## 依赖环境

+ Python2.2或更新版本
+ windows 上的 pywin32扩展
+ Java/Jython上的 "Java Communications" (JavaComm)或者兼容包

## 安装

*pip/easy_install*

    pip install pyserial 

    easy_install pyserial 

*windows*

下载地址 ： http://sourceforge.net/project/showfiles.php?group_id=46487

##  快速上手

Open port 0 at "9600,8,N,1", no timeout

    >>> import serial  
    >>> ser = serial.Serial(0)  # open first serial port  
    >>> print ser.portstr       # check which port was really used  
    >>> ser.write("hello")      # write a string  
    >>> ser.close()             # close port 

Open named port at "19200,8,N,1", 1s timeout

    >>> ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)  
    >>> x = ser.read()          # read one byte  
    >>> s = ser.read(10)        # read up to ten bytes (timeout)  
    >>> line = ser.readline()   # read a '/n' terminated line  
    >>> ser.close()  

Open second port at "38400,8,E,1", non blocking HW handshaking

    >>> ser = serial.Serial(1, 38400, timeout=0,  
    ...                     parity=serial.PARITY_EVEN, rtscts=1)  
    >>> s = ser.read(100)       # read up to one hundred bytes  
    ...                         # or as much is in the buffer  

Get a Serial instance and configure/open it later

    >>> ser = serial.Serial()  
    >>> ser.baudrate = 19200  
    >>> ser.port = 0  
    >>> ser  
    Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)  
    >>> ser.open()  
    >>> ser.isOpen()  
    True  
    >>> ser.close()  
    >>> ser.isOpen()  
    False  

如果给定端口，端口将在创建对象之后立即打开，如果没有给定端口，可选`timeout`参数

    timeout=None            # wait forever  
    timeout=0               # non-blocking mode (return immediately on read)  
    timeout=x               # set timeout to x seconds (float allowed)  

## Serial实例的可用方法

    open()                  # 打开端口
    close()                 # 立即关闭端口  
    setBaudrate(baudrate)   # change baud rate on an open port  
    inWaiting()             # return the number of chars in the receive buffer  
    read(size=1)            # read "size" characters  
    write(s)                # 把字符串s写到该端口  
    flushInput()            # 清除输入缓存区，放弃所有内容
    flushOutput()           # 清除输出缓冲区，放弃输出  
    sendBreak()             # 发送中断条件  
    setRTS(level=1)         # set RTS line to specified logic level  
    setDTR(level=1)         # set DTR line to specified logic level  
    getCTS()                # return the state of the CTS line  
    getDSR()                # return the state of the DSR line  
    getRI()                 # return the state of the RI line  
    getCD()                 # return the state of the CD line

## Serial实例的属性

只读

    portstr                 # 设备名称  
    BAUDRATES               # list of valid baudrates  
    BYTESIZES               # list of valid byte sizes  
    PARITIES                # list of valid parities  
    STOPBITS                # list of valid stop bit widths  

下面属性值被更改后端口会重新配置，即使端口已经打开

    port                    # port name/number as set by the user  
    baudrate                # current baud rate setting  
    bytesize                # byte size in bits  
    parity                  # parity setting  
    stopbits                # stop bit with (1,2)  
    timeout                 # timeout setting  
    xonxoff                 # if Xon/Xoff flow control is enabled  
    rtscts                  # if hardware flow control is enabled  

## 异常

    serial.SerialException  

## 常量

parity:

    serial.PARITY_NONE  
    serial.PARITY_EVEN  
    serial.PARITY_ODD  

stopbits

    serial.STOPBITS_ONE  
    al.STOPBITS_TWO 

bytesize:

    serial.FIVEBITS  
    serial.SIXBITS  
    serial.SEVENBITS  
    serial.EIGHTBITS  


翻译(有删减)仅供参考

原文地址：http://blog.csdn.net/dainiao01/article/details/5885122
官方文档：http://pyserial.sf.net/
