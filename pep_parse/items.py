import scrapy


class PepParseItem(scrapy.Item):
    """Item for parsing info about peps"""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
