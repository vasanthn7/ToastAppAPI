from lxml import html
import requests
import json

url = "http://foodandspice.blogspot.com/2013/01/pumpkin-gingerbread-waffles.html"
page1 = requests.get(url)
#print page1.text
tree = html.fromstring(page1.content)
directions = tree.xpath('//li[@itemprop="recipeInstructions"]/p/text()')
for i in range(len(directions)):
	print directions[i]
print len(directions)
#@id="mpprecipe-instruction-0" and 