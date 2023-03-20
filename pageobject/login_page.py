import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    #页面元素
    username_loc = (By.NAME, "name")
    password_loc = (By.NAME, "password")
    submit_loc = (By.XPATH, "//*[@class='el-button el-button--primary el-button--medium']")
    username1_loc = (By.XPATH, "//span[@class='user-name']")

    #页面动作
    def login_ecshop(self,username="shelly",password="xlxh12120627"):
        try:
            self.send_keys(LoginPage.username_loc,username)
            self.send_keys(LoginPage.password_loc,password)
            self.click_keys(LoginPage.submit_loc)
        except:
            raise

    def get_except_result(self,username="shelly"):
        try:
            time.sleep(10)
            if self.get_test(LoginPage.username1_loc) == username:
                return "pass"
            else:
                return "fail"
        except:
            return "fail"






