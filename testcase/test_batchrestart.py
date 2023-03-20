import time
from base.base_util import BaseUtil
from common.network_util import NetworkUtil
from pageobject.batch_page import BatchresatrtPage

def repeat(times):
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)

        return callHelper
    return repeatHelper

# @repeat(5)
class TestBatchrestart(BaseUtil):
    @repeat(5)
    def test_01_batchrestart(self):
        while True:
            result = NetworkUtil().run_ping()
            if result == "fail":
                continue
            else:
                lp = BatchresatrtPage(self.driver)
                lp.bachrestart()
                time.sleep(10)
                break



