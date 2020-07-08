import unittest
import scrape
from selenium import webdriver

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.driver = scrape.scrape()
        self.driver.get('https://nackademin.leanpoint.se/')
        print("Browser Opened")

    def test_driver(self):
        self.assertTrue(self.driver)
        print("driver found...")

    def test_open_learpoint(self):
        expected_url = 'https://nackademin.learnpoint.se/LoginForms/LoginForm.aspx?ReturnUrl=%2f'
        expected_title = 'Nackademin - LearnPoint'
        self.assertEqual(expected_url, scrape.get_url(self.driver).current_url )
        self.assertEqual(expected_title, scrape.get_url(self.driver).title)
        print("checking if site is reachable...")
       
    def test_login_learnpoint(self):
        scrape.login_user(self.driver)
        print("Trying to login with credentials...")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()