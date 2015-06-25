Django_Blog是一个基于Django、Bootstrap开发的极简博客，基于响应式设计，支持markdown语法WYSIWYG(所见即所得)编辑方式，核心代码不到100行。
####为什么会有这个博客
经历过Javaeye，GitHub，WordPress发现没一个是我想要的（其实是不折腾会死星人）。同时此项目也可以作为绝大数Python初学者练手代码，做到真正学以致用。
####安装运行
版本要求：python2.7 or python3.4（其他的依赖包参见requirements/base.txt)。
推荐使用virtualenv安装方式，virtualenv能提供一个隔离的python环境，首先安装virtualenv:  
    
    $ pip install --upgrade virtualenv

然后使用virtualenv创建一个python虚拟环境  

    $ mkdir ~/.virtualenvs
    $ virtualenv ~/.virtualenvs/django_blog
激活虚拟环境django_blog  

    $ source ~/.virtualenvs/django_blog/bin/activate
如果你使用windows：  

    $ ~/virtualenvs/django_blog/bin/activate    

下载安装第三方依赖包：  
    
    (django_blog) $ cd /home/${user}/workspace #你可以把project下载到任意你想放的地方
    (django_blog) $ git clone https://github.com/lzjun567/django_blog.git
    (django_blog) $ cd django_blog
    (django_blog) $ pip install -r requirements/dev.txt
    (django_blog) $ python manage.py syncdb
    (django_blog) $ python manage.py migrate apps.blog
    (django_blog) $ python manage.py runserver localhost:8000

####预览效果 
![预览效果 ][1]

管理登录地址：[http://localhost:8000/admin](http://localhost:8000/admin)，用户名:admin   密码:123456  

####开发文档
[develop.md](./doc/develop.md)

####TODO
4. 优化管理界面编辑体验

任何建议或者参与开发，可以[New Issue](https://github.com/lzjun567/django_blog/issues)。项目遵循[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议  
 
  [1]: http://foofish.qiniudn.com/v1.2.png

