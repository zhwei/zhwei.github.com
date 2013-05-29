#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime

# TARGET_FILE = os.getcwd() + "/_posts/"
TARGET_FILE = "/home/zhwei/apps/jekyll_blog/_posts/"


def loca(art):
    return TARGET_FILE + art


def show_help():
    print(
        """
    Usage:\n
    ##################################################
    -h --help                      show this help;

    -p --post
    -p <博客url> -t <博客标题>     发布新博客, -t 为可选参数

    -r --recent  <可选>            打开最近创建的博客文件
                                   -r 还可以加参数(可选), 序号从0开始,
                                   比如:
                                      倒数第二篇为 -r -2
                                      最旧的文章 -r 1

    -m  --match <可选>             关键词匹配, 后面可加关键词, 也可不加,
                                   然后在终端中多次输入关键词
    ##################################################
    """
    )


def printerr(num):
    errors = [
        "Error: 请输入自定义url!!",
        "Error: 请输入合法数字",
        "Error: 您没有那么多博客文件",
        "Error: 未匹配到您输入的关键字",
    ]
    print "\033[49;31;5m%s" % errors[num]


def post(argv):
    """
    新建markdown博客文件, 填入博客标题等标准内容
    如果不填写标题参数则为空
    """
    time_str = str(datetime.datetime.now())  # 获取当前时间并转化为字符串
    try:
        # 是否存在url参数
        argv[2]
    except IndexError:
        return printerr(0)

    argv_1 = argv[2:]
    try:
        title = ' '.join(argv_1[argv_1.index("-t") + 1:])
        filename = time_str[0:10] + "-" + '-'.join(
            argv_1[0:argv_1.index("-t")]) + ".markdown"
    except ValueError:
        title = ' '.join(argv_1)
        filename = time_str[0:10] + "-" + '-'.join(argv_1) + ".markdown"
        pass

    # slash_content = {
    #    "layout": "post",
    #    "date": time_str[0:16],
    #    "title": title,
    #    "tags": " ",
    #}
    wr = open(TARGET_FILE + filename, "w")
    wr.write("---\n")
    wr.write("layout: post\n")
    wr.write('title: "' + title + '"\n')
    wr.write("date: " + time_str[0:16] + "\n")
    wr.write("comments: true\n")
    wr.write("tags: \n")
    # for key in slash_content.keys():
    #    content = key + ": " + str(slash_content[key]) + "\n"
    #    wr.write(content)
    wr.write("---\n")
    wr.close()
    os.system("vim " + TARGET_FILE + filename)
    print("成功创建文章" + title + ", 再次打开可以使用generte.py -r")


def recent(argv):
    """
    打开最近创建的markdown博客文件, 可以添加相应序号
    然后打开第几篇文章, 文件名以时间开头,所以以文件
    名排序
    """
    try:
        num = int(argv[2])
    except IndexError:
        num = 0
        pass
    except ValueError:
        return printerr(1)

    li = os.listdir(TARGET_FILE)
    d_ctime = {}        # 文件名: 文件创建时间 字典
    for doc in li:
        # d_ctime[doc] = os.path.getctime(TARGET_FILE + doc)
        d_ctime[doc] = doc

    d_ctime = sorted(d_ctime.iteritems(),
                     key=lambda k_v: (k_v[1], k_v[0]),
                     reverse=True)  # 字典按值排序, 生成元组列表

    try:
        os.system("vim " + TARGET_FILE + d_ctime[-num][0])
    except IndexError:
        printerr(2)


def match(argv, keys=None, artlist=None):
    """
    匹配文件名查找, 如果不输入关键词则在终端中提示
    用户输入文章序号或者关键词, 关键词多次叠加检索
    直至匹配到单一文章
    """
    if artlist is None:
        artlist = os.listdir(TARGET_FILE)
    if keys is None:
        keys = argv[2:]

    for key in keys:
        i = 0
        leng = len(artlist)
        while i < leng:
            d = artlist.pop()
            if d.find(key) != -1:
                artlist.insert(0, d)
            else:
                pass
            i = i + 1
    if len(artlist) > 1:
        for a in artlist:
            print "<%s> %s" % (str(artlist.index(a)), a[11:-9].replace("-", " "))
        tar = raw_input("输入你想打开的文章序号或者关键词(输入q退出)-->")
        if tar == "q":
            return 0
        try:
            name = artlist[int(tar)]
        except ValueError:
            keys = tar.split(" ") + keys
            return match(None, keys, artlist)
        os.system("vim " + loca(name))
    elif len(artlist) == 1:
        command = "vim " + loca(artlist[0])
        os.system(command)
    else:
        printerr(3)


def main():
    """
    主程序, 判断参数调用不同方法
    """
    argv = sys.argv
    try:
        ar = argv[1]
    except IndexError:
        return show_help()
    if ar == "--help" or ar == "-h" or ar is None:
        show_help()
    elif ar == "--post" or ar == "-p":
        post(argv)
    elif ar == "--recent" or ar == "-r":
        recent(argv)
    elif ar == "--match" or ar == "-m":
        match(argv)
    else:
        return show_help()

if __name__ == "__main__":
    main()
