## lite version ##
## only for test ##
## beta ##

# import
import os
import platform
import getpass
import sys

# main
windows = []
for info in sys.getwindowsversion():
    windows.append(info)

# windows info
print(f"Microsoft Windows [Version {windows[0]}.{windows[1]}.{windows[2]}]")
while True:
    print(f"┌──([{getpass.getuser()}]@[{platform.node()}])-[{os.getcwd()}]")
    command = input("└─$ ")
    cml = command.split(" ")
    cmd = cml[0]
    # ls
    if cmd == "ls":
        if len(cml) == 1:
            files = os.listdir()
            for file in files:
                if os.path.isdir(file):
                    print(f"<DIR>\t{file}")
                else:
                    print(f"<FILE>\t{file}")
        elif len(cml) == 2:
            try:
                files = os.listdir(cml[1])
            except NotADirectoryError:
                print(f"this is a file -> [{cml[1]}] -> ._.")
            except FileNotFoundError:
                print("not found")
            else:
                for file in files:
                    if os.path.isdir(file):
                        print(f"<DIR>\t{file}")
                    else:
                        print(f"<FILE>\t{file}")
        else:
            print("error")
    # pwd
    elif cmd == "pwd":
        if len(cml) == 1:
            print(f"{os.getcwd()}")
        else:
            print("error")
    # cd
    elif cmd == "cd":
        if len(cml) == 2:
            try:
                os.chdir(cml[1])
            except FileNotFoundError:
                print("not found")
            except NotADirectoryError:
                print(f"this is a file -> [{cml[1]}] -> ._.")
            else:
                pass
        else:
            print("error")
    # cat
    elif cmd == "cat":
        if len(cml) == 2:
            try:
                file = open(cml[1])
            except PermissionError:
                print("error")
            else:
                for line in file:
                    print(line)
        else:
            print("error")
    # echo
    if cmd == "echo":
        if len(cml) > 1:
            for item in cml[1:]:
                print(item, end = " ")
            print("")
        else:
            print("error")
    # exit
    elif cmd == "exit":
        if len(cml) == 1:
            exit()
        else:
            print("error")
