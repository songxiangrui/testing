# -*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest
from random import randint
from time import sleep
import re
import string
# from shoppingTest import login
# from shoppingTest import get_element

class TestNihao(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["app"] = "/Users/sxr/Library/Developer/Xcode/DerivedData/BeingTime-dwtslihoezrwyjgssaxlsitpqzma/Build/Products/Debug-iphonesimulator/BeingTime.app"
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "iPhone 6s"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        el2 = self.driver.find_element_by_class_name("XCUIElementTypeTextField")
        el2.send_keys("songxiangrui")
        self.assertEqual(el2.get_attribute('value'),'songxiangrui')
        el3 = self.driver.find_element_by_class_name("XCUIElementTypeSecureTextField")
        el3.send_keys("123456")
        el4 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"登录\"]")
        el4.click()
        sleep(1)

    def get_element(self,element,is_id):
        count = 0
        while(True):
            try:
                if(is_id):
                    return self.driver.find_element_by_accessibility_id(element)
                else:
                    return self.driver.find_element_by_xpath(element)
            except:
                count += 1
                if count >= 15:
                    raise Exception("The element is not find: %s" % element)
                sleep(1)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)


    def test_set_name(self):
        btn_login = self.get_element("//XCUIElementTypeButton[@name=\"iconMeNor\"]",False)
        btn_login.click()
        self.login()
        btn_manage_account = self.get_element("//XCUIElementTypeStaticText[@name=\"账户管理\"]",False)
        self.assertEqual(btn_manage_account.get_attribute("name"),u'账户管理')
        btn_manage_account.click()
        txt_name = self.get_element("//XCUIElementTypeStaticText[@name=\"名字\"]",False)
        txt_name.click()
        btn_clear = self.get_element("//XCUIElementTypeButton[@name=\"清除文本\"]",False)
        btn_clear.click()
        txt_name_send = self.get_element("//XCUIElementTypeImage[@name=\"ic_search_bg\"]/XCUIElementTypeTextField",False)
        self.assertEqual(txt_name_send.get_attribute('value'),u"编辑名字")
        txt_name_send.send_keys("adk_177")
        sleep(2)
        btn_save = self.get_element("//XCUIElementTypeButton[@name=\"保存\"]",False)
        btn_save.click()

    def test_address(self):
        btn_login = self.get_element("//XCUIElementTypeButton[@name=\"iconMeNor\"]",False)
        btn_login.click()
        self.login()
        btn_manage_account = self.get_element("//XCUIElementTypeStaticText[@name=\"账户管理\"]",False)
        self.assertEqual(btn_manage_account.get_attribute("name"),u'账户管理')
        btn_manage_account.click()
        btn_address = self.get_element("//XCUIElementTypeStaticText[@name=\"收货地址\"]",False)
        btn_address.click()
        btn_new_address = self.get_element("//XCUIElementTypeButton[@name=\"新增收货地址\"]",False)
        btn_new_address.click()
        txt_name = self.get_element("//XCUIElementTypeStaticText[@name=\"请输入收货姓名\"]",False)
        txt_name.send_keys("kk_a_ss")
        txt_phone = self.get_element("//XCUIElementTypeStaticText[@name=\"请输入联系电话\"]",False)
        txt_phone.send_keys("123456789")
        txt_address = self.get_element("//XCUIElementTypeStaticText[@name=\"请输入收货地址\"]",False)
        txt_address.send_keys(u"北京市海淀区朱房北二街177号")
        btn_message_verify = self.get_element("//XCUIElementTypeButton[@name=\"确认信息\"]",False)
        btn_message_verify.click()
        sleep(1)
        btn_use = self.get_element("(//XCUIElementTypeButton[@name=\"常用收货地址\"])[2]",False)
        self.assertEqual(btn_use.get_attribute("name"),u"常用收货地址")
        btn_use.click()

    def test_group_buy(self):
        btn_interact = self.get_element("//XCUIElementTypeButton[@name=\"精彩互动\"]",False)
        btn_interact.click()
        btn_group_buy = self.get_element("//XCUIElementTypeButton[@name=\"拼单\"]",False)
        btn_group_buy.click()
        self.login()
        btn_doing = self.get_element("//XCUIElementTypeButton[@name=\"进行中\"]",False)
        btn_doing.click()
        sleep(1)
        btn_buy_now = self.get_element("//XCUIElementTypeButton[@name=\"立即加入\"]",False)
        btn_buy_now.click()
        btn_add_now = self.get_element("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]",False)
        btn_add_now.click()
        btn_verify_group = self.get_element("//XCUIElementTypeButton[@name=\"确认拼单\"]",False)
        self.assertEqual(btn_verify_group.get_attribute("name"),u"确认拼单")
        btn_verify_group.click()
        btn_succsee = self.get_element("//XCUIElementTypeButton[@name=\"完成\"]",False)

    def test_group_old_buy(self):
        btn_interact = self.get_element("//XCUIElementTypeButton[@name=\"精彩互动\"]",False)
        btn_interact.click()
        btn_group_buy = self.get_element("//XCUIElementTypeButton[@name=\"拼单\"]",False)
        btn_group_buy.click()
        self.login()
        btn_doing = self.get_element("//XCUIElementTypeButton[@name=\"往期\"]",False)
        btn_doing.click()
        sleep(1)
        # drop_el1 = self.get_element("(//XCUIElementTypeStaticText[@name=\"宋昕冉\"])[1]",False)
        # drop_el2 = self.get_element("(//XCUIElementTypeStaticText[@name=\"宋昕冉\"])[3]",False)
        # self.driver.scroll(drop_el1,drop_el2)
        self.driver.swipe(63,592,63,98,500)
        btn_see_order = self.get_element("(//XCUIElementTypeButton[@name=\"查看订单\"])[1]",False)
        btn_see_order.click()
        print("查看订单")
        btn_done = self.get_element("//XCUIElementTypeButton[@name=\"完成\"]",False)
        self.assertEqual(btn_done.get_attribute("name"),u"完成")
        btn_done.click()
        sleep(1)

    def test_homepage(self):
        btn_login = self.get_element("//XCUIElementTypeButton[@name=\"iconMeNor\"]",False)
        btn_login.click()
        self.login()
        btn_back = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"backNor\"]")
        btn_back.click()
        btn_interact = self.get_element("//XCUIElementTypeButton[@name=\"精彩互动\"]",False)
        btn_interact.click()
        btn_allow = self.get_element("//XCUIElementTypeButton[@name=\"允许\"]",False)
        btn_allow.click()
        sleep(1)
        btn_allow_allow = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Allow\"]")
        btn_allow_allow.click()
        # lenth = self.get_size()
        # print(lenth)
        # x1 = int(lenth[0]*0.75)
        # x2 = int(lenth[0]*0.25)
        # y1 = int(lenth[1]*0.25)
        # y2 = int(lenth[1]*0.75)
        # print(x1,x2,y1)
        count = 1
        while count < 10:
            self.driver.flick(300,150,100,150)
            count += 1
            print(count)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestNihao('test_set_name'))
    suite.addTest(TestNihao('test_address'))
    suite.addTest(TestNihao('test_group_buy'))
    suite.addTest(TestNihao('test_group_old_buy'))
    suite.addTest(TestNihao("test_homepage"))
    unittest.TextTestRunner().run(suite)
