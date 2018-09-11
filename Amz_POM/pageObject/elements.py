from Amz_POM.common.basetest import BaseTestClass
from time import sleep
class ElementsClass(BaseTestClass):

    b_tst = BaseTestClass()
    driver = b_tst.setUp()

    def getLoginBtn(self):
        signin = self.driver.find_element_by_xpath('//a[@id="nav-link-yourAccount"]')
        return signin

    def getEmailField(self):
        emailAddress = self.driver.find_element_by_xpath("//input[@type='email']")
        return emailAddress

    def getEmailCont(self):
        emailCont = self.driver.find_element_by_xpath('//input[@id="continue"]')
        return emailCont

    def getPassField(self):
        passwd = self.driver.find_element_by_xpath('//input[@id="ap_password"]')
        return passwd

    def getSigninBtn(self):
        loginBtn = self.driver.find_element_by_xpath('//input[@id="signInSubmit"]')
        return loginBtn

    def getSearchBox(self):
        searchBox = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        return searchBox

    def getSearchBtn(self):
        searchBtn = self.driver.find_element_by_xpath('//input[@value="Go"]')
        return searchBtn

    def getSearchtext(self):
        searchTxt = self.driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']")
        return searchTxt