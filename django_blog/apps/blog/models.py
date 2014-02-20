#! coding=utf-8
from django.db import models
from django.contrib.auth.models import User

from tinymce import models as tinymce_models
from django import forms
from tinymce.widgets import TinyMCE

class Blog(models.Model):
    title = models.CharField(u'标题', max_length=150, db_index=True, unique=True)
    content = models.TextField(u'内容')
    #content = tinymce_models.HTMLField(u'内容')
    add_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    access_count  = models.IntegerField(u'访问次数', default=1)
    category = models.ForeignKey('Category', verbose_name=u'所属分类')
    tags = models.ManyToManyField('Tag', verbose_name=u'标签集合')
    author = models.ForeignKey(User, verbose_name=u'作者')




class Category(models.Model):
    '''
    大分类
    '''
    title = models.CharField(u'名称', max_length=50, db_index=True,unique=True)

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    '''
    小标签
    '''
    title = models.CharField(u'名称', max_length=50, db_index=True,unique=True)

    def __unicode__(self):
        return self.title


#class FlatPageForm(forms.ModelForm):
#    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
#    class Meta:
#        model = Blog
