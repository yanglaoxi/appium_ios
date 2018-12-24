from ftplib import FTP
import sys
import subprocess
import re
import os

ftp = FTP()
timeout = 30
port = 21

# job_num = sys.argv[1]

g_job_num = input("please input your number:")


# def get_ftp(job_num):
# ftp.connect('ftp.afpai.com', port, timeout)     # 连接FTP服务器
# ftp.login('prod', 'Product')                    # 登录
# ftp.cwd("iOS_dev_zhibo/{}".format(job_num))     # 切换到目录
# ftp.retrlines('LIST')
# list1 = ftp.nlst()
# for file in list1:
#     if job_num in file:
#         fp = open('./{}'.format(file), 'wb')
#         ftp.retrbinary('RETR %s' % file, fp.write, 1024)
#         fp.close()

# get_ftp(job_num)

def get_from_ftp(g_job_num):
    port = 21
    timeout = 30
    ftp.connect('ftp.afpai.com', port, timeout)  # 连接FTP服务器
    ftp.login('prod', 'Product')  # 登录
    ftp.cwd("iOS_dev_zhibo/{}".format(g_job_num))  # 切换到目录
    ftp.retrlines('LIST')
    list1 = ftp.nlst()                              # 列举出远程FTP下所有文件的名字
    for file in list1:
        if g_job_num in file:
            # print(file)                               # 调试打印出对应文件的名字？
            fp = open('../App/{}'.format(file), 'wb')
            ftp.retrbinary('RETR %s' % file, fp.write, 1024)
            fp.close()


get_from_ftp(g_job_num)
#
# file_dir = './App/'
#
#
# def file_name(file_dir):                      # 安装下载的iPa 到连接的手机
#     L = []
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if g_job_num in file:
#                 L.append(os.path.join(root, file))
#     return L


