import unittest
from HTMLTestRunner import HTMLTestRunner
from webssh import worker

if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover("./testcase", "test_login.py")
    report_file=open("./report/report.html","wb")
    runner=HTMLTestRunner(stream=report_file, verbosity=1, title="云平台测试报告", description="报告详情如下")
    runner.run(suite)