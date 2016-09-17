# -*- coding: utf-8 -*-

from django.conf import settings

"""
上下文处理器，函数返回的字典对象会自动加入到Context对象中
Context对象中的值可以使用在所有模版中
"""


def theme(request):
    """
    加载博客主题模版配置
    """
    theme_data = dict()
    theme_data['site_title'] = getattr(settings, "SITE_TITLE")
    theme_data['site_subtitle'] = getattr(settings, "SITE_SUBTITLE")
    theme_data['keywords'] = getattr(settings, "KEYWORDS", '')

    theme_data['scheme'] = getattr(settings, "SCHEME", "")
    theme_data['use_motion'] = "use-motion" if getattr(settings, "USE_MOTION") else ""
    theme_data['google_site_verification'] = getattr(settings, "GOOGLE_SITE_VERIFICATION", "")
    theme_data['baidu_site_verification'] = getattr(settings, "BAIDU_SITE_VERIFICATION", "")
    theme_data['qihu_site_verification'] = getattr(settings, "QIHU_SITE_VERIFICATION", "")
    theme_data['fancybox'] = getattr(settings, "FANCYBOX", True)
    theme_data['version'] = getattr(settings, "VERSION", '')
    theme_data['rss'] = getattr(settings, "RSS", '')
    theme_data['favicon'] = getattr(settings, "FAVICON", '')
    theme_data['sidebar'] = getattr(settings, "SIDEBAR", {})
    theme_data['menu'] = getattr(settings, "MENU", {})
    theme_data['menu_icons'] = getattr(settings, "MENU_ICONS", {})
    theme_data['duoshuo_shortname'] = getattr(settings, "DUOSHUO_SHORTNAME", '')
    theme_data['social'] = getattr(settings, "SOCIAL", {})
    theme_data['alipay'] = getattr(settings, "ALIPAY", None)
    theme_data['wechatpay'] = getattr(settings, "WECHATPAY", None)
    theme_data['google_analytics'] = getattr(settings, "GOOGLE_ANALYTICS", None)

    return {"theme": theme_data}
