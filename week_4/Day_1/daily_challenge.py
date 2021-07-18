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

#3 - 
print(f"{user_input[0]} \n{user_input[1]} \n{user_input[2]} \n{user_input[3]} \n{user_input[4]}")

print("Or:")
for i in user_input:
    user_input = i
    print(user_input)
    
    
    
#4
import random
inbar = "inbar"
inbar_list = list(inbar)
print(inbar_list)

random.shuffle(inbar_list)
print(inbar_list) #shuffled

#change the list to a str:
shaufle_inbar = "".join(inbar_list)
print(type(shaufle_inbar))
print(shaufle_inbar)




















