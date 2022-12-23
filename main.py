import requests
import random
import os
import time
from colorama import Fore
from pystyle import *
def check():
  os.system('cls')
  print(Colorate.Horizontal(Colors.blue_to_purple, """
  _   __          _ __         _______           __          
 | | / /__ ____  (_) /___ __  / ___/ /  ___ ____/ /_____ ____
 | |/ / _ `/ _ \/ / __/ // / / /__/ _ \/ -_) __/  '_/ -_) __/
 |___/\_,_/_//_/_/\__/\_, /  \___/_//_/\__/\__/_/\_\\__/_/   
                     /___/                                   


 """, 1))
  while True:
    proxie = open('proxies.txt', 'r').read().splitlines()
    prox = random.choice(proxie)
    proxies = {'http://': f'http://{prox}', 'https://': f'http://{prox}'}
    #invite = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz1234567890')) for x in range(2))
    vanitys = open("vanitys.txt")
    invite = random.choice(vanitys.read().splitlines())
    vanitys.close()
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language': 'en-US,en;q=0.9',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'none',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
  }
  
    r = requests.get(f'https://discord.com/api/v9/invites/{invite}', headers=headers, proxies=proxies)
    if r.status_code == 404:
      print(Fore.RESET + Fore.GREEN + f"Available: {invite}")
      with open("available.txt", "a") as f:
        f.write("discord.gg/" + invite + "\n")
      time.sleep(1111.1)
      
    if r.status_code == 200:
      print(Fore.RESET + Fore.RED + f"Taken: {invite}") 






check()
