# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:38:20 2021

@author: Inbar
"""

#w4_d2_xp
# =============================================================================
# #1
# my_fav_numbers = {1,4,7}
# new = {5,8}
# my_fav_numbers.update(new)
# print(my_fav_numbers)
# r = my_fav_numbers.remove(max(my_fav_numbers))
# print(my_fav_numbers)
# friend_fav_numbers = {0}
# our_fav_nums = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_nums)
# 
# #2 
# # no - tuples are immutable
# 
# #3
# #for num in range(1:21): #syntax error
# for num in range(21):
#     print(num)
# 
# #4
# i = 1
# while i < 5:
#     i += 0.5
#     print(i)
#     
# #5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# print(basket)
# 
# basket.append("Kiwi")
# print(basket)
# basket.insert(0,"Apples")
# print(basket)
# print(basket.count("Apples"))
# print(dir(basket))
# basket.clear()
# print(basket)
# 
# #6
# user_name = input("what's your name?")
# while user_name != "Inbar": 
#     user_name = input("what's your name?")
# #without repeating user_name:
# while True:
#     user_input = input("what's your name?")
#     if user_input == "Inbar":
#         break
#     
# =============================================================================
# =============================================================================
# #7
# list_num = list(range(0,10))
# print(list_num)
# for i in list_num:
#     if i%2==0:
#         print(i)
#         
# #8
# list_num2 = list(range(1500,2500))
# # checking: list_num2 = [35,50]
# for i in list_num2:
#     if i % 5 == 0 and i % 7==0:
#         print(i)
# =============================================================================
# =============================================================================
# 
# #9 Favorite Fruits
# user_fruits = input("what are your favorite fruit(s)? seperated by one space: ")
# #print(list(user_fruits))
# user_fruits_list = list(user_fruits.split(" "))
# print(user_fruits_list)
# another_fruit = input("name anoher fruot you like: ")
# if another_fruit in user_fruits_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else: 
#     print("You chose a new fruit. I hope you enjoy")
# =============================================================================

# =============================================================================
# #10 vWho Ordered A Pizza ?
# active = True
# pizza = []
# #"".join(pizza)
# 
# while active: 
#     toppings = input("Please enter pizza topings (enter 'quit' when you are finished): ")
#     if toppings == 'quit':
#         active = False
#     else:
#         print("You chose:", toppings)
#         pizza.append(toppings)
# 
# pizza = ' '.join(pizza)
# print(f"you chose all these toppings:{pizza} total price is: {2.5*len(pizza)}$")
# 
# =============================================================================

#11: Cinemax
# =============================================================================
# x = "inbar fi"
# print(list(x.split(" ")))
# [int(x) for x in input().split()]
# =============================================================================
# =============================================================================
# ages = input("type family memmbers ages: ")
# ages_list = list(ages.split(" "))
# print(ages_list)
# total_price = 0
# for age in ages_list:
#     if int(age) < 3:
#         total_price += 0
#     elif int(age) > 3 and int(age) < 12:
#         total_price += 10
#     elif int(age) > 12:
#         total_price += 15
#     print(f"total price is: {total_price}")
# =============================================================================
        
# =============================================================================
# #12 Who Is Under 16?
# names = ["Rony", "Amy", "Shai"]
# empty = []
# for name in names:
#     age = int(input("what's your age?"))
#     print(len(names))
#     if age < 16:
#         continue
#         #names.remove(name) #it will iterate over the new reduced list
#         
#     else: #continue
#         empty.append(name)
#     print(empty)
# =============================================================================

# =============================================================================
# #13 & 14
# sandwich_orders = ["Slopijoe", "Tuna", "Omlet", "Hotdog"]
# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     finished_sandwiches += sandwich_orders
#     print(f"I made your {sandwich} sandwich!")
# 
# pastrami_num = sandwich_orders.count('pastrami')
# print("pastrami is in the list", pastrami_num, "times")
# if pastrami_num == 0:
#     sandwich_orders += (['pastrami'] * 3)
# elif pastrami_num == 1:
#     sandwich_orders += (['pastrami'] * 2)
# elif pastrami_num == 2:
#     sandwich_orders += (['pastrami'] * 1)
# print(sandwich_orders)
# print(pastrami_num)
# #check num of pastrami now:
# pastrami_num = sandwich_orders.count('pastrami')
# print(pastrami_num)
# 
# print("Deli has run out of pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#     print(sandwich_orders)
# =============================================================================

    
    
    
    
    
    
    
    
    
    
    
    
    
    





    
