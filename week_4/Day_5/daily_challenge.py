# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:37:51 2021

@author: Inbar
"""

#w4_d5_daily_chaallenge

#accepts a comma separated sequence of words as input and prints 
#the words in a comma-separated sequence after sorting them alphabetically.

# =============================================================================
# #using sort function:
# def sort_this_sequence():
#     user_seq = input("write a sentence, seperate each word with a comme: ")
#     print(type(user_seq))
#     user_seq_list = user_seq.split(',')
#     user_seq_list.sort()
#     return ', '.join(user_seq_list)
# 
# #cat,banana,ariel
# print(sort_this_sequence())
# =============================================================================

#a = input("asdasd:")
#list_words = a.split(',') # split input:
list_words = ['dodo', 'anvil', 'jax', 'thor', 'yondle','JAX', 'alfred', 'aadf', 'abad']
#list_words = ['cba', 'cab', 'aab', 'ab','aaa']
#list_words = ['aaaa', 'aab', 'aaa']
#print(list_words[0][0])

def switch(item1, item2, index):
    if item1[index] < item2[index]:
        return item2, item1
           
    elif item1[index] == item2[index] and index+1 < len(item1) and index+1 < len(item2):
        item1, item2 = switch (item1, item2, index +1)
    
    return item1, item2
    


def sort(lst):
    index = 0
    for i in range(len(lst)):
        for j in range(len(lst)):         
               lst[i], lst[j] = switch(lst[i].lower(), lst[j].lower(), index)
             
         

sort(list_words)
print(list_words)


#user_seq = input("write a sentence, seperate each word with a comme: ")
# =============================================================================
# empty_list = []
# x = list(user_seq[0])
# xx = ''.join(x)
# print(xx)
# #min_letter = min(ord(xx))
# print(ord(xx))
# 
# =============================================================================


# =============================================================================
# #numerical representation of each letter 
# key = []
# #print(word[-1][-1])
# print(user_seq.split(','))
# for word in list(user_seq.split(',')):
#     empty = []
#     for letter in word:
#         #print(letter)
#         empty.append(ord(letter))
#         #print(empty)
#     key.append(empty)
#         
# print("key:", key)
# 
# def my_sort(my_key):
#     for index in range(len(key)):
#         for index2 in range(len(key)):
#             if key[index] < key[index2]:
#                 key[index],key[index2] = key[index2],key[index]
#             #if key[index] == key[index2]:
#                 
#                     
#     print(key)
# ef,ab,cd
# =============================================================================





# using reduce to get one output
# =============================================================================
# from functools import reduce
# 
# def min_ord():
# =============================================================================  
#using List Comprehension   
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       