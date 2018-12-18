import scrapy


class Page(scrapy.Item):
    __table_name__ = 'pages'

    # define the uniq field names for your items here like: (Optional)
    __uniq_fields__ = ['url']

    # define the fields for your items here like:
    url = scrapy.Field()
    title = scrapy.Field()
