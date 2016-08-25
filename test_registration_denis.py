import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from functions import *
from os.path import abspath, join, dirname


class SimpleIOSRegistrationTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = abspath(join(dirname(__file__),'/apps/TrustedInsight.ipa'))
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app':app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 5'
            })

    def tearDown(self):
        self.driver.quit()


    def test_registration(self):

    	self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATextField[1]").send_keys('test+iOSRegistration-' + random_string() + '@thetrustedinsight.com')
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]").click()
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]").send_keys("Denis")
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[2]").send_keys("SuperTest123")
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASecureTextField[1]").send_keys("avatar1260")
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[3]").click()
        sleep(10)
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").click()
        sleep(10)
    	


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSRegistrationTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

