# coding:utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["app"] = "/Users/sxr/Library/Developer/Xcode/DerivedData/BeingTime-dwtslihoezrwyjgssaxlsitpqzma/Build/Products/Debug-iphonesimulator/BeingTime.app"
caps["platformName"] = "iOS"
caps["platformVersion"] = "10.3"
caps["deviceName"] = "iPhone 6s"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconMeNor\"]")
el1.click()
el2 = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\" 现在注册\"]")
el2.click()
el3 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTextField")
el3.send_keys("sxr11302")
el4 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeSecureTextField")
el4.send_keys("111111")
el5 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"登录\"]")
el5.click()
el6 = driver.swipe(100, 100, 100, 400)
el7 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"backNor\"]")
el7.click()
driver.quit()