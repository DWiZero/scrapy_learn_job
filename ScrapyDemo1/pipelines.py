# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Scrapydemo1Pipeline(object):
    def __init__(self):
        self.db = pymysql.Connect("localhost", "root", "123456", "python_conn", charset="utf8")

    def process_item(self, BossJob_Item, spider):
        # try:
        cursor = self.db.cursor()
        sql = "INSERT INTO boss_job(job_name, job_pay, job_description, company_name, company_description) VALUES ('" + \
              BossJob_Item['job_name'] + "','" + BossJob_Item['job_pay'] + "','" + BossJob_Item[
                  'job_description'] + "','" + BossJob_Item['company_name'] + "','" + BossJob_Item[
                  'company_description'] + "')"
        cursor.execute(sql)
        # 执行sql语句
        self.db.commit()
        # except:
        #     self.db.rollback()
        # # 关闭数据库连接
        # self.db.close()
        return BossJob_Item
