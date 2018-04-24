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
        next_page=sel.xpath("//div/div[@class='job-list']/div[@class='page']/a[@class='next']/@href").extract()
        # print("_______________")
        # print(next_page)
        # print("_______________")
        next_page_url="https://www.zhipin.com"+next_page[0]
        yield Request(next_page_url)
        item = BossJob_Item()
        sites = sel.select("//div[@class='job-list']/ul/li")
        for site in sites:
            item['job_name'] = site.select("div/div[@class='info-primary']/h3/a/div[@class='job-title']").extract()
            item['job_name'] = ''.join(item['job_name'])
            item['job_pay'] = site.select("div/div[@class='info-primary']/h3/a/span").extract()
            item['job_pay'] = ''.join(item['job_pay'])
            item['job_description'] = site.select("div/div[@class='info-primary']/p").extract()
            item['job_description'] = ''.join(item['job_description'])
            item['company_name'] = site.select("div/div[@class='info-company']/div/h3").extract()
            item['company_name'] = ''.join(item['company_name'])
            item['company_description'] = site.select("div/div[@class='info-company']/div/p").extract()
            item['company_description'] = ''.join(item['company_description'])
            yield item
