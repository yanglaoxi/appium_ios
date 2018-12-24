import time

from Base.getIphoneConf import *
from Base.public import phoneLoad
from page.page_yike import page_yike
from page.page_mine import page_mine

subprocess.run(['ideviceinstaller', '-i', '/Users/yangshaopeng/PycharmProjects/lianxi/iOS/App/1837qa.ipa'])

phoneLoad.openApp(phoneLoad)
time.sleep(10)
phoneLoad.clickId(phoneLoad, page_yike.allow)
time.sleep(5)
phoneLoad.clickId(phoneLoad, page_yike.allow)
time.sleep(6)
phoneLoad.clickId(phoneLoad, page_yike.Photo_hands)
time.sleep(7)
phoneLoad.clickId(phoneLoad, page_yike.Photo_2_guide)
time.sleep(6)
print("=====")
time.sleep(1)



