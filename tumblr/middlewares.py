# -*- coding: utf-8 -*-
from scrapy import signals


class TumblrSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        return None

    def process_spider_output(response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        pass

    def process_start_requests(start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
