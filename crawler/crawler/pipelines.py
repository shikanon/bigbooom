#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine


class JsonWithEncodingPipeline(object):
    '''输出json lines文件'''
    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True)

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        pass

