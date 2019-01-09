
import scrapy


class BrickSetSpider(scrapy.Spider):

	# name - of the spider
	name = "brickSet_spider"

	# start_urls - list of URLs start to crawl from
	start_urls = ['http://brickset.com/sets/year-2016']


	# looking at the web page, we can see that each set of LEGO is specified with the class
	# set in HTML tag, thus we will use .set for CSS selector: <article class='set'>
	
	# the name of each set stored within an a tag inside an h1 tag:
	# <h1><a href='/sets/10251-1/Brick-Bank'>Brick Bank</a></h1>
	
	# the image of the set in the src attribute of an img tag inside an a tag at the start of set
	# <img src="http://images.brickset.com/sets/small/10251-1.jpg?201510121127" title="10251-1: Brick Bank"></a>

	# # of pieces: dt tag that contains the text Pieces, and then a dd tag that follows it which contains the actual number of pieces
	# <dl><dt>Pieces</dt>
    #    <dd><a class="plain" href="/inventories/10251-1">2380</a></dd></dl>

    # # of minifigs: similar to getting the number of pieces
    # <dt>Minifigs</dt>
    #   <dd><a class="plain" href="/minifigs/inset-10251-1">5</a></dd>

	# pass the selector into the response object
	def parse(self, response):

		SET_SELECTOR = '.set'

		# grab all the sets on the page and loops over them to extract the data
		for brickset in response.css(SET_SELECTOR):
			
			# ::text is a CSS pseudo-selector that fetches the text inside of the a tag 
			# rather than the tag itself
			NAME_SELECTOR = 'h1 ::text'
			PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
			MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
			IMAGE_SELECTOR = 'img ::attr(src)'

			yield {
				# call extract() on the object returned by brickset.css(NAME_SELECTOR)
				# return a list, but we only want the name string: {'name': ' Horses'}
				'name': brickset.css(NAME_SELECTOR).extract_first(),
				'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
				'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
				'image': brickset.css(IMAGE_SELECTOR).extract_first(),
			}

			# define a selector for the "next page" link
			NEXT_PAGE_SELECTOR = '.next a ::attr(href)'

			# extract the first match
			next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

			# recursively looking for next page, until we can't find a new link to next
			# check if it exists
			if next_page:
				# scrap the webpage if exists
				yield scrapy.Request(
					response.urljoin(next_page),
					# once got the html from this page, pass it back so we can parse it, 
					# extract the data and then find the next page
					callback=self.parse
					)



















