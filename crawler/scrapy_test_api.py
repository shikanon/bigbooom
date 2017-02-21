import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .crawler.spiders.crawler_spider import jianshu_Spider


#get_project_settings()是字典形式，如{'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
process = CrawlerProcess(get_project_settings())
# 'followall' is the name of one of the spiders of the project.
#需要同时跑多个爬虫只需要
#process.crawl(MySpider1)
#process.crawl(MySpider2)
process.crawl(jianshu_Spider)
process.start() # the script will block here until the crawling is finished
