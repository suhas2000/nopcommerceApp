import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginP
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("****Test_003_AddCustomer****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginP(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login Successfull****")

        self.logger.info("****Starting Add Customer Test****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()
        self.addcust.clickonAddnew()

        self.logger.info("****Providing Customer Info****")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Suhas")
        self.addcust.setLastName("Joshi")
        self.addcust.setGender("Male")
        self.addcust.setDOB("09/13/2000")
        self.addcust.setCompanyName("PSL")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setMngrOfVendor("Vendor 2")
        self.addcust.setAdminComment("This is for testing..........")
        self.addcust.clickOnSave()

        self.logger.info("****Saving Customer Info****")
        self.logger.info("****Add Customer Validation Started****")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("****Test Case Passed Successfully****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer.png")
            self.logger.info("****Test Case Failed****")
            assert False

        self.driver.close()
        self.logger.info("****Ending Add Customer Test****")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))