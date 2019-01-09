# WebCrawler
using Python and Scrapy

To run:
 $ scrapy runspider scraper.py

Step 1: creating a basic scrapper
	- systematically find and download web pages
	- take those web and extract info from them


Step 2: extracting data from a page
	- take http://brickset.com/sets/year-2016 as example
	- first grab each LEGO set by looking for the parts of the page that have the data we want
	- then, for each set, grab the data we want from it by pulling the data out of the HTML tags


Step 3: crawling multiple pages
	- notice that the top and bottom of each page has '>' that links to the next page of results,
	<li class="next">
    <a href="http://brickset.com/sets/year-2017/page-2">&#8250;</a>
  	</li>
  	li tag with the class of next, and an a tag inside with the link to the next page

