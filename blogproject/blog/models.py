# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .mixin import TimeModelMixin, EditorModelMixin, BaseModel
# Create your models here.


class Category(TimeModelMixin, EditorModelMixin, BaseModel):
    name = models.CharField(max_length=100)


class Tag(TimeModelMixin, EditorModelMixin, BaseModel):
    name = models.CharField(max_length=100)


class Article(TimeModelMixin, EditorModelMixin, BaseModel):
    title = models.CharField(u'文章标题', max_length=70)
    body = models.TextField(u'文章主体')

    abstract = models.CharField(u'文章摘要', max_length=120, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ForeignKey(Tag, blank=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

