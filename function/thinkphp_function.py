from module.ThinkPHP.thinkphp_exp import tp5_rce, tp2_rce, t5inject
from module.ThinkPHP.thinkphp_exp import tp5023_rce
import os


def input_url(tk, tab4):
    global url_text
    global urls
    urls = tk.StringVar()
    l1 = tk.Label(tab4, text="URL: ")
    l1.place(x=26, y=29)
    url_text = tk.Entry(tab4, width=63, bd=2, textvariable=urls)
    url_text.place(x=60, y=30)


def result_output(tk, tab4):
    global result_text
    result_text = tk.Text(tab4, width=78, bd=2, height=33)
    result_text.place(x=60, y=80)


def get_url():
    global urls
    global url
    result_text.delete("0.0", "end")
    url = urls.get()

    t2_ = tp2_rce.tp2()
    t2_.check_tp2(url)

    t5_ = tp5_rce.tp5()
    t5_.check_tp5(url)

    t5023_ = tp5023_rce.tp5023()
    t5023_.check_tp5023(url)

    t5inject_ = t5inject.t5inject()
    t5inject_.check_tp5inject(url)
    with open("tp_check.log", "r") as re:
        res = re.read()
    result_text.insert("end", res)
    os.system("del tp_check.log")