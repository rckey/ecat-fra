# -*- coding: UTF-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Frame
from function import bypass_function
from function import obfuscate_function
from module.bypass import config
from function import av_list_function
from function import thinkphp_function
from module.struts2 import str2_check
from function import struts2_function

def ecat_logo():
    print('''
    ==============================================================================================================
    
                ███████╗ ██████╗ █████╗ ████████╗              ████████╗ ██████╗  ██████╗ ██╗     
                ██╔════╝██╔════╝██╔══██╗╚══██╔══╝              ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                █████╗  ██║     ███████║   ██║       █████╗       ██║   ██║   ██║██║   ██║██║     
                ██╔══╝  ██║     ██╔══██║   ██║       ╚════╝       ██║   ██║   ██║██║   ██║██║     
                ███████╗╚██████╗██║  ██║   ██║                    ██║   ╚██████╔╝╚██████╔╝███████╗
                ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝                    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝


    Version: 2021_01
    Author: 薛定的_饿猫
    Tanks to: 拉拉
    ==============================================================================================================
    output>>                '''.format())
ecat_logo()


window = tk.Tk()
window.title("薛定的_饿猫 - ecat Framework")
window.geometry('800x650')

tab_main=ttk.Notebook()
tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)


tab1 = Frame(tab_main)
tab1.place(x=0, y=30)
tab_main.add(tab1, text='免杀生成')


tab3 = Frame(tab_main)
tab3.place(x=0, y=30)
tab_main.add(tab3, text='杀软识别')


tab2 = Frame(tab_main)
tab2.place(x=0, y=30)
tab_main.add(tab2, text='命令行混淆')


tab4 = Frame(tab_main)
tab4.place(x=0, y=30)
tab_main.add(tab4, text='ThinkPHP检测')

tab5 = Frame(tab_main)
tab5.place(x=0, y=30)
tab_main.add(tab5, text='Struts2检测')

avs = config.avs


bypass_function.AddCheckButton(tab1, av_name="火绒", column=0)
bypass_function.AddCheckButton(tab1, av_name="360", column=1)
bypass_function.AddCheckButton(tab1, av_name="Windows Defender", column=2)


bypass_function.enter(tk, tab1)

make_button = tk.Button(tab1, text="生成EXE", command=bypass_function.MakeEXE, width = 20, height = 2)
make_button.place(x=265, y=480)


obfuscate_function.enter_cmd(tk, tab2)
obfuscate_function.output_cmd(tk, tab2)

ob_button_1 = tk.Button(tab2, text="混淆模块1", command=obfuscate_function.obfuscate_1, width = 20, height = 2)
ob_button_1.place(x=160, y=257)

ob_button_2 = tk.Button(tab2, text="混淆模块2", command=obfuscate_function.obfuscate_2, width = 20, height = 2)
ob_button_2.place(x=360, y=257)


av_list_function.enter_tasklist(tk, tab3)
av_list_function.output_avlist(tk, tab3)

re = tk.Button(tab3, text="杀软识别", command=av_list_function.av_re, width=12, height=2)
re.place(x=305, y=240)


thinkphp_function.input_url(tk, tab4)
thinkphp_function.result_output(tk, tab4)

def bug_check(tk, tab4):
    check = tk.Button(tab4, text="ThinkPHP检测", command=thinkphp_function.get_url, width=12, height=1)
    check.place(x=520, y=25)

bug_check(tk, tab4)


struts2_function.input_url(tk, tab5)
struts2_function.result_output(tk, tab5)


def struts2_check(tk, tab5):
    check = tk.Button(tab5, text="Struts2检测", command=struts2_function.get_url, width=12, height=1)
    check.place(x=520, y=25)

struts2_check(tk, tab5)




window.mainloop()