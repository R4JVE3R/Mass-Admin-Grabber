import urllib3
import time
import os
from colorama import Fore

possibleAdmin = ['admin','Admin','administrator','adminpanel','webadmin','wp-admin','admin.php','login.php','Login.php']
foundAdminList = []
print(Fore.RED+'''
█▀▄▀█ █▀▀█ █▀▀ █▀▀   █▀▀█ █▀▀▄ █▀▄▀█ ░▀░ █▀▀▄   █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█
█░▀░█ █▄▄█ ▀▀█ ▀▀█   █▄▄█ █░░█ █░▀░█ ▀█▀ █░░█   █░▀█ █▄▄▀ █▄▄█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀
▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀   ▀░░▀ ▀▀▀░ ▀░░░▀ ▀▀▀ ▀░░▀   ▀▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀░ ▀▀▀ ▀░▀▀

                                                            - By R̴4̴J̴V̴E̴3̴R̴  ♥
'''+Fore.RESET)
print('''
================================================
[~]Facebook  : https://facebook.com/R4JVE3R/
[~]Instagram : https://instagram.com/R4JVE3R/
[~]Twitter   : https://twitter.com/R4JVE3R/
================================================
''')

http = urllib3.PoolManager()
siteList = open("list.txt","r")
result = open('Result.txt','w')
error = open('error.txt','w')
if(os.stat("list.txt").st_size == 0 or os.stat("list.txt").st_size == 1):
    print(Fore.RED+"List.txt File is Empty Please Enter Your Targets Inside It.")
    exit()
total = siteList.readlines()

for site in total:
    print("[-] "+site.rstrip('\n')+" Scanning...")
    for admin in possibleAdmin:
        req = site.rstrip('\n')+"/"+admin
        try:
            respo = http.request('GET',req)  
        except urllib3.exceptions.MaxRetryError as identifier:
            error.write("Exception Occured at "+req+'\n')
        except:
            pass
        if(respo.status == 200 or respo.status == 302):
            foundAdminList.append(req)
            break

print("\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Here is List of Sites Where i Found Admin Panel +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n")
time.sleep(2)

for site in foundAdminList:
    print(Fore.GREEN+"[+] "+site)
    result.write(site+'\n')

print('\n\n++++++++++Done Bro++++++++++')
print('All Sites with Admin Panel Saved in Result.txt\n')
