from lxml import html
import requests
import json



api_key='a7117cb7dc7f8b768ec323b949e752dd'
page = requests.get('http://food2fork.com/api/search?key='+api_key+'&q=milk,cashew')
parsed = json.loads(page.text)

# url = parsed['recipes'][1]['f2f_url']
# url = 'http://food2fork.com/view/Roast_Sticky_Chicken_Rotisserie_Style/26851'
# page1 = requests.get(url)
# tree = html.fromstring(page1.content)
# ingredients = tree.xpath('//li[@itemprop="ingredients"]/text()')
#print ingredients

count = parsed['count']

for i in range (0,count):
	print parsed['recipes'][i]['publisher']
	

print json.dumps(parsed,indent = 2)







#print output
#recipe_list = parsed['recipes']
# output = json.dumps(parsed,indent=2)
# print output
#f2f_url = parsed['recipes'][0]['f2f_url']
#source_url = parsed['recipes'][0]['source_url']
#page1 = requests.get(f2f_url)
#page2 = requests.get(source_url)
#print page1.content
#print '****************************************************************************************************************************************************************************************'
#print page2.content

#print source
# print parsed['recipes'][i]['title']
# print parsed['recipes'][i]['source_url']
# print parsed['recipes'][i]['f2f_url']
# print 
#re=requests.get('http://tastykitchen.com/recipes/desserts/chocolate-covered-cashew-filled-caramels')