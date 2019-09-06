from caseManage import app
from caseManage.common.CURD import insert,select,update
# from flask import render_template

from flask import Flask,jsonify,request,abort

@app.route('/casemanage/api/insert/', methods=['POST'])
def insertCase():

    data = request.get_json()

    insert(**data)
    return jsonify({'code':200,'msg':'录入成功'})

@app.route('/casemanage/api/update/', methods=['POST'])
def updateCase():

    data = request.get_json()
    update('TestCase',**data)
    return jsonify({'code':200,'msg':'修改成功'})

@app.route('/casemanage/api/select/', methods=['GET','POST'])
def selectCase():

    data = request.get_json()
    records = select("TestCase", **data)
    response = {}
    for record in records:
        case = {}
        case['id'] = record.id
        case['api_purpose'] = record.api_purpose
        case['request_url'] = record.request_url
        case['request_method'] = record.request_method
        case['request_data_type'] = record.request_data_type
        case['request_data'] = record.request_data
        case['assert_method'] = record.assert_method
        case['check_point'] = record.check_point
        case['correlation'] = record.correlation
        case['active'] = record.active
        case['creater'] = record.creater
        case['project'] = record.project

        response[case['id']] = case
    return jsonify(response)


if __name__ =='__main__':
    app.run(debug=True)