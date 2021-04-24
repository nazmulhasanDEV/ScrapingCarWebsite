import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    # allowed_domains = ['https://www.cars.com/research/bmw-740-2021/']
    start_urls = ['https://www.cars.com/research/bmw-740-2021/']

    def parse(self, response):
        category1 = response.xpath("//span[@class='rating__count']/b/text()").get()
        all_review_cats = response.xpath("//div[@class='rating-breakdown__item']/dt/text()").getall()
        all_review_values = response.xpath("//div[@class='rating-breakdown__item']/dd/div[@class='rating__count']/text()").getall()
        data = {}
        data["overall_review"] = category1
        for x in range(5):
            data[all_review_cats[x]] = all_review_values[x]
        yield data