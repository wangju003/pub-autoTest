from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] #指定json编码格式 如果为False 就不使用ascii编码
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"#指定浏览器渲染的文件类型，和解码格式；
# from caseManage import views= False
