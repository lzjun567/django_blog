#! coding=utf-8
import datetime

from django.contrib import admin
import reversion
from .models import Tag, Blog, Category
from .forms import BlogForm
from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row


@register.inclusion_tag('admin/blog/submit_line.html', takes_context=True)
def submit_row(context):
    """
        删除"保存后添加"按钮
    """
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': False,
    })
    return ctx


class BlogAdmin(reversion.VersionAdmin):
    list_display = ('title', 'is_public', 'status', 'publish', 'access_count')
    fields = (
        'title',
        'link',
        'snippet',
        'content',
        ('is_public', 'is_top',),
        'category',
        'status',
        'tags'
    )

    exclude = ('publish_time',)
    search_fields = ('title',)
    prepopulated_fields = {"link": ("link",)}
    ordering = ('-add_time', )
    list_per_page = 60
    form = BlogForm
    actions = ['make_published']

    def create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d')

    create_time.short_description = u"创建时间"

    def publish(self, obj):
        if obj.publish_time:
            return obj.publish_time.strftime('%Y-%m-%d')
        else:
            return ''

    publish.short_description = u"发布时间"

    def make_published(self, request, queryset):
        """
        $modeladmin: current modeladmin
        $request: the current request
        $queryset: the set of objects selected by user
        """
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

    make_published.short_description = u"发表"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class TagAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)





