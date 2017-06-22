zhwei 的学习笔记
===========

+ 原生`jekyll`, 没有使用插件
+ 模板修改自[Greyshade](htt,kjkp://shashankmehta.in/archive/2012/greyshade.html)
+ 博客文章直接放在`_post`下
+ 本地运行：
    ```bash
    docker run --rm --volume=$PWD:/srv/jekyll -it -p 4000:4000 jekyll/minimal:3.4.3 jekyll serve
    ```

    Visit http://127.0.0.1:4000
