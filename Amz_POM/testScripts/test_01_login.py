from Amz_POM.common.basetest import BaseTestClass
from Amz_POM.pageObject.page_actions import PageActionsClass

class test_01_login(BaseTestClass):

    pg_act = PageActionsClass()
    PageActionsClass.login_action(pg_act)
    PageActionsClass.searchAction(pg_act)
    srch = PageActionsClass.searchedTxt(pg_act)
    print(srch)
    if srch == '"iphone 6s"':
        PageActionsClass.AddToCart(pg_act)
        PageActionsClass.Proceed(pg_act)
        PageActionsClass.DeliverToAddress(pg_act)

