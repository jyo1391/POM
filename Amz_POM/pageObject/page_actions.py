from Amz_POM.pageObject.elements import ElementsClass
from time import sleep

class PageActionsClass(ElementsClass):

    ec = ElementsClass()

    def login_action(self):
        self.getLoginBtn().click()
        self.getEmailField().send_keys('email')
        self.getEmailCont().click()
        self.getPassField().send_keys('password')
        self.getSigninBtn().click()

    def searchAction(self):
        self.getSearchBox().send_keys('iphone 6s')
        self.getSearchBtn().click()

    def searchedTxt(self):
        srchTxt = self.getSearchtext().text
        print(srchTxt)
        return srchTxt

    def AddToCart(self):
        self.getWindowBefore()
        self.getFirstProd().click()
        self.switchWindow()
        sleep(20)
        self.getAddCartBtn().click()

    def Proceed(self):
        self.getProceedBtn().click()

    def DeliverToAddress(self):
        self.getAddressBtn().click()

