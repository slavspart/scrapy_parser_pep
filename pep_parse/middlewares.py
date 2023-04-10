from scrapy import signals


class CustomMiddlewareClass:
    """Parent class for inheritance of custom middlewares"""
    # Сами классы, которые были по умолчанию описывать не стал
    # т.к. в текущем проекте они не используются
    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        crawler.signals.connect(
            spider.spider_opened,
            signal=signals.spider_opened)
        return spider

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for item in result:
            yield item

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            yield request

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
