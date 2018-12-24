import subprocess
import time
import re
from Base.public import phoneLoad
'''
def aa():
    subprocess.run(["cd", "/Users/yangshaopeng/Downloads"])
    dir = subprocess.getoutput('pwd')
    print(dir)

    # 使用libmobileevice库
    # 获取设备信息uid, name version  同时能够获取到同一WI-FI下的设备信息
    udid = subprocess.getoutput("idevice_id -l")
    print(udid)
    name = subprocess.getoutput("idevicename")
    print(name)
    version = subprocess.getoutput("ideviceinfo -k ProductVersion")
    print(version)
'''


# 全部信息  包括
def getIosInfo():
    all_info = subprocess.getoutput("Instruments -s devices")
    lines = all_info.splitlines()
    devices = {}

    pat = re.compile("(.*?) \[(.*)\]")
    for line in lines[2:]:
        if line.find("(Simulator)") == -1:
            groups = pat.findall(line)
            devices[groups[0]] = groups[0]

    for k, v in devices:
        # print(k, '==>', v)
        info_all = k.split()
        n = info_all[0]
        ver = info_all[1]
        # print(Name, Version)

        return n, ver, v
        print(n, ver, v)

info = getIosInfo()
g_Name = info[0]
g_Version = info[1]
g_Udid = info[2]
#print(Name, Version, Udid)



'''
# 测试12306 安装卸载
# 安装app,
subprocess.run(['ideviceinstaller', '-i', '/Users/yangshaopeng/PycharmProjects/lianxi/iOS/App/12306_v4.0.2.ipa'])

time.sleep(10)
# 卸载app
subprocess.run(['ideviceinstaller', '-U', 'cn.12306.rails12306'])

# 作业帮覆盖安装1825 使用的qa证书
subprocess.run(['ideviceinstaller', '-i', '/Users/yangshaopeng/PycharmProjects/lianxi/iOS/App/1825qa.ipa'])
time.sleep(10)
subprocess.run(['ideviceinstaller', '-i', '/Users/yangshaopeng/PycharmProjects/lianxi/iOS/App/1828-qa.ipa'])



# 安装卸载app的方法
class app(object):
    def installApp(self):
        self.subprocess.run(['ideviceinstaller', '-i', '/Users/yangshaopeng/PycharmProjects/lianxi/iOS/App/1825qa.ipa'])

    def uninstallApp(self):
        self.subprocess.run(['ideviceinstaller', '-U', 'com.baidu.qa.homework'])
'''
