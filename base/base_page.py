from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self,driver):
       self.driver = driver
    #定位元素的关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    def hover(self, loc):
        element = self.locator_element(loc)
        ActionChains(self.driver).move_to_element(element).perform()

    #设置值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)
    #点击关键字
    def click_keys(self,loc):
        self.locator_element(loc).click()

    def waittime(self,vlaue):
        self.driver.implicitly_wait(vlaue)

    #进入框架
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    #退出框架
    def qiut_frame(self):
        self.driver.switch_to.default_content()

    #选中下拉关键字
    def choice_select(self,loc,value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    #获取文本内容
    def get_test(self,loc):
        value = str(self.locator_element(loc).text)
        return value

    def get_test1(self,loc):
        value = str(self.locator_element(loc).get_attribute('value'))
        return value
    #根据定位标签获取其属性值
    def get_attribute(self,loc,lei):
        attribute = str(self.locator_element(loc).get_attribute(lei))
        return attribute
