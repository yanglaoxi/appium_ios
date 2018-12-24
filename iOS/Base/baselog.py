# -*- coding: UTF-8 -*-
import logging
import time
import os


def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    # 当前文件的绝对路径
    return path


def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 设置所有日志和错误日志的存放路径
    path = get_cwd()
    # 通过getcwd来拼接日志存放路径
    all_log_path = os.path.join(path, 'Logs/All_Logs/')
    # 设置日志文件名
    all_log_name = all_log_path + rq + '.logs'

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


log1 = get_log("appium")
