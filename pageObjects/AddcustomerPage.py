import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id = 'DateOfBirth']"
    txtCompanyName_xpath = "//input[@id = 'Company']"
    txtCustomersRole_xpath = "(//div[@class = 'k-multiselect-wrap k-floatwrap'])[2]"
    listitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    listitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    listitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    listitemVendors_xpath = "//li[contains(text(), 'Vendors')]"
    listitemForumModerators_xpath = "//li[contains(text(), 'Forum Moderators'')]"
    drpMngrOfVendor_xpath = "//select[@id = 'VendorId']"
    txtAdminComment_xpath = "//textarea[@name = 'AdminComment']"
    btnSave_xpath = "//button[@name = 'save']"


    def __init__(self, driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element("xpath", self.lnkCustomers_menu_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element("xpath", self.lnkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element("xpath", self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element("xpath", self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("xpath", self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element("xpath", self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath", self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element("id", self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element("id", self.rdFemaleGender_id).click()
        else:
            self.driver.find_element("id", self.rdMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element("xpath", self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element("xpath", self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRole(self, custrole):
        self.driver.find_element("xpath", self.txtCustomersRole_xpath).click()
        time.sleep(3)
        if custrole == 'Registered':
            self.listitem = self.driver.find_element("xpath", self.listitemRegistered_xpath)
        elif custrole == 'Administrators':
            self.listitem = self.driver.find_element("xpath", self.listitemAdministrators_xpath)
        elif custrole == 'Guests':
            time.sleep(3)
            self.driver.find_element("xpath", "//span[@title='delete']").click()
            self.listitem = self.driver.find_element("xpath", self.listitemGuests_xpath)
        elif custrole == 'Vendors':
            self.listitem = self.driver.find_element("xpath", self.listitemVendors_xpath)
        elif custrole == 'Forum Moderators':
            self.listitem = self.driver.find_element("xpath", self.listitemForumModerators_xpath)
        else:
            self.listitem = self.driver.find_element("xpath", self.listitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMngrOfVendor(self, value):
        drp = Select(self.driver.find_element("xpath", self.drpMngrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element("xpath", self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element("xpath", self.btnSave_xpath).click()