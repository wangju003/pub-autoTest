
from caseManage.common.getdb import db

from flask import jsonify, request
from caseManage import app

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name

def printKwargs(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    # data={'name': '小李哥', 'email': 'land@163.com'}
    # print('before', type(data), data)
    # insert(**data)

    @app.route('/casemanage/api/insert/', methods=['POST'])
    def insert():
        data = request.get_json()

        print('before', type(data), data)
        printKwargs(**data)

        # return jsonify(request.json), 201  #并且返回这个添加的task内容和状态码
        return jsonify({'code': 200, 'msg': '录入成功'})

    app.run(debug=True)