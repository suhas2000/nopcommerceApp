import pytest

from pageObjects.LoginPage import LoginP
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_004_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regrssion
    def test_searchCustomerByName(self, setup):
        self.logger.info("****Test_005_SearchCustomerByName****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginP(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login Successfull****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()

        self.logger.info("****Search Customer By Name****")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Brenda")
        self.searchcust.setLastName("Lindgren")
        self.searchcust.clickOnSearch()
        time.sleep(5)
        status = self.searchcust.SearchCustomerByName("Brenda Lindgren")
        self.driver.close()
        assert True == status
        self.logger.info("****Ending Search Customer By Name Test Case****")