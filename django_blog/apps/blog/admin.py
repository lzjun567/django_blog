#! coding=utf-8
from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
import reversion
from .models import Tag, Blog, Category


class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 150, 'rows': 30}))
    class Meta:
        model = Blog

class BlogAdmin(reversion.VersionAdmin):
    list_display = ('id', 'title', 'add_time', 'update_time','access_count')
    search_fields = ('title',)
    ordering = ('-add_time', )
    list_per_page = 60
    form = FlatPageForm
    class Media:
        pass
        #js = ('js/textarea.js','tiny_mce/tiny_mce.js')

class TagAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
