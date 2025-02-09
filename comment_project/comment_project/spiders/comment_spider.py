import scrapy


class CommentSpiderSpider(scrapy.Spider):
    name = "comment_spider"
    allowed_domains = ["website-url.com"]
    start_urls = ["https://website-url.com"]

    def parse(self, response):
        pass
