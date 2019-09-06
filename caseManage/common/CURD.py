from caseManage import model
from caseManage.model import TestCase
from caseManage.common.getdb import db


#获取model名
def getModel(classname):
    return getattr(model,classname)

def select(classname,**kwargs):
    '''
    数据库查询操作
    :param classname: dbModel名称
    :param kwargs: 查询条件  condition
    :return: 查询结果
    '''
    dbModel = getModel(classname)
    obj = dbModel.query.filter_by(**kwargs).all()
    return obj

def insert(**kwargs):

    print('after',type(kwargs),kwargs)
    api_purpose = kwargs['api_purpose']
    request_url = kwargs['request_url']
    request_method = kwargs['request_method']
    request_data_type = kwargs['request_data_type']
    request_data = kwargs['request_data']
    assert_method = kwargs['assert_method']
    check_point = kwargs['check_point']
    correlation = kwargs['correlation']
    active = kwargs['active']
    creater = kwargs['creater']
    project = kwargs['project']

    case = TestCase(api_purpose=api_purpose, request_url=request_url, request_method=request_method,
                    request_data_type=request_data_type, request_data=request_data,
                    assert_method=assert_method, check_point=check_point,
                    correlation=correlation, active=active,
                    creater=creater, project=project)

    db.session.add(case)
    db.session.commit()

#数据库更新操作
def update(classname,**kwargs):

    '''
    更新数据
    :param classname: dbModel名称
    :param kwargs: 查询条件 更新的字段和值 condition,field 字段,value 字段值
    :return: True or False
    '''
    dbModel=getModel(classname)
    obj = dbModel.query.filter_by(**kwargs['condition']).first()

    #根据循环修改
    for field,value in kwargs['updatedate'].items():

        try:
            #exec函数将字符串转为变量名
            str = 'obj.{field}="{value}"'.format(field=field,value=value)
            exec(str)
        except AttributeError:
            print('未查询到匹配的记录')
            #一旦查条件不成立,则停止赋值操作
            break

    db.session.commit()

def delete():
    pass

if __name__ == '__main__':
    filters={'api_purpose':'中文名'}
    records=select("TestCase",**filters)
    response={}
    for record in records:
        case={}
        case['id']=record.id
        case['api_purpose']=record.api_purpose
        case['request_url']=record.request_url
        case['request_method']=record.request_method
        case['request_data_type']=record.request_data_type
        case['request_data']=record.request_data
        case['assert_method']=record.assert_method
        case['check_point']=record.check_point
        case['correlation']=record.correlation
        case['active']=record.active
        case['creater']=record.creater
        case['project'] = record.project

        response[case['id']]=case
    print(response)



