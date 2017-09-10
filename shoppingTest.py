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

def setUp():
    caps = {}
    caps["app"] = "/Users/sxr/Library/Developer/Xcode/DerivedData/BeingTime-dwtslihoezrwyjgssaxlsitpqzma/Build/Products/Debug-iphonesimulator/BeingTime.app"
    caps["platformName"] = "iOS"
    caps["platformVersion"] = "10.3"
    caps["deviceName"] = "iPhone 6s"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

def tearDown():
    driver.quit()

def login():
    el2 = driver.find_element_by_class_name("XCUIElementTypeTextField")
    el2.send_keys("songxiangrui")
    # self.assertEqual(el2.get_attribute('value'),'songxiangrui')
    el3 = driver.find_element_by_class_name("XCUIElementTypeSecureTextField")
    el3.send_keys("123456")
    el4 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"登录\"]")
    el4.click()
    sleep(1)

def isExist(self,element):
    exist = True
    try:
        self.driver.find_element_by_xpath(element)
        return exist
    except:
        exist = False
        return exist
    if exist == False:
        sleep(1)
        self.isExist(element)

def get_element(element,is_id):
    count = 0
    while(True):
        try:
            if(is_id):
                return driver.find_element_by_accessibility_id(element)
            else:
                return driver.find_element_by_xpath(element)
        except:
            count += 1
            if count >= 15:
                raise Exception("The element is not find: %s" % element)
            sleep(1)

class TestNihao(unittest.TestCase):
    # def setUp(self):
    #     caps = {}
    #     caps["app"] = "/Users/sxr/Library/Developer/Xcode/DerivedData/BeingTime-dwtslihoezrwyjgssaxlsitpqzma/Build/Products/Debug-iphonesimulator/BeingTime.app"
    #     caps["platformName"] = "iOS"
    #     caps["platformVersion"] = "10.3"
    #     caps["deviceName"] = "iPhone 6s"
    #
    #     self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #
    # def tearDown(self):
    #     self.driver.quit()
    #
    # def login(self):
    #     el2 = self.driver.find_element_by_class_name("XCUIElementTypeTextField")
    #     el2.send_keys("songxiangrui")
    #     self.assertEqual(el2.get_attribute('value'),'songxiangrui')
    #     el3 = self.driver.find_element_by_class_name("XCUIElementTypeSecureTextField")
    #     el3.send_keys("123456")
    #     el4 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"登录\"]")
    #     el4.click()
    #     sleep(1)
    #
    # def isExist(self,element):
    #     exist = True
    #     try:
    #         self.driver.find_element_by_xpath(element)
    #         return exist
    #     except:
    #         exist = False
    #         return exist
    #     if exist == False:
    #         sleep(1)
    #         self.isExist(element)
    #
    # def get_element(self,element,is_id):
    #     count = 0
    #     while(True):
    #         try:
    #             if(is_id):
    #                 return self.driver.find_element_by_accessibility_id(element)
    #             else:
    #                 return self.driver.find_element_by_xpath(element)
    #         except:
    #             count += 1
    #             if count >= 15:
    #                 raise Exception("The element is not find: %s" % element)
    #             sleep(1)
        # else:
   #           try:
   #               return self.driver.find_element_by_accessibility_id (element)
   #           except:
   #               count += 1
   #               if count >= 15:
   #                   raise Exception("The element is not find: %s" % element)
   #               sleep(1)


    def test_shopping(self):
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"立即抢购\"]")
        el1.click()
        sleep(1)
        self.login()
        el55 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]")
        el5 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeTextField")
        rnd = randint(1, 10)
        print(rnd)
        el5.send_keys(rnd)
        print(el5.get_attribute('value'))
        self.assertEqual(el5.get_attribute('value'),str(rnd))
        sleep(2)
        price = re.search('(\d+\.\d*)', '￥3.00/秒')
        price_num = string.atof(price.group(0))
        print(price_num)
        el51 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText")
        # print(el51)
        price_all = el51.get_attribute('value')
        price_all = price_all.encode('utf-8')
        print('1: ', price_all)
        price_all = re.search("(\d+\.\d*)",price_all)
        price_all = price_all.group(0)
        print('price_all: ',price_all)
        # print('2:',unicode(price_all))
        # pricenum = string.atof(price_all[0][-5:])
 #        print(pricenum)
        self.assertEqual(price_num * rnd , string.atof(price_all))
        el6 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"提交订单\"]")
        el6.click()
        sleep(3)
        el7 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确认付款\"]")
        el7.click()
        sleep(3)
        el8 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"完成\"]")
        el8.click()
        sleep(1)

    def test_Auction(self):
        el11 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconMeNor\"]")
        el11.click()
        sleep(1)
        self.login()
        el12 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"backNor\"]")
        el12.click()
        sleep(1)
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"精彩互动\"]")
        el1.click()
        sleep(1)
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"允许\"]")
        el2.click()
        sleep(1)
        el3 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Allow\"]")
        el3.click()
        sleep(1)
        el4 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"竞拍\"]")
        el4.click()
        sleep(1)
        el5 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"预告\"]")
        self.assertTrue(el5.get_attribute('value'))

    def test_buylist(self):
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconMeNor\"]")
        el1.click()
        sleep(1)
        self.login()
        sleep(2)
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")
        el2.click()
        sleep(1)
        el3 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"兑换\"]")
        el3.click()
        el3.click()
        sleep(1)
        el4 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el4.click()
        sleep(1)
        el41 = self.driver.find_element_by_xpath("//XCUIElementTypeImage[@name=\"ic_exchange_success_medley\"]")
        print(el41.get_attribute('name'))
        self.assertEqual(el41.get_attribute('name'),'ic_exchange_success_medley')
        el5 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"完成\"]")
        el5.click()

    def test_search(self):
        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconSearchNor\"]")
        el1.click()
        sleep(1)
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField")
        el2.send_keys(u"宋")
        sleep(3)
        el3 = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"你好时间\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")
        el3.click()
        sleep(1)
        el4 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"btn more white\"]")
        el4.click()
        sleep(1)
        el5 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"微信\"]")
        self.assertEqual(el5.get_attribute('name'),u'微信')
        el5.click()

