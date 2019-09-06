
from flask_sqlalchemy import SQLAlchemy
from caseManage.common import config

connStr = config.getconnStr()


# app = Flask(__name__)
from caseManage import app

# 设置连接数据库的URI
app.config['SQLALCHEMY_DATABASE_URI'] = connStr

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#response显示中文json,
app.config['JSON_AS_ASCII']=False

# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)




