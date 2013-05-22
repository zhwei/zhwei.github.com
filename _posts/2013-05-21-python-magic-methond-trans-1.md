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

什么事魔法方法? 它是面向对象的python中的所有东西. 它们是你能够自己向类中定义的特殊方法, 能够给你的类带来魔法般的效果! 它们以`__`开头以`__`结尾(eg: `__init__`或者`__lt__`). 它们的文档也比所期望的要少得多. python魔法方法总是出现在python文档的相同部分, 但是总是松散的, 并且很难在其中找到响应的案例, 当然也有可能是故意的, 所有的魔法方法在_语言参考 (language reference)_都有详细地列了出来, 附加还有令人厌烦的语法说明等等.

所以呢, 为了修复我所感受到的python文档的不完美之处, 我着手为python魔法方法准备一些更简明并且有详细案例的文档. 我开始每周整理一篇博客, 到现在为止我已经全部完成了, 整理成了这篇指导. 

我希望你能喜欢, 把它当做一篇教程 复习资料或者参考, 我仅仅希望他能作为一篇人性化的python魔法方法指导. 


## 构造和初始化

每个人都知道最基础的魔法方法`__init__`, 我们可以用它来定义对象的初始化行为. 然而, 当我们调用`x = SomeClass()`时, `__init__`却不是第一个被调用的方法, 实际上被第一个调用的方法叫做`__new__`, 是它创建的实例并且将所有参数在创建的同时转递给初始化器. 在对象的预期的存活期限有一个`__del__`方法, 下面我们详细看下这三个方法:

+ `__new__(cls, [...)`  
 
	- `__new__` 是在对象的初始化时调用的第一个方法, 它取走类然后将其他参数都传递给`__init__`, `__new__`用的真的很少, 但它也有其独到之处, 尤其是在将一个不可变的类型(例如元组或者字符串)子类化的时候. 我不想研究太多`__new__`的细节, 因为它用的真不怎么多, 但在[python文档](http://www.python.org/download/releases/2.2/descrintro/#__new__)里有详细的介绍.
	
+ `__init__(self, [...)`  
 
	- 类的初始化器. 它获取在主要构造函数被调用时伴随的所有参数(例如: 我们在调用`x = SomeClass(10, 'foo'))`时, `__init__`获取`10`和`'foo'`作为参数. 在python类的定义时, 几乎人人都能用到`__init__`.
	
+ `__del(self)__`

	- 如果`__new__`和`__init__`组成了对象的构造函数, 那么`__del__`就是析构函数. 它的功能不是通过`del x`来实现(那样的话代码会被转换成`x.__del__()`). 事实上, 它定义了当一个对象在垃圾回收时候的行为, 它对那些有可能不仅仅需要删除还需要额外清理的对象非常有用, 就像sockets或者文件对象(file objects). 但是要小心, 因为`__del__`没有任何保证不会在对象存活时间或者当解释器正在运行的时候运行. 所以`__del__`不能当做好的编码实践的替代品(有可能经常在你正在处理的时候断开链接). 其实, `__del__`最好永远不用, 因为当你调用它之后你已经处于"危险环境"之内, 一定要小心使用!


这里有一个`__init__`和`__del__`在实际中的使用:

```::python
	from os.path import join

	class FileObject:
		'''Wrapper for file objects to make sure the file gets closed on deletion.'''

		def __init__(self, filepath='~', filename='sample.txt'):
			# open a file filename in filepath in read and write mode
			self.file = open(join(filepath, filename), 'r+')

		def __del__(self):
			self.file.close()
			del self.file
```
