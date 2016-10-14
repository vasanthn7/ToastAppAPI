#!bin/python
from flask import Flask, jsonify
from getrecipe import get_recipe

app = Flask(__name__)

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
l = [
    {'a':1, 'b':2},
    {'c':3, 'd':4}
]

@app.route('/api/recipe/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks':tasks})

@app.route('/api/recipe/tasks/<string:ing>', methods=['GET'])
def get_task(ing):
    # task = [task for task in tasks if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # ing = 'shredded chicken,'
    # get_r =
    return get_recipe(ing, 1)
    #print get_r.return_recipe.content
    # return jsonify(l)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
