import time
import unittest
from Base.public import phoneLoad
from page.page_mine import page_mine


class login(phoneLoad):
    def setUp(self):
        self.openApp()

    def tearDown(self):
        self.closeDriver()

    def test_login(self):
        self.driver.implicitly_wait(10)
        if self.findId(page_mine.unLogin):
            try:
                self.clickId(page_mine.unLogin)
                self.clickId(page_mine.Login_register)
                self.inputPhone("18800181346", "123456")
            except:
                print("已登录状态")
        elif self.findId("我"):
            try:
                self.clickId("我")
                self.swipeUp(1000)
                time.sleep(5)
                self.clickPath(page_mine.set_p)  # 点击设置
                self.clickId(page_mine.Account_and_security)
                self.clickId(page_mine.Exit_the_account)
                self.clickId(page_mine.Exit_the_current_account)
                self.clickId(page_mine.set_page_login_account)
                self.inputPhone("17190000175", "123456")
            except:
                print("登录账户失败")

        elif self.findId(page_mine.Logout_notice):
            try:
                self.clickId(page_mine.Logout_notice_close)  # 无效
                print("尝试关闭失败")
            except Exception as e:
                self.clickId(page_mine.reLogin)
                print(e, "重新登录")
                self.clickId("我")
                self.swipeUp(1000)
                self.clickPath(page_mine.set_p)  # 点击设置
                self.clickId(page_mine.Account_and_security)
                self.clickId(page_mine.Exit_the_account)
                self.clickId(page_mine.Exit_the_current_account)
                self.clickId(page_mine.set_page_login_account)
                self.inputPhone("17190000175", "123456")

        elif self.findId(page_mine.Welcome_to_homework):
            self.inputPhone("17190000170", "123456")


if __name__ == '__main__':
    unittest.main()
    '''
    suit = unittest.TestSuite()
    suit.addTest(login('test_login'))
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suit)
    '''
