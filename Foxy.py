from logging import ERROR, error
import os
import subprocess as sp
import datetime
import socket
import urllib
import webbrowser
import requests
from urllib import request
from rich import print
from rich.console import Console
console = Console()
date_object = datetime.date.today()
os.system('cls')
foxy_run = True
print("Enter user name")
user = input()
os.system('cls')
console.print("Foxy [Version 0.0.1]",style="bold red")
console.print("Python [Version 10.0.0]",style="bold blue")
console.print("Nguyen Le Phuc Vinh",style="bold yellow")
while foxy_run:
            command = input(str(date_object) + " " + user +"@Foxy>").lower()
            if command == ".date":
                console.print(date_object,style="bold red")
            elif "foin soft-install" in command:
                console.print("Enter url of the file you want to download:", style="bold red")
                fox_soft_installer_internet_url = input()
                url = fox_soft_installer_internet_url
                r = requests.get(url, allow_redirects=True)
                print("Downloading the file from url:'" + url + "'")
            elif command == ".time":
                console.print(date_object,style="bold blue")
            elif command == "foxy.notepad":
                print("Opening notepad")
                programName = "notepad.exe"
                sp.Popen([programName])
            elif command == "cls":
                os.system('cls')
            elif command == "clear":
                os.system('cls')
            elif command == "foin":
                console.print("use 'foin soft-install' to download file on internet",style="bold green")
                console.print("use 'foin infor.get' to get information on internet",style="bold green")
            elif command == "make folder":
                console.print("Enter folder name:",style="bold red")
                file_make = input()
                console.print("Enter location of folder",style="bold blue")
                folder_path = input()
                os.mkdir(folder_path + file_make)
            elif command == "exe":
                console.print("Enter file location",style="bold red")
                file_location = input()
                os.system(file_location)
            elif command == "cd":
                console.print("Enter location",style="bold red")
                cd_location = input()
                os.system(cd_location)
                console.print("Moved to '" + cd_location + "'",style="bold green")
            elif command == "exit":
                print("Done!")
                break
            elif command == "end":
                print("Done!")
                break
            elif command == "list":
                os.system('dir')
            elif command == "diskpart":
                os.system('diskpart')
            elif command == "cmd":
                programName = "cmd.exe"
                sp.Popen([programName])
            elif command == '':
                print(" ")
            elif command == ' ':
                print(" ")
            elif command == "ip":
                print("Your IP location:")
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                print(s.getsockname()[0])
                s.close()
            elif command == "foin infor.get":
                print("What's information do you search?")
                infor_foin_get = input()
                try:
                        from googlesearch import search
                except ImportError:
                        print("No module named 'google' found")
                query = infor_foin_get
                for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
            elif command == ".help":
                console.print("'.help' to help",style = "bold yellow")
                print("'.time' to print time now")
                console.print("'.date' to print date now",style = "bold green")
                print("'foxy.notepad' to open notepad")
                print("'cls' to clear screen")
                print("'clear' to clear screen")
                print("'make folder' to make a file")
                print("'exe' + file name.exe to open a file exe")
                console.print("'exit','end' to exit Foxy",style = "bold yellow")
                console.print("'ip' to see your IP Location",style = "bold yellow")
                console.print("'cmd' to open terminal",style = "bold yellow")
                print("use 'foin soft-install' to download file on internet")
                print("use 'foin' to get help of foin")
            else:
                console.print("UnexpectedCase: The command '" + command + "' is unavailable or misspelling or keyword. Please try again.",style="bold red") , print("UnknowERROR: ERRORCODE: UNKNOW_ERROR"), console.print("Conecting to your Windows Powsershell or Command Prompt")
                os.system(command)
