#导入依赖
import jenkins
import time,random
# 定义远程的jenkins master server 的url,以及port
jenkins_server_url = 'http://10.2.1.92:8080/jenkins/'  #测试服务器

# 定义用户的Userid 和 api token
user_id = 'admin'
api_token = '11d8c79994b1e6d554c857b1d96fcf4dfe' #测试服务器

# 实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
jobName1='pubTest1'
jobName2='pubTest2'
# 获取job名为testJob的job的最后次构建号
autoLBN = server.get_job_info(jobName1)['lastBuild']['number']
scriptLBN= server.get_job_info(jobName2)['lastBuild']['number']

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

def buildJob():
    '''
    构建automation,ScriptTest
    :return:
    '''
    buildResult={}
    if server.build_job(jobName1):
        buildResult[jobName1]='Start'

    if server.build_job(jobName2):
        buildResult[jobName2]='Start'
    return buildResult

    try:
        next_bn = server.get_job_info(jobName2)['nextBuildNumber']
    except:
        buildResult['msg']='next_bn获取异常，重试'
        print('next_bn获取异常，重试')
        time.sleep(5)
        next_bn = server.get_job_info(jobName2)['nextBuildNumber']
    else:
        buildResult['next_bn':next_bn]
        print('本次执行的jenkins job编号为：', next_bn)
    try:
        server.build_job(jobName2)
    except:
        buildResult['msg'] = '启动jenkinsjob异常，重试'
        print("启动jenkinsjob异常，重试")
        time.sleep(5)
        server.build_job(jobName2)
    else:
        buildResult['msg'] = 'jenkins job启动成功'
        print('jenkins job启动成功')

    # 启动一个job的时候经常会有延迟的，这是个经验值，暂定10秒，可根据实际情况进行更改。
    time.sleep(10)
    sleeptime = 0
    while sleeptime < 50:
        # print "sleep 循环中"
        try:
            server.get_build_info(jobName2, next_bn)['building']
        except:
            time.sleep(5)
            buildResult['msg'] = 'jenkins job还没有启动起来，继续等待5秒...'
            print("jenkins job还没有启动起来，继续等待5秒...")
            sleeptime = sleeptime + 5
        else:
            buildResult['msg'] = 'jenkins job启动成功'
            print("jenkins job启动成功")
            sleeptime = 50
    print("sleeptime", sleeptime)
    print("退出sleep循环")


def getBuildState():
    '''
    获取jenkins构建结果
    :return: True 构建中 False 构建结束
    '''

    # 判断job是否还在构建中,False表示构建结束，True表示构建中

    autoStatus = server.get_build_info(jobName1, autoLBN)['building']
    scriptStatus=server.get_build_info(jobName2,scriptLBN)['building']

    if autoStatus or scriptStatus:
        return True
    else:
        return False


def getReport():
    '''
    构建完成，获取测试报告
    :return: result 构建结束返回测试报告地址；构建中 返回{}
    '''
    buildState = getBuildState() #False表示构建结束，True表示构建中
    print('11111',buildState)
    result = {}
    if not buildState:
        result['automationTest'] = 'http://1.1.1.1/report.html'
        result['ScriptTest'] = 'http://2.2.2.2/report.html'
        return result
    else:
        return False
if __name__ == '__main__':
    b=getReport()
    print(b)