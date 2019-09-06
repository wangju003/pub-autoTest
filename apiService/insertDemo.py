#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:admin123456@10.1.71.32:3306/test'

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name

def insert(*args,**kwargs):
    caseList=[]
    for i in args:
        print('i is',i)
        name=i['name']


    #     case=Role(name=name)
    #
    #     caseList.append(case)
    # db.session.add_all(caseList)
    # db.session.commit()
    print("INSERT SUCCESS!")

if __name__ == '__main__':
    #数据源-要批量添加的case数据 list套dict
    a=[{'name':'lisa'},{'name':'bob'}]
    insert(*a)





