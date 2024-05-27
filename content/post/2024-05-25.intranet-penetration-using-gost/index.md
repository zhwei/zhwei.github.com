---
title: 使用 Gost 实现内网穿透
date: 2024-05-25
slug: intranet-penetration-using-gost
image: media/the-tunnel-1446786.jpg
tags:
    - Tools
---


> Photo by <a href="/photographer/theraygun-46352">theraygun</a> on <a href="/">Freeimages.com</a>


## 前因

这里的内网穿透是指能够在家庭网络环境之外接入家庭局域网，能够正常访问 NAS、Homelab 等。

此前已经使用 Wireguard 组建虚拟网的方式实现了上面需求，wg 安装在 Homelab 机器上，但最近想用 PVE 重装下 Homelab ，为了避免在此期间影响接入，准备将穿透服务迁移到群晖 NAS 上。
但并没有官方构建的群晖 Wireguard Package，使用第三方的构建没有安全感，所以准备换用其他方案实现，之前方案中也用到了 gost 来提供云端的 SS 代理，发现其 v3 版本中提供了很多转发特性，所以准备用它来实现。

Gost 的优点：
1. 纯命令行方案，可以不使用配置文件。
2. 使用 go 开发，单个二进制文件，方便部署。



## 安装

前往 GitHub 下载对应架构的二进制包，也可自行构建。

https://github.com/go-gost/gost/releases


## 使用


### 云主机

云主机需要有公网 IP ，方便移动设备接入。

```
gost -L "relay+ssh://:56786?bind=true&nodelay=true&authorizedKeys=$HOME/.ssh/authorized_keys"
```

上面命令会使用 [relay](https://gost.run/tutorials/protocols/relay/) + [ssh](https://gost.run/tutorials/protocols/ssh/) 协议监听本地 56786 端口，授权密钥使用当前用户的 `~/.ssh/authorized_keys` 文件。


其中 bind=true 允许请求方指定绑定的端口，nodelay=true 降低延迟。


### 家庭 NAS

NAS 在家庭内网，建议使用 docker 运行下面命令，更容易部署，减少依赖。

```
gost \
    -L rtcp://:56787/:8848 \
    -F "relay+ssh://root@CLOUD_SERVER_HOST:56786?privateKeyFile=/path/to/ssh_private_key&nodelay=true" \
    -L ss://AEAD_CHACHA20_POLY1305:xxx@:8848
```

上面命令中：
`-L rtcp://:56787/:8848` 会将本地的 8848 端口转发到远程的 56787 端口，-F 选项指定了转发协议和链接信息。

第二个 -L 在 8848 端口启动一个 ss 代理。


上面达成的效果是：当移动设备使用 ss 协议连接到云主机的 56787 端口时，会通过 ssh 代理转发到家庭 NAS 的 8848 端口，实现内网穿透，访问家庭网络内的服务。
