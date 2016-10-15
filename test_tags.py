from lxml import html
import requests
import json

url = "http://whatsgabycooking.com/skinny-asparagus-and-gruyere-tart/"
page1 = requests.get(url)
#print page1.text
tree = html.fromstring(page1.content)
directions = tree.xpath('//li[@class="instruction" and @itemprop="recipeInstructions"]/text()')
for i in range(len(directions)):
	print directions[i]
print len(directions)
