# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossJob_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 工作名称
    job_name = scrapy.Field()
    # 工作薪资
    job_pay = scrapy.Field()
    # 工作描述
    job_description = scrapy.Field()

    # 工司名称
    company_name = scrapy.Field()
    # 工司描述
    company_description = scrapy.Field()
    # pass
