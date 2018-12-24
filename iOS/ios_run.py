import time
import unittest
from Base import HTMLTestRunner
from Base.public import phonelanuch
from run import creatsuite

case_dir = './case/'


def creatsuite():
    testing = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='start_*.py')
    for test_suit in discover:
        for test_case in test_suit:
            testing.addTest(test_case)
        print(testing)
    return testing





if __name__ == '__main__':
    # 测试报告存放路径

    now = time.strftime("%Y-%m-%d_%H_%M_%S_", time.localtime())
    filename = './result/' + now + '_result.html'

    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'作业帮iOS功能测试报告',
        description=u'用例执行详情：'
    )

    runner.run(creatsuite())
    fp.close()
