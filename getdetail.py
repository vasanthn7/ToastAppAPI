from lxml import html
import requests
import json
from tags import tags

class get_detail(object):
    def __init__(self,id):
        self.id = id
    def return_detail(self):
        api_key='a7117cb7dc7f8b768ec323b949e752dd'
        response = []
        print type(self.id)
        page = requests.get('http://food2fork.com/api/get?key='+api_key+'&rId='+str(self.id))
        parsed = json.loads(page.text)
        publisher = parsed['recipe']['publisher']
        print parsed['recipe']['publisher']
        if (publisher == "All Recipes"):
    		tag = '//span[@class="recipe-directions__list--item"]/text()'
    	elif (publisher == "Back to Her Roots"):
    		tag = '//li[@class="instruction"]/text()'
    	elif (publisher == "BBC Food"):
    		tag = '//p[@class="recipe-method__list-item-text"]/text()'
    	elif (publisher == "Bon Appetit"):
    		tag = '//div[@class="text" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Closet Cooking"):
    		tag = '//li[@itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Cookin Canuck"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Epicurious"):
    		tag = '//li[@class="preparation-step"]/text()'
    	elif (publisher == "Epicurious"):
    		tag = '//li[@class="preparation-step"]/text()'
    	elif (publisher == "Food Republic"):
    		tag = '//span[@itemprop="recipeInstructions"]/ol/li/text()'
    	elif (publisher == "Framed Cooks"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Healthy Delicious"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Jamie Oliver"):
    		tag = '//ol[@class="recipeSteps"]/li/text()'
    	elif (publisher == "Lisa's Kitchen"):
    		tag = '//li[@itemprop="recipeInstructions"]/p/text()'
    	else:
    		tag = 404

        if (tag == 404):
            response = json.dumps({'Status':0},sort_keys=False,separators=(',',':'))
            return str(response).replace("'",'')
        ingredients = parsed['recipe']['ingredients']
        # print ingredients
        url = parsed['recipe']['source_url']
        page1 = requests.get(url)
        #print page1.text
        tree = html.fromstring(page1.content)
        directions = tree.xpath(tag)
        response = json.dumps({'Status':1,'Ingredients':ingredients,'Direction':directions},sort_keys=False,separators=(',',':'))
        return str(response).replace("'",'')

if __name__ == '__main__':
    obj = get_detail("35437")
    obj.return_detail()
