from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django_blog.sitemaps import BlogSitemap, IndexSitemap
from django.http import HttpResponse
from apps.blog.views import LatestPosts
from apps.blog.views import BlogListView
from django.views.generic import TemplateView
from apps.blog.views import AboutView
admin.autodiscover()

sitemaps = {
    'index': IndexSitemap,
    'blog': BlogSitemap,

}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BlogListView.as_view(), name="home"),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^404', TemplateView.as_view(template_name="404.html")),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^humans.txt$', TemplateView.as_view(template_name="humans.txt", content_type="text/plain")),
    url(r'^rss/', LatestPosts(), name='feeds')
]


    #
    #
    #
    # patterns('',
    #                    url(r'^about$', TemplateView.as_view(template_name="about.html"), name='about'),
    #                    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    #                    url(r'^$', BlogListView.as_view(), name='index'),
    #                    url(r'^admin/', include(admin.site.urls)),
    #                    url(r'404', TemplateView.as_view(template_name="404.html")),
    #                    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #                        name='django.contrib.sitemaps.views.sitemap'),
    #                    url(r'^robots.txt$',
    #                        lambda r: HttpResponse(
    #                            "User-agent: *\nDisallow: /admin/\nSitemap: http://foofish.net/sitemap.xml",
    #                            content_type="text/plain")),
    #                    url(r'^baidu_verify_3ymtDfPE09.html',
    #                        lambda r: HttpResponse("3ymtDfPE09", content_type="text/plain"), name='baidu'),
    #                    url(r'^rss/', LatestPosts(), name='feeds'),
    #
    #                    )
