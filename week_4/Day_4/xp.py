# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:27:03 2021

@author: Inbar
"""

#w4_d4_xp
#part 1
# =============================================================================
# #1
# def display_message():
#     return "I'm learning Python"
# 
# print(display_message())
# 
# #2
# def favorite_book(title):
#     return f"One of my favorite books is {title}"
# 
# print(favorite_book('Harry Potter'))
# 
# #3
# def describe_city(city, country):
#     return f"{city} is in {country}"
# print(describe_city('TLV', 'Israel'))
# 
# #4
# import random
# def check_numbers(num):
#     if num <= 100 and num >= 1:
#         random_num = random.randint(1,101)
#         print(random_num)
#         if num == random_num:
#             return "same num"
#         else: return "not same num"
# 
# print(check_numbers(2))
# =============================================================================
# =============================================================================
# #5 
# 
# def make_shirt(size = 'large', text = "I love Python"):
#     
#     return (f"size is: {size.lower()}, text is: {text}")
# 
# print(make_shirt(text='hello'))
# #Using Keyword Argumwents:
# print(make_shirt(size='S', text='hello'))
# 
# #using **args
# def make_shirt(*args): #size, text
#     if args[0].lower() == 'm' or 'l':
#         return (f"size is: {args[0]}, text is: {args[1]}")
# 
# # =============================================================================
# =============================================================================
# #6 return a list of the magician names
# magicians_names = ["Dambeldor", "Biatris", "Potter"]
# def show_magicians(magicians_names):
#     empty_list = []
#     for name in magicians_names:
#         
#         empty_list.append(name)
#     return empty_list
# 
# #y = show_magicians(magicians_names) save the return to a variable
# show_magicians(magicians_names)
# 
# def make_great(magicians_names):
#     empty_list_2 = []
#     for name in magicians_names:
#         #print("The great", name)
#         empty_list_2.append(f"The great {name}")
#     return empty_list_2
# print(make_great(magicians_names))
# =============================================================================
# #part 2
# =============================================================================
# # 7 - When Will I Retire ?
# #  67 for men, and 62 for women (born after April, 1947)
# # Return True if the person can retire, and False if he/she can’t
# def get_age(): #return the age
#     current_year = 2021
#     user_birth_year = int(input("what year were you born? "))
#     age = current_year - user_birth_year
#     return age #f"your age is: {age}"
#     
# #print(get_age(1993, 1, 27))
# #get_age(1993, 1, 27) 
# 
# def can_retire(gender, my_age): #call the get_age function
# #or using one paremeter and assigning my_age =  get_age()
#     if my_age >= 67:
#         return True #"can retire"
#     else:
#         if gender.lower() == "female" and my_age >=60:
#           return True #"can retire"
#         else: 
#          return False #"can't retire"
#          
#         
# print(can_retire("female", get_age()))
# =============================================================================

# =============================================================================
# #8
# # a function that accepts one parameter (an int: X) and 
# # returns the value of X+XX+XXX+XXXX. 
# 
# def calculate_method():
#     inp = input("write a number between 1-9: ")
#     print(int(inp) + int(inp * 2) + int(inp * 3) + int(inp * 4))
#     
# calculate_method()
# =============================================================================




