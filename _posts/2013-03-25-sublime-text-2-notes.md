---
layout: post
title: "sublime text 2 备忘"
date: 2013-03-25 21:39
comments: true
tags: Notes
---
### 安装包管理

**Ctrl + `**
	import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'
回车

### 快捷键

安装插件,以Alignment为例

	Shift + Ctrl + p
	install
	alignment

代码补齐

	Shift + Ctrl + a

### zencoding

	Ctrl + Alt + Enter
	div#page>div.logo+ul#navigation>li*5>a

	<div id="page">
			<div class="logo"></div>
			<ul id="navigation">
					<li><a href=""></a></li>
					<li><a href=""></a></li>
					<li><a href=""></a></li>
					<li><a href=""></a></li>
					<li><a href=""></a></li>
			</ul>
	</div>

### vim模式

Shift + Ctrl + P
输入settings user 调出Preferences：Settings - User
打开Preferences.sublime-settings文件
将文件中方括号中的"Vintage"删掉，sublime默认是将其ignored的
最后是酱紫滴：

	{
		"ignored_packages":[]
	}

### jinjia2

插件jinjia2方便jinjia2模板语言的书写, 初始化文件
ctrl + shift + p
ssjinjia

### auto pep8插件

rt
快捷键

	ctrl + shift +8  自动排版
	ctrl + 8 预览

