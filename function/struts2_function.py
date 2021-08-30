from module.struts2 import str2_check

def input_url(tk, tab5):
    global url_text
    global urls
    urls = tk.StringVar()
    l2 = tk.Label(tab5, text="URL: ")
    l2.place(x=26, y=29)
    url_text = tk.Entry(tab5, width=63, bd=2, textvariable=urls)
    url_text.place(x=60, y=30)


def result_output(tk, tab5):
    global result_text
    result_text = tk.Text(tab5, width=78, bd=2, height=33)
    result_text.place(x=60, y=80)


def get_url():
    global urls
    global url

    url = urls.get()
    str2_check.run(url)