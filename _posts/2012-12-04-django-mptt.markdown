---
l ayout: post
title: "dajngo-mptt向数据库中存储层级结构"
date: 2012-12-04 13:52
comments: true
categories: django
---
###MPTT
在为多层分类向数据库中存储犯愁时找到的一个解决方案,Django-mptt是个Django第三方组件，目标是使Django项目能在数据库中存储层级数据（树形数据）。它主要实现了修改过的前序遍历算法。如果项目不是使用的Django，可以参考具体的实现原理.  
###安装:  
	easy_install-2.7 django-mptt
官方文档:[http://django-mptt.github.com/django-mptt/index.html](http://django-mptt.github.com/django-mptt/index.html)  
github:[https://github.com/django-mptt/django-mptt](://github.com/django-mptt/django-mptt)  
###使用案例:  
####model:  
	from mptt.models import MPTTModel
	
	class Sorts(MPTTModel):
		name=models.CharField(max_length=20,verbose_name="分类名称",unique=True)
		parent=TreeForeignKey("self", blank=True, null=True, related_name="children")

####view:  
	#显示  
	def show_sort(request):
	    return render_to_response(
				"goods/show_sort.html",
				{'nodes':Sorts.objects.all()},
				context_instance=RequestContext(request)
				)
	#新建分类
	Sorts.objects.create(name = 'name' , parent = parent_instance)
	
	parent_instance 必须是已存在的Sorts实例

####template:  
	{% load mptt_tags %}
	<ul>
		 {% recursetree nodes %}
			<li>
				{{ node.name }}
				{% if not node.is_leaf_node %}
					<ul class="children">
						 {{ children }}
					</ul>
				{% endif %}
			</li>
		 {% endrecursetree %}
	</ul>	
