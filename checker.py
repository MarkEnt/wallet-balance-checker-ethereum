import ressy
import requests
import colorama
import time
import os


def check_one(address):
    r = requests.get("https://api.debank.com/token/cache_balance_list?user_addr=" + address)
    
    try:
        data = r.json()['data']
    except Exception as e:
        print(e)
    
    balance = 0
    for bl in data:
        balance += bl['amount'] * bl['price']
    
    return float(f"{balance:.2f}")


def check_forever(givelist):
    for j in givelist:
        j = j.replace('\n','')
        balance = check_one(j)

        if balance > 0:
            print(f"{colorama.Fore.GREEN}[ {j} ] Balance: {balance}")
        else:
            print(f"{colorama.Fore.RED}[ {j} ] Balance: {balance}")
        time.sleep(3)
        

selection = int(input(
"""
[ 1 ] 12 Wordlist/Privkey List
[ 2 ] Address List
"""))
os.system("cls")
if selection == 1:
    check_forever(open("keys.txt", "r", encoding="utf-8").readlines())

else:
    check_forever(open("addresses.txt", "r", encoding="utf-8").readlines())
