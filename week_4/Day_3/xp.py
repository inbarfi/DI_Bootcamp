# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:29:53 2021

@author: Inbar
"""

#w4_d3_xp
# =============================================================================
# #1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# coverted_to_dict = dict(zip(keys, values))
# print(coverted_to_dict)
# =============================================================================
#2
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#print(type(family["rick"]))

# =============================================================================
# total_price = 0
# #or: 
# # for value in family.values():
# for key in family:
#     if family[key] < 3:
#         pay = 0
#         total_price += 0
#         print(f"you need to pay: {pay}$")
#     elif family[key] > 3 and family[key] < 12:
#         pay = 10
#         total_price += 10
#         print(f"you need to pay: {pay}$")
#     else: 
#         pay = 15
#         total_price += 15
#         print(f"you need to pay: {pay}$")
# print(f"Total price is: {total_price}$")
# =============================================================================

#Bonus: Ask the user to input the names and ages instead of 
#------
#using the provided family variable (Hint: ask the user for names and ages 
#and add them into a family dictionary that is initially empty).

#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# first input: ask for number of family memebers
# a while loop 
# second input: for each member ask for name and then third input: ask for age
# append names and ages to empty lists
# zip to lists to a dic

num_family_memebers = int(input("Hey, how many people are you?: "))
empty_names = []
empty_ages = []
members = 0
while members < num_family_memebers:
    members += 1
    name = input("what's your name? ")
    empty_names.append(name)
    age = int(input("what's your age? "))
    empty_ages.append(age)
family_dict = dict(zip(empty_names,empty_ages))
print(family_dict)







# =============================================================================
# #3
# brand = {
#     'name': 'Zara', 
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'], 
#     'number_stores': 7000,
#     'major_color': 
#         {'France': 'blue', 
#         'Spain': 'red', 
#         'US': ['pink', 'green']
#         }
#     }   
#     
# #print(brand["major_color"]["France"]) 
# brand['number_stores'] = 2
# print(brand["number_stores"])
# print(f"{brand['name']} clients are {brand['type_of_clothes'][0]} and {brand['type_of_clothes'][1]}")
# brand["country_creation"] = "Spain"
# print(brand["country_creation"])  
# if 'international_competitors' in brand.keys():
#     brand['international_competitors'].append('Desigual')
# print(brand['international_competitors'])
# del brand["creation_date"]
# #print(brand)
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(brand.keys())
# 
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
#     }
# print(more_on_zara)
# 
# 
# brand.update(more_on_zara)
# print(brand)
# print("number_stores on brand updated to the one of more_on_zara value")
#
# =============================================================================
#4.1
#users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
#num1 = list(range(0,5))
#print(num1)
#print(dict(zip(users,num1)))
#for loop:
# =============================================================================
# empty_dict = {} #find a way to solve with enumerate
# for item in enumerate(users):
# =============================================================================
# =============================================================================
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# empty_dict = {}
# for character in users:
#     empty_dict[character] = users.index(character)    
# #print(empty_dict)
# =============================================================================
          
#4.2
# =============================================================================
# empty_dict2 = {}
# for character in users:
#     empty_dict2[users.index(character)] = character    
# print(empty_dict2)
# =============================================================================
          
# =============================================================================
# #4.3
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# users_sorted = sorted(users)
# empty_dict = {}
# for character in users_sorted:
#     empty_dict[character] = users_sorted.index(character) 
# print(empty_dict)
#           
# =============================================================================

          

          
