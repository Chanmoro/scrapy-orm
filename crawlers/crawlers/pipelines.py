# -*- coding: utf-8 -*-

# Define your items pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .orm import generate_model_class


class ScrapyOrmPipeline(object):
    def process_item(self, item, spider):
        _table_name = getattr(item, '__table_name__', None)
        _uniq_keys = getattr(item, '__uniq_fields__', {})

        # Generate orator model class.
        model_class = generate_model_class(type(item).__name__, item.keys(), _table_name)

        # If there is a record having same keys return it, if not create new record, doing like "upsert".
        model = model_class.first_or_new(**{k: item[k] for k in _uniq_keys})

        # Set model attributes from item.
        for attr in item.keys():
            setattr(model, attr, item[attr])
        model.save()
        return item
