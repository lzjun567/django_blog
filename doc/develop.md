开发文档
===============
django_blog v1.2进行了大量改动，django升级到了1.8.2，数据库迁移工具不在依赖第三方库south，该方案已经集成到了django1.7。核心代码views.py缩减至100行内。

####目录结构
项目目录结构参考[Recommended Django Project Layout](http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/)，此方案比django自动生成的目录结构更加灵活。

    ├── README.md
    ├── apps
    │   ├── __init__.py
    │   └── blog
    ├── config
    │   └── gunicorn_start.sh
    ├── db.sqlite3
    ├── django_blog
    │   ├── __init__.py
    │   ├── db.sqlite3
    │   └── sitemaps.py
    ├── doc
    │   └── develop.md
    ├── manage.py
    ├── middleware
    │   ├── __init__.py
    │   └── profile.py
    ├── requirements
    │   ├── base.txt
    │   ├── dev.txt
    │   └── prod.txt
    ├── settings
    │   ├── __init__.py
    │   ├── base.py
    │   ├── dev.py
    │   └── prod.py
    ├── static
    │   ├── css
    │   ├── favicon.ico
    │   ├── fonts
    │   ├── img
    │   └── js
    ├── templates
    │   ├── 404.html
    │   ├── about.html
    │   ├── admin
    │   └── base.html
    ├── urls.py
    └── wsgi.py

####项目(Projects) vs 应用(apps)
一个应用(App)指的某个具体的子系统，比如博客系统，评论系统等等，而项目就是由这些子系统构成的一个完成系统，一个项目可有多个应用，一个应用可存在于多个项目中。

####开发---dev.py
开发环境数据库使用的是sqlite，详情可以查看settings/dev.py文件，项目运行时是如何指定该配置的呢？启动时在manage.py中指定具体使用哪个配置文件

    # manage.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")

####生产环境---prod.py
生产环境的部署方案是：Supervisor+Nginx+Gunicorn+MySQL

正式环境有gunicorn_start.sh来指定

    # gunicorn_start.sh
    DJANGO_SETTINGS_MODULE=django_blog.settings.prod
    
