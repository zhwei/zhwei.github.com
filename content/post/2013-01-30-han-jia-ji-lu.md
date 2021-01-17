---
comments: true
date: "2013-01-30T00:00:00Z"
tags:
    - Notes
title: 寒假记录
---
## 学习使用`socket`模块
### 2013-01-30  
创建`tcp`服务器 客户端时,遇到如下错误,由于不能上网,无法查询特此记录  
	Traceback (most recent call last):
		File "tsTserv.py", line 21, in <module>
		data = tcpSerSock.recv(BUFSIZ)
	File "/usr/lib/python2.7/socket.py", line 170, in _dummy
		raise error(EBADF, 'Bad file descriptor')
	socket.error: [Errno 9] Bad file descriptor
