import scrapy


class Eyerim2(scrapy.Spider):
    name = "eyerim2"
    start_urls = [
        
		'http://eyerim.cz/brand/35-139-tokyo/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                #'product_name': models.css('span.product-name').get(),
				#'price': models.css('span.price::text').get().partition('K')[0].rstrip().replace(u'\xa0', u''),	
				'model' : models.css('span.model::text').extract(),
				'price':  models.css('span::attr(content)').extract()
            }