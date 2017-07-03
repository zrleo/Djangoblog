# -*- coding:utf-8 -*-

from django import template


from ..models import Article, Category

register = template.Library()


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by("-created_time")[:num]


@register.simple_tag
def archives():
    '''归档模板标签函数'''
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
