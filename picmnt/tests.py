from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from pyvirtualdisplay import Display


class ImageTest(LiveServerTestCase):

    def setUp(self):
        self.SERVER = 'http://picmnt.dev'
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def test_main_page(self):
        self.browser.get(self.SERVER + '/')
        title = self.browser.title
        self.assertIn('Picmnt', title)

    def test_random_image(self):
        self.browser.get(self.SERVER + '/random')
        title = self.browser.title
        self.assertIn('Picmnt', title)
