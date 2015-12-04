# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
