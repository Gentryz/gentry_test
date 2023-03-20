import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class BatchresatrtPage(BasePage):
    #页面元素
    button_loc = (By.XPATH, "//span[contains(text(), 'OU25978')]/../../../../../td[1]/div/label")
    iframe_loc = (By.XPATH, "//div[@class='el-table__header-wrapper']")
    Device_loc = (By.XPATH, "//span[contains(text(), 'Device List')]")
    batch_loc = (By.XPATH, "//*[@id='app']/div/div[2]/section/div[1]/div/div[4]/div[2]/table/thead/tr/th[1]/div/label/span/span")
    bulk_loc = (By.XPATH,"//span[contains(text(), 'Bulk Action')]")
    restart_loc = (By.XPATH, "//body/ul/li[4]")
    confirm_loc=(By.XPATH," //span[contains(text(), 'Confirm and view')]")
    username1_loc = (By.XPATH, "//span[@class='user-name']")
    out_loc=(By.XPATH,"// span[contains(text(), 'Log Out')]")
    # // *[starts-with(@ id, 'dropdown')]
    #页面动作
    def bachrestart(self):
        lp = LoginPage(self.driver)
        lp.login_ecshop()
        time.sleep(10)
        self.click_keys(BatchresatrtPage.Device_loc)
        time.sleep(10)
        self.hover(BatchresatrtPage.batch_loc)
        test = self.get_test(BatchresatrtPage.iframe_loc)
        time.sleep(1)
        self.click_keys(BatchresatrtPage.batch_loc)
        time.sleep(1)
        self.click_keys(BatchresatrtPage.bulk_loc)
        self.hover(BatchresatrtPage.bulk_loc)
        time.sleep(1)
        self.hover(BatchresatrtPage.restart_loc)
        self.click_keys(BatchresatrtPage.restart_loc)
        self.click_keys(BatchresatrtPage.confirm_loc)
        time.sleep(1)
        self.click_keys(BatchresatrtPage.username1_loc)
        time.sleep(1)
        self.click_keys(BatchresatrtPage.out_loc)
        time.sleep(5)








