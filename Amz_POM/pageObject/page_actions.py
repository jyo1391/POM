from Amz_POM.pageObject.elements import ElementsClass

class PageActionsClass(ElementsClass):


    def login_action(self):
        ec = ElementsClass()
        ec.getLoginBtn().click()
        ec.getEmailField().send_keys('jyothi1391@gmail.com')
        ec.getEmailCont().click()
        ec.getPassField().send_keys('123jyothi123')
        ec.getSigninBtn().click()





