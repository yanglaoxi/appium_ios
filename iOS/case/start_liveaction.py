# coding=utf-8
import time
import unittest
from Base.public import phoneLoad
from page.page_player import player_Page
from page.page_yike import page_yike


class roomAction(phoneLoad):

    def setUp(self):
        # self.openApp("12.0","iphone 8","e988584a93da7df8794b7537fbef332cab5f1325")
        self.openApp()
        print("running")

    def test_actionroom(self):
        self.driver.implicitly_wait(10)
        self.clickId("一课")
        self.tanchuang()
        self.clickId(page_yike.take_lesson)
        self.enterClassRoom()
        time.sleep(100)

        # 刷新
        self.clickBlank()
        self.clickId(player_Page.help)
        self.clickId(player_Page.refresh)
        print("刷新一下")

        # 重新收取
        time.sleep(3)
        self.clickBlank()
        self.clickId(player_Page.help)
        self.clickId(player_Page.recharge)
        print("重新收取")
        time.sleep(10)
        # 护眼模式
        self.clickBlank()
        self.clickId(player_Page.more)
        self.clickId(player_Page.Eye_protection_mode)
        print("护眼开启")
        time.sleep(20)

        self.quitClassRoom()

    def tearDown(self):
        self.closeDriver()


if __name__ == '__main__':
    unittest.main()
