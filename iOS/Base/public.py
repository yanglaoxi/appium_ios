import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from page.page_player import player_Page
from page.page_yike import page_yike
from page.page_mine import page_mine
from Base.getIphoneConf import *


class phoneLoad(unittest.TestCase):
    # 启动app,传入手机参数
    def openApp(self):

        caps = {}
        caps["platformName"] = "ios"
        caps["platformVersion"] = g_Version
        caps["deviceName"] = g_Name
        caps["udid"] = g_Udid
        caps["bundleId"] = "com.baidu.qa.homework"
        caps["xcodeOrgId"] = "H8HNFLJVBJ"
        caps["xcodeSigningId"] = "iPhone Developer"
        caps["automationName"] = "XCUITest"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print("启动作业帮app")

        '''
        while self.driver.find_element_by_accessibility_id(page_yike.allow):  # 获取各种权限
            self.clickId(page_yike.allow)
            print("获取权限")
            time.sleep(5)
        '''

    # 关闭driver
    def closeDriver(self):
        try:
            self.driver.quit()
            print("close driver")
        except Exception as e:
            print(e, ":close driver failed")

    # 查找元素
    def findId(self, id):
        try:
            element = self.driver.find_element_by_accessibility_id(id)
            return element
        except Exception as e:
            print(e, "not find this id element:", id)

    def findPath(self, path):
        try:
            element = self.driver.find_element_by_xpath(path)
            return element
        except Exception as e:
            print(e, "not find this  xpath element:", path)

    # 点击事件
    def clickId(self, idele):
        try:
            self.driver.find_element_by_accessibility_id(idele).click()
            print("点击", idele)
            time.sleep(5)
        except Exception as e:
            print(e, "click id failed")

    def clickPath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            print("点击", xpath)
            time.sleep(5)
        except Exception as e:
            print(e, "click xpath failed")

    # 点击某一点
    def clickCoordinates(self, x, y):
        try:
            self.driver.tap([x, y])
        except Exception as e:
            print(e, "coordinates error")

    # 清理事件
    def clearId(self, id):
        try:
            self.driver.find_element_by_accessibility_id(id).clear()
        except Exception as e:
            print(e, "clear id failed")

    def clearPath(self, path):
        try:
            self.driver.find_element_by_xpath(path).clear()
        except Exception as e:
            print(e, "clear path failed")

    # 清空账号
    def clearPhone(self):
        try:
            self.clearPath(page_mine.Clear_phone_number_p)
            print("清空电话号码")
        except Exception as e:
            print(e, "clear phone number failed")

    # 输入事件
    def inputId(self, id, inputvalue):
        try:
            self.driver.find_element_by_accessibility_id(id).send_keys(inputvalue)
            print("id input。。。。", inputvalue)
        except Exception as e:
            print(e, "send_keys failed")

    def inputPath(self, path, inputvalue):
        try:
            self.driver.find_element_by_xpath(path).send_keys(inputvalue)
            print("path input...", inputvalue)
        except Exception as e:
            print(e, "path input failed")

    # 电话号码输入方法
    def inputUser(self, phone):
        try:
            self.clearPhone()
            self.findPath(page_mine.Phone_number_input_box_p).sendkeys(phone)
            time.sleep(1)
            self.clickId(page_mine.next_step)
        except Exception as e:
            print(e, "input number failed")

    # 密码输入方法
    def inputPassword(self, password):
        try:
            if self.findId("1"):
                self.findPath(page_mine.Password_entry_box_p).send_keys(password)
            else:
                self.clickPath("more")
                time.sleep(1)
                self.findPath(page_mine.Password_entry_box_p).send_keys(password)
            self.clickId(page_mine.Login)
        except Exception as e:
            print(e, "input password failed")

    # 一些账号登录后会选择身份

    def inputPhone(self, phone, password):
        self.driver.implicitly_wait(5)
        self.clearPhone()
        self.inputUser(phone)
        self.inputPassword(password)
        if self.findId("请选择你的身份"):
            self.clickId("学生")
            print("默认选择学生身份")
        else:
            print("------选择身份失败----")
        time.sleep(2)
        if self.findId("请选择你的年级"):
            self.clickId("一年级")
            print("默认选择一年级")
        else:
            print("-----选择年级失败----")
        time.sleep(2)
        self.clickId("完成，进入作业帮")

    # 进入教室

    def enterClassRoom(self):
        try:
            self.clickId(page_yike.enter_classroom)
            time.sleep(2)
            if self.findId(player_Page.Traffic_tips):
                print("使用流量播放")
                self.clickId(player_Page.Continue_play)
            time.sleep(2)
            if self.findId("好"):
                print("获取麦克风权限")
                self.clickId("好")
            print("进入教室")
        except Exception as e:
            print(e, "进入教室失败")

    # 调起上下导航条
    def clickBlank(self):
        try:
            TouchAction(self.driver).tap(x=169, y=86).perform()
            time.sleep(1)
        except Exception as e:
            print(e, "坐标错误")

    # 退出教室
    def quitClassRoom(self):
        try:
            self.clickBlank()
            self.clickId(player_Page.Leave_classroom)
            self.clickId(player_Page.exit)
            print("退出教室")

        except Exception as e:
            print(e, " 退出失败")

    # 弹窗处理
    def tanchuang(self):
        try:
            self.clickId(page_yike.Close_Windows)
            print("有弹窗fk关闭弹窗")
        except Exception as e:
            print(e, "无弹窗")

    # 获取设备窗口大小

    def swipeUp(self, t):
        time.sleep(8)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        ll = [x, y]
        x1 = int(ll[0] * 0.55)  # x坐标
        y1 = int(ll[1] * 0.75)  # 起始y坐标
        y2 = int(ll[1] * 0.25)  # 终点y坐标
        self.driver.swipe(1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        time.sleep(8)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        ll = [x, y]
        x1 = int(ll[0] * 0.5)  # x坐标
        y1 = int(ll[1] * 0.25)  # 起始y坐标
        y2 = int(ll[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipeLeft(self, t):
        time.sleep(8)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        ll = [x, y]
        x1 = int(ll[0] * 0.75)
        y1 = int(ll[1] * 0.5)
        x2 = int(ll[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipeRight(self, t):
        time.sleep(8)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        ll = [x, y]
        x1 = int(ll[0] * 0.05)
        y1 = int(ll[1] * 0.5)
        x2 = int(ll[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
