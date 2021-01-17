---
comments: true
date: "2013-05-20T00:00:00Z"
tags:
    - SQL
title: sql备忘
---

### mysql初始化密码

	/etc/init.d/mysql stop
	# mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
	# mysql -u root mysql
	mysql> UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
	mysql> FLUSH PRIVILEGES;
	mysql> quit

	# /etc/init.d/mysql restart
	# mysql -uroot -p
	Enter password: <输入新设的密码newpassword>

###获取最后n个字段

建临时表带自动增1的id字段

	select top 5 * from temp_table order by id desc
