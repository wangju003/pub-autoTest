import configparser
import os


def getconnStr():
    '''
    获得连接数据库字符串
    :param db_path: 配置文件存储路径
    :return mysql连接字符串
    :confset  配置文件字典
    '''
    dirname, filename = os.path.split(os.path.abspath(__file__))
    db_path = os.path.join(dirname, "db.ini")


    #读取ini配置文件
    config=configparser.RawConfigParser()
    config.read(db_path)
    confset={}
    # env = "database" #正式库
    env = "databaseTest" #测试库
    confset["username"]= config.get(env,"username")
    confset["password"]= config.get(env,"password")
    confset["url"]= config.get(env,"url")
    confset["port"]=config.get(env,"port")
    confset["dbname"]= config.get(env,"dbname")
    confset["charset"]=config.get(env,"charset")
    'mysql+mysqlconnector://root:admin123456@10.1.71.32:3306/test'

    connStr = "mysql+mysqlconnector://{username}:{password}@{url}:{port}/{dbname}?charset={charset}".format(
        username=confset["username"],
        password=confset["password"],
        url=confset["url"],
        port=confset["port"],
        dbname=confset["dbname"],
        charset=confset["charset"]
    )
    return  connStr



if __name__ == '__main__':

    print(getconnStr())