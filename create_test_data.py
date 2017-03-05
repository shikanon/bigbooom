#coding:utf8
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigbooom.settings")
django.setup()

from moderna.models import Category, Paper
from citizen.models import Citizen
from django.contrib.auth.models import User

category_all_kwargs = [
    {'name':u'游戏玩家', 'introduction': '单机游戏、游戏攻略'},
    {'name': u'新闻资讯', 'introduction': '各类新闻、新闻快报'},# 央视新闻
    {'name': u'二次元', 'introduction': '二次元资讯、点评'},
    {'name': u'技术前沿', 'introduction': '技术博客、前沿资讯'},# 开发者头条、InfoQ
    {'name': u'娱乐八卦', 'introduction': '搞笑段子、娱乐新闻、八卦新闻'},# UC神评论
    {'name': u'女性生活', 'introduction': '美丽、时尚、女性、生活'},# 蒙咪
    {'name': u'金融投资', 'introduction': '投资热点、今日头条'},# 36kr
    {'name': u'同性社区', 'introduction': '未知的领域，等待你加入，更精彩'},
    {'name': u'算法建模', 'introduction': '智慧资讯、科技盛宴、人工智能'},# 机器之心、新智元、open-open
    {'name': u'高出不胜寒', 'introduction': '起舞弄清影，高学历自娱自乐'},# 中科院
]

for kwargs in category_all_kwargs:
    try:
        category = Category(**kwargs)
        category.save()
    except:
        pass


user_kwargs = {"username": u"泛资讯收割者",
                  "email": u"shikanon@foxmail.com",
                  "is_staff": True,
                  "is_active": True,}
user = User(**user_kwargs)
user.set_password('new password')
user = User.objects.get(username=u"泛资讯收割者")
user.citizen.nickname = u"资讯收割者1号"
user.citizen.is_gril = False
user.save()
# citizen_kwargs = {"nickname": u"资讯收割者1号","is_gril": False}
# people = Citizen(**citizen_kwargs)
# people.user = user
# people.save()