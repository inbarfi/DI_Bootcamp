# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:10:06 2021

@author: Inbar
"""

#w4_d1_daily_challenge

user_input = input("type in a string 10 or more characters: ")
user_input_length = len(user_input)
if user_input_length < 10:
    print('string not long enough')
elif user_input_length > 10:
    print('string too long')


#2
print(f"first character is: {user_input[0]}, last is: {user_input[-1]}")

#3 - why does it print it weirdly?
print(f"{user_input[0]} \n {user_input[1]} \n {user_input[2]} \n {user_input[3]} \n {user_input[4]}")

# =============================================================================
# #4
# import random
# inbar = "inbar"
# inbarr = list(inbar)
# print(inbarr)
# #print(random.shuffle(inbarr))
# =============================================================================

