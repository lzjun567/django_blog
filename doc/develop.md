开发文档
===============
开发---dev.py

启动时在manage.py中指定具体使用那个配置文件

    # manage.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.dev")


正式环境有gunicorn_start.sh来指定

    # gunicorn_start.sh
    DJANGO_SETTINGS_MODULE=django_blog.settings.prod