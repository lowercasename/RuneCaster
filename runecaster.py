#!/usr/bin/env python

import math
from halo import Halo
from jsonrpcclient import request

APIKey = '' # Paste your RANDOM.ORG API key here

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

spinner = Halo(text='Casting...', spinner='dots')

class color:
   PURPLE = '\033[35m'
   CYAN = '\033[36m'
   DARKCYAN = '\033[46m'
   BLUE = '\033[34m'
   GREEN = '\033[32m'
   YELLOW = '\033[33m'
   RED = '\033[31m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[2m'
   END = '\033[0m'

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))  
       if 1 <= userInput <= 24:
          return userInput
          break
       else:
          print(color.RED + 'You can cast between 1 and 24 runes.' + color.END)    
          continue 
    except ValueError:
       print(color.RED + "Please enter a number." + color.END)
       continue

runes = ["\u16A0 Fehu","\u16A2 Uruz","\u16A6 Thurisaz","\u16AB Ansuz","\u16B1 Raido","\u16B2 Kenaz","\u16B7 Gebo","\u16B9 Wunjo","\u16BA Hagalaz","\u16BE Nauthiz","\u16C1 Isaz","\u16C3 Jera","\u16C7 Eihaz","\u16C8 Pertho","\u16C9 Algiz","\u16CA Sowilo","\u16CF Teiwaz","\u16D2 Berkana","\u16D6 Eihwaz","\u16D7 Mannaz","\u16DA Laguz","\u16DC Ingwaz","\u16DF Othala","\u16DE Dagaz"]

print('\n' + color.PURPLE + 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ' + color.END)
print(color.PURPLE + 'Ｗｅｌｃｏｍｅ ｔｏ ＲｕｎｅＣａｓｔｅｒ' + color.END)
print(color.PURPLE + 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ' + color.END + '\n') 

cast = True

while cast:

    if APIKey == '':
        print(color.RED + 'Error: No API key found' + color.END)
        print(color.RED + 'Please paste your RANDOM.ORG API key into the runecaster.py file (see README.md for instructions)' + color.END)
        break
    
    number_of_runes = inputNumber('How many runes do you require? ')
    
    spinner.start()
    
    response = request('https://api.random.org/json-rpc/2/invoke', 'generateIntegers', apiKey=APIKey, n=number_of_runes, min='1', max='24', replacement=False)
    
    spinner.stop()
    
    print ("\n" + color.BOLD + "Your runes" + color.END)
    
    for i in response.data.result['random']['data']:
        print(runes[i-1])

    cast_again = input("\n"  + color.GREEN + "Would you like to cast again? [Y/n] " + color.END).lower()
    
    if cast_again in no:
        cast = False