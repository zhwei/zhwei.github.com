---
layout: post
title: "django从一个form保存到两个model"
date: 2014-10-25 21:37
comments: true
tags: django
---

```python

    from django.forms.models import model_to_dict, fields_for_model

    class UserDetailsForm(ModelForm):
        def __init__(self, instance=None, *args, **kwargs):
            _fields = ('first_name', 'last_name', 'email',)
            _initial = kwargs.pop('initial') # pop出initial参数
            _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
            super(UserDetailsForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
            self.fields.update(fields_for_model(User, _fields))

        class Meta:
            model = UserDetails
            exclude = ('user',)

        def save(self, *args, **kwargs):
            u = self.instance.user
            u.first_name = self.cleaned_data['first_name']
            u.last_name = self.cleaned_data['last_name']
            u.email = self.cleaned_data['email']
            u.save()
            profile = super(UserDetailsForm, self).save(*args,**kwargs)
            return profile
```
取自 http://stackoverflow.com/questions/15889794/creating-one-django-form-to-save-two-models

不过原文中的代码会出现 `__init__() got multiple values for keyword argument` 报错。

是因为kwargs中已经包含initial参数，而在调用父类的初始化方法时候将initial独立传递, 这样就造成了传递了两次 initial参数，所以会报出上面的错误。只要将 initial从kwargs中pop出来就可以了。