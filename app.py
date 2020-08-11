# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:00:24 2020

@author: Supriyo
"""
#import math
#print(math.fabs(2.9));

#is_hot= False
#is_cold=False
#
#if is_hot:
#    print("Very Hot day")
#    print("Drin water")
#elif is_cold:
#    print("very cold day")
#    print("Wear arm clothes")
#else:
#    print("It is  a lovely day")

#price= 10000
#has_credit=True
#if has_credit:
#    down_payment= 0.1* price
#else:
#    down_payment=0.2* price
#print(f"Downpayment is: ${down_payment}")

#name ="Jesikalabaromi"
#if len(name) <3:
#    print("Name must be atleast 3 characters")
#elif len(name) >10:
#    print("name must be max 5 characters")
#else:
#    print("Name is fine")

#weight= int(input('weight'))
#unit = input('(L)bs or (K)g: ')
#
#if unit.upper() =="L":
#    converted = weight *0.45
#    print(f"You are {converted} kilos")
#else:
#    converted = weight /0.45
#    print(f"You are {converted} pounds")

#guess number

secret_number=10
guess_count=0
guess_limit=3
while guess_count < guess_limit:
   guess = int(input('Guess :'))
   guess_count +=1
   if guess == secret_number:
       print('You re winner')
       break
else:
    print('Sorry you have failed')



























