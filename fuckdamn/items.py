# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
#import scrapy
class Person(Item):
    name = Field()
    age = Field()
    bullet = Field()
    nationnality = Field()
#   height = scrapy.Field()
    fit = Field()
#    pass
#   race = scrapy.Field()
#   education = scrapy.Field()
#   marriage = scrapy.Field()
    price = Field()
#    language = scarpy.Field()
