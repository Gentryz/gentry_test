import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pageobject.login_page import LoginPage


class BangPage(BasePage):
    #页面元素
    Device_loc = (By.XPATH, "//span[contains(text(), 'Device List')]")
    Tbody_loc = (By.XPATH, "//tbody")
    #页面动作
    def check_bind(self):
        try:
            lp = LoginPage(self.driver)
            lp.login_ecshop()
            time.sleep(10)
            self.click_keys(BangPage.Device_loc)
            time.sleep(20)
            self.driver.implicitly_wait(60)
            # self.get_test(BangPage.Tbody_loc)

        except:
            raise


    def get_except_result(self,uutname="OU25978"):
        try:
            Tbody_value = self.get_test(BangPage.Tbody_loc)
            if uutname in Tbody_value:
                print('设备已绑定..............')
                return "pass"
            else:
                print('设备未绑定..............')
                return "fail"

        except:
            return "fail"
