# -*- coding:utf-8 -*-


import markdown
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Article, Category

# Create your views here.


def index(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page('1')
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request, 'blog_tmp/index.html', context={'article_list': article_list})


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,  extensions=[
                                                               'markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc',
                                                               ])
    return render(request, 'blog_tmp/detail.html', context={'article': article})


def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month).order_by("-created_time")
    return render(request, 'blog_tmp/index.html', context={'article_list': article_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by("-created_time")
    return render(request, 'blog_tmp/index.html', context={'article_list': article_list})


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blog_tmp/error.html', context={'error_msg': error_msg})
    article_list = Article.objects.filter(title__icontains=q)
    return render(request, 'blog_tmp/result.html', {'error_msg': error_msg,
                                                    'article_list': article_list})
