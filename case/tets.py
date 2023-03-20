import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCase(unittest.TestCase):
    def loggin(self):
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        # 加载网页
        self.driver.get("https://cloud-test.gl-inet.cn/#/device/list")
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Device List')]").click()
        self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[2]/div").find_element(By.CLASS_NAME, "el-tooltip svg-icon").get_attribute("style")
