#!encoding=utf-8
from django.contrib.sitemaps import Sitemap 
from django.core.urlresolvers import reverse
from apps.blog.models import Blog 

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(is_public=True).filter(status='p')

    def lastmod(self, item):
        return item.update_time

    def location(self, item):
        return  r'/blog/%d/%s' % (item.id, item.link)

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about','blog:archives', 'home']

    def location(self, item):
        return reverse(item)
