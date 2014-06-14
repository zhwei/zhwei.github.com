---
layout: post
title: "Web敏捷开发"
date: 2014-06-13 19:21
comments: true
tags: 
menu: true
---

## 什么是敏捷开发

一种应对快速变化的需求的一种软件开发能力。

> 它们的具体名称、理念、过程、术语都不尽相同，相对于“非敏捷”，更强调程序员团队与业务专家之间的紧密协作、面对面的沟通（认为比书面的文档更有效）、频繁交付新的软件版本、紧凑而自我组织型的团队、能够很好地适应需求变化的代码编写和团队组织方法，也更注重软件开发中人的作用。

### 工具集

+ Git
  - 版本控制
  - 缺陷报告

+ Trello
  - 进度跟踪
  - 工作分配

- 持续集成


## Web敏捷开发

### 网站开发组成部分

+ 数据库
+ 业务逻辑
+ 访问控制
+ 前端设计

### 我的选择

**Django**

The Web framework for perfectionists with deadlines.

> Django makes it easier to build better Web apps more quickly and with less code.

+ ORM
  - 用于实现面向对象编程语言里不同类型系统的数据之间的转换
  - 优势
    - 避免手写复杂的SQL语句和SQL注入场景

        ```python
        from django.db import models
        from ckeditor.fields import RichTextField

        class Pages(TimeStampedModel):
            """
            Pages
            """

            title = models.CharField(verbose_name='标题', max_length=100)
            content = RichTextField(verbose_name='内容', config_name="default")

            mark = models.CharField(verbose_name='唯一标志', unique=True, max_length=20)

            class Meta:
                verbose_name = "页面"
                verbose_name_plural = "  页面"

            def __unicode__(self):
                return self.title
        ```

    - 通过面向对象变成的方式操作数据库

        ```python
        class TimeStampedModel(models.Model):
            """工具类
            用来给你的model添加下面两个字段，分别是创建时间和更新时间
            Usage: class YourModel(TimeStampedModel): ...
            """

            created_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
            updated_date = models.DateTimeField(verbose_name='更新时间', auto_now=True)

            class Meta:
                abstract = True
        ```

+ Admin Site
  - 经过简单配置即可拥有完备后台

      ```python
      class DownloadAdmin(admin.ModelAdmin):

          list_display = ('name', 'description', 'download_link', 'created_date')
          list_filter = ('created_date',)
          search_fields = ('name', 'description', )
          form = forms.UploadFileForm

          fieldsets = (
              (None, {
                  'fields': ('document', 'description')
              }),
              ('Advanced options', {
                  'classes': ('collapse',),
                  'fields': ('name',)
              }),
          )

          def download_link(self, obj):
              link = "<strong><a href={0}>下载</a></strong>".format(reverse('file',
                                             kwargs=dict(file_id=obj.id)))
              return mark_safe(link)
          download_link.short_description = "下载链接"

          def delete_model(self, request, obj):
              storage, path = obj.document.storage, obj.document.path
              super(DownloadAdmin, self).delete_model(request, obj)
              storage.delete(path)

      admin.site.register(models.Download, DownloadAdmin)
      ```

  - 高度可定制
    ![添加页面](http://ww4.sinaimg.cn/large/9f62afa1gw1ehdena1b2hj213j0irabk.jpg)

+ Views
  + Generic View

      ```python
      class RegisterMeeting(generic.CreateView):
          """
           注册会议
          """
          model = models.Members
          template_name = "register.html"
          success_url = '/'

          def get_success_url(self):
              messages.success(self.request, "注册成功！")
              return reverse_lazy("index")
      ```

+ Template
  - 分离设计和逻辑
  - 灵活可扩展

+ Others
  + 优雅的URL
  + Cache
  + 国际化

**Bootstrap**

简洁、直观、强悍、移动设备优先的前端开发框架，让web开发更迅速、简单。

+ 响应式
+ 丰富的第三方工具
+ 完善的文档

