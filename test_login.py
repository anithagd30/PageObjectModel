import pytest
from selenium import webdriver
from pageObjects.Loginpage import loginpage
import time

class Test_001_Login:
    URL = "https://www.cansrdev.com/clinical/dashboard/"
    email = "thomas.n.oneill@yopmail.com"
    password = "Test@123"

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self. URL)
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