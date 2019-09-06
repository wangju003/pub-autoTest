#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request,abort
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

# 设置连接数据库的URL
# 不同的数据库采用不同的引擎连接语句：
# MySQL： mysql://username:password@hostname/database

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:admin123456@10.1.71.32:3306/test'

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#response显示中文json,
app.config['JSON_AS_ASCII']=False

# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)


# 测试用例表
class TestCase(db.Model):
    __tablename__ = "testcase"
    id = db.Column(db.Integer, primary_key=True)
    api_purpose = db.Column(db.String(50))
    request_url = db.Column(db.String(100))
    request_method = db.Column(db.Enum("POST", "GET"))
    request_data_type = db.Column(db.Enum("Data", "Form", "File"))
    request_data = db.Column(db.Text, nullable=False)
    assert_method = db.Column(db.Enum("assertIn", "assertNotIn In"), default="assertIn")
    check_point = db.Column(db.String(255))
    correlation = db.Column(db.String(100))
    active = db.Column(db.Enum("Yes", "No"))
    creater = db.Column(db.String(50))
    project = db.Column(db.Enum("gw", "hw", "gw_lt"), default="gw")

    def __repr__(self):
        return "<TestCase.%s>" % self.api_purpose

#批量插入case
def insert(*args,**kwargs):
    '''1.args数据格式{}
    2.向testcase批量插入case'''

    for i in args:
        api_purpose=i['api_purpose']
        request_url=i['request_url']
        request_method=i['request_method']
        request_data_type = i['request_data_type']
        request_data = i['request_data']
        assert_method = i['assert_method']
        check_point = i['check_point']
        correlation = i['correlation']
        active = i['active']
        creater = i['creater']
        project = i['project']

        case=TestCase(api_purpose=api_purpose,request_url=request_url,request_method=request_method,
                       request_data_type=request_data_type,request_data=request_data,
                       assert_method=assert_method,check_point=check_point,
                       correlation=correlation,active=active,
                       creater=creater,project=project)

        # caseList.append(case)
    db.session.add(case)
    db.session.commit()
    print("INSERT SUCCESS!")

def select(*args,**kwargs):
    id = kwargs['id']


    obj = TestCase.query.get(id)
    # obj = TestCase.query.filter_by(request_url=request_url).first()
    # print(obj)
    result={}
    result['id']=obj.id
    result['api_purpose']=obj.api_purpose
    result['request_url']=obj.request_url
    result['request_method']=obj.request_method
    result['request_data_type']=obj.request_data_type
    result['request_data'] =obj.request_data
    result['assert_method'] =obj.assert_method
    result['check_point'] =obj.check_point
    result['correlation'] =obj.correlation
    result['active'] =obj.active
    result['creater'] =obj.creater
    result['project'] = obj.project

    return result

def update(*args,**kwargs):
    pass



@app.route('/insert', methods=['POST'])
def insertCase():

    j_data = request.get_json()
    # print(type(j_data),j_data)
    insertData = [j_data]
    # print(insertData)


    insert(*insertData)
    # return jsonify(request.json), 201  #并且返回这个添加的task内容和状态码
    return jsonify({'code':200,'msg':'录入成功'})

@app.route('/select/<int:case_id>')
def selectCase(case_id):

    return jsonify(select(id=case_id))

if __name__ == '__main__':

    app.run(debug=True)



