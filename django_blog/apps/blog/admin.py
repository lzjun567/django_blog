#! coding=utf-8
from django.contrib import admin
from django import forms
import reversion
from .models import Tag, Blog, Category
from pagedown.widgets import AdminPagedownWidget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Blog

class BlogAdmin(reversion.VersionAdmin):
    list_display = ('id', 'title', 'add_time', 'update_time','access_count')
    search_fields = ('title',)
    ordering = ('-add_time', )
    list_per_page = 60
    form = BlogForm
    class Media:
        pass

class TagAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
