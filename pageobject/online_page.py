import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pageobject.band_page import BangPage
from pageobject.login_page import LoginPage


class OnlinePage(BasePage):
    #页面元素
    # Device_loc = (By.XPATH, "//span[contains(text(), 'Device List')]")
    Tbody_loc = (By.XPATH, "//tbody")
    Uut_loc = (By.XPATH, "//span[contains(text(), 'OU25978')]")
    Color_loc = (By.XPATH, "//*[@class='el-tooltip router-online svg-icon']")

    #页面动作

    def chech_status_ecshop(self,uutname ="OU25978"):
        try:
            lp = BangPage(self.driver)
            lp.check_bind()
            time.sleep(10)
            Tbody_value = self.get_test(BangPage.Tbody_loc)
            if uutname in Tbody_value:
                print('设备已绑定..............')
                self.click_keys(OnlinePage.Uut_loc)
                time.sleep(3)
                self.driver.implicitly_wait(60)
                self.get_attribute(OnlinePage.Color_loc,"style")
            else:
                print('设备未绑定')
        except:
            raise

    def get_except_result(self,color="color: rgb(34, 244, 187);",onlinestatus="online",offlinestatus="offline"):
        try:
            online_color = self.get_attribute(OnlinePage.Color_loc, "style")
            self.driver.back()
            print(online_color)
            if online_color == color:
                print(onlinestatus)
                return "pass"
            else:
                return "fail"
        except:
            return "fail"