#     def test_AuctionBuy(self):
#         el11 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconMeNor\"]")
#         el11.click()
#         sleep(1)
#         self.login()
#         sleep(1)
#         el12 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"backNor\"]")
#         el12.click()
#         sleep(1)
#         el1 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"精彩互动\"]")
#         el1.click()
#         sleep(1)
#         el2 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"允许\"]")
#         el2.click()
#         sleep(1)
#         el3 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Allow\"]")
#         el3.click()
#         sleep(1)
#         el4 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"竞拍\"]")
#         el4.click()
#         sleep(1)
#         el5 = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"预告\"]")
#         sleep(1)
#         elbeing = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"进行中\"]")
#         elbeing.click()
#         sleep(1)
#         btn_join = self.get_element("//XCUIElementTypeButton[@name=\"参与竞拍\"]",False)
#         btn_join.click()
#         sleep(2)
#         btn_offer_price = self.get_element("bidBtn",True)
#         # btn_offer_price = self.driver.find_element_by_ios_uiautomation("");
#         btn_offer_price.click()
#         print(btn_offer_price)
#         # btn_offer_verify = self.get_element("//XCUIElementTypeButton[@name=\"确认竞拍\"]")
# #         btn_offer_verify.click()
#         el8 = self.get_element("//XCUIElementTypeButton[@name=\"确认出价\"]",False)
#         self.assertEqual(el8.get_attribute('name'),u'确认出价')
#         el8.click()
#         sleep(2)
def test_AuctionBuy():
    el11 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"iconMeNor\"]")
    el11.click()
    sleep(1)
    login()
    sleep(1)
    el12 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"backNor\"]")
    el12.click()
    sleep(1)
    el1 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"精彩互动\"]")
    el1.click()
    sleep(1)
    el2 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"允许\"]")
    el2.click()
    sleep(1)
    el3 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Allow\"]")
    el3.click()
    sleep(1)
    el4 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"竞拍\"]")
    el4.click()
    sleep(1)
    el5 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"预告\"]")
    sleep(1)
    elbeing = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"进行中\"]")
    elbeing.click()
    sleep(1)
    btn_join = get_element("//XCUIElementTypeButton[@name=\"参与竞拍\"]",False)
    btn_join.click()
    sleep(2)
    btn_offer_price = get_element("bidBtn",True)
    btn_offer_price.click()
    print(btn_offer_price)
    el8 = get_element("//XCUIElementTypeButton[@name=\"确认出价\"]",False)
    self.assertEqual(el8.get_attribute('name'),u'确认出价')
    el8.click()
    sleep(2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestNihao('test_shopping'))
    # suite.addTest(TestNihao('test_Auction'))
    # suite.addTest(TestNihao('test_buylist'))
    # suite.addTest(TestNihao('test_search'))
    suite.addTest(TestNihao('test_AuctionBuy'))
    unittest.TextTestRunner().run(suite)
