import random

def enter_cmd(tk, tab2):
    global text_1
    text_1 = tk.Text(tab2, width=80, height=15)
    text_1.place(x=60, y=30)


def output_cmd(tk, tab2):
    global text_2
    text_2 = tk.Text(tab2, width=80, height=15)
    text_2.place(x=60, y=320)


def get_cmd():
    global u_cmd
    u_cmd = text_1.get('0.0', 'end')


def ob_str():
    global ob_list
    global ob_word
    ob_list = "abcdefghijklmnopqrstuvwxyzABCDEFHHIJKLMNOPQRSTUVWXYZ0123456789012345678901234567890123456789!@#$*!@#$*!@#$*!@#$*!@#$*!@#$*!@#$*"
    ob_word = random.sample(ob_list, random.randint(7,17))
    ob_word = "".join(ob_word)


def _cmd_():
    global cmd
    str = "cmd"
    cmd = ""
    for str_ in str:

        k = random.choice(list(range(1, 9, 2)))
        global yy_char
        yy_char = ""
        for j in range(0, k):
            y_char = "^"
            y = random.choice(list(range(4, 14, 2)))
            for i in range(1, y):
                y_char = y_char + "\""
            yy_char = y_char + yy_char
        cmds = yy_char + str_
        cmd = cmd + cmds

def _fenhao_():
    global fenhao
    fenhao = ""
    x = random.randint(8, 14)
    for i in range(4, x):
        fenhao = fenhao + ";"


def _cmdob_():
    global ob_words
    ob_lists = "ab,;,;,;,;cdefghij,;,;,;,kl\mnopqrstu,;,;,;,;,;vwxyzABC,;,;,;,;DEFHHI,;,;,JKLMNOP,;,;,;,;,;QRSTUVWXYZ0,;,;,;,;,;123456789012345678901234567890123456789"
    ob_words = random.sample(ob_lists, random.randint(12, 25))
    ob_words = "".join(ob_words)



def obfuscate_1():
    global u_cmd
    global cmd
    global ob_words
    global ob_word
    global text_2
    get_cmd()
    _cmd_()
    _cmdob_()
    _fenhao_()
    ob = ""
    ob_dic = [""]
    ob_str()
    for x in u_cmd:
        ob = ob + ob_word + x
    name = "I_am_ecat_Welcome_To_Use_My_Framework"
    cmd = cmd + ";;" + ob_words + ";\",;\",;\",;\";;\",\";\",;\",;,;" + "/C " + "\"" + "s^e^t " + name + "=" + ob + " & echo %" + name + ":" + ob_word + "=% | c\"\"\"\"\"\"\"\"\"\"\"m\"\"\"\"d\"\"\"\"\"\"\"\"\"\"" + "\""
    cmd = cmd.replace("\n", "")
    text_2.delete("0.0", "end")
    text_2.insert("end", cmd)

    print("    \033[0;36;40mcmd obfuscation success!\033[0m")

def obfuscate_2():
    get_cmd()










