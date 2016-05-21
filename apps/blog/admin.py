# -*- coding: utf-8 -*-

import datetime

from django.contrib import admin
from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row

from .models import Tag, Blog, Category, Friend
from .forms import BlogForm


@register.inclusion_tag('admin/blog/submit_line.html', takes_context=True)
def submit_row(context):
    """
    移除"保存后添加"按钮
    移除"保存继续编辑"按钮
    添加"保存为草稿"按钮
    """
    # ctx = original_submit_row(context)
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    show_save = context.get('show_save', True)
    show_save_and_continue = context.get('show_save_and_continue', True)
    from django.template.context import Context

    ctx = Context(context)
    ctx.update({
        'show_delete_link': True,

        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': (
            context['has_add_permission'] and not is_popup and
            (not save_as or context['add'])
        ),
        'show_save_and_continue': not is_popup and context['has_change_permission'] and show_save_and_continue,
        'show_save': False,
        'show_save_as_draft': True,
    })
    # ctx.update({
    #     'show_save_and_add_another': False,
    #     'show_save_as_draft': True,
    #     'show_save_and_continue': False,
    # })
    return ctx


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'is_public', 'status', 'publish', 'access_count')
    fields = (
        'title',
        'link',
        'cover',
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
            # 只有是操作状态的文章才更新发布时间
            if obj.status == 'd':
                obj.publish_time = datetime.datetime.now()
            obj.status = Blog.STATUS_CHOICES[1][0]
        elif '_save_as_draft' in request.POST.keys():
            obj.status = Blog.STATUS_CHOICES[0][0]
        super(BlogAdmin, self).save_model(request, obj, form, change)
        # obj.save()

    def change_view(self, request, object_id, form_url='', extra_context=None):
        more_context = {}
        more_context.update(extra_context or {})
        return super(BlogAdmin, self).change_view(request, object_id, form_url, more_context)


class TagAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class FriendAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'position', 'active')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Friend, FriendAdmin)
