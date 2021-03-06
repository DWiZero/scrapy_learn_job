
import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from scrapy.http import Response, TextResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def getCityCodeList():
    cityCodeList = set()
    browser = webdriver.Chrome()
    browser.get('https://www.zhipin.com/')
    wait = WebDriverWait(browser, 10)
    # 点击城市选择元素->才会生成相应元素
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.city-sel')))
    input = browser.find_element_by_class_name("city-sel")
    input.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='city-box']/ul['@class=dorpdown-province']")))
    input = browser.find_elements_by_xpath("//div[@class='city-box']/ul['@class=dorpdown-province']/li")
    # 依据出现的城市标签
    for ul in input:
        # 相应的焦点出现的城市，会出现具体元素
        ActionChains(browser).move_to_element(ul).perform()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='city-box']/div[@class='dorpdown-city']/ul[@class='show']")))
        city = browser.find_elements_by_xpath(
            "//div[@class='city-box']/div[@class='dorpdown-city']/ul[@class='show']/li")
        for li in city:
            if li.text:
                # print('c' + li.get_attribute("data-val"))
                cityCodeList.add('c' + li.get_attribute("data-val"))
    browser.close()
    # 去除全国这一编码
    cityCodeList.remove('c'+'100010000')
    return cityCodeList



if __name__ == '__main__':
    a = getCityCodeList()
    print(a)