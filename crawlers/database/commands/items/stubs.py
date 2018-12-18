# -*- coding: utf-8 -*-

MODEL_DEFAULT_STUB = """import scrapy


class DummyClass(scrapy.Item):
    __table_name__ = 'dummy_table'

    # define the uniq field names for your items here like: (Optional)
    # __uniq_fields__ = []

    # define the fields for your items here like:
    # name = scrapy.Field()
"""
