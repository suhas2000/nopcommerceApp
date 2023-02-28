class LoginP:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@type='submit']"
    link_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("xpath", self.textbox_username_xpath).clear()
        self.driver.find_element("xpath", self.textbox_username_xpath).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element("xpath", self.textbox_password_xpath).clear()
        self.driver.find_element("xpath", self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element("xpath", self.link_logout_xpath).click()