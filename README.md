zhwei 的学习笔记
===========

+ 原生`jekyll`, 没有使用插件
+ 模板修改自[Greyshade](htt,kjkp://shashankmehta.in/archive/2012/greyshade.html)
+ 博客文章直接放在`_post`下


为了书写方便, 编写了`generte.py`脚本, 具体功能:

+ 创建博客文章, 有相关参数为博客标题
+ 打开最近创建的博客文章, 可以加参数使其打开 倒数第n篇文章
+ 匹配关键词并打开文章, 可重复输入关键词, 直至匹配出单篇文章. 也可以直接输入提示的序号打开某篇文章.

详细操作:

`generte.py --help`
