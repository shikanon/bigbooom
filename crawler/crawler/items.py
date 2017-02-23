# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
import sys
import os
from os.path import dirname
PROJECT_APP_PATH = dirname(dirname(dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_APP_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bigbooom.settings'
from moderna.models import Paper

class PaperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Paper
