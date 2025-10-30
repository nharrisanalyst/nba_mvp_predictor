from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
    
    def test_for_init_setup(self):
       self.browser.get(self.live_server_url)
       self.assertIn('NBA MVP Predictor', self.browser.title)
       
        