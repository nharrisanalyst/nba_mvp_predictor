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
       
    def test_for_table(self):
        self.browser.get(self.live_server_url)
        table = self.browser.find_element(By.TAG_NAME, 'table')
        thead = table.find_element(By.TAG_NAME, 'thead')
        thead_row = thead.find_element(By.TAG_NAME, 'tr')
        table_th = thead_row.find_elements(By.TAG_NAME, 'th')
        
        self.assertEqual(len(table_th),20)
        
        first_table_th = table_th[0].text
        self.assertEqual(first_table_th, 'Player')
        
        GP_table_th = table_th[1].text
        self.assertEqual(GP_table_th, 'GP')
        
        mp_table_th = table_th[2].text
        self.assertEqual(mp_table_th, 'MP')
        
        second_table_th = table_th[3].text
        self.assertEqual(second_table_th, 'W')
        
        third_table_th = table_th[4].text
        self.assertEqual(third_table_th, 'W Rank')
       
        fourth_table_th = table_th[5].text
        self.assertEqual(fourth_table_th, 'L')
        
        fith_table_th = table_th[6].text
        self.assertEqual(fith_table_th, 'L Rank')
        
        sixth_table_th = table_th[7].text
        self.assertEqual(sixth_table_th, 'PPG')
        
        seventh_table_th = table_th[8].text
        self.assertEqual(seventh_table_th , 'PPG Rank')
        
        eighth_table_th = table_th[9].text
        self.assertEqual(eighth_table_th, 'FGM')
        
        ninth_table_th = table_th[10].text
        self.assertEqual(ninth_table_th , 'FGA')
        
        tenth_table_th = table_th[11].text
        self.assertEqual(tenth_table_th , 'FG%')
        
        eleventh_table_th = table_th[12].text
        self.assertEqual(eleventh_table_th , 'EFG%')
        
        twelth_table_th = table_th[13].text
        self.assertEqual(twelth_table_th , 'TRB')
        
        thirteenth_table_th = table_th[14].text
        self.assertEqual(thirteenth_table_th , 'TRB Rank')
        
        ast_table_th = table_th[15].text
        self.assertEqual(ast_table_th, 'AST')
        
        ast_rank_table_th = table_th[16].text
        self.assertEqual(ast_rank_table_th, 'AST Rank')
        
        ws_table_th = table_th[len(table_th)-3].text
        self.assertEqual(ws_table_th, 'WS')
        
        ws_ranked_table_th = table_th[len(table_th)-2].text
        self.assertEqual(ws_ranked_table_th, 'WS Rank')
        
        ws_ranked_table_th = table_th[len(table_th)-1].text
        self.assertEqual(ws_ranked_table_th, 'MVP Probability')
        
        ## Table Row 
        
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        
   
       
       
        