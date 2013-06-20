---
layout: post
title: "zhwei@Notes:~$"
date: 2013-05-25 15:41
comments: false
tags: note
customcss: <link rel="stylesheet" href="/stylesheets/cusli.css" />
---

+ django 使用 tinymce1.5.1, 同步生成数据库时, 会出现`ImportError: cannot import name smart_unicode`报错, 在其官方[issue](https://code.google.com/p/django-tinymce/issues/detail?id=63) 已有提出, 可以手动将`...site-packages/tinymce/widgets.py`文件第14行改成 `from django.utils.encoding import smart_unicode`

+ django 使用 image model 时需要安装 PIL ,在 virtualenv 使用时需要再次安装, apt 安装的python-imaging 并不起作用, 可以在 [link](http://www.pythonware.com/products/pil/) 下载到包, 已经下载并保存到dropbox.

+ django自定义表单工具 autoforms
+ coffee 中 `@` = `this`
+ ubuntu 中virtualbox安装extension pack 时使用root或者sudo运行, 否则无法安装
+ ubuntu安装virutalbox最好是在官网安装, 通过ubuntu源安装的不能使用usb映射.
+ 查看git库中各个用户提交的次数,并且递减排序 `git shortlog -sn`
+ virtualbox下的windowns虚拟机需要先安装**VBoxGuestAdditions**才能成功创建共享文件夹或者共享剪贴板. `Dives->Install Guest Additions`
+ 正则表达式匹配时, 加`?`表示非贪心匹配, 直接匹配最近的符合项. eg: `<p>.*?</p>`
+ python 字符串比较, `cmp(a, b)`, 相同时返回 `0`
