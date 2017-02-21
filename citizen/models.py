#coding:utf8
from django.db import models
from datetime import datetime

# class MyUserManager(models.Model):
#
#     def create_user(self, username, password, **kwargs):
#         if not username:
#             raise ValueError(u'username 不能为空')
#         if len(password) >= 8:
#             raise ValueError(u'密码必须8位以上')
#
#         user = self.model(username=username, **kwargs)
#         user.set_password(password)
#         user.save()
#         return user


class Citizen(models.Model):

    user = models.OneToOneField("auth.User")

    username = models.CharField(max_length=50, unique=True)
    regist_date = models.DateField(u'注册时间', auto_now=True)
    nickname = models.CharField(u'昵称', max_length=32, null=True)
    #is_staff = models.BooleanField(u'是否为管理员', default=False)
    level = models.IntegerField(u'用户等级', default=1)
    age = models.IntegerField(u'年龄', default=18)
    is_gril = models.BooleanField(u'性别', default=None)
    ch_stat = ((1, u'正常'), (0, u'已禁用'))
    stat = models.SmallIntegerField(u'状态', choices=ch_stat, default=1)
    #email = models.CharField(u'邮件地址', max_length=64, unique=True, null=True)
    telephone = models.CharField(u'手机', max_length=16, null=True, blank=True)
    create_IP = models.GenericIPAddressField()
    last_login_IP = models.GenericIPAddressField()
    last_login_date = models.DateField(u'注册时间', auto_now=datetime.now())