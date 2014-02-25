#! coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms

STATUS_CHOICES = (
    ('d', u"草稿"),
    ('p', u"发布"),
)

class Blog(models.Model):
    title = models.CharField(u'标题', max_length=150, db_index=True, unique=True)
    link = models.CharField(u'链接', max_length=150, null=True, blank=True, unique=True)
    snippet = models.CharField(u'摘要', max_length=500, default='', blank=True) 
    content = models.TextField(u'内容',)

    add_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    publish_time = models.DateTimeField(u'发表时间', null=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    status = models.CharField(u'状态', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    #published = models.BooleanField(u'发布', default=False)

    is_public = models.BooleanField(u'公开', default = True)
    is_top = models.BooleanField(u'置顶', default=False)
    access_count  = models.IntegerField(u'浏览量', default=1, editable=False)
    category = models.ForeignKey('Category', verbose_name=u'所属分类')
    tags = models.ManyToManyField('Tag', verbose_name=u'标签集合', null=True, blank=True)
    tags.help_text = ''
    author = models.ForeignKey(User, verbose_name=u'作者')

    




class Category(models.Model):
    '''
    大分类
    '''
    title = models.CharField(u'名称', max_length=50, db_index=True,unique=True)

    class Meta:
        ordering = ['title',]

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    '''
    小标签
    '''
    title = models.CharField(u'名称', max_length=50, db_index=True,unique=True)

    def __unicode__(self):
        return self.title



