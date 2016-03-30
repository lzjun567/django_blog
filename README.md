关于Django_Blog
=====================
Django_Blog是一款基于Python3.x、Django1.8.x 开发的个人博客系统，按照《Two Scoops of Django Best Practices for Django》实践而成，使用极简主义风格。在管理后台可以用WYSIWYG(所见即所得)编辑方式。系统主题经过3次大的改动，最初前端使用BootStrap开发完成，目前最新版本使用的是Ghost主题，因为Ghost的简洁实在是太吸引我了。
####为什么会有这个博客
写博客是我作为开发者一直以来的习惯，最早在Javaeye记录，后来用[DigitalOcean](https://www.digitalocean.com/?refcode=af4cff8f42bc)（注：从链接点进去注册使用服务，你和我都会得到$10优惠券）自己搭建一个VPS转用WordPress，不过在使用体验上都存在这样那样的不足（其实是不折腾会死星人）。于是自己开始着手打造一个轮子，能满足自己需求即可。这个项目是我第一次接触Python的时候写的，Django的强大以至于你可以完全专注于业务。因此项目亦可作为绝大数Python初学者练手，希望对你有所帮助。
####Features
- WYSIWYG编辑模式
- 支持代码高亮
- 支持原生HTML标签
- 支持内嵌JavaScript脚本

####安装运行
Python版本使用3.4，首先确保系统有Python3的环境。还没安装的请移步至：[Python安装](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)。项目的安装推荐使用virtualenv，它能提供一个完全隔离的python环境，安装virtualenv:  
    
    $ pip install --upgrade virtualenv

然后使用virtualenv创建一个python虚拟环境  

    $ mkdir ~/.virtualenvs
    $ virtualenv -p python3 ~/.virtualenvs/django_blog
激活虚拟环境django_blog  

    $ source ~/.virtualenvs/django_blog/bin/activate
如果你使用windows，运行：  

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

管理登录地址：[http://localhost:8000/admin](http://localhost:8000/admin)，用户名:admin   密码:123456  生产环境部署请参考[Django应用部署](http://foofish.net/blog/18/django-deploy)

####开发文档
[develop.md](./doc/develop.md)

####TODO

任何建议或者参与开发，可以[New Issue](https://github.com/lzjun567/django_blog/issues)。项目遵循[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议  
 
  [1]: http://foofish.qiniudn.com/v1.2.png

