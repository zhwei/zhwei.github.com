#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime

TARGET_FILE = os.getcwd() + "/_posts/"


def show_help(num=0):
    print(
        [
            """
    Usage:\n
    ##################################################
    --help          OR -h           show this help;

    post <url>      OR -p           发布新博客
    -p <博客url>    -t <博客标题>   发布新博客, -t 为可选参数

    recent          OR -r           打开最近创建的博客文件
                                    -r 还可以加参数(可选), 序号从0开始,
                                    比如:
                                        倒数第二篇为 -r -2
                                        最旧的文章 -r 1
    ##################################################
    """,
            "Error: 请输入自定义url!!",
            "Error: 请输入合法数字",
            "Error: 您没有那么多博客文件"
        ][num]
    )


def post(argv):
    """
    新建markdown博客文件, 填入博客标题等标准内容
    """
    time_str = str(datetime.datetime.now()) # 获取当前时间并转化为字符串
    try:
        # 是否存在url参数
        argv[2]
    except IndexError:
        return show_help(1)

    argv_1 = argv[2:]
    try:
        title = ' '.join(argv_1[argv_1.index("-t") + 1:])
        filename = time_str[0:10] + "-" + '-'.join(
            argv_1[0:argv_1.index("-t")]) + ".markdown"
    except ValueError:
        title = ' '.join(argv_1)
        filename = time_str[0:10] + "-" + '-'.join(argv_1) + ".markdown"
        pass

    #slash_content = {
    #    "layout": "post",
    #    "date": time_str[0:16],
    #    "title": title,
    #    "tags": " ",
    #}
    wr = open(TARGET_FILE + filename, "w")
    wr.write("---\n")
    wr.write("layout: post\n")
    wr.write('title: "'+title+'"\n')
    wr.write("date: "+time_str[0:16]+"\n")
    wr.write("comments: true\n")
    wr.write("tags: \n")
    #for key in slash_content.keys():
    #    content = key + ": " + str(slash_content[key]) + "\n"
    #    wr.write(content)
    wr.write("---\n")
    wr.close()
    os.system("vim " + TARGET_FILE + filename)
    print("成功创建文章"+title+", 再次打开可以使用generte.py -r")


def recent(argv):
    """
    打开最近创建的markdown博客文件
    """
    try:
        num = int(argv[2])
    except IndexError:
        num = 0
        pass
    except ValueError:
        return show_help(2)

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
        show_help(3)

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
    elif ar == "post" or ar == "-p":
        post(argv)
    elif ar == "recent" or ar == "-r":
        recent(argv)
    else:
        return show_help()

if __name__ == "__main__":
    main()
