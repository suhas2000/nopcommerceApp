class SearchCustomer:
    txtSearchEmail_xpath = "//input[@name = 'SearchEmail']"
    txtSearchFname_xpath = "//input[@name = 'SearchFirstName']"
    txtSearchLname_xpath = "//input[@name = 'SearchLastName']"
    btnSearchCustomer_xpath = "//button[@id = 'search-customers']"
    table_xpath = "//table[@id = 'customers-grid']"
    table_row_xpath = "//table[@id = 'customers-grid']/tbody/tr"
    table_coloumn_xpath = "//table[@id = 'customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element("xpath", self.txtSearchEmail_xpath).clear()
        self.driver.find_element("xpath", self.txtSearchEmail_xpath).send_keys(email)

    def setFirstName(self,f_name):
        self.driver.find_element("xpath", self.txtSearchFname_xpath).clear()
        self.driver.find_element("xpath", self.txtSearchFname_xpath).send_keys(f_name)

    def setLastName(self,l_name):
        self.driver.find_element("xpath", self.txtSearchLname_xpath).clear()
        self.driver.find_element("xpath", self.txtSearchLname_xpath).send_keys(l_name)

    def clickOnSearch(self):
        self.driver.find_element("xpath", self.btnSearchCustomer_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements("xpath", self.table_row_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements("xpath", self.table_coloumn_xpath))

    def SearchCustomerByEmail(self,email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            emailid = table.find_element("xpath","//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            name = table.find_element("xpath","//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag