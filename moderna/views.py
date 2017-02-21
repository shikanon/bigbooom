#coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from moderna.models import Category, Paper


# Create your views here.
def home_index(request):
    all_category = Category.objects.all()
    context = {'categories': all_category}
    return render(request, 'index.html', context)


def page(request, page_id):
    """
    slug为文章标题
    """
    page = get_object_or_404(Paper, id=page_id)
    context = {'paper':page}
    return render(request, 'pages/paper.html', context)


def page_list(request, category_id):
    #category = get_object_or_404(Category, category=category_id)
    pages = Paper.objects.filter(category=category_id)
    category = get_object_or_404(Category, id=category_id)
    context = {"pages": pages, "category":category}
    return render(request, 'page_lists/index.html', context)