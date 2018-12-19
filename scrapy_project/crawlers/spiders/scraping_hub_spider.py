import scrapy

from ..items import Page


class ScrapingHubSpider(scrapy.Spider):
    name = 'scraping_hub'

    def start_requests(self):
        url = 'https://blog.scrapinghub.com/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield Page(
                url=post.css('div.post-header h2 a::attr(href)').extract_first(),
                title=post.css('div.post-header h2 a::text').extract_first()
            )

        next_page = response.css('div.blog-pagination a.next-posts-link::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(next_page, self.parse)
