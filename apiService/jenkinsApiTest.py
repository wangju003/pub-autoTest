#导入依赖
import jenkins
from threading import Timer
import time



# 定义远程的jenkins master server 的url,以及port
jenkins_server_url = 'http://10.2.1.92:8080/jenkins/'  #测试服务器

# 定义用户的Userid 和 api token
user_id = 'admin'
api_token = '11d8c79994b1e6d554c857b1d96fcf4dfe' #测试服务器

# 实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

#实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)

# 构建job名为testJob的job
server.build_job('pubTest1')
# server.build_job('pubTest2')


while True:
    time.sleep(2)
    lastbuildNumber = server.get_job_info('pubTest1')['lastBuild']['number']
    print('最后1次构建版本号：', lastbuildNumber)

    # #判断testJob是否还在构建中,构建中返回false,构建结束返回true
    status = server.get_build_info('pubTest1', lastbuildNumber)['building']
    print(status)

    if status:
        print('报告地址html')
        break





