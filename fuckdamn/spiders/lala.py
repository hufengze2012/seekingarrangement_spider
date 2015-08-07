import re
import json
import os

#from scrapy.spiders import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector
from scrapy.http import HtmlResponse  
#from sweetheart.items import *
from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from fuckdamn.items import *
from scrapy.contrib.loader import XPathItemLoader
import scrapy
from scrapy import log
class shspider(CrawlSpider):
    name = "sweetheartspider"
    allowed_domains = ["seekingarrangement.com"]
    username = "361805529@qq.com"
    password = "hfz7215"
    num = 0
    start_urls = "https://www.seekingarrangement.com/zh/login.php?previous_url=/member/search.php?default=on&last_login_dt=1404713999&sort=created_dt_desc"
    def start_requests(self):
        return [scrapy.FormRequest(self.start_urls,formdata={'email': self.username,'pass': self.password},callback=self.list_item)]
    def list_item(self, response):
#        log.msg("the reponse_URL:%s" % response.url,level=log.DEBUG)
        sel=Selector(text=response.body)
        result_list=sel.xpath("//div[@class='result-list-item__inner']").extract()
#        logging.info("the reponse URL:%s" % response.url)
#        with open("temp.txt",'wb') as f:
#            f.write(response.selector.xpath("//div[@class='result-list-item__inner']").extract())
#        result_list=response.xpath("//div[@class='result-list-item__inner']").extract()
        num=0
        for result_item in result_list:
            num=num+1
            log.msg("this is the %d item" % num,level=log.DEBUG)
            loader=XPathItemLoader(item=Person(),selector=Selector(text=result_item))
            loader.add_xpath('name',".//h4[@class='member-title result-name']/text()")
            loader.add_xpath('age',".//div[@class='primary-description truncated-line']/text()[1]")
            loader.add_xpath('bullet',".//div[@class='primary-description truncated-line']/text()[2]")
            loader.add_xpath('fit',".//ul[@class='unstyled-list'][1]/li[1]/text()")
            loader.add_xpath('nationnality',".//ul[@class='unstyled-list'][1]/li[2]/text()")
            loader.add_xpath('price',".//ul[@class='unstyled-list'][2]/li/text()")
#            items.append(item)
            yield loader.load_item()
        
        url=sel.xpath("//li[@class='pagination__next ']/a/@href").extract()
#        print url
        yield Request(url[0],callback=self.list_item)


