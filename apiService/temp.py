'''
需求：
想把数据中的一条数据，转化为用使用字典存储－这样就可以让一个字段对应一个值，方便调用

数据库中的数据复制出来长这样：
'4089', '获取楼盘相关资讯', '/appapi/article/estate', 'POST', 'Data', '{\"estateID\":18703,\"propertyTypeID\":1,\"typeID\":1,\"page\":1,\"pageSize\":10}', 'assertIn', '\"status\":\"200\",\"msg\":\"成功\"', '', 'Yes', '温泉', 'gw'
我希望的格式是这样：
'api_purpose': '获取楼盘相关资讯'
即列名，和值一一对应

'''
#将数据源使用列表存储
a=[['获取楼盘相关资讯', '/appapi/article/estate', 'POST', 'Data', '{\"estateID\":18703,\"propertyTypeID\":1,\"typeID\":1,\"page\":1,\"pageSize\":10}', 'assertIn', '\"status\":\"200\",\"msg\":\"成功\"', '', 'Yes', '温泉', 'gw']]
# print(type(a))
#使用字典重新组装数据
d={}
#最终的结果是这[{对象},{}]
res=[]

l = len(a)
for i in a:
    d['api_purpose']=i[0]
    d['request_url']=i[1]
    d['request_method'] = i[2]
    d['request_data_type'] = i[3]
    d['request_data'] = i[4]
    d['assert_method'] = i[5]
    d['check_point'] = i[6]
    d['correlation'] = i[7]
    d['active']=i[8]
    d['creater'] = i[9]
    d['project'] = i[10]
    res.append(d)
print(res)
import json
print(json.dumps(res[0]))