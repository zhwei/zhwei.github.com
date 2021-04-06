---
title: 虚拟组网工具推荐
date: 2021-02-05
slug: virtual-networking
image: media/world-1264062_1920.jpg
tags:
    - Tools
---

## 引子

推荐虚拟组网工具前先说一下个人网络环境。

在前司工作时，由于一直是远程工作，几乎随时都要联通公司内网，前司的 VPN 用的深信服的 SSL VPN。Mac 端的客户端非常难用，几乎隔几小时就要断一次，于是写了个 AppleScript 自动重连脚本续了一段时间。但有个问题，手机上很难访问公司内网，且不说其手机客户端有多难用，深信服 VPN 限定了一个用户只能有一个设备在线，想在手机上测试时非常痛苦。

另外，一直使用 Surge 作为代理客户端，增强模式真的是非常强大，除了强大的规则、代理功能之外，日常用来抓包也非常方便。

于是有了个想法，能不能把公司的内网转发也交给 Surge 处理呢？

说干就干，在公有云申请了一台 Windows Server 主机作为 Gateway，之所以用 Windows 是因为深信服 VPN 的 Windows 客户端相对更稳定一些，然后在 WinServer 运行 VPN 客户端，又写了一个 AutoIT 脚本守护这个客户端，一旦断开自动重连。最后，通过 SS 暴露给 Surge 使用，非常完美！从此以后彻底摆脱了深信服的 VPN 客户端，手机端也可以非常顺滑的访问公司内网资源。

有了带公网 IP 的 Gateway 后，我又盯上了家里的 NAS ！这玩意怎样在保证安全的前提下载公网使用呢？


## 虚拟组网

本地组网相比大家都非常熟悉，一堆设备挂在交换机或者路由器下面，就可以组成一个简单的局域网，各设备直接可通过局域网 IP 访问。

与本地组网不同的是，虚拟组网设备之间没有通过网线连接，甚至不在一个机房、国家甚至地区。但通过 P2P 或者中转节点，实现了局域网的效果。

下面列一下从开始使用到目前为止遇到的组网工具机器优缺点。


### ZeroTier

> https://www.zerotier.com

我目前用的工具，放在最开始并不意味着它是最好的，但它是最适合我的个人场景的。

优点
- P2P 通信
- 支持自建 moon 节点，用于服务发现（已自建）
- 当无法建立 P2P 通信时，流量也会通过 moon 节点转发
    - 国内运营商会限制 UDP 流量，甚至分配假的公网 IP，导致无法建立 P2P 链接
    - 所以还是用自己的更放心 :)
- 有 Windows、NAS GUI 客户端，配对简单
- 有在线 Central 管理功能，强大又方便（相对于下面方案需要自己手写配置配置文件）
    - 在线路由管理很强大

缺点
- 商业公司（各有利弊吧）
- 免费套餐有节点数目限制



### Nebula

> https://github.com/slackhq/nebula

Slack 出品的开源项目

优点
- 开源
- P2P 通信
- 命令行生成配置文件，相对简单
- 完全自建 Lighthouse 节点，安全信得过


缺点
- 人工管理证书，人工分发，相对麻烦
- 无法统一管理授信客户端，只能增加黑名单
  - 证书泄露了会很危险，需要更新所有节点配置文件
- 只支持 P2P 通信
  - 无法通过 Lighthouse 节点转发流量，遇到国内奇葩的网络环境时就废了


### Tinc

> https://www.tinc-vpn.org

老牌 VPN ，看官网样式就能 GET 到了。我在另一个生产环境用到了 Tinc，虽然 ZeroTier 也不错，但毕竟是个商业服务，不如开源项目用起来放心 + **便宜**。

优点
- 开源
- P2P
- main 节点支持流量转发
- 支持在 main 节点统一管理授信节点

缺点
- 人工管理证书，人工分发，相对麻烦


### 其他

tailscale，<https://tailscale.com>
- 也是个商业服务，没有使用过，暂不评价

WireGuard，<https://www.wireguard.com>
- 也是老牌子了，tailscale 基于它开发的
- 之前在生产项目中也尝试过，但它对内核有要求，需要重启机器，弃用了
- 没有深度使用，无法评价优缺点

### 内网穿透代理

下面两个工具和前面提到的虚拟组网并不是一类工具，但在特定场景用起来会非常方便。例如，在本地开发时需要接受第三方服务的 callback 时，可以使用下面工具临时暴露本地服务到公网。

- ngrok，<https://ngrok.com>
- frp，<https://github.com/fatedier/frp>


### 配置过程中的一些参考文章

- [Tinc: windows 路由配置比较清晰的文章](https://blog.sgdylan.com/2018/09/21/tinc-note/)

---


> 题图：由 [TheAndrasBarta](https://pixabay.com/zh/users/theandrasbarta-2004841/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1264062) 在 [Pixabay](https://pixabay.com/zh/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1264062) 上发布