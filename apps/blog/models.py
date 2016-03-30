#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import re

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', "已发布"),
    )

    title = models.CharField('标题', max_length=150, db_index=True, unique=True)
    link = models.CharField('链接', max_length=150, default='')
    link.help_text = "Cool URIs don't change"
    snippet = models.CharField('摘要', max_length=500, default='')
    content = models.TextField('内容', )

    add_time = models.DateTimeField('创建时间', auto_now_add=True)
    publish_time = models.DateTimeField('发表时间', null=True)
    update_time = models.DateTimeField('修改时间')
    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    is_public = models.BooleanField('公开', default=True)
    is_top = models.BooleanField('置顶', default=False)
    access_count = models.IntegerField('浏览量', default=1, editable=False)
    category = models.ForeignKey('Category', verbose_name='所属分类')
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', null=True, blank=True)
    tags.help_text = '标签'
    author = models.ForeignKey(User, verbose_name='作者')

    def save(self, *args, **kwargs):
        self.link = slugify(self.link)
        self.snippet = self.snippet or self.content[:140]
        modified = kwargs.pop("modified", True)
        if modified:
            self.update_time = datetime.datetime.utcnow()
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=(self.id, self.link))

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    大分类
    """
    title = models.CharField('名称', max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['title', ]

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    小标签
    """
    title = models.CharField('名称', max_length=50, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        self.title = re.sub("\s", "", self.title)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
