# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from page.page_yike import page_yike
from page.page_player import player_Page
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "ios"
caps["platformVersion"] = "11.4.1"
caps["deviceName"] = "iPhone -M2224"
caps["udid"] = "00a06c704fbaad7c85984cab8099a2befb959a59"
caps["bundleId"] = "com.baidu.homework"
caps["xcodeOrgId"] = "H8HNFLJVBJ"
caps["xcodeSigningId"] = "iPhone Developer"
caps["automationName"] = "XCUITest"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

#driver.get_screenshot_as_png("/Users/yangshaopeng/Downloads/")
driver.save_screenshot("./image/123.png")

time.sleep(10)


driver.get_screenshot_as_file("./image/")

time.sleep(10)















