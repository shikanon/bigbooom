#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(u'昵称', max_length=32, null=True)
    level = models.IntegerField(u'用户等级', default=1)
    age = models.IntegerField(u'年龄', default=18)
    is_gril = models.BooleanField(u'性别', default=False)

    telephone = models.CharField(u'手机', max_length=16, null=True, blank=True)
    create_IP = models.GenericIPAddressField(null=True)
    last_login_IP = models.GenericIPAddressField(null=True)

    #regist_date = models.DateField(u'注册时间', auto_now=True)
    #last_login_date = models.DateField(u'最后登录时间', auto_now=datetime.now())
    # ch_stat = ((1, u'正常'), (0, u'已禁用'))
    # stat = models.SmallIntegerField(u'状态', choices=ch_stat, default=1)
    # email = models.CharField(u'邮件地址', max_length=64, unique=True, null=True)
    # is_staff = models.BooleanField(u'是否为管理员', default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Citizen.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.citizen.save()