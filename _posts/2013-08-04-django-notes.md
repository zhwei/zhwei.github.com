---
layout: post
title: "django相关笔记"
date: 2013-08-04 22:09
comments: true
tags: django python
menu: true
---

# 权限判断的装饰符

## 判断用户是否staff
is_staff isn't a permission so instead of permission_required you could use:

{% highlight python %}
    @user_passes_test(lambda u: u.is_staff)

    #或者

    from django.contrib.admin.views.decorators import staff_member_required
    @staff_member_required
  
{% endhighlight %}

[link](http://stackoverflow.com/questions/5833184/django-is-staff-permission-decorator)

## 如果已经登陆则跳转

### 适用于方法

{% highlight python %}

def ver_not_login(func):
    def ver(*args):
        request = args[0]
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return func(request)
    return ver

{% endhighlight %}

#### 使用

{% highlight python %}

@ver_not_login
def register(request):
    pass

{% endhighlight %}

### 适用于url

{% highlight python %}

def ver_not_login_with_template(func):
    def ver(*args, **kwargs):
        request = args[0]
        template_name = kwargs['template_name']
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return func(request, template_name)
    return ver

{% endhighlight %}


#### 使用

{% highlight python %}
url(r'^$', ver_not_login_with_template(login),
     {'template_name':'login.html'},
  ),
{% endhighlight %}

# 用户操作相关

## 组管理

添加用户到组
{% highlight python %}

dian = Group.objects.filter(name='dian')[0] 
user.groups.add(dian)

{% endhighlight %}

# 其他

## 调用django项目环境

{% highlight python %}

  from django.core.management import setup_environ
  import webtest.settings
  setup_environ(webtest.settings)

{% endhighlight %}

## django form ChoiceFields

遇到 too many values to unpack

choice 格式 ("label":"内容"),("label":"内容"),


遭遇 `IOError: decoder jpeg not available`

安装libjpeg8-dev

此处使用PIL或者pillow均可以，只要修改setup.py文件中库的引用位置

http://three99.com/posts/how-to-install-pil-on-ubuntu-with-jpeg-support/
