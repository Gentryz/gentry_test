import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import selenium.webdriver.support.ui as ui

import unittest

def repeat(times):
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)

        return callHelper

    return repeatHelper

class TestCase(unittest.TestCase):
    # @repeat(10)
    # def test_04_fdff(self):
    #     print('1111')

    # @repeat(2)
    def test_01_login(self):
        global driver
        # 打开浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(1)

        # 加载网页
        driver.get("http://localhost:8888")
        driver.find_element(By.NAME,"hostname").send_keys("192.168.4.1")
        driver.find_element(By.NAME, "username").send_keys("root")
        driver.find_element(By.NAME, "password").send_keys("goodlfie1")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Connect')]").click()
        # driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div").find_element(By.XPATH, "@class=el-tooltip svg-icon").get_attribute("style")
        # homepage_handle = driver.current_window_handle
        # # 输入用户名密码
        # driver.find_element(By.LINK_TEXT, "网盘").click()
        # # wait = ui.WebDriverWait(driver, 5)
        # # wait.until(lambda driver:driver.find_element(By.XPATH,"//input[@name='userName']"))
        # time.sleep(10)
        # handles = driver.window_handles
        # for handle in handles:
        #     if handle != homepage_handle:
        #         # 激活新窗口
        #         driver.switch_to.window(handle)
        #         break
        #
        # time.sleep(5)
        # driver.find_element(By.XPATH,"//input[@name='userName']").click()
        # driver.find_element(By.XPATH,"//input[@name='userName']").send_keys("32345545")
    #     driver.find_element(By.NAME, "password").send_keys("xlxh12120627")
    #     # 点击登入
    #     driver.find_element(By.XPATH, "//*[@class='el-button el-button--primary el-button--medium']").click()
    #     driver.implicitly_wait(20)
    #     name = driver.find_element(By.XPATH, "//span[@class='user-name']").text
    #     print(name)
    #     driver.close()
    #     time.sleep(3)
    #     return name
    #
    # def test_02_online(self):
    #     global driver
    #     #打开浏览器
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(1)
    #     #加载网页
    #     driver.get("https://cloud-test.gl-inet.cn/#/login")
    #     #输入用户名密码
    #     driver.find_element(By.NAME, "name").send_keys("shelly")
    #     driver.find_element(By.NAME, "password").send_keys("xlxh12120627")
    #     #点击登入
    #     driver.find_element(By.XPATH, "//*[@class='el-button el-button--primary el-button--medium']").click()
    #     driver.implicitly_wait(20)
    #     name = driver.find_element(By.XPATH, "//span[@class='user-name']").text
    #     # print(name)
    #     driver.implicitly_wait(1)
    #     driver.find_element(By.XPATH, "//span[contains(text(), 'Device List')]").click()
    #     time.sleep(10)
    #     Tbody_value=str(driver.find_element(By.XPATH,"//tbody").text)
    #     # print(Tbody_value)
    #     if 'OU25978' in Tbody_value:
    #         print('111111111111111')
    #         time.sleep(3)
    #         driver.find_element(By.XPATH, "//span[contains(text(), 'OU25978')]").click()
    #         driver.implicitly_wait(5)
    #         online_color=driver.find_element(By.XPATH, "//*[@class='el-tooltip router-online svg-icon']").get_attribute("style")
    #         time.sleep(5)
    #         driver.back()
    #         passcolor= "color: rgb(178, 178, 183);"
    #         online = "online"
    #         if online_color == passcolor:
    #             return online
    #         else:
    #             print('offline')
    #     else:
    #         print('222222222222')
    # def test_03_update(self):
    #     # 打开浏览器
    #     global driver
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(1)
    #     # 加载网页
    #     driver.get("https://cloud-test.gl-inet.cn/#/login")
    #     # 输入用户名密码
    #     driver.find_element(By.NAME, "name").send_keys("shelly")
    #     driver.find_element(By.NAME, "password").send_keys("xlxh12120627")
    #     # 点击登入
    #     driver.find_element(By.XPATH, "//*[@class='el-button el-button--primary el-button--medium']").click()
    #     driver.implicitly_wait(20)
    #     name = driver.find_element(By.XPATH, "//span[@class='user-name']").text
    #     driver.implicitly_wait(1)
    #     driver.find_element(By.XPATH, "//span[contains(text(), 'Device List')]").click()
    #     time.sleep(10)
    #     Tbody_value = str(driver.find_element(By.XPATH, "//tbody").text)
    #     # print(Tbody_value)
    #     if 'OU25978' in Tbody_value:
    #         driver.find_element(By.XPATH, "// span[contains(text(), 'OU25978')] /../../../../../ td[16]/div/div").click()
    #         time.sleep(5)
    #         driver.find_element(By.XPATH,"//ul[@x-placement='bottom-end']/li[6]").click()
    #         driver.find_element(By.XPATH, "//button[@class='el-button el-button--default el-button--small el-button--primary ']").click()
    #         test =driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div[1]/div/div[11]/div/div[3]/div/button").text
    #         print(test)
    #     #     time.sleep(5)
    #     #     ale=driver.switch_to.alert
    #     #     ale.accept()
    #     else:
    #         print('545441415')