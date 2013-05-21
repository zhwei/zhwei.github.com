---
layout: post
title: "[翻译]python魔法方法指导(1)"
date: 2013-05-21 19:48
comments: true
tags: trans python magic
---

# A Guide to Python's Magic Methods | python魔法引导

## 原文作者:[Rafe Kettler](http://www.rafekettler.com)
### 原文链接: http://www.rafekettler.com/magicmethods.html
### Copyright © 2012 Rafe Kettler
### Version 1.17

本文档的英文pdf版本在[pdf](http://www.rafekettler.com/magicmethods.pdf)或者[Github](https://github.com/RafeKettler/magicmethods/raw/master/magicmethods.pdf). 我在[这里](http://www.github.com/RafeKettler/magicmethods)建了一个repo, 所有的issues可以在那里报告, 当然也可是是评论, 更可以是赞助!

内容列表:

1. [介绍]()
1. [构造和初始化]()
1. [在任意类中使用运算符]()
	- [比较魔法方法]()
	- [数值魔法方法]()
1. [类的表现形式]()
1. [属性访问控制]()
1. 



## 介绍

这篇方法引导总结了几个月来的博客文章. 它的标题是魔法方法.  

什么事魔法方法? 它是面向对象的python中的所有东西. 它们是你能够自己向类中定义的特殊方法, 能够给你的类带来魔法般的效果! 它们以`__`开头以`__`结尾(eg: `__init__`或者`__lt__`). 它们的文档也比所期望的要少得多(翻译中...)
