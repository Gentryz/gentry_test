import unittest

from selenium import webdriver

from base.base_util import BaseUtil
from pageobject.reboot_page import RebootPage

class TestRboot(BaseUtil):
    def test_01_reboot(self):
        """重启设备"""
        lp = RebootPage(self.driver)
        lp.reboot_ecshop()

