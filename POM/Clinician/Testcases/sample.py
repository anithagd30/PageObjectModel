import pytest
from selenium import webdriver
from pageObjects.Loginpage import loginpage
import time
from selenium.webdriver.chrome.options import Options


class Test_001_Login:
    URL = "https://www.cansrdev.com/clinical/dashboard/"
    email = "thomas.n.oneill@yopmail.com"
    password = "Cansr@21"

    def test_homepage_title(self, setup):
        self.driver = setup
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
        self.driver.get(self.URL)
        print('test')
        self.driver.close()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Cansr | Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self. URL)
        self.lp = loginpage(self.driver)
        self.lp.setEmailId(self.email)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clicklogin()
        time.sleep(5)
        actual_title = self.driver.title
        if actual_title == "Radiologist Dashboard":
            assert True
        else:
            assert False
            file_name = "test_login.png"
            self.driver.save_screenshot(file_name)
        driver.close()
