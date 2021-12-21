from selenium import webdriver


class loginpage:
    textbox_email_id = "inp_loginid"
    textbox_password_id = "inp_password"
    button_login_xpath = "//button[contains(text(),'Login')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setEmailId(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

