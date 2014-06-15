---
layout: post
title: "[翻译]A Guide to Python's Magic Methods"
date: 2013-05-21 19:48
comments: true
tags: Trans
---

> 原文作者:[Rafe Kettler](http://www.rafekettler.com)  
> 原文链接: [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)  
> Copyright © 2012 Rafe Kettler  
> Version 1.17  
>
> 本文档的英文pdf版本在[pdf](http://www.rafekettler.com/magicmethods.pdf)或者[Github](https://github.com/RafeKettler/magicmethods/raw/master/magicmethods.pdf). 我在[这里](http://www.github.com/RafeKettler/magicmethods)建了一个repo, 所有的issues可以在那里报告, 当然也可是是评论, 更可以是赞助!

内容列表:

  1. [介绍]()
  1. [构造和初始化]()
  1. [在任意类中使用运算符]()
    - [比较 magic methods]()
    - [数值 magic methods]()


## 介绍

  这篇方法引导总结了几个月来的博客文章. 它的标题是 magic methods.  

  什么事 magic methods? 它是面向对象的python中的所有东西. 它们是你能够自己向类中定义的特殊方法, 能够给你的类带来魔法般的效果! 它们以`__`开头以`__`结尾(eg: `__init__`或者`__lt__`). 它们的文档也比所期望的要少得多. python魔法方法总是出现在python文档的相同部分, 但是总是松散的, 并且很难在其中找到响应的案例, 当然也有可能是故意的, 所有的魔法方法在_语言参考 (language reference)_都有详细地列了出来, 附加还有令人厌烦的语法说明等等.

  所以呢, 为了修复我所感受到的python文档的不完美之处, 我着手为python magic methods准备一些更简明并且有详细案例的文档. 我开始每周整理一篇博客, 到现在为止我已经全部完成了, 整理成了这篇指导. 

  我希望你能喜欢, 把它当做一篇教程 复习资料或者参考, 我仅仅希望他能作为一篇人性化的python magic methods指导. 


## 构造和初始化

  每个人都知道最基础的 magic methods`__init__`, 我们可以用它来定义对象的初始化行为. 然而, 当我们调用`x = SomeClass()`时, `__init__`却不是第一个被调用的方法, 实际上被第一个调用的方法叫做`__new__`, 是它创建的实例并且将所有参数在创建的同时转递给初始化器. 在对象的预期的存活期限有一个`__del__`方法, 下面我们详细看下这三个方法:

  + `__new__(cls, [...)`  

  - `__new__` 是在对象的初始化时调用的第一个方法, 它取走类然后将其他参数都传递给`__init__`, `__new__`用的真的很少, 但它也有其独到之处, 尤其是在将一个不可变的类型(例如元组或者字符串)子类化的时候. 我不想研究太多`__new__`的细节, 因为它用的真不怎么多, 但在[python文档](http://www.python.org/download/releases/2.2/descrintro/#__new__)里有详细的介绍.

  + `__init__(self, [...)`  

  - 类的初始化器. 它获取在主要构造函数被调用时伴随的所有参数(例如: 我们在调用`x = SomeClass(10, 'foo'))`时, `__init__`获取`10`和`'foo'`作为参数. 在python类的定义时, 几乎人人都能用到`__init__`.

  + `__del(self)__`

  - 如果`__new__`和`__init__`组成了对象的构造函数, 那么`__del__`就是析构函数. 它的功能不是通过`del x`来实现(那样的话代码会被转换成`x.__del__()`). 事实上, 它定义了当一个对象在垃圾回收时候的行为, 它对那些有可能不仅仅需要删除还需要额外清理的对象非常有用, 就像sockets或者文件对象(file objects). 但是要小心, 因为`__del__`没有任何保证不会在对象存活时间或者当解释器正在运行的时候运行. 所以`__del__`不能当做好的编码实践的替代品(有可能经常在你正在处理的时候断开链接). 其实, `__del__`最好永远不用, 因为当你调用它之后你已经处于"危险环境"之内, 一定要小心使用!


  这里有一个`__init__`和`__del__`在实际中的使用:

{% highlight python %}
from os.path import join

class FileObject:
  '''Wrapper for file objects to make sure the file gets closed on deletion.'''

     def __init__(self, filepath='~', filename='sample.txt'):
      # open a file filename in filepath in read and write mode
       self.file = open(join(filepath, filename), 'r+')

       def __del__(self):
         self.file.close()
         del self.file
{% endhighlight %}


## 让运算符在任意类中使用

python magic methods最大的优势就是能够让对象向内置类型一样进行运算, 并且使用简单! 这就意味着你能够避免使用丑陋 违反语感 不标准的方法来实现基本运算符. 在很多语言中, 通常使用这种方法实现:  

{% highlight python %}
    if instance.equals(other_instance):
        # do something
{% endhighlight %}

  当然你也可以在python中这样实现, 但这样添了很多不必要的麻烦. 不同的函数库也许使用不同的名字来命名相同的操作, 但这样会让客户端做很多额外的工作. 现在见识下 magic methods的强大之处吧, 我们可以定义这样一个方法(在案例中是`__eq__`), 然后我们能够实现:

  {% highlight python %}
      if instance == other_instance:
          #do something
  {% endhighlight %}

  这是python magic methods的强大的一方面, magic methods中的绝大部分是让我们能够定义运算符的实际操作, 从而使我们的类能够像内置类型一样进行各种运算.

### 比较运算 magic methods

  python中设计了大量的魔法方法来通过运算符实现对象之间直观的比较, 而不是调用笨拙的方法。另外也提供了一种方法去通过引用重写Python对象之间默认的比较行为。下面就是这样的一系列方法和用法：

+ `__cmp__(self, other)`

  `__cmp__`方法是比较系列magic methods中最基础的方法。事实上它为其他的比较操作符(`<, ==, !=` 等等)提供了提供了实现的方法,但是他的判断方式或许不是你想要的，比如说，判断某个实例是否与另一个实例相等是依据某个标准而是否大于则是依据另一个标准。`__cmp__`在`self < other`时返回一个负数，相等的时候返回0, `self > other`时返回正数。一般来说，最好分别定义你需要的操作符行为而不是一次性定义全部。但是在当你需要的比较操作都是依赖相似的标准时，`__cmp__`也是一种好方法来避免重复并且也能让代码更整洁。  

+ `__eq__(self, other)`

  定义操作符**==**的行为

+ `__ne__(self, other)`

  定义操作符**!=**的行为

+ `__lt__(self, other)`

  定义操作符**<**的行为

+ `__gt__(self, other)`

  定义操作符**>**行为

+ `__le__(self, other)`

  定义操作符**<=**行为

+ `__ge__(self, other)`

  定义操作符**>=**行为

比如，我们把一个类想做一个单词，我们有可能需要按照字典的规则(字母表的顺序)比较, 而单词默认的比较是按照字符串比较。我们也有可能需要按照其他的标准来比较，诸如长度、数字、音节等，在下面的例子中我们按照单词的长度来比较，下面是具体实现：

{% highlight python %}

class Word(str):
    '''单词类, 依据单词的长度比较单词大小'''

    def __new__(cls, word):
        # 注意到我们用了__new__方法, 因为字符串是不可变类型，这样我们初始化是更加方便。
        if ' ' in word:
            print "单词中包含空格，这里取第一个空格前的单词."
            word = word[:word.index(' ')] # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

{% endhighlight %}


现在我们通过`Wrod("foo") and Word("bar")`可以创建两个实例, 然后通过判断它们的长度比较大小，注意到我们这里没有定义`__eq__`和`__ne__`方法，这是因为如果定义了会导致一些怪异的行为，尤其是判断`Word('foo') == Word('bar')`会返回`True`，这样通过长度判定两个单词相等是没有意义的，所以我们让回落到字符串的范畴中判断是否相等。

其实有时候我们需要大量比较操作的时候并不需要自己定义大量的magic method, 如果你只需要定义`__eq__`或者`__gt__`、`__lt__`等，Python的标准库`functools`中已经提供了一个很友好的类装饰器，这个特性只在Python2.7中可用，如果你有机会使用`@total_ordering`的话一定能节省大量的时间和精力。


### 数值运算魔法方法

就像你可以使用某种方法让类可以通过比较操作符进行比较一样，你也可应定义他们使用数学运算符时的表现行为。睁大眼睛注意了，其实有很多这样的魔法方法，为了条理清晰，我把它们分为五类：一元运算符、普通算数运算符、反射算数运算符(稍后详述)、增量赋值和类型转换。

#### 一元运算符和方法

一元运算符只有一个操作数，比如：取反、绝对值等。

  `__pos__(self)`  
  一元运算符取正值的实现 (e.g. `+some_object`)

  `__neg__(self)`  
  一元运算符取反的实现(e.g. `-some_object`)

  `__abs__(self)`  
  定义使用内置`abs()`方法时的行为

  `__invert__(self)`  
  定义使用内置操作符`～`时的行为，具体实例见[the Wikipedia article on bitwise operations](http://en.wikipedia.org/wiki/Bitwise_operation#NOT)

  `__round__(self, n)`  
  定义使用内置方法`round()`时的行为, `n`是四舍五入时保留的小数位数

  `__floor__(self)`  
  定义调用方法`math.floor()`时的行为， 返回离数字上舍整数

  `__ceil__(self)`  
  定义调用方法`math.ceil()`时的行为， 返回离数字上舍整数

  `__trunc__(self)`  
  定义调用方法`math.trunc()`时的行为， 截取数字的整数部分

#### 常用运算符


现在我们来看下常用的二元运算符以及几个方法(像：`+`，`-`，`*`等等), 这些中的大部分是很通俗易懂的。

  `__add__(self, other)`  
  定义加法

  `__sub__(self, other)`  
  定义减法

  `__mul__(self, other)`  
  定义乘法

  `__floordiv__(self, other)`  
  定义整除

  `__div__(self, other)`  
  定义除法

  `__truediv__(self, other)`  
  定义整数除法，只有在`from __future__ import division` 时使用

  `__mod__(self, other)`  
  定义取模运算

  `__divmod__(self, other)`  
  定义长除法，调用`divmod()`时的行为

  `__pow__(self, other)`  
  定义运算符`**`

  `__lshift__(self, other)`  
  定义左移运算符`<<`

  `__rshift__(self, other)`  
  定义右移运算符`>>`

  `__and__(self, other)`  
  定义按位与，`&`操作符

  `__or__(self, other)`  
  定义按位或，`|`操作符

  `__xor__(self, other)`  
  定义按位异或， `^`操作符
