from lxml import html
import requests
import json
app_id = 'a133f816'
api_key='1fecb12997d299d43e32bd9453513305'
search_recipe = requests.get('http://api.yummly.com/v1/api/recipes?_app_id='+app_id+'&_app_key='+api_key+'&allowedIngredient[]=chicken&allowedIngredient[]=chilli')
parsed = json.loads(search_recipe.text)
recipe_id = parsed['matches'][2]['id']
temp = 'http://api.yummly.com/v1/api/recipe/'+recipe_id+'?_app_id='+app_id+'&_app_key='+api_key
get_recipe = requests.get(temp)
#tree = html.fromstring(search_recipe.text)
parsed1 = json.loads(get_recipe.text)
output = json.dumps(parsed,indent = 2)
print temp
#print output