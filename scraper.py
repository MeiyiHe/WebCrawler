
import scrapy


class BrickSetSpider(scrapy.Spider):

	# name - of the spider
	name = "brickSet_spider"

	# start_urls - list of URLs start to crawl from
	start_urls = ['http://brickset.com/sets/year-2016']

	


