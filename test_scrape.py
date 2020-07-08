import unittest
import scrape
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestScrape(unittest.TestCase):

    def setUp(self):
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://nackademin.learnpoint.se/')
        print("\nBrowser Opened")

    def test_driver(self):
        self.assertTrue(self.driver)
        print("\ndriver found...")

    def test_open_learpoint(self):
        expected_url = 'https://nackademin.learnpoint.se/LoginForms/LoginForm.aspx?ReturnUrl=%2f'
        expected_title = 'Nackademin - LearnPoint'
        self.assertEqual(expected_url, scrape.get_url(self.driver).current_url )
        self.assertEqual(expected_title, scrape.get_url(self.driver).title)
        print("\nchecking if site is reachable...")
       
    def test_login_learnpoint(self):
        scrape.login_user(self.driver)
        print("\nTrying to login with credentials...")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()