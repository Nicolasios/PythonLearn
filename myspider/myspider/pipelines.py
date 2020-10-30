# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

logger = logging.getLogger(__name__)

class MyspiderPipeline(object):
    #process_item不能改为其他的名称
    def process_item(self, item, spider):
        if spider.name == "itcast":
            logger.warning("-" * 10)
        return item
