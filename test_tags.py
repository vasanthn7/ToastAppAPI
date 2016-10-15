from lxml import html
import requests
import json

url = "http://www.realsimple.com/food-recipes/browse-all-recipes/zucchini-spice-bread"
page1 = requests.get(url)
#print page1.text
tree = html.fromstring(page1.content)
directions = tree.xpath('//section[@class="directions recipe-info-section" and @itemprop="recipeInstructions"]/div/ol/li/text()')
for i in range(len(directions)):
	print directions[i]
print len(directions)
