# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tag, Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'last_update', 'category', 'author']

admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
