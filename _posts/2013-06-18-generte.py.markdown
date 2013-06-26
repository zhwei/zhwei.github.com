---
layout: post
title: "本站用的管理工具"
date: 2013-06-18 20:36
comments: true
tags: blog
---

脚本可见 [https://gist.github.com/zhwei/5613474](https://gist.github.com/zhwei/5613474)  


## 字典排序 line.118

{% highlight python %}

dict1 = sorted(dict1.iteritems(),
    key=lambda k_v: (k_v[1], k_v[0]),
    reverse=True)  # 字典按值排序, 生成元组列表

{% endhighlight %}

通过 `.iteritems()`方法将字典转化成元组列表, 然后按元组的第二元素进行排序.


## 文章查找  line.128

将博客文件读入列表  
对每一元素`pop()`使用`find()`方法查找关键词, 如果找到则将其插入列表首部, 循环一个列表长度后剩下的元素均是包含关键词的

{% highlight python %}
      for key in keys:
        i = 0
        leng = len(artlist)
        while i < leng:
            d = artlist.pop()
            if d.find(key) != -1:
                artlist.insert(0, d)
            else:
                pass
            i = i + 1
{% endhighlight %}

然后可以再将处理后的文章列表作文参数传入, 再次匹配


## 操作git line.177

每次敲git命令也是挺麻烦的, 做了一个全自动的, 除了需要自己写 `commit message`  

需要安装`sh`模块

{% highlight  %}
def git(argv):
    """
    将修改提交到git仓库
    """
    try:
        import sh
        git = sh.git.bake(_cwd=ROOT_FILE)  # 初始化 git, ROOT_FILE 为 .git 文件夹所在目录
    except ImportError:
        print("请安装 sh 模块")
 
    try:
        argv[2]          # 如果还有其他参数就返回 git status
        print(git.status())
    except IndexError:
        print(git.add("."))
        print(git.status())
        m = raw_input("|--commit message -->")
        print(git.commit(m=m))
        os.chdir(ROOT_FILE)
        print("|--pushing to " + ORIGIN)
        os.system("git push origin " + ORIGIN)
{% endhighlight %}

  git = sh.git.bake(_cwd=ROOT_FILE)  

初始化 git, ROOT_FILE 为 .git 文件夹所在目录
