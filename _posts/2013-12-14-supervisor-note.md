---
layout: post
title: "Supervisor笔记"
date: 2013-12-14 21:37
comments: true
tags: notes
menu: true---

Supervisor是一个C/S系统，用来监控和控制多个服务进程，只限于UNIX-like操作系统。

# 官方文档
http://supervisord.org/

# 安装
setuptools
```

    pip install supervisor
    # or
    easy_install supervisor
```

# 初始使用

## 创建配置文件

需要以root身份执行

    echo_supervisord_conf > /etc/supervisord.conf
## 调整配置文件

+ 增加web管理界面


取消配置文件中的下列行，并按需配置用户名密码
```
    [inet_http_server]
    port=*:9001
    username=your_username           ; (default is no username (open server))
    password=your_password           ; (default is no password (open server))
```

## 添加服务

配置文件详解
```conf

    [supervisorctl]
    serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
    ;serverurl=http://127.0.0.1:9001 ; use an http:// url to specify an inet socket
    ;username=chris              ; should be same as http_username if set
    ;password=123                ; should be same as http_password if set
    ;prompt=mysupervisor         ; cmd line prompt (default "supervisor")
    ;history_file=~/.sc_history  ; use readline history if available
    添加单个进程

    ; 管理单个进程的配置，可创建多个，下面是所有可能的配置选项
    ;[program:theprogramname]
    ;command=/bin/cat              ; 启动进程的命令 使用相对路径，可以加参数
    ;process_name=%(program_name)s ; 进程名称 表达式 (默认 %(program_name)s)
    ;numprocs=1                    ; 进程数目 (def 1)
    ;directory=/tmp                ; 执行命令所在的目录 (def no cwd)
    ;umask=022                     ; 进程默认权限 (default None)
    ;priority=999                  ; 进程启动相对优先权 (default 999)
    ;autostart=true                ; 跟随supervisor启动时启动 (default: true)
    ;autorestart=unexpected        ; 计划启动 (default: unexpected)
    ;startsecs=1                   ; 延时启动 (def. 1)
    ;startretries=3                ; 最多连续启动失败 (default 3)
    ;exitcodes=0,2                 ; 进程结束代码 (default 0,2)
    ;stopsignal=QUIT               ; signal used to kill process (default TERM)
    ;stopwaitsecs=10               ; 最长结束等待时间，否则使用 SIGKILL (default 10)
    ;stopasgroup=false             ; 是否想UNIX进程组发送结束信号 (default false)
    ;killasgroup=false             ; SIGKILL UNIX 进程组 (def false)
    ;user=chrism                   ; 设置启动此程序的用户
    ;redirect_stderr=true          ; 重定向程序的标准错误到标准输出 (default false)
    ;stdout_logfile=/a/path        ; 标准输出的日志路径, NONE for none; default AUTO
    ;stdout_logfile_maxbytes=1MB   ; 日志文件最大值，否则循环写入 (default 50MB)
    ;stdout_logfile_backups=10     ; 标准输出日志备份数目 (default 10)
    ;stdout_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
    ;stdout_events_enabled=false   ; emit events on stdout writes (default false)
    ;stderr_logfile=/a/path        ; 标准错误输出日志路径, NONE for none; default AUTO
    ;stderr_logfile_maxbytes=1MB   ; 日志文件最大值，否则循环写入 (default 50MB)
    ;stderr_logfile_backups=10     ; 标准错误日志备份数目 (default 10)
    ;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
    ;stderr_events_enabled=false   ; emit events on stderr writes (default false)
    ;environment=A="1",B="2"       ; 进程附加环境 (def no adds)
    ;serverurl=AUTO                ; override serverurl computation (childutils)
```

## 添加事件监听器

```conf

    ; The below sample eventlistener section shows all possible
    ; eventlistener subsection values, create one or more 'real'
    ; eventlistener: sections to be able to handle event notifications
    ; sent by supervisor.
    ; 下面是事件监听器的可选配置, supervisor能够处理事件通知.
    ;
    ; ** 译者注： 和上面相同的解释没有翻译 **

    ;[eventlistener:theeventlistenername]
    ;command=/bin/eventlistener    ; the program (relative uses PATH, can take args)
    ;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
    ;numprocs=1                    ; number of processes copies to start (def 1)
    ;events=EVENT                  ; event notif. types to subscribe to (req'd)
    ;buffer_size=10                ; 事件缓冲队列的大小 (default 10)
    ;directory=/tmp                ; directory to cwd to before exec (def no cwd)
    ;umask=022                     ; umask for process (default None)
    ;priority=-1                   ; the relative start priority (default -1)
    ;autostart=true                ; start at supervisord start (default: true)
    ;autorestart=unexpected        ; whether/when to restart (default: unexpected)
    ;startsecs=1                   ; number of secs prog must stay running (def. 1)
    ;startretries=3                ; max # of serial start failures (default 3)
    ;exitcodes=0,2                 ; 'expected' exit codes for process (default 0,2)
    ;stopsignal=QUIT               ; signal used to kill process (default TERM)
    ;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
    ;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
    ;killasgroup=false             ; SIGKILL the UNIX process group (def false)
    ;user=chrism                   ; setuid to this UNIX account to run the program
    ;redirect_stderr=true          ; redirect proc stderr to stdout (default false)
    ;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
    ;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
    ;stdout_logfile_backups=10     ; # of stdout logfile backups (default 10)
    ;stdout_events_enabled=false   ; emit events on stdout writes (default false)
    ;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
    ;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
    ;stderr_logfile_backups        ; # of stderr logfile backups (default 10)
    ;stderr_events_enabled=false   ; emit events on stderr writes (default false)
    ;environment=A="1",B="2"       ; process environment additions
    ;serverurl=AUTO                ; override serverurl computation (childutils)
    
  ```
    

  
## 添加进程组

```conf

    ; The below sample group section shows all possible group values,
    ; create one or more 'real' group: sections to create "heterogeneous"
    ; process groups.
    ; 下面是进程组的可选配置，可以创建一个或多个进程组。

    ;[group:thegroupname]
    ;programs=progname1,progname2  ; 这里的进程名是上文 [program:theprogramname] 定义的theprogramname
    ;priority=999                  ; the relative start priority (default 999)
```

## 命令行工具 supervisorctl


查看所有命令

```bash

    $ supervisorctl help

    default commands (type help ):
    =====================================
    add    clear  fg        open  quit    remove  restart   start   stop  update
    avail  exit   maintail  pid   reload  reread  shutdown  status  tail  version
    命令功能

    作者:	飞龙 http://feilong.me/2011/03/monitor-processes-with-supervisord
    supervisord，初始启动Supervisord，启动、管理配置中设置的进程。
    supervisorctl stop programxxx，停止某一个进程(programxxx)，programxxx为[program:chatdemon]里配置的值，这个示例就是chatdemon。
    supervisorctl start programxxx，启动某个进程
    supervisorctl restart programxxx，重启某个进程
    supervisorctl stop groupworker: ，重启所有属于名为groupworker这个分组的进程(start,restart同理)
    supervisorctl stop all，停止全部进程，注：start、restart、stop都不会载入最新的配置文件。
    supervisorctl reload，载入最新的配置文件，停止原有进程并按新的配置启动、管理所有进程。
    supervisorctl update，根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启。
    注意：显示用stop停止掉的进程，用reload或者update都不会自动重启。
```