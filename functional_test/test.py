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
       
       ##test their is a header title
       header =self.browser.find_element(By.ID, 'main_header')
       header_text = self.browser.find_element(By.ID, 'main_header').text
       ## make sure the header is not empty
       self.assertGreater(len(header_text),0)
       
       #test there is a explanation paragraph
       ex_paragraph = self.browser.find_element(By.ID, 'main_paragraph')
       ex_paragraph_text = self.browser.find_element(By.ID, 'main_paragraph').text
       # test the pragraph has some text
       self.assertGreater(len(ex_paragraph_text),0)
       
       
       
        