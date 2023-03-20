from ddt import data, ddt, unpack

from base.base_util import BaseUtil
from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage


@ddt
class TestLogin(BaseUtil):
    @data(*ExcelUtil().read_excel(sheetname="login"))
    @unpack
    def test_01_login(self,index,username,password,results):
        """登入 """
        # print(index,username,password,results)
        lp = LoginPage(self.driver)
        lp.login_ecshop(username=username, password=password)
        # 断言
        if index==index:
            assert lp.get_except_result(username) == results



    # def test_02(self,index,username,password):
    #     print(index,username,password)



