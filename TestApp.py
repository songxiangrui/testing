# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest
from time import sleep
from random import randint

class TestAppTest(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["app"] =           "/Users/sxr/workspace/sample-code/sample-code/apps/TestApp/build/release-iphonesimulator/TestApp.app"
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "iPhone 7 Plus"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    
    def tearDown(self):
        self.driver.quit()
        
    def _populate(self):
           # populate text fields with two random numbers
        els = [self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@name=\"IntegerA\"]"),
                  self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@name=\"IntegerB\"]")]

        self._sum = 0
        for i in range(2):
            rnd = randint(0, 10)
            els[i].send_keys(rnd)
            self._sum += rnd
               
    def test_computation(self):
        self._populate()
        self.driver.find_element_by_accessibility_id('ComputeSumButton').click()
        sum = self.driver.find_element_by_accessibility_id('Answer').text
        self.assertEqual(int(sum), self._sum)
         
    def test_scroll(self):
        els = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        els[5].click()

        sleep(1)
        try:
            el = self.driver.find_element_by_accessibility_id('Allow')
            el.click()
            sleep(1)
        except:
            pass

        el = self.driver.find_element_by_xpath('//XCUIElementTypeMap[1]')

        location = el.location
        self.driver.swipe(start_x=location['x'], start_y=location['y'], end_x=0.5, end_y=location['y'], duration=800)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    