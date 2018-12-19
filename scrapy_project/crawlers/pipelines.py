# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from orator import DatabaseManager
from orator import Model
from database import settings
from database.models.page import Page

db = DatabaseManager(settings.DATABASES)
Model.set_connection_resolver(db)


class ScrapyOrmPipeline(object):
    def process_item(self, item, spider):
        if not Page.where('url', '=', item['url']).take(1).count():
            p = Page()
            for attr in item.keys():
                setattr(p, attr, item[attr])
            p.save()
        return item
