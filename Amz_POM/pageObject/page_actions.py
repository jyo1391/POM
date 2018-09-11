from Amz_POM.pageObject.elements import ElementsClass

class PageActionsClass(ElementsClass):

    ec = ElementsClass()

    def login_action(self):
        self.getLoginBtn().click()
        self.getEmailField().send_keys('jyothi1391@gmail.com')
        self.getEmailCont().click()
        self.getPassField().send_keys('123jyothi123')
        self.getSigninBtn().click()

    def searchAction(self):
        self.getSearchBox().send_keys('iphone 6s')
        self.getSearchBtn().click()

    def searchedTxt(self):
        self.getSearchtext().text

