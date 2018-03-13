import scrapy

class house_scrapy(scrapy.Spider):
	name = 'lianjia'
	start_urls = ['''https://sh.fang.lianjia.com/loupan/pg{}/'''.format(i) for i in range(2,30)]

	def parse(self,response):
		for house in response.css('body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper > li'):
			yield {
			'picture': house.css('img::attr(data-original)').extract_first(),
			'name': house.css('a.name::text').extract_first(),
			'address': house.css('div.resblock-location a::text').extract(),
			"tags":house.css('div.resblock-tag span::text').extract(),
			'unit_price': house.css('div.main-price span.number::text').extract_first(),
			'total_price':house.css('div.second::text').extract_first(),
			'jushi':house.css('a.resblock-room span::text').extract_first(),
			}

#		yield response.follow(next(a), callback=self.parse)

