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
        tag = tags(parsed['recipe']['publisher'])
        print parsed['recipe']['publisher']
        if (tag == 404):
            return 404
            quit()
        ingredients = parsed['recipe']['ingredients']
        # print ingredients
        url = parsed['recipe']['source_url']
        page1 = requests.get(url)
        #print page1.text
        tree = html.fromstring(page1.content)
        directions = tree.xpath(tag)
        response = json.dumps({'Ingredients':ingredients,'Direction':directions},sort_keys=False,separators=(',',':'))
        return str(response).replace("'",'')

if __name__ == '__main__':
    obj = get_detail("35196")
    obj.return_detail()
