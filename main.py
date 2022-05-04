import random
import string
import colorama
import os
import time

#from
from colorama import Fore, Style, Back

colorama.init()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
os.system('cls')
print(f"""

{Fore.LIGHTGREEN_EX}████████████████{Fore.CYAN}███████████████████
{Fore.LIGHTGREEN_EX}█─▄▄▄─█▄─▄████▀▄{Fore.CYAN}─██▄─█▀▀▀█─▄█░▄▄░▄█        {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Devved By @9thr On Github{Fore.LIGHTGREEN_EX}
{Fore.LIGHTGREEN_EX}█─███▀██─██▀██─▀{Fore.CYAN}─███─█─█─█─███▀▄█▀█
{Fore.LIGHTGREEN_EX}▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀{Fore.CYAN}▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀ 

            [ CLAWZ, Wallet Mining Service. ]

        {Fore.WHITE}[ {Fore.CYAN}1 {Fore.WHITE}] : {Fore.CYAN}Start BTC Wallet Mining
        {Fore.WHITE}[ {Fore.CYAN}2{Fore.WHITE} ] : {Fore.CYAN}Quit
""")

print(f'{Fore.WHITE}[ {Fore.RED}?{Fore.WHITE} ] : {Fore.GREEN}', end="")
option = input('')
if option == '1':
    print(f'{Fore.WHITE}[ {Fore.RED}Bitcoin Wallet Address{Fore.WHITE} ] : {Fore.GREEN}', end="")
    wallet = input('')
    os.system('cls')

if option == '2':
    print(f'{Fore.RED} Closing CLAWZ Bitcoin Wallet Miner..')
    exit(0)

print(f'{Fore.WHITE}[{Fore.RED}Confirm This Is YOUR Bitcoin Wallet (Y/N) {Fore.WHITE}] :{Fore.GREEN} [{wallet}]', end="\n")
print(f'{Fore.WHITE}[ {Fore.RED}?{Fore.WHITE} ] : {Fore.GREEN}', end="")
confirmation = input('')
if confirmation == 'Y':
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet.')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet..')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet...')
    time.sleep(0.5)
    os.system('cls')
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet.')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet..')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Checking Wallet...')
    time.sleep(0.5)
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}Successfull, Wallet Address Is VALID!')
    time.sleep(1.5)
    os.system('cls')
    print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}Wallet Mining Begins In 3 Seconds.')
    time.sleep(3)
else:
    print(f'{Fore.WHITE} [{Fore.RED}ERROR{Fore.WHITE}] {Fore.GREEN}Please use capital Y, or N. If still not working, contact SUPPORT or check your Wallet Address. [Quiting]')
    time.sleep(1.2)

for line in range(3000):
    result = print(f'{Fore.WHITE}({Fore.GREEN}BTC : {Fore.RED}0{Fore.WHITE}) {Fore.WHITE}[ {Fore.RED}!{Fore.WHITE} ] : {Fore.LIGHTCYAN_EX}1 {Fore.GREEN}', "".join(random.choice(letters) for i in range(42)))
    print(result)
print(f'{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] : {Fore.LIGHTMAGENTA_EX} Found Hit! Press ENTER To Continue.\n')
input()
btc_amount = "1.00 BTC"
btc_usd_amount = "37,869.60 USD"
print(f'{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] : {Fore.RED}HIT DETAILS:\n BTC ADDRESS: {Fore.LIGHTCYAN_EX} 1 {Fore.LIGHTGREEN_EX}', ''.join(random.choice(letters) for i in range(42)), f'\n {Fore.RED}BTC AMOUNT: {Fore.CYAN}{btc_amount} {Fore.WHITE}, {Fore.WHITE}( {Fore.GREEN}{btc_usd_amount} {Fore.LIGHTYELLOW_EX}${Fore.WHITE} )\n{Fore.LIGHTRED_EX} Press {Fore.GREEN}Enter{Fore.LIGHTRED_EX} To Transact The Funds Into YOUR, BTC Wallet.')
input()
print(f'{Fore.WHITE} [{Fore.RED}!{Fore.WHITE}] {Fore.MAGENTA}Transferring Funds Into BTC Address: [{Fore.RED}{wallet}{Fore.LIGHTMAGENTA_EX}]..')
time.sleep(1)
print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.GREEN}SUCCESFULLY{Fore.WHITE} TRANSFERRED {Fore.RED}{btc_amount}{Fore.WHITE} , ( {Fore.LIGHTMAGENTA_EX}{btc_usd_amount} {Fore.LIGHTYELLOW_EX}$ {Fore.WHITE}) INTO BTC ADDRESS {Fore.WHITE}[{Fore.RED}{wallet}{Fore.WHITE}]!')
print(f'{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Closing CLAWZ Wallet Miner.')
exit(0)
