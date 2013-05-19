---
layout: post
title: "djando 使用css、js等静态文件"
date: 2012-11-15 20:39
comments: true
categories: djando
---

django 的url默认是动态生成，动态访问的，django本身不会处理静态文件的，所以为使用静态文件例如css、js等，就需要配置下。
	#url.py
	from django.conf import settings
	.
	.
	.
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'static_root':settings.STATIC_ROOT}),


	setting.py

	STATIC_ROOT = 'templates/static'
	# URL prefix for static files.
	# Example: "http://media.lawrence.com/static/"

	STATIC_URL = '/static/'

	STATICFILES_DIRS = (
		"templates/static/css",
		"templates/static/js",
		"templates/static/image",
		"templates/static/img",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	)

网页文件
	page.html
	<head>
    {% load static %}
    <link rel="stylesheet" href="{% static "bootstrap.css" %}" type="text/css" media="screen">
	</head>
	
	<div id="button" class="btn-group">
	   <a href="{%url login%}" class="btn badge-success">登陆</a>
	</div>
