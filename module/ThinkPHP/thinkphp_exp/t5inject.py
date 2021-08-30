# -*-coding:utf-8-*-
import requests

class t5inject:
    def check_tp5inject(self, url):
        url = url + r"/index.php?ids[]=1&ids[]=2"
        re = requests.get(url).text
        if "Hello" in re:
            print("    \033[0;36;31m存在Thinkphp5 SQL注入漏洞和敏感信息泄露漏洞!\033[0m")
            with open("tp_check.log", "a+") as res:
                res.write("存在Thinkphp5 SQL注入漏洞和敏感信息泄露漏洞!\n\n")
            res.close()