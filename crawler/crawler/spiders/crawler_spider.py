#coding:utf8
import scrapy
from crawler.items import crawlerItem
import logging

logger = logging.getLogger(__name__)


class jianshu_Spider(scrapy.Spider):
    name = "jianshu"
    allowed_domains = ["jianshu.com"]
    start_urls = [
        "http://www.jianshu.com/"
    ]

##    post方法
##    def start_requests(self):
##        payload = None
##        return [scrapy.http.FormRequest(url=start_url,formdata=payload,
##                    callback=self.parse, dont_filter=True) for start_url in self.start_urls]

    def parse(self, response):
        for url in response.css("#list-container .title::attr(href)").extract()
            yield scrapy.Request(response.urljoin(url), callback=self.parse_content)

    def parse_content(self, response):
        title = response.css(".title::text").extract_first()
        # 将url替换为完整地址
        content_etree = response.css(".show-content")
        for tag in content_etree.getiterator():
            if "href" in tag.attrib:
                tag.attrib["href"] = response.urljoin(tag.attrib["href"])
        content = content_etree.extract_unquoted()
        pure_content = "\n".join(response.css(".show-content p::text").extract())

    def test(self, response):
        '''测试方法，回调进入交互式测试'''
        from scrapy.shell import inspect_response
        inspect_response(response, self)
