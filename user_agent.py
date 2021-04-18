#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/Cicadadenis/

import sys, time, socket, random, requests
from os import system
import os, sys, time, socket, random, requests


baner = ("""


		                                            _   
		 _   _ ___  ___ _ __  __ _  __ _  ___ _ __ | |_ 
		| | | / __|/ _ \ '__|/ _` |/ _` |/ _ \ '_ \| __|
		| |_| \__ \  __/ |  | (_| | (_| |  __/ | | | |_ 
	         \__,_|___/\___|_|___\__,_|\__, |\___|_| |_|\__|
		                           |___/                

				CICADA_3301
				   2021	
			
""")


def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
	
	
__all__ = ["replace_placeholders", "user_agent"]

from faker import Faker

faker = Faker()

user_agent = faker.user_agent()
print(baner)
print("\n"  + 	">>>>>>    " +  user_agent  + "     <<<<<<" +  "\n" + "\n >>>>> Нажми Enter для герерации   \n \n >>>>> Чтоб выйти cntr+z \n\n")

input()

os.system("clear")
restart_program()
