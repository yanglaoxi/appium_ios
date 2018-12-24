# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "ios"
caps["platformVersion"] = "12.0"
caps["deviceName"] = "iphone 8"
caps["udid"] = "e988584a93da7df8794b7537fbef332cab5f1325"
caps["bundleId"] = "com.baidu.homework"
caps["xcodeOrgId"] = "H8HNFLJVBJ"
caps["xcodeSigningId"] = "iPhone Developer"
caps["automationName"] = "XCUITest"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_accessibility_id("一课")
el1.click()
el2 = driver.find_element_by_accessibility_id("上课")
el2.click()
el3 = driver.find_element_by_accessibility_id("进入教室")
el3.click()
time.sleep(10)

TouchAction(driver).tap(x=169, y=86).perform()
el4 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"live zhibo back icon\"]")
el4.click()
el5 = driver.find_element_by_accessibility_id("退出")
el5.click()

time.sleep(10)

driver.quit()