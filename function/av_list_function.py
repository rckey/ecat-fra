# -*-coding:utf-8-*-
import module.AvRecognition.avlists
import re

def enter_tasklist(tk, tab3):
    global tasklist
    tasklist = tk.Text(tab3, width=37, height=35)
    tasklist.place(x=30, y=30)



def output_avlist(tk, tab3):
    global avlist
    avlist = tk.Text(tab3, width=37, height=35)
    avlist.place(x=410, y=30)


def av_re():
    avlist.delete("0.0", "end")
    task = tasklist.get("0.0", "end").replace("\n", "@")
    g_list = re.findall(r'[A-Za-z0-9]*.exe', task)
    output_av = []
    for av_name in g_list:
        if av_name in module.AvRecognition.avlists.av_list:
            output_av.append(av_name)
    if output_av != []:
        for av_name in output_av:
            avlist.insert("end", av_name+": "+module.AvRecognition.avlists.av_list[av_name]+"\n")

        print("    \033[0;36;40mSuccess!\033[0m")
    else:
        print("    \033[0;31;40mFailed!\033[0m")

