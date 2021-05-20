#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/Cicadadenis/
from threading import Thread
from random import randint
import asyncio
import sys, time, socket, random, requests
from os import system
import os, sys, time, socket, random, requests
from my_fake_useragent import UserAgent
import requests
import time
import colorama
import os
import threading
import urllib.request
import zipfile
import random
import datetime
import sys
import re
import json
from colorama import Fore, Back
from threading import Thread
from random import randint
import asyncio
from requests import get
def mask(str, maska):
    if len(str) == maska.count('#'):
        str_list = list(str)
        for i in str_list:
            maska=maska.replace("#", i, 1)
        return maska0




def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
print("     💎 User Agent 💎    ")
print("  🌟 Developer Cicada 🌟 ")
print(" ⚙️ support: @Satanasat ⚙️")
time.sleep(1)
  

print("     1️⃣  ANDROID ✅")
print("     2️⃣  WINDOWS ✅")
print("     3️⃣   Linux  ✅")
print("     4️⃣    MAC   ✅")
print("     5️⃣    IOS   ✅")


while True:
        try:
            
            den = input("✴️ Выбери устройстра 📱💻🖥 ▶️▶️▶️")
            thr = int(input("✴️ Введите количество ▶️▶️▶️ ")) 

            
            if den == "1":
                def android(counet):
                    ua = UserAgent(os_family = 'android')
                    res = ua.random()
                    print('🔴', res, '🔴')
                for i in range(thr):
                    t = threading.Thread(target= android, args=(i, ), )
                    try:
                        t.start()
                        print(f"user-agent {i} 📌 получен!")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка <{e}> user-agent `{i}`")
                        android()
                print("\n\n 🎉🎉🎉🎉   Выполнено   🎉🎉🎉🎉 \n\n")

                sys.exit(1)
                
                
            elif  den == "2":
                def WINDOWS(counet):
                    ua = UserAgent(os_family = 'windows')
                    res = ua.random()
                    print('🔴', res, '🔴')
                    time.sleep(1)
                for i in range(thr):
                    t = threading.Thread(target= WINDOWS, args=(i, ), )
                    try:
                        t.start()
                        print(f"user-agent {i} 📌 получен!")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка <{e}> user-agent `{i}`")
                        WINDOWS()
                print("\n\n 🎉🎉🎉🎉   Выполнено   🎉🎉🎉🎉 \n\n")
                sys.exit(1)
                
                
            elif  den == "3":
                def Linux(counet):
                    ua = UserAgent(os_family = 'linux')
                    res = ua.random()
                    print('🔴', res, '🔴')
                    time.sleep(1)
                for i in range(thr):
                    t = threading.Thread(target= Linux, args=(i, ), )
                    try:
                        t.start()
                        print(f"user-agent {i} 📌 получен!")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка <{e}> user-agent `{i}`")
                        Linux()
                print("\n\n 🎉🎉🎉🎉   Выполнено   🎉🎉🎉🎉 \n\n")
                sys.exit(1)
                
                
                
            elif  den == "4":
                def MAC(counet):
                    ua = UserAgent(os_family = 'mac')
                    res = ua.random()
                    print('🔴', res, '🔴')
                    time.sleep(1)
                for i in range(thr):
                    t = threading.Thread(target= MAC, args=(i, ), )
                    try:
                        t.start()
                        print(f"user-agent {i} 📌 получен!")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка <{e}> user-agent `{i}`")
                        MAC()
                print("\n\n 🎉🎉🎉🎉   Выполнено   🎉🎉🎉🎉 \n\n")
                sys.exit(1)
                
                
            elif  den == "5":
                def IOS(counet):
                    ua = UserAgent(os_family = 'ios')
                    res = ua.random()
                    print('🔴', res, '🔴')
                    time.sleep(1)
                for i in range(thr):
                    t = threading.Thread(target= IOS, args=(i, ), )
                    try:
                        t.start()
                        print(f"user-agent {i} 📌 получен!")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка <{e}> user-agent `{i}`")
                        IOS() 
                print("\n\n 🎉🎉🎉🎉   Выполнено   🎉🎉🎉🎉 \n\n")
                sys.exit(1)

        except Exception as e:
            print("\n⚠️ ОШИБКА ⚠️ "+e)





restart_program()

