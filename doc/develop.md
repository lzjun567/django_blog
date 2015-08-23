开发文档
===============
django_blog v1.2进行了大量改动，django升级到了1.8.2，数据库迁移工具不在依赖第三方库south，该方案已经集成到了django1.7。核心代码views.py缩减至100行内。

####目录结构
项目目录结构参考[Recommended Django Project Layout](http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/)，此方案比django自动生成的目录结构更加灵活。


        ├── apps                         # 应用根目录，该目录可以有多个应用
        │   ├── __init__.py
        │   ├── blog                     # 博客app
        │   │   ├── __init__.py
        │   │   ├── admin.py
        │   │   ├── forms.py
        │   │   ├── migrations
        │   │   ├── models.py            # 博客app模型
        │   │   ├── processor.py
        │   │   ├── static               # 静态资源文件
        │   │   ├── templates
        │   │   ├── templatetags         # 自定义模板标签
        │   │   ├── urls.py              # 博客app的路由规则
        │   │   ├── views.py             # 业务逻辑
        ├── collectedstatic
        │   └── CACHE
        │       ├── css
        │       └── js
        ├── db.sqlite3
        ├── django_blog
        │   ├── __init__.py
        │   ├── db.sqlite3
        │   ├── settings                  # 项目的配置目录，分为开发和生产环境的配置。
        │   │   ├── __init__.py
        │   │   ├── base.py
        │   │   ├── dev.py
        │   │   └── prod.py
        │   ├── sitemaps.py
        │   ├── urls.py                   #路由规则
        │   ├── wsgi.py
        ├── doc
        ├── fabfile.py
        ├── gunicorn_start.sh
        ├── manage.py
        ├── middleware                    # 中间件，比如：性能监测工具
        ├── requirements                  # 系统锁依赖的第三方模块
        │   ├── base.txt
        │   ├── dev.txt
        │   └── prod.txt
        └── templates                     # 项目通用的模板文件
            ├── 404.html
            └── admin

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