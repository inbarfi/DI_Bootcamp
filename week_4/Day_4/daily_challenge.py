# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:14:33 2021

@author: Inbar
"""

#w4_d4_daily_challenge
my_matrix = [['7','i','3'], ['T','s','i'], ['h','%','x'], ['i',' ','#'], ['s','M', ' '], ['$', 'a', ' '], ['#','t','%'], ['^','r','!']]

empty_list = []
print(len(my_matrix)) #8 - number of rows i
print(len(my_matrix[0])) #3 - number of columns j


def find_letters_in_matrix(insert_matrix):
    flag = 0             
    for j in range(len(my_matrix[0])):
        for i in range(len(my_matrix)):
             if my_matrix[i][j].isalpha() and flag == 1:
                 empty_list.append(' ')
                 empty_list.append(my_matrix[i][j])     
                 flag = 0
             elif my_matrix[i][j].isalpha():
                 empty_list.append(my_matrix[i][j])
             elif not my_matrix[i][j].isalpha() and not my_matrix[i][j].isnumeric():
                 flag = 1
                
        
    result = print(''.join(empty_list))
    return result

find_letters_in_matrix(my_matrix)




