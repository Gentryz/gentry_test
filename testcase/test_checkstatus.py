import unittest

from selenium import webdriver

from base.base_util import BaseUtil
from pageobject.online_page import OnlinePage


class TestStatus(BaseUtil):

    def test_01_onlin(self):
        """判断设备状态"""
        lp = OnlinePage(self.driver)
        lp.chech_status_ecshop(uutname ="OU25978")
        assert lp.get_except_result() == "pass"




