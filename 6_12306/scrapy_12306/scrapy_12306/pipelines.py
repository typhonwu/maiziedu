# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

from scrapy.exceptions import DropItem
from project23.items import CommitItem


class ProvincePipeline2(object):
    def process_item(self, item, spider):
        print item["name"], "--------"
        return item

class ProvincePipeline1(object):
    def process_item(self, item, spider):
        if item["name"]:
            return item
        else:
            raise DropItem("none item")

class AgencySQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', port = 3306, 
                                        user = '12306',
                                        password = '12306',
                                        db = '12306-train',
                                        charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.sql = "INSERT IGNORE INTO `agencys` (`province`, `city`,\
                `county`, `address`, `name`, `windows`,\
                `start`, `end`) VALUES\
                (%s, %s, %s, %s, %s, %s, %s, %s)"

    def process_item(self, item, spider):
        # 如果提交的是commititem，就执行一次数据库提交
        # 这给出一个思路：通过定义某些特殊item，然后爬虫把它们当做信号来通知pipeline进行特定处理
        # 耦合度就低很多了
        if isinstance(item, CommitItem):
            self.conn.commit()
        else:
            self.cursor.execute(self.sql, (item["province"], item["city"],
                item["county"], item["address"],
                item["name"], item["windows"],
                item["start"] + u"00",
                item["end"] + u"00"))
        
