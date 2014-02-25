#! coding=utf-8
import datetime

from django.contrib import admin
from django import forms
import reversion
from .models import Tag, Blog, Category
from .forms import BlogForm

from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row

@register.inclusion_tag('admin/blog/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': False,
        })                                                                  
    return ctx 




class BlogAdmin(reversion.VersionAdmin):

    list_display = ('title', 'status', 'publish','access_count')
    fields = ('title','snippet', 'content', ('is_public', 'is_top',), 'category', 'author', 'status', 'tags')
    exclude = ('publish_time',) 
    search_fields = ('title',)
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
        '''
        $modeladmin: current modeladmin
        $request: the current request
        $queryset: the set of objects selected by user
        '''
        rows_updated = 0
        for entry in queryset:
            if entry.status != 'p':
                entry.status = 'p'
            if entry.publish_time is None:
                entry.publish_time = datetime.datetime.now()
                rows_updated += 1
                entry.save()
        if rows_updated == 1:
            message_bit = "1 blog was"
        else:
            message_bit = "%s blogs ware "%rows_updated
        self.message_user(request, "%s successfully published" % message_bit)
        
    make_published.short_description = u"发布"

    


    #def change_view(self, request, object_id, form_url='', extra_context=None):
    #    extra_context = extra_context or {}
    #    extra_context['show_save_and_add_another'] = False
    #    # or
    #    extra_context['really_hide_save_and_add_another_damnit'] = True
    #    return super(BlogAdmin, self).change_view(request, object_id,
    #        form_url, extra_context=extra_context)
    
    

    class Media:
        pass

class TagAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)





