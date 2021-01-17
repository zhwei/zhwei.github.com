---
comments: true
date: "2012-11-23T00:00:00Z"
tags:
    - Linux
title: ubuntu12.10 配置记录
---
很久没更新的ubuntu12.04更新了下，结果直接挂掉了。。。
前几天装上了新出的12.10，gnome还是老样子，效果有一丢丢改进.
为了以后安装方便，很多环境的配置方法记录下。

为了使用pyCharm，要用sun jdk，openjdk明显不给力。。。

sunjdk文件可以在[oracle](http://www.oracle.com/technetwork/java/javase/downloads/jdk7u9-downloads-1859576.html)，已经保存到百度网盘。

	chmod +x jdk-6u32-linux-x64.bin

	sudo ./jdk-6u32-linux-x64.bin

	sudo mv jdk1.6.0_32 /usr/lib/jvm/

	#配置环境变量，这是更改后的

	PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/jvm/jdk1.6.0_34/bin" 
	     
	CLASSPATH="/usr/lib/jvm/jdk1.6.0_34/lib"
	 
	JAVA_HOME="/usr/lib/jvm/jdk1.6.0_34"


<!--more-->
[ruby on rails](http://ruby-china.org/wiki/install_ruby_guide)
