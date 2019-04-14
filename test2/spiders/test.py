import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'http://eyerim.cz/brand/35-139-tokyo/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'aaaaa-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)