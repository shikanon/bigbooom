#coding:utf8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True)
    introduction = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(u'创建时间', auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    create_date = models.DateField(u'创建时间', auto_now=True)


class Source(models.Model):
    name = models.CharField(max_length=200, unique=True)
    star = models.IntegerField(default=0)
    url = models.URLField(null=True, blank=True)
    tag = models.ManyToManyField(Tag)


class Paper(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(u'创建时间', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)#外键被删除时，paper不影响
    content = models.TextField(null=True, blank=True)# 网页源码
    pure_content = models.TextField(null=True, blank=True)# 纯文字
    doc_vector = models.CharField(max_length=100, null=True, blank=True)# 文章向量
    origin_url = models.URLField(u'源地址', null=True, blank=True)

    tags = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    Source = models.ForeignKey(Source, null=True, blank=True)