import unittest
import time
import random
from Base.public import phoneLoad
from page.page_player import player_Page
from page.page_yike import page_yike

'''
    课中连麦3
    选项卡2
    是否卡1
'''


class lessonInteraction(phoneLoad):     # 测试装饰器是否生效
    @classmethod
    def setUpClass(cls):
        cls.openApp(cls)

    @classmethod
    def tearDownClass(cls):
        cls.closeDriver(cls)

    def setUp(self):
        self.clickId(page_yike.yike)
        while self.findId(page_yike.Close_Windows):
            self.clickId(page_yike.Close_Windows)
        self.clickId(page_yike.take_lesson)
        self.clickId(page_yike.enter_classroom)

    def tearDown(self):
        self.quitClassRoom()

    def test_interaction1(self):  # 随机选择是都卡选项
        self.driver.implicitly_wait(20)
        try:
            self.findPath(player_Page.isShiFou)
            shi = self.clickPath(player_Page.isShiFou_yes)
            fou = self.clickPath(player_Page.isShiFou_no)
            listshifou = [shi, fou]
            random.choice(listshifou)
            print("随机选择是或否")  # 待完善截图
        except Exception as e:
            print(e, "未发现是否卡")

    def test_interaction2(self):  # 随机选择选项卡选项
        self.driver.implicitly_wait(20)
        if self.findId(player_Page.isTabShow):
            listXuan = self.findId(player_Page.Choose_card)
            random.choice(listXuan)  # 选择一个
            # random.sample("listXuan",2)                # 选择2个
            self.clickId(player_Page.commit)
            print("随机选择选项")

        else:
            print("未发现选项卡弹窗")

    def test_interaction3(self):
        self.driver.implicitly_wait(20)
        if self.findId(player_Page.isMic) and self.findId(player_Page.jushou1):
            try:
                self.clickPath(player_Page.Raise_hand_p)
                print("尝试举手中。。。。")
                time.sleep(3)
                while self.findId(player_Page.yijushou1):
                    print("举手成功，等待上麦")
                else:
                    print("举手失败，再次尝试")
                    self.clickPath(player_Page.Raise_hand_p)
            except Exception as e:
                print(e, "举手失败,再次尝试")
                self.clickPath(player_Page.Raise_hand_p)
        elif self.findId(player_Page.isMic) and self.findId(player_Page.yijushou1):
            try:
                self.clickPath(player_Page.Raise_hand_p)
                self.clickId(player_Page.think_again)  # 不取消举手
                time.sleep(3)
                self.clickId(player_Page.Cancel_hands)  # 取消举手
            except Exception as e:
                if self.findId(player_Page.isMic) and self.findId(player_Page.yijushou1):
                    print(e, "取消举手失败")
        elif self.findId(player_Page.isMic) and self.findId(player_Page.shangmai1):
            print("当前已上麦，开始连麦吧。。")
        else:
            print("当前不在连麦状态")


if __name__ == "__main__":
    unittest.main()
