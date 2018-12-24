import unittest
from Base.public import phoneLoad
import time
from page.page_mine import page_mine
from page.page_yike import page_yike


class openAp(phoneLoad):
    def setUp(self):
        self.openApp()
        print("首次安装")

    def tearDown(self):
        self.closeDriver()

    def test_A_oPen(self):  # 首次启动app 获取推送权限并处理引导弹窗
        # self.clickId(page_yike.allow)
        # time.sleep(3)
        # self.clickId(page_yike.allow)
        # time.sleep(2)
        # self.clickId(page_yike.Photo_hands)
        # time.sleep(2)
        # self.clickId(page_yike.Photo_2_guide)
        # time.sleep(2)
        # self.clickId(page_yike.Photo_3_guide)

        while self.findId(page_yike.allow):
            try:
                self.clickId(page_yike.allow)
                time.sleep(2)
                print("点击允许，获取相应权限")
            except Exception as err:
                print(err, "获取权限失败")
        if self.findId(page_yike.Photo_hands):
            try:
                self.clickId(page_yike.Photo_hands)
                print("点击第一个引导")
            except Exception as err:
                print(err, "处理第一个引导失败")
        if self.findId(page_yike.Photo_2_guide):
            try:
                self.clickId(page_yike.Photo_2_guide)
                print("处理第二个引导--百宝箱")
            except Exception as err:
                print(err, "百宝箱引导处理失败")
        if self.findId(page_yike.Photo_3_guide):
            try:
                self.clickId(page_yike.Photo_3_guide)
                print("第三个引导，下来刷新")
            except Exception as err:
                print(err, "下拉刷新引导处理失败")

    def test_B_open(self):                      # 首次启动app弹出登录
        if self.findId(page_yike.Welcome_to_homework):
            try:
                self.inputUser("17190000171")
                time.sleep(2)
                self.clickId(page_mine.next_step)
                time.sleep(2)
                self.inputPassword("123456")
                self.clickId(page_mine.Login)
            except Exception as err:
                print(err, "输入账号失败")

    def test_a_oPen(self):
        time.sleep(5)
        if self.findId(page_mine.Welcome_to_homework):  # 欢迎来到作业帮就登录171 账号
            try:
                self.inputPhone("17190000171", "123456")
            except Exception as e:
                print(e, "登录账号失败")
        elif self.findId(page_mine.Logout_notice):  # 发现登出通知，重新登录
            try:
                self.clickId(page_mine.Logout_notice_close)
            except Exception as e:
                print(e, "关闭登出通知失败，重新登录原来账号")
                self.clickId(page_mine.reLogin)

        else:
            print("暂未发现是存在否登录账号,try.....")
            try:
                self.findId(page_yike.my)
                print("已登录，查看当前登录账号。。")  # case有待完善
            except Exception as e:
                print(e, "未登录,尝试登录账号170")
                self.clickId(page_yike.my_unLogin)
                self.clickId(page_mine.Login)
                self.clearPhone()
                self.inputPhone("17190000170", "123456")


if __name__ == '__main__':
    unittest.main()
