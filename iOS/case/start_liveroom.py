# coding=utf-8
import time
import unittest
from Base.public import phoneLoad
from page.page_yike import page_yike
from page.page_player import player_Page


class room(phoneLoad):
    @classmethod
    def setUpClass(self):
        print('run')
        # self.openApp("12.0","iphone 8","e988584a93da7df8794b7537fbef332cab5f1325")
        # self.openApp("11.4.1", "iPhone -M2224", "409ea1da1401667d5712dc8928594325d422a231")
        self.openApp()

    def test_inAndOutRoom(self):  # 进出教室case
        self.driver.implicitly_wait(20)
        self.clickId(page_yike.yike)
        self.tanchuang()
        self.clickId(page_yike.take_lesson)
        self.enterClassRoom()

        time.sleep(10)
        self.quitClassRoom()

    def test_fullScreen(self):  # 全屏切换case
        self.driver.implicitly_wait(20)
        self.clickId(page_yike.yike)
        if self.findId(page_yike.Close_Windows):
            self.tanchuang()
        else:
            self.clickId(page_yike.take_lesson)
        self.enterClassRoom()

        self.clickId(player_Page.full_screen)  # 全屏操作
        time.sleep(3)
        self.clickId(player_Page.full_screen)  # 切换至三分屏
        time.sleep(3)
        self.quitClassRoom()

    @classmethod
    def tearDownCLass(self):
        print("closed")
        self.closeDriver()


if __name__ == '__main__':
    unittest.main()

'''
    suite = unittest.TestSuite()
    suite.addTest(room("test_inAndOutRoom"))
    
    # 执行测试
    # verbosity 参数可以控制输出的错误报告的详细程度，
    # 默认是 1；如果设为 0，则不输出每一用例的执行结果；如果设为 2，则输出详细的执行结果
    
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)
'''

