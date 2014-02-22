#! coding=utf-8
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

    list_display = ('title', 'published', 'last_update','access_count')
    fields = ('title', 'content', ('is_public', 'is_top'), 'category', 'tags')
    exclude = ('publish_time', 'published')
    search_fields = ('title',)
    ordering = ('-add_time', )
    list_per_page = 60
    form = BlogForm

    extra_context = {
              'show_save_and_add_another': False,
                'show_save_and_continue': False
                }
    


    def create_time(self, obj):
        return obj.add_time.strftime('%Y-%m-%d')
    create_time.short_description = u"创建时间"

    def last_update(self, obj):
        return obj.update_time.strftime('%Y-%m-%d')
    last_update.short_description = u"最后更新时间"


    
    def response_change(self, request, obj):
        '''保存为草稿，这种方法很蠢，please fix me'''
        #FIXME
        res = super(BlogAdmin, self).response_change(request, obj)
        if "_continue" in request.POST:
            obj.published = False
            obj.save()
        return res

    


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
