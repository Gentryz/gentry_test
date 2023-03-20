from ddt import data, unpack, ddt

from base.base_util import BaseUtil
from common.excel_util import ExcelUtil
from pageobject.band_page import BangPage

@ddt
class TestBind(BaseUtil):
    """绑定设备"""
    @data(*ExcelUtil().read_excel(sheetname="bind"))
    @unpack
    def test_01_bind(self,index,uutname,results):
        lp = BangPage(self.driver)
        lp.check_bind()
        if index==index:
            assert lp.get_except_result(uutname=uutname) == results
