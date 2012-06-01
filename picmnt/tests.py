from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time
from pyvirtualdisplay import Display
import os

class ImageTest(LiveServerTestCase):

    def setUp(self):
        self.SERVER = 'http://picmnt.dev'
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def test_random_image(self):
        self.browser.get(self.SERVER + '/random')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Home', body.text)
        
