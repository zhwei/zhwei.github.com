---
layout: post
title: "About"
date: 2013-05-25 15:41
comments: false
---


## 简介

+ 基本信息
  - 张卫/男
  - 山东理工大学/计算机科学与技术/2011级
  - 常用名: zhwei

+ 生活
  - 杏园中的野草
  - 真诚的Pythoner， 热爱生活的程序猿
  - 有代码洁癖，git深度患者

## 简历

### Python

  + 熟悉Python, 熟悉Python元方法, 多线程, 生成器
  + 熟悉Django, web.py, Bottle
  + 熟悉PEP8编码风格
  + 熟悉PIL
  + 配合使用过Redis, MongoDB
  + 使用过WMI, PyWin32
  + 使用gunicorn部署web站点
  + 使用supervisor管理系统服务
  + 了解tornado

### Linux

  + 日常工作使用Arch, Ubuntu
  + 写过服务器监控程序[ServerMonitor](#ServerMonitor)
  + 熟悉Nginx日常配置
  + 维护多台Ubuntu CentOS RedHat Oracle服务器
  + 了解XenServer
  + 了解Shell基本语法
  + 使用OpenWrt做路由器
  + 使用tmux

### Web

  + 熟悉HTML, CSS基础语法, 使用过Less, CoffeeScript
  + 熟悉Bootstrap前端框架及定制化设计
  + 能用JQuery进行简单DOM操作
  + 了解HTTP协议

### Geek生活

  + 熟悉Git常用操作
  + 使用Hanouts与小伙伴交流
  + 常年使用Shadowsocks, GoAgent

### 团队协作

  + 使用Git做版本控制
  + 有多次团队协作经验
  + 使用过Trello, Tower等在线协作平台

## 作品

  ### [Gotit](https://github.com/zhwei/gotit)

    + 校外信息查询系统
    + 描述: 帮助使用校外网的同学使用正方教务系统查询成绩, 从初学Python到现在一直在升级维护, 为了提高用户体验增加了页面缓存和验证码识别等功能. 访问量最高的时候PV/天 接近7万, 曾为多款Android提供接口服务.

    + 平台组成:
      - Web查询
      - 微信公众帐号
      - 对外开放的API
      - 网站后台

    + 功能组成:
      - 成绩 课表 考试时间查询
      - 平均学分基点计算
      - CET成绩查询
      - 图书馆借书查询

  ### [ServerMonitor](http://git.oschina.net/zhwei/ServerMonitor)

      + 服务器机房监控
      + 描述: 记录服务器的基本状况, 监控机房温度, 网站运行状态,服务器状况由服务端隔一段时间向客户端发起一次轮询,获取相关信息, 机房温度是通过串口从51单片机获取, 网站运行状态使用过pycurl获取网站各个阶段的响应时间. 数据存入MongoDB.

      + 主要组件
        - Web站点
        - 服务端
        - Linux客户端
        - Windows客户端

      + 监控内容
        - 服务器
          + uptime
          + 操作系统基本信息
          + 流量
          + 硬盘
          + CPU使用率
          + 内存使用率
          + 系统平均负载
        - 网站
          + 标题/编码/页面类型
          + 关键字测试
          + 页面加载时间
            - 总时间
            - 连接时间
            - 域名解析时间
            - 响应中途时间
        - 机房
          + 温度


