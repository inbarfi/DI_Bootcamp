# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:54:00 2021

@author: Inbar
"""

#w4_d2_Daily_challenge

#27/01/1993
user_birthday = input("when's your bday? in this format of DD/MM/YYYY: ")
current_year = 2021
#calculate user age:
#first, extract year from input
user_year = user_birthday[-4:]
user_year_int = int(user_year)
print(user_year)
age = current_year -  user_year_int
print(age)
last_num = str(age)[-1]
print(last_num)
print(type(last_num)) #str
last_num_int = int(last_num)
#print(last_num_int * 'i')
print(f"""             ___{last_num_int * 'i'}___
              |:H:a:p:p:y:|
            __|___________|__
           |^^^^^^^^^^^^^^^^^|
           |:B:i:r:t:h:d:a:y:|27/01/1993
           
           |                 |
           ~~~~~~~~~~~~~~~~~~~""")
