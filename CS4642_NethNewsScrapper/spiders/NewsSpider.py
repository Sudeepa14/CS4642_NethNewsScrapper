
import scrapy

class NewsSpider(scrapy.Spider):

    name = "News"

    start_urls = [
        'http://nethnews.lk/category/5'
    ]

    def parse(self, response):
        for news in response.css('div.breaking_news'):
            yield {
                'title':news.xpath('//h3[@class="entry-title"]/a/@title').extract_first(),
                'date': news.xpath('//div[@class="publish_date"]/text()').extract_first(),
                'details': news.xpath('//div[@class="top_breaking_news_discription"]/text()').extract_first(),
                'link': news.xpath('//h3[@class="entry-title"]/a/@herf').extract_first()
            }

        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
