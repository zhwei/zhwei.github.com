---
layout: post
title: "Docker Jenkins Run Tests in Docker"
date: 2017-12-04
comments: true
tags: Docker
---

## 起因

团队使用 Jenkins CI 来对 Pull Request 进行上线前的检查，例如：编码风格、静态分析、测试等。


最近遇到了测试时的并发问题，由于 Jenkins 需要在 PR 更新时重新检查，每完整测试一次需要 10 到 15 分钟，同时有很多开发者提交 PR 时，就会导致长时间无意义的等待，有此希望能提高 Jenkins 的并发测试能力。


## 选择方案

先介绍下项目测试时依赖的环境：

    - PHP
    - Redis
    - MySQL
    - ElasticSearch


多个 PR 测试进程之间，ES、Redis 是可以共享的，但 MySQL 不可以，其中考虑的方案是考虑能否通过改变项目中的数据库名称从而共享同一台 MySQL Server ，但实际调试中发现除去 ORM 能够简单变更数据库外，还是有很多场景中的数据库名称是写死在代码里面的，所以这条方案宣告放弃。

如标题所说，我们的 Jenkins 是运行在 docker 中的，那测试是不是也可以在 docker 中运行呢，所有依赖环境、软件包，全部通过 docker 打包整理，最终 Jenkins 在发起测试时需要调用的是一个 docker 命令，那么问题来了，怎样让 Jenkins 调用 docker ？想到的有以下两个思路：


- Jenkins 中完整安装 docker ，关注点：
    - 需要重新 build jenkins image，调试会很麻烦
    - 性能会不会有问题？docker 中运行了一个 docker ，然后在这个 docker 里运行了四个实例
    - 网络会不会有问题？172 这个网段会不会混乱（还是调试问题）

- Jenkins 中调用宿主机的 docker ，关注点：
    - **是否可行？**
    - 优点：不需要重新 build jenkins image ，开箱即用，扩展 slave 会很方便


> 后来发现前者的思路就是 GitLab CI 的测试方式，不过当时为了调试方便，以及减轻后续 jenkins 镜像升级的痛苦，选择了后者，也在网上确认到了确实有人这么实践过，并且 work 。
 

## 使用宿主机 docker 运行测试

Jenkins 调用宿主机 docker 的方法其实很简单：

  - jenkins 中需要安装 docker client
    > 推荐 [Docker CE](https://docs.docker.com/engine/installation/linux/docker-ce/binaries/) ，二进制文件，下载下来就能用


  - 映射宿主机的 `/var/run/docker.sock` 到 jenkins
    > 这样我们上面安装的 docker client 可以直接通过此 socket 文件与宿主机的 docker daemon 通信


之后可以测试下能否正常通信：`./docker ps`，打印出的应该是宿主机中正在运行的容器。

> 由于 Jenkins 容器的运行用户为 `jenkins` ，而挂载的 volume 默认用户是 root ，所以需要在容器运行后修改一下 `docker.sock` 文件的权限，这里我的容器是使用 `docker compose` 启动的，所以使用了命令：`docker-compose exec --user=0 master chmod o+rw /var/run/docker.sock` 来赋予 `jenkins` 读写 sock 文件的权限

这样 jenkins 中的 docker 就能够与宿主机的 docker daemon 通信了。


## 测试中的坑

- volume 映射

> 由于 jenkins 运行 docker 时实际是在宿主机运行的，所以如果你需要将代码库位置映射进测试容器，那映射的真实路径应该是宿主机的路径，如下：
>
>   - 宿主机的 JENKINS_HOME ：`/home/docker/jenkins/volume/master`
>   - Jenkins 中的 HOME ：`/var/jenkins_home/`
>   - Jenkins 运行测试时的映射命令：
>     > `... -v /home/docker/jenkins/volume/master/workspaces/ProjectName:/ProjectName`


- 环境变量

如上 volume 映射，也要再设置一遍

```
... -e "MYSQL_HOST=${MYSQL_HOST}"
```



## 参考链接

- [Using Docker-in-Docker for your CI or testing environment? Think twice.](http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)
- [Docker-in-Docker](https://github.com/jpetazzo/dind)
