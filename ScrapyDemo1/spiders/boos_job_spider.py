import scrapy
from scrapy import Request

from ..items import BossJob_Item


class jobSpider(scrapy.Spider):
    name = "boss_job"
    allowed_domains = ["zhipin.com"]
    start_urls = [
        "https://www.zhipin.com/c101280600-p100101/"
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        next_page = sel.xpath("//div/div[@class='job-list']/div[@class='page']/a[@class='next']/@href").extract()
        # print("_______________")
        # print(next_page)
        # print("_______________")
        if next_page:
            next_page_url = "https://www.zhipin.com" + next_page[0]
            yield Request(next_page_url)
        item = BossJob_Item()
        sites = sel.select("//div[@class='job-list']/ul/li")
        for site in sites:
            item['job_name'] = \
            site.select("div/div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()[0]
            item['job_pay'] = site.select("div/div[@class='info-primary']/h3/a/span/text()").extract()[0]

            #标签里有多个文本
            job_descriptions = site.select("div/div[@class='info-primary']/p/text()").extract()
            item['job_age'] = job_descriptions[0]
            item['job_area'] = job_descriptions[1]
            item['education'] = job_descriptions[2]

            item['company_name'] = site.select("div/div[@class='info-company']/div/h3/a/text()").extract()[0]
            item['company_url'] = "https://www.zhipin.com" + \
                                  site.select("div/div[@class='info-company']/div/h3/a/@href").extract()[0]

            company_descriptions = site.select("div/div[@class='info-company']/div/p/text()").extract()
            item['company_description'] = ''.join(company_descriptions)
            yield item
