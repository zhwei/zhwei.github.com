---
layout: post
title: "响应式页面设计"
date: 2013-06-16 21:52
comments: true
tags: CSS
---

要交web基础作业了, 一直没想出做什么页面, 想起自己的博客没有一个**aboutme**页面, 又想学一下响应式布局, 所以, 如你所见: [aboutme](http://zhangweide.cn/about)

要针对不同的终端写不同的 css

这是 bootstrap 的分辨率区间划分

{% highlight css %}

/* 大屏幕 */
@media (min-width: 1200px) { ... }
 
/* 平板电脑和小屏电脑之间的分辨率 */
@media (min-width: 768px) and (max-width: 979px) { ... }
 
/* 横向放置的手机和竖向放置的平板之间的分辨率 */
@media (max-width: 767px) { ... }
 
/* 横向放置的手机及分辨率更小的设备 */
@media (max-width: 480px) { ... }

{% endhighlight %}

首先要在 head 里面加上
{% highlight css %}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{% endhighlight %}

然后在上面大括号中写不同分辨率的 css 样式就可以了


这是我的

{% highlight css %}
/* 大屏幕 */
@media (min-width: 1200px) { .. }

/* 横向放置的手机及分辨率更小的设备 */
@media (max-width: 480px) {

/* 横向放置的手机和竖向放置的平板之间的分辨率 */
@media (min-width: 481px) and (max-width: 767px) {


/* 小显示屏与横向平板之间的分辨率 */
@media (min-width: 768px) and (max-width: 979px) {


/* 大屏小屏之间的分辨率 */
@media (min-width: 980px) and (max-width: 1199px) {

{% endhighlight %}

在某一分辨率区间的css时, 我的做法是直接将网页内容宽度直接定义为分辨率区间的最小值:

{% highlight css %}

/* 小显示屏与横向平板之间的分辨率 */
@media (min-width: 768px) and (max-width: 979px) {

.container {
  width: 768px;  /* <-- */
  margin-left: auto;
  margin-right: auto;
}
{% endhighlight %}

这样可以保证在此区间变动时, 网页样式不会发生变化.

## OT

一个简单的jquery对话框例子

{% highlight javascript %}
    $(document).ready(function(){
        $('#me').click(function(){$('#layer').fadeIn();});    //弹出层
        $('#close').click(function(){$('#layer').fadeOut();});    //关闭层
    });
{% endhighlight %}

点击 #me 的元素时, 弹出对话框, 对话框内容为 #layer, 可以在 #layer 中添加链接 #close , 点击可以关闭对话框.
