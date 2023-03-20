import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pageobject.login_page import LoginPage
from pageobject.online_page import OnlinePage


class RebootPage(BasePage):
    #页面元素
    Actions_loc=(By.XPATH, "// span[contains(text(), 'OU25978')] /../../../../../td[16]/div/div")
    Reboot_loc=(By.XPATH, "//ul[@x-placement='bottom-end']/li[6]")
    Fenble_loc=(By.XPATH,"//button[@class='el-button el-button--default el-button--small el-button--primary ']")
    Tenble_loc=(By.XPATH,"//*[@id='app']/div/div[2]/section/div[1]/div/div[11]/div/div[3]/div/button")
    #页面动作
    def reboot_ecshop(self):
        lp = OnlinePage(self.driver)
        lp.chech_status_ecshop()
        if lp.get_except_result() == "pass":
            time.sleep(10)
            self.waittime(60)
            self.click_keys(RebootPage.Actions_loc)
            time.sleep(2)
            self.click_keys(RebootPage.Reboot_loc)
            time.sleep(1)
            self.click_keys(RebootPage.Fenble_loc)
            time.sleep(1)
            self.click_keys(RebootPage.Tenble_loc)
        else:
            print("设备不在线，testfail")

