---
layout: post
title: "51最小开发板使用记录及virtualbox相关"
date: 2013-06-10 16:48
comments: true
tags: 51 vbox
---

最近对51开发板感兴趣, 用[ma6174](http://ma6174.cnblogs.com)的51小板搞了下.  
不过上来就卡住了, 由于笔记本双系统 `ubuntu`+`win8`, 在win8下死活装不上 usb转串口的驱动程序, 只能考虑使用虚拟机. 由于使用的主系统是ubuntu, 所以选择在ubuntn中的`virtualbox`中安装xp.

xp安装不讲  

### usb映射

最需要的虚拟机的一个功能是usb映射, 系统中的vbox是通过ubuntu源安装的, 装好系统后google了好久都没有把usb映射搞好, 在官方论坛中找到了原因, ** ubuntu源安装的不支持usb映射 **...  

官网下载安装好后, 运行提示没有权限控制usb子系统, 需要将用户添加到`vboxusers`用户组.

`"FAILED TO ACCESS THE USB SUBSYSTEM.....`

执行:
{% highlight bash %}
	sudo usermod -a -G vboxusers youruser
{% endhighlight %}

建议注销一下

`-a` 参数是将你的用户添加到新的用户组而不将你从原来的用户组中删除.

现在已经能够进行usb映射了,如果是笔记本的话还能够自动识别内置摄像头.

![usb](/images/a/51-1.jpg)

### STC ISP 握手失败  
提示信息

	Chinese:正在尝试与 MCU/单片机 握手连接 ...
	Chinese:连接失败，请尝试以下操作：
	 1.在单片机停电状态下，点下载按钮，再给单片机上电
	...
	 仍在连接中, 请给 MCU 上电...
	MCU Type is: STC89C52RC
	MCU Firmware Version: 4.3C
	Chinese:MCU 固件版本号: 4.3C
	Double speed / 双倍速:          12T/单倍速
	振荡放大器增益:                  full gain
	下次下载时 P1.0/P1.1 与下载无关
	内部扩展AUX-RAM:        允许访问(强烈推荐)
	下次下载用户应用程序时将数据Flash区擦除: NO
	用户软件启动内部看门狗后:     复位关看门狗
	内部时钟频率:11.059326M.
	外部时钟频率:11.059326M.
	Chinese:正在重新连接 ...
	Connection failed. / 握手失败 (End: 17:23:05)

在 [这里](http://www.amobbs.com/thread-4453586-1-1.html)找到了一个原因:  
> STC单片机下载引导程序需要CPU完全断电，注意：完全断电！完全断电！完全断电！

> 1、要知道电源并非只从VCC进入，其他管脚也可能有微弱电流，至于多大，并不是非得达到CPU工作的电流。  
> 2、说到这里，大家可能明白了一点，微弱电源就是从你已经连好的ISP下载线进入了，下载线供电能力，有个体和偶然因素，所以很多人换根线或是改改波特率就好了，会判断是下载线不兼容的假像！这个假相迷惑了数代有识青年，并当做教本教育下一代，呵呵。  
> 3、问题如何解决：STC串口线TXD串一个300-500欧电阻、RXD串一个IN4148，保证你从此告别STC下载烦劳。  

我串联了两个180欧的电阻接上后还是握手失败, 又没有IN4148, 遂把最高波特率和最低波特率都改成`2400`, 了事.

	Current Baud is: / 当前波特率为: 2400 bps.
	We are erasing MCU flash...
	正在擦除应用程序区... ( 00:01 )
	正在下载... ( 开始时间: 17:46:48 )
	Program OK / 下载 OK
	Verify  OK / 校验 OK
	erase times/擦除时间 :  00:01
	program times/下载时间: 00:15
	Encrypt OK/ 已加密
