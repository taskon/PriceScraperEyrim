"""
	Scrapes prices for all products for each website

	Author:Anastasios

"""
import scrapy


class EyreimSpider(scrapy.Spider):
    
	name = "eyerimFollow"
	start_urls = [
	
        'https://www.eyerim.cz/brand/35-139-tokyo',
		'https://www.eyerim.cz/brand/alexander-mcqueen',
		'https://www.eyerim.cz/brand/arnette',
		'https://www.eyerim.cz/brand/bob',
		'https://www.eyerim.cz/brand/bolle',
		'https://www.eyerim.cz/brand/boss-by-hugo-boss',
		'https://www.eyerim.cz/brand/boss-orange',
		'https://www.eyerim.cz/brand/bottega-veneta',
		'https://www.eyerim.cz/brand/briko',
		'https://www.eyerim.cz/brand/bvlgari',
		'https://www.eyerim.cz/brand/carrera',
		'https://www.eyerim.cz/brand/cebe',
		'https://www.eyerim.cz/brand/chloe',
		'https://www.eyerim.cz/brand/christopher-cloos',
		'https://www.eyerim.cz/brand/diesel',
		'https://www.eyerim.cz/brand/dior',
		'https://www.eyerim.cz/brand/dior-homme',
		'https://www.eyerim.cz/brand/dolce-gabbana',
		'https://www.eyerim.cz/brand/dsquared2',
		'https://www.eyerim.cz/brand/emilio-pucci',
		'https://www.eyerim.cz/brand/emporio-armani',
		'https://www.eyerim.cz/brand/ermenegildo-zegna',
		'https://www.eyerim.cz/brand/fendi',
		'https://www.eyerim.cz/brand/fossil',
		'https://www.eyerim.cz/brand/g-star-raw',
		'https://www.eyerim.cz/brand/giorgio-armani',
		'https://www.eyerim.cz/brand/gucci',
		'https://www.eyerim.cz/brand/guess',
		'https://www.eyerim.cz/brand/havaianas',
		'https://www.eyerim.cz/brand/horsefeathers',
		'https://www.eyerim.cz/brand/jimmy-choo',
		'https://www.eyerim.cz/brand/juicy-couture',
		'https://www.eyerim.cz/brand/just-cavalli',
		'https://www.eyerim.cz/brand/kerbholz',
		'https://www.eyerim.cz/brand/komono',
		'https://www.eyerim.cz/brand/lacoste',
		'https://www.eyerim.cz/brand/luxottica',
		'https://www.eyerim.cz/brand/marc-jacobs',
		'https://www.eyerim.cz/brand/max-mara',
		'https://www.eyerim.cz/brand/max-co',
		'https://www.eyerim.cz/brand/michael-kors',
		'https://www.eyerim.cz/brand/miss-sixty',
		'https://www.eyerim.cz/brand/miu-miu',
		'https://www.eyerim.cz/brand/moncler',
		'https://www.eyerim.cz/brand/mont-blanc',
		'https://www.eyerim.cz/brand/moschino',
		'https://www.eyerim.cz/brand/nike',
		'https://www.eyerim.cz/brand/oakley',
		'https://www.eyerim.cz/brand/oxydo',
		'https://www.eyerim.cz/brand/persol',
		'https://www.eyerim.cz/brand/pierre-cardin',
		'https://www.eyerim.cz/brand/polaroid',
		'https://www.eyerim.cz/brand/polaroid-junior',
		'https://www.eyerim.cz/brand/polaroid-premium',
		'https://www.eyerim.cz/brand/polaroid-sport',
		'https://www.eyerim.cz/brand/police',
		'https://www.eyerim.cz/brand/polo-ralph-lauren',
		'https://www.eyerim.cz/brand/prada',
		'https://www.eyerim.cz/brand/prada-linea-rossa',
		'https://www.eyerim.cz/brand/ralph-by-ralph-lauren',
		'https://www.eyerim.cz/brand/ralph-lauren',
		'https://www.eyerim.cz/brand/ray-ban',
		'https://www.eyerim.cz/brand/ray-ban-junior',
		'https://www.eyerim.cz/brand/roberto-cavalli',
		'https://www.eyerim.cz/brand/safilo',
		'https://www.eyerim.cz/brand/seventh-street',
		'https://www.eyerim.cz/brand/sferoflex',
		'https://www.eyerim.cz/brand/smith',
		'https://www.eyerim.cz/brand/stella-mccartney',
		'https://www.eyerim.cz/brand/swarovski',
		'https://www.eyerim.cz/brand/tiffany-co',
		'https://www.eyerim.cz/brand/timberland',
		'https://www.eyerim.cz/brand/tommy-hilfiger',
		'https://www.eyerim.cz/brand/tommy-hilfiger-junior',
		'https://www.eyerim.cz/brand/uvex',
		'https://www.eyerim.cz/brand/versace',
		'https://www.eyerim.cz/brand/vogue',
		'https://www.eyerim.cz/brand/web',
		'https://www.eyerim.cz/brand/yacht-club',
		'https://www.eyerim.cz/brand/yves-saint-laurent',
	
		
	]
		
	def parse(self, response):
			
		for models in response.css('li.item.col-sm-4.col-xs-6'):  #holds all the models
			yield {
				'product_name': models.css('span.product-name::text').extract(),
				#'price': models.css('span.price::text').get().partition('K')[0].rstrip().replace(u'\xa0', u''),	
				'model' : models.css('span.model::text').extract(),
				'price':  models.css('span::attr(content)').extract(),
				'url' : response.url.split('/')[2], # get the url 
            }
		#
		# crawl recursively all the sites in the page for each of the products in start_urls
		#
		for next_page in response.css('ul.international a::attr(href)').getall(): # get a list of all the sites
			if next_page is not None and next_page != "https://www.eyerim.com/brand/35-139-tokyo/": # skip .com as it redirects to cz 
					yield scrapy.Request(next_page, callback=self.parse) 
