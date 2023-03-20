import os
import subprocess
import multiprocessing

class NetworkUtil:

    def get_object_path(self):
        return os.path.abspath(os.path.dirname(__file__)).split("common")[0]

    def check_alive(self,ip=""):
        results = True
        result = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)
        if result == 0:
            # h = subprocess.getoutput('ping ' +ip)
            # returnnum = h.split('平均 = ')[1]
            # print('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' %(ip,returnnum))
            return results
        else:
            with open('notong.txt','a') as f:
                f.write(ip)
                print('\033[31m%s\033[0m ping 不通！' % ip)
                results = False
                return results

    def run_ping(self):
        print("开始批量ping所有IP！")
        with open(NetworkUtil().get_object_path()+"data/ip.txt", 'r') as f:
            for i in f:
                result = NetworkUtil().check_alive(i)
                if result:
                    continue
                else:
                    break
            return result
