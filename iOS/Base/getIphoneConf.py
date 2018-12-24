import subprocess
import re


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


info = getIosInfo()
print(info)
g_Name = info[0]
g_Version = info[1]
g_Udid = info[2]
