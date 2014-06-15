---
layout: post
title: "vagrant 备忘"
date: 2013-01-25 21:37
comments: true
tags: Notes
---

![](http://www.vagrantup.com/images/logo_vagrant-81478652.png)


### 安装

	gem install vagrant

### Vagrant Official Boxes
[https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Boxes](https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Boxes)

### 使用

	第一次使用,进入工作目录
	vagrant box add lucid32 http://files.vagrantup.com/lucid32.box
	#初始化虚拟机
	vagrant init lucid32
	#启动虚拟机
	vagrant up
	#ssh进入
	vagrant ssh
	#关闭虚拟机
	vagrant halt
	#打包虚拟机
	vagrant package --output base-ubuntu-rvm.box

### 配置文件

Vagrantfile
端口转发

	#将虚拟机80端口转发到宿主机8080端口
	config.vm.forward_port 80, 8080
