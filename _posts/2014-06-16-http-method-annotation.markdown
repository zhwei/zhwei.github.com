---
layout: post
title: "HTTP请求方式注解"
date: 2014-06-16 13:19
comments: true
tags: Notes
menu: true
---

被问到了HTTP常见的几个方法，也有些迷惑的地方，整理如下。

# GET

GET是http的默认请求方式， 一般用来获取数据， 传输的数据经过url编码后放在路径`?`之后， 多个键值对通过`&`连接， 另外get的传输长度一般不推荐超过255个字节。


GET方法一般被视为安全方法， 因为它仅用来获取数据而不会对服务器有其他改动。

> **安全方法**  
> 像HEAD、GET、OPTIONS 和 TRACE这几种http方法是被认为是“安全的”， 这意味着它们只会进行获取数据而不会修改服务器的状态， 换句话说，它们不会产生负面影响， 当然除了常见的无害操作，比如记录日志、创建缓存或者创建其他统计信息。  
> 正相反， 像POST、PUT、DELETE 和 PATCH 等方法是有可能产生副作用。网络爬虫等一般不会使用这些方式(笔者注:搜索引擎的暗网抓取可能会使用这些方法)。  
> 尽管GET方法是一般被视为“安全的”，但如果在实际使用中没有做任何设置，比如可以无限制的抓取等情况， 也会导致一些不可预料的问题，比如web缓存或者搜索引擎问题。  

# POST

POST一般用来上传文件或者提交一个完整的web表单。  

这是Chrome中查看到的POST内容  
![Chrome中查看POST内容](http://ww1.sinaimg.cn/large/9f62afa1tw1ehfyundfwpj20bw03zt90.jpg)

实际数据是这样的  

```
user=554101&user_code=eNWyXdrrTpC6hoSvzPHBYKLljGkcDw79QsWtNeMu&attachment=0&code_brush=&code_snippet=&msg=test
```

浏览器中提交表单时，这里与get类似，每个键值对都是通过`&`分割, 其他非字母数字会进行url转码。

**为什么一些请求会使用POST提交数据?**

+ GET请求数据都可以在URL中看到
+ GET提交的数据都会有长度限制
+ 一般规范，POST用来修改数据，GET用来获取数据
+ **GET请求请提交的数据放置在HTTP请求协议头中，而POST提交的数据则放在实体数据中**

# 其他请求方式

## HEAD

获取某个URI响应头信息，基本与GET相同但是不返回响应主体。

## PUT

通过提供的URI获取到特定的内容主体，如果存在则修改内容，如果不存在则创建。

## DELETE

通过URI删除指定内容

## TRACE

返回接受到的请求，用来查看数据经过中间服务器时发生了哪些变动

## OPTIONS

返回给定URL支持的所有HTTP方法

## CONNECT

要求使用SSL和TLS进行TCP通信

## PATCH

请求修改局部数据

# 参考链接

+ [http://en.wikipedia.org/wiki/POST_(HTTP)](http://en.wikipedia.org/wiki/POST\_\(HTTP\))
+ [http://en.wikipedia.org/wiki/GET_(HTTP)](http://en.wikipedia.org/wiki/GET\_\(HTTP\)#Request_methods)
