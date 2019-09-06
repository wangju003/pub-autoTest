#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置连接数据库的URL
# 不同的数据库采用不同的引擎连接语句：
# MySQL： mysql://username:password@hostname/database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin123456@10.1.71.32:3306/test'

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
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name


if __name__ == '__main__':
    # 打印一下db,确认数据库已经连接成功
    # print(db)

    # db.drop_all()
    # 创建Role 和　User表
    # db.create_all()

    # 在role表中插入2条测试数据

    ro1 = Role(name='Lisa')
    # ro2 = Role(name='user')
    db.session.add_all([ro1])
    db.session.commit()

    # 过滤查询
    # ro1=Role.query.filter_by(name='admin').first()
    # ro2=Role.query.filter_by(name='user').first()

    # 在user表中插入2条测试数据
    # us1 = User(name='zhangsan', email='zhangsan@qq.com',pswd='12345a',role_id=ro1.id)
    # us2 = User(name='lisi', email='lisi@qq.com', pswd='12345a', role_id=ro2.id)
    # db.session.add_all([us1, us2])
    # db.session.commit()

    # caseManage.run(debug=True)