# -*- coding: utf-8 -*-
"""
上下文处理器，函数返回的字典对象会自动加入到Context对象中
Context对象中的值可以使用在所有模版中
"""
from django.db import connection

from .models import Blog
from .models import Category
from .models import Friend


def theme(request):
    """
    加载博客主题模版配置
    :param request:
    :return:
    """
    from django.conf import settings

    theme_data = dict()
    theme_data['site_title'] = getattr(settings, "SITE_TITLE")
    theme_data['site_subtitle'] = getattr(settings, "SITE_SUBTITLE")
    theme_data['scheme'] = getattr(settings, "SCHEME", "")
    theme_data['use_motion'] = "use-motion" if getattr(settings, "USE_MOTION") else ""
    theme_data['google_site_verification'] = getattr(settings, "GOOGLE_SITE_VERIFICATION", "")
    theme_data['baidu_site_verification'] = getattr(settings, "BAIDU_SITE_VERIFICATION", "")
    theme_data['qihu_site_verification'] = getattr(settings, "QIHU_SITE_VERIFICATION", "")
    theme_data['fancybox'] = getattr(settings, "FANCYBOX", True)
    theme_data['version'] = getattr(settings, "VERSION", '')
    theme_data['keywords'] = getattr(settings, "KEYWORDS", '')
    theme_data['rss'] = getattr(settings, "RSS", '')
    theme_data['favicon'] = getattr(settings, "FAVICON", '')
    theme_data['sidebar'] = getattr(settings, "SIDEBAR", {})
    theme_data['menu'] = getattr(settings, "MENU", {})
    theme_data['menu_icons'] = getattr(settings, "MENU_ICONS", {})
    theme_data['duoshuo_shortname'] = getattr(settings, "DUOSHUO_SHORTNAME", '')
    theme_data['social'] = getattr(settings, "SOCIAL", {})
    print(theme_data)

    return {"theme": theme_data}


def tag_list(request):
    """
    获取每个标签的文章数量，sqlite不支持right join on
    """
    cursor = connection.cursor()
    sql = "SELECT title, c FROM (\
                        SELECT tag_id AS tid, COUNT(*) AS c \
                        FROM blog_blog_tags GROUP BY tag_id) AS t2 \
                        LEFT JOIN blog_tag ON blog_tag.id=t2.tid";
    cursor.execute(sql)
    tags = cursor.fetchall()
    ctx = {'tags': [tag[0] for tag in tags]}
    return ctx


def google_analytics(request):
    from django.conf import settings
    return {'ga_id': settings.GOOGLE_ANALYTICS_ID, 'disqus_name': settings.DISQUS_NAME}


def recent_blog_list(request):
    """
    最近文章列表
    """

    # 最近发布的文章列表
    recent_blogs = Blog.objects.filter(status='p', is_public=True).order_by('-publish_time')[:10]

    # 分类
    categories = Category.objects.all()

    # 友情链接
    friends = Friend.objects.filter(active=True).order_by('position')

    return {'recent_blogs': recent_blogs, 'categories': categories, 'friends': friends}
