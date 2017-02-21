#coding:utf8
from moderna.views import home_index, page, page_list
from django.conf.urls import url


app_name = 'home'
urlpatterns = [url(r'^$', home_index, name='index'),
               url(r'^page/(\d+)/$', page, name='page'),
               url(r'^list/(\d+)/', page_list, name='page_list')]