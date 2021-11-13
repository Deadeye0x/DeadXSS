print("                   ______")
print("          |\_______________ (_____\\______________")
print(" HH======#H###############H#######################")
print('          \' ~""""""""""""""`##(_))#H\"""""Y########')
print('           ))    \#H\       `"Y###')
print('           "      }#H)')
print('                      _')
print()
import requests
import time
import colorama
import sys
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + "Welcome to " + Fore.RED + "XSS Scanner" + Style.RESET_ALL)
print()
print(Fore.GREEN + "Are you Ready For Scanning")
time.sleep(2)
print()
pog = input(Fore.BLUE + "Please select POST or GET, p/g: ")
print()
if pog == 'g':
    try:
        site = input(Fore.YELLOW + "Enter your target for scanning (with parameters): ")
        r = requests.post(site)
        time.sleep(2)
        print(Fore.RED + "Site Responded Well")
    except:
        print()
        time.sleep(1)
        print(Fore.GREEN + "Site is not reachable")
        sys.exit(0)
    print()
    try:
        payload = input("Enter your payload list here: ")
        resp = open(payload, 'r')
        print()
    except FileNotFoundError:
        print(Fore.GREEN + "File is not Found")
        time.sleep(1)
        sys.exit(0)

    print()
    print(Fore.RED + "Testing...\n")
    time.sleep(0)
    f = open(payload, 'r')
    l = 1
    for line in f:
        print()
        print(Fore.GREEN + "Testing the payload" + str(1))
        if line in requests.get(site + line).text:
            print(Fore.RED + "XSS FOUND HERE!!!")
            print(requests.get(site + line).url)
        else:
            print(Fore.GREEN + "The Payload" + str(1) + "did not trigger XSS here" )
elif pog == 'p':
    try:
        site = input("Enter your target for scanning (with parameters): ")
        data = input("Enter data to post here: ")
        r = requests.post(site)
        time.sleep(2)
        print(Fore.RED + "OK ")
    except:
        print()
        time.sleep(1)
        print(Fore.GREEN + "Site is not reachable")
        sys.exit(0)
    print()
    try:
        payload = input("Enter your payload list here: ")
        resp = open(payload, 'r')
        print()
    except FileNotFoundError:
        print(Fore.GREEN + "File is not Found")
        time.sleep(1)
        sys.exit(0)
print()
print(Fore.RED + "Testing...\n")
time.sleep(0)

f = open(payload, 'r')
l = 1
for line in f:
    print()
    print(Fore.GREEN + "Testing the payload" + str(1))
    if line in requests.get(site + line).text:
        print(Fore.RED + "XSS FOUND HERE!!!")
        print(requests.get(site + line).url)
    else:
        print(Fore.GREEN + "The Payload" + str(1) + "did not trigger XSS here" )
        print()
        l = 1
else:
    print("Unknown Error")
    sys.exit(0)


    



