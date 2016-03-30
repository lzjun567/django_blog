# -*- coding: utf-8 -*-

import datetime

from django.contrib import admin
from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row

from .models import Tag, Blog, Category
from .forms import BlogForm


@register.inclusion_tag('admin/blog/submit_line.html', takes_context=True)
def submit_row(context):
    """
    移除"保存后添加"按钮
    移除"保存继续编辑"按钮
    添加"保存为草稿"按钮
    """
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': False,
        'show_save_as_draft': True,
        'show_save_and_continue': False,
    })
    return ctx


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', 'status', 'publish', 'access_count')
    fields = (
        'title',
        'link',
        'content',
        'snippet',
        ('is_public', 'is_top',),
        'category',
        'tags'
    )

    exclude = ('publish_time',)
    search_fields = ('title',)
    prepopulated_fields = {"link": ("link",)}
    ordering = ('-add_time',)
    list_per_page = 60
    form = BlogForm
    actions = ['make_published']

    def create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d')

    create_time.short_description = "创建时间"

    def publish(self, obj):
        if obj.publish_time:
            return obj.publish_time.strftime('%Y-%m-%d')
        else:
            return ''

    publish.short_description = "发布时间"

    def make_published(self, request, queryset):
        rows_updated = 0
        for entry in queryset:
            if entry.status != 'p':
                entry.status = 'p'
                rows_updated += 1
                if entry.publish_time is None:
                    entry.publish_time = datetime.datetime.now()
                entry.save()
        message_bit = "%s 篇博客 " % rows_updated
        self.message_user(request, "%s 成功发布" % message_bit)

    make_published.short_description = "发表"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        if '_save' in request.POST.keys():
            obj.status = Blog.STATUS_CHOICES[1][0]
        elif '_save_as_draft' in request.POST.keys():
            obj.status = Blog.STATUS_CHOICES[0][0]
        super(BlogAdmin, self).save_model(request, obj, form, change)
        # obj.save()

    def response_action(self, request, queryset):
        print(request)
        return super(BlogAdmin, self).response_action(request, queryset)

    def response_change(self, request, obj):
        print(obj)
        return super(BlogAdmin, self).response_change(request, obj)


class TagAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
