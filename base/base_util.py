import itertools
import os
import re
import time
import unittest
import zipfile

import requests
from selenium import webdriver
from selenium.common import SessionNotCreatedException


class BaseUtil(unittest.TestCase):

    def getChromeDriver(self,options=None):
        global browser
        try:
            self.path = os.path.abspath(os.curdir)
            self.driver_path = self.path + '\chromedriver.exe'
            self.browser = webdriver.Chrome(self.driver_path)
            return browser
        except SessionNotCreatedException as e:
            self.driver_version = re.search(
                "Chrome version ([\d.]+)", str(e)).group(1)
            self.chrome_version = re.search(
                "Current browser version is ([\d.]+) with", str(e)).group(1)
            print(f"驱动版本：{self.driver_version}，谷歌游览器版本：{self.chrome_version}，不兼容\n开始更新驱动...")
            self.res = requests.get(
                "https://registry.npmmirror.com/-/binary/chromedriver/")
            self.versions = [obj["name"][:-1] for obj in self.res.json() if re.match("\d+",
                                                                           obj["name"]) and obj["name"].count(".") == 3]
            self.versions = {key: max(versions_split, key=lambda x: int(x[x.rfind(".") + 1:]))
                        for key, versions_split in itertools.groupby(self.versions, key=lambda x: x[:x.rfind(".")])}
            self.dest_version = self.versions[self.chrome_version[:self.chrome_version.rfind(".")]]
            print("驱动将更新到:{}".format(self.dest_version))
            file = f"chromedriver_{self.dest_version}_win32.zip"
            if not os.path.exists(file):
                self.url = f"https://registry.npmmirror.com/-/binary/chromedriver/{self.dest_version}/chromedriver_win32.zip"
                self.res = requests.get(self.url)
                with open(file, 'wb') as f:
                    f.write(self.res.content)
            else:
                print("文件已经下载到当前目录，下面直接使用缓存解压覆盖...")
            with zipfile.ZipFile(file) as zf:
                zf.extract("chromedriver.exe", ".")
            browser = webdriver.Chrome(options=options)
            return browser

    def setUp(self) -> None:
        global driver
        # 打开浏览器
        # self.driver = webdriver.Chrome()
        # driver = self.driver
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(1)
        # # 加载网页
        # self.driver.get("https://cloud-test.gl-inet.cn/#/login")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging', 'enable-automation'])
        self.driver = BaseUtil.getChromeDriver(self.options)
        url = r'http://' + "192.168.4.1" + '/'
        self.driver.get("https://cloud-test.gl-inet.cn/#/login")
        time.sleep(2)

    def tearDown(self) -> None:
        pass

