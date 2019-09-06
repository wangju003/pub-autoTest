#导入依赖
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
#创建一个服务
app = Flask(__name__)

#配置app属性
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:admin123456@10.1.71.32:3306/test'

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False

#response显示中文json,
app.config['JSON_AS_ASCII']=False

#生成一个sqlalchemy对象
db = SQLAlchemy(app)

#创建模型，在python中通过Role类映身roles表
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email=db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name
#获取model名
def getModel(name):
    return globals()[name]


def update(dbModel,**kwargs):
    dbModel=getModel(dbModel)
    obj = dbModel.query.filter_by(**kwargs).first()
    print(obj)
    obj.name="lily"
    print(obj.name)
    print("True")


#     obj=Role.query.filter_by()
    # obj.factor_up=factor_back
    # print(obj.field)


filters={'name':'lisa'}
update("Role",**filters)




#通过用户名查询用户
# obj= Role.query.filter_by(name='lisa').first()
# obj.name='吕洞宾'



