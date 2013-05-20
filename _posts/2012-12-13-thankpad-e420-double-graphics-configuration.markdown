---
layout: post
title: "thankpad E420 ubuntu 双显卡配置"
date: 2012-12-13 15:19
comments: true
tags: ubuntu
---
###首先卸载曾经的显卡驱动
	sudo apt-get remove --purge fglrx  fglrx-amdcccle  fglrx-dev  
###安装闭源前准备的库
	sudo apt-get install build-essential cdbs fakeroot dh-make debhelper debconf libstdc++6 dkms libqtgui4 wget execstack libelfg0 dh-modaliases linux-headers-generic  

###如果是64位ubuntu,安装32位库:
	sudo apt-get install ia32-libs  


###然后下载最新催化剂驱动  
	wget http://www2.ati.com/drivers/linux/amd-driver-installer-catalyst-12.10-x86.x86_64.zip  
	unzip amd-driver-installer-catalyst-12.10-x86.x86_64.zip  
	chmod +x amd-driver-installer-catalyst-12.10-x86.x86_64.run   

<!--more-->
###创建`deb`安装包并安装  
	sudo sh ./amd-driver-installer-catalyst-12.10-x86.x86_64.run --buildpkg Ubuntu/precise  
	sudo dpkg -i fglrx*.deb    

###生成配置文件：  
	sudo aticonfig --initial -f  

###防止配置未生效：
	sudo aticonfig --input=/etc/X11/xorg.conf --tls=1  

重启检查是否成功
	fglrxinfo  

以上来自[Ubuntu Precise Installation Guide](http://wiki.cchtml.com/index.php/Ubuntu_Precise_Installation_Guide#Installing_Catalyst_Manually_.28from_AMD.2FATI.27s_site.29)    

实测后报错  
	X Error of failed request:  BadRequest (invalid request code or no such operation)  

有重新执行了一遍,删除了`xorg.comf` 文件
	sudo apt-get install --reinstall libgl1-mesa-glx:i386 libgl1-mesa-dri:i386 xserver-xorg-core    
	sudo dpkg-reconfigure xserver-xorg  

重启后成功了.
