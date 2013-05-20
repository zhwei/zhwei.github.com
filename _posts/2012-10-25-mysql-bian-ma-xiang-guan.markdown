---
layout: post
title: "mysql 编码相关"
date: 2012-10-25 21:39
comments: true
tags: mysql
categories: sql,encode
---
### 配置文件 my.cnf ###

	默认字符集为 utf-8
	default-character-set = utf-8
	character-set-server= utf-8

<!--more-->
### mysql 命令 ###
	mysql设置编码命令 

	SET character_set_client = utf8; 
	SET character_set_connection = utf8; 
	SET character_set_database = utf8; 
	SET character_set_results = utf8;/*这里要注意很有用*/ 
	SET character_set_server = utf8; 

	SET collation_connection = utf8_bin; 
	SET collation_database = utf8_bin; 
	SET collation_server = utf8_bin; 


	#查看数据库编码
	show variables like 'characte%';

	+--------------------------+----------------------------+
	| Variable_name | Value |
	+--------------------------+----------------------------+
	| character_set_client | utf8 | 
	| character_set_connection | utf8 | 
	| character_set_database | utf8 | 
	| character_set_filesystem | binary | 
	| character_set_results | utf8 | 
	| character_set_server | utf8 | 
	| character_set_system | utf8 | 
	| character_sets_dir | /usr/share/mysql/charsets/ | 
	+--------------------------+----------------------------+

	#创建数据库时指定编码

	#GBK: 
	create database test2 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
	#UTF8: 
	CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci

	#数据库连接串中指定字符集
	URL=jdbc:mysql://yourIP/college?user=root&password=yourPassword&useUnicode=true&characterEncoding=gbk
