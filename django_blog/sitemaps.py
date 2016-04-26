#!encoding=utf-8
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Blog
from django.core.urlresolvers import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Blog.objects.filter(is_public=True).filter(status='p').order_by('-add_time')

    def lastmod(self, item):
        return item.update_time

    def location(self, item):
        return r'/blog/%d/%s' % (item.id, item.link)

class IndexSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
