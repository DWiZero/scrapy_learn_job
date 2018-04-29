import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from ..items import BossJob_Item

class jobSpider(scrapy.Spider):
    name = "boss_job"
    allowed_domains = ["zhipin.com"]
    start_urls = [
        "https://www.zhipin.com/",
        "https://www.zhipin.com/c101280600-p100101/"
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        self.getAllJobClass(sel)
        self.getCityDistrict(sel)
        self.getDistrictStreet(sel)
        # yield from self.getNextPageUrl(sel)
        yield from self.getJobInfo(sel)


    def getJobInfo(self, sel):
        item = BossJob_Item()
        sites = sel.select("//div[@class='job-list']/ul/li")
        for site in sites:
            item['job_name'] = \
                site.select("div/div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()[0]
            item['job_pay'] = site.select("div/div[@class='info-primary']/h3/a/span/text()").extract()[0]

            job_url = site.select("div/div[@class='info-primary']/h3/a/@href").extract()[0]
            item['job_url'] = "https://www.zhipin.com" + job_url
            # 标签里有多个文本
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

    # 获取页面的下一页连接
    def getNextPageUrl(self, sel):
        next_page = sel.xpath("//div/div[@class='job-list']/div[@class='page']/a[@class='next']/@href").extract()
        if next_page:
            next_page_url = "https://www.zhipin.com" + next_page[0]
            yield Request(next_page_url)

    # 获取所有的分类
    def getAllJobClass(self, sel):
        allJobClass = []
        jobClass = sel.xpath("//div/div[@class='job-menu']/dl/div[@class='menu-sub']").extract()

        if jobClass:
            for item in jobClass:
                soup = BeautifulSoup(item, 'lxml')
                for link in soup.find_all('a'):
                    uri = link.get('href')
                    if uri.startswith('/'):
                        allJobClass.append("https://www.zhipin.com" + uri)
        print("_____allJobClass______")
        print(allJobClass)
        print("_____allJobClass______")

    # 获取所有的城市的所有区
    def getCityDistrict(self, sel):
        allDistrict = []
        District = sel.xpath(
            "//div[@class='condition-box']/dl[@class='condition-district show-condition-district']").extract()
        if District:
            for item in District:
                soup = BeautifulSoup(item, 'lxml')
                for link in soup.find_all('a'):
                    uri = link.get('href')
                    if uri.startswith('/'):
                        allDistrict.append("https://www.zhipin.com" + uri)
        print("_____allDistrict______")
        print(allDistrict)
        print("_____allDistrict______")

    # 获取所有的城市的区的街道
    def getDistrictStreet(self, sel):
        allStreet = []
        Street = sel.xpath(
            "//div[@class='condition-box']/dl[@class='condition-area']").extract()
        if Street:
            for item in Street:
                soup = BeautifulSoup(item,'lxml')
                for link in soup.find_all('a'):
                    uri = link.get('href')
                    if uri.startswith('/'):
                        allStreet.append("https://www.zhipin.com" + uri)
        print("_____allStreet______")
        print(allStreet)
        print("_____allStreet______")
