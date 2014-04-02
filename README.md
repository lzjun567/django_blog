Django_Blog是一个基于Django、Bootstrap开发的极简博客应用，响应式设计，支持markdown格式WYSIWYG(所见即所得)的编辑方式。
####为什么会有这个博客
经历过iteye，github，wordpress发现没一个是我想要的
####开发哲学
简约原则
####项目结构

    ├─django_blog
    │  ├─libs
    │  └─settings
    ├─requirements
    ├─templates
    │  └─admin
    │      └─blog
    └─apps
        ├─blog
        │  ├─templates
        │  ├─static
        │  │  ├─css
        │  │  ├─js
        │  │  └─fonts
        │  ├─templatetags
        │  └─migrations
        └─bootstrap_paginationDuplicate
            ├─templates
            │  └─bootstrap_pagination
            └─templatetags

####安装运行

推荐使用virtualenv安装方式，virtualenv能提供一个隔离的python环境，首先安装virtualenv:  
    
    $ pip install --upgrade virtualenv

然后使用virtualenv创建一个python虚拟环境  

    $ mkdir ~/.virtualenvs
    $ virtualenv ~/.virtualenvs/django_blog
激活虚拟环境django_blog  

    $ source ~/.virtualenvs/django_blog/bin/activate
如果你使用用windows：  

    $ ~/virtualenvs/django_blog/bin/activate    

现在正式开始下载安装：  
    
    (django_blog) $ cd /home/${user}/workspace #你可以把project下载到任意你想放的地方
    (django_blog) $ git clone https://github.com/lzjun567/django_blog.git
    (django_blog) $ cd django_blog
    (django_blog) $ pip install -r requirements/dev.txt
    (django_blog) $ python manage.py syncdb
    (django_blog) $ python manage.py migrate apps.blog
    (django_blog) $ python manage.py migrate reversion
    (django_blog) $ python manage.py runserver localhost:8000

####预览效果 
![预览效果 ][1]

管理登录地址：[http://localhost:8000/admin](http://localhost:8000/admin)，用户名:admin   密码:123456  


####TODO
1. 添加调度任务ping_google
2. 快速修改文章
2. 本地上传文件到云存储服务商
4. 优化管理界面编辑体验

任何建议或者参与开发，可以[New Issue](https://github.com/lzjun567/django_blog/issues)。项目遵循[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议  
 
  [1]: https://photos-2.dropbox.com/t/0/AACd5mYhFLs75kaWhp96onwOUxcVCZxF8zYA4Sw3OzGLjA/12/71722329/png/1024x768/3/1395331200/0/2/preview.png/y6NzGiPUvieoTm5bNtA6hsnM7Caeb44Dd7zrzOX36S0

