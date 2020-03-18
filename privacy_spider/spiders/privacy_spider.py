import scrapy
import re

filename = 'privacy_titles.html'
htmlstart = "<!doctype html>\n<html lang='en'>\n" + \
		"<head>\n\t<title>Privacy Articles</title>\n</head>\n<body>\n"
targetstr = '<h3 class="node__title node__title"><a href="'


class PrivacySpider(scrapy.Spider):
	""" scrape some article links and titles from privacy sites """
	name = "privacy_spider"
	allowed_domains = ['eff.org/deeplinks']
	start_urls = ['https://eff.org/deeplinks/']

	def parse(self, response):
		eff_links = response.css('h3.node__title').extract()

		with open(filename, 'w+') as f:
			f.write(htmlstart)
			f.write("<h1>eff.org/deeplinks</h1>\n<ul>\n")

			for eff_link in eff_links:
				temp_link = re.sub(targetstr, '<a href="https://eff.org', eff_link)
				good_link = re.sub('rel="bookmark"', 'target="_blank"', temp_link)
				f.write("\t<li>" + re.sub('</h3>', '', good_link) + "</li>\n")

			f.write("</ul>\n")
			f.write("</body>\n</html>\n")

