#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t:t['id'] == task_id,tasks))
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
#如果请求里面没有json数据，或者json数据里面title的内容为空
    if not request.json or not 'title' in request.json:
        abort(400) #返回404错误
    task = {
        'id': tasks[-1]['id'] + 1, #取末尾tasks的id号+1
        'title': request.json['title'], #title必须设置，不能为空。
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task) #完了之后，添加这个task进tasks列表
    return jsonify({'task': task}), 201  #并且返回这个添加的task内容和状态码

if __name__ == '__main__':
    app.run(debug=True)