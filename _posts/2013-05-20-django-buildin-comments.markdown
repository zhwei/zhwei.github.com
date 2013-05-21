---
layout: post
title: "django自带comments模块"
date: 2012-05-20 21:37
comments: true
tags: django
---
[官方文档](https://docs.djangoproject.com/en/dev/ref/contrib/comments/)

### 初始化

添加app&&更新数据库&&添加URL

	INSTALLED_APPS=(‘django.contrib.comments’,)
	python manage.py syncdb
	url(r'^comments/', include('django.contrib.comments.urls')),

### 在模板中使用comments

在模板文件中加载comments这个模板标签：

	{%load comments%}

获取评论列表并显示

	{%get_comment_list for [object] as comment_list %}
	{%for comment in comment_list%}
		<p>on {{comment.submit_date|date:”F,j,Y”}}, {{comment.user_name}} said: {{comment.comment|safe}}</p>
	{%endfor%}

添加评论

	{%render_comment_form for [object]%}

自定义评论表单

        {% get_comment_form for com as form %}
    <form action='{%comment_form_target%}' method='post'>
        {% csrf_token %}{{form.object_pk}}{{form.content_type}}
        {{form.timestamp}}{{form.security_hash}}
        <div class="detail dl-msg"><table><tr>
	  <td class="infoName"><label for="id_name">
	  <strong>姓名（必填）：</strong></label></td>
	  <td class="infoContent"><input name="name" id="id_name"></td></tr>
          <tr><td class="infoName"><label for="id_email">
          <strong>邮箱（必填）：</strong></label></td>
          <td class="infoContent"><input name="email" id="id_email"></td></tr>
          <tr><td class="infoName"><label for="id_comment">
          <strong>评论：</strong>(请填写必要的联系信息,以便服务人员与您联系)</label></td>
          <td class="infoContent">
          <textarea name="comment" id="id_comment" rows="15" style="width:520px;">
          </textarea></td></tr>
          <tr><td></td><input type="hidden" name="next" value="{% url comments-comment-done %}"/></td>
          <td><input name="post" value="提交留言" type="submit"  /></td>
          </tr></table>
        </div>
    </form>
#### 提交后重定向 ->{%url comments-comment-done%}

	<input type=”hidden” name=”next” value=”{%url comments-comment-done%}”/>

#### 显示评论数量 comment_count

	{%get_comment_count for [object] as comment_count %}

详细见[http://newliu.com/post/11/](http://newliu.com/post/11/)
