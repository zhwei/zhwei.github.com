---
layout: post
title: "my nook color"
date: 2012-11-10 16:06
comments: true
categories: nook
---
##入手
* * *
前几天入手的nook color，新刷的cm7系统，主要是为了看书购入的，感觉还不错，ips屏还是比较给力的。  
![正面](http://pic.yupoo.com/waqei_v/Cpdaqzbo/14tRpy.jpg)  

还有一个号称二十美刀的原装皮套，不过感觉好沉。。。  
![皮套](http://pic.yupoo.com/waqei_v/CpdapX9W/pV950.jpg)  
![皮套2](http://pic.yupoo.com/waqei_v/CpdaqExr/N4JFS.jpg)  

##使用
*  * *
cm7默认将内置存储挂载到emmc，但是软件安装是要求必须有内存卡，在购进一个card太麻烦了，看了一下cm7的fstab  
位置：/system/etc/vold.fstab
	
	dev_mount sdcard /mnt/sdcard auto /devices/platform/mmci-omap-hs.1/mmc_host/mmc1
	
	#改成

	dev_mount sdcard /mnt/sdcard 8 /devices/platform/mmci-omap-hs.1/mmc_host/mmc0

pdf mobi epub 阅读用的是静读天下专业版  
html用 iReader
