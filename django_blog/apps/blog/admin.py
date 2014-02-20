#! encoding=utf-8
from django.contrib import admin
import reversion
from .models import Tag, Blog, Category

class BlogAdmin(reversion.VersionAdmin):
    list_display = ('id', 'title', 'add_time', 'update_time')
    search_fields = ('title',)
    ordering = ('-add_time', )
    list_per_page = 60

class TagAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
