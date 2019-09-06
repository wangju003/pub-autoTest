#导入依赖
import jenkins

# 定义远程的jenkins master server 的url,以及port
jenkins_server_url = 'http://10.2.1.92:8080/jenkins/'  #测试服务器

# 定义用户的Userid 和 api token
user_id = 'admin'
api_token = '11d8c79994b1e6d554c857b1d96fcf4dfe' #测试服务器

# 实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

def testDemo():
    #定义远程的jenkins master server 的url,以及port
    jenkins_server_url = 'http://10.1.71.51:8080/jenkins'  #IOS机器地址

    #定义用户的Userid 和 api token
    user_id = 'admin'
    api_token = '11a7a8151dbde5173fa19b346ad46b5efe'  #IOS机器地址

    #实例化jenkins对象，连接远程的jenkins master server
    server = jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)
    #打印一下server查是否连接成功
    # print(server) #返回一个jenkins对象<jenkins.Jenkins object at 0x10807d190>

    # 构建job名为testJob的job（不带构建参数）
    # server.build_job('testJob')

    #查看某个job的构建信息
    job_info=server.get_job_info('testJob')
    # print(job_info)

    #获取job名为testJob的job的最后次构建号
    lastbuildNumber=server.get_job_info('testJob')['lastBuild']['number']

    #获取job名为testJob的job的最后1次构建的执行结果状态
    result =server.get_build_info('testJob',lastbuildNumber)['result']

    #判断testJob是否还在构建中
    status = server.get_build_info('testJob',lastbuildNumber)['building']
    print(status)

def buildJob(jobName):
    # 构建job名为testJob的job（不带构建参数）
    server.build_job(jobName)




if __name__ == '__main__':
    buildJob('testJob')
    # 获取job名为testJob的job的最后次构建号
    lastbuildNumber = server.get_job_info('testJob')['lastBuild']['number']
    status = server.get_build_info('testJob', lastbuildNumber)['building']
    print(status)