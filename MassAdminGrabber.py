import urllib3
import time
import os
from colorama import Fore,init
import threading

init(autoreset=True)
print(Fore.RED+'''
█▀▄▀█ █▀▀█ █▀▀ █▀▀   █▀▀█ █▀▀▄ █▀▄▀█ ░▀░ █▀▀▄   █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█
█░▀░█ █▄▄█ ▀▀█ ▀▀█   █▄▄█ █░░█ █░▀░█ ▀█▀ █░░█   █░▀█ █▄▄▀ █▄▄█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀
▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀   ▀░░▀ ▀▀▀░ ▀░░░▀ ▀▀▀ ▀░░▀   ▀▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀░ ▀▀▀ ▀░▀▀

                                                            - By R̴4̴J̴V̴E̴3̴R̴  ♥
''')
print('''
==================================================
[~]Facebook  : https://facebook.com/R4JVE3R/
[~]Instagram : https://instagram.com/R4JVE3R/
[~]Twitter   : https://twitter.com/R4JVE3R/
==================================================
''')

if(os.stat("list.txt").st_size == 0 or os.stat("list.txt").st_size == 1):
    print(Fore.RED+"List.txt File is Empty Please Enter Your Targets Inside It.\n")
    exit()

http = urllib3.PoolManager()
possibleAdmin = [
    'admin','Admin','login','Login','administrator','Administrator','adminpanel','webadmin','wp-admin','admin.php','login.php','Login.php','admincontrol','pages/admin','siteadmin',
    'webmaster','UserLogin','myadmin','members','user','adminLogin.php']
foundAdminList = []
foundAdminList1 = []

def Boost(LengthForThis):
    for site in range(LengthForThis):
        print("[*] "+total[site].rstrip('\n')+"  :  "+Fore.BLUE+"Scanning...")

        for admin in possibleAdmin:
            req = total[site].rstrip('\n')+"/"+admin
            try:
                respo = http.request('GET',req)  
            except urllib3.exceptions.MaxRetryError as identifier:
                error.write("Exception Occured at "+req+'\n')
            if(respo.status == 200 or respo.status == 302):
                foundAdminList1.append(req)
                break
    

siteList = open("list.txt","r")
result = open('result.txt','w')
error = open('error.txt','w')

total = siteList.readlines()
HalfLength = (len(total))/2
t1 = threading.Thread(target=Boost,args=(int(HalfLength),))
t1.start()
time.sleep(0.3)

for site in range(int(HalfLength),int(HalfLength+HalfLength)):
    print("[*] "+total[site].rstrip('\n')+"  :  "+Fore.BLUE+"Scanning...")

    for admin in possibleAdmin:
        req = total[site].rstrip('\n')+"/"+admin
        try:
            respo = http.request('GET',req)  
        except urllib3.exceptions.MaxRetryError as identifier:
            error.write("Exception Occured at "+req+'\n')
        if(respo.status == 200 or respo.status == 302):
            foundAdminList.append(req)
            break


print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Here is List of Sites Where i Found Admin Panel +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
time.sleep(2)

for site in foundAdminList:
    print(Fore.GREEN+"[+] "+site)
    result.write(site+'\n')
for site in foundAdminList1:
    print(Fore.GREEN+"[+] "+site)
    result.write(site+'\n')
print('\n\n++++++++++Done Bro++++++++++\n')
