# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:25:55 2021

@author: Inbar
"""

#w4_d3_daily_challenge - cryptography
user_input = int(input("for encryption press 1, for decryption press 2: "))

print(f"Alright!. let's start!")
text = input(f"write a word: ").lower()
cypher_text = ""
shift = 3 
for letter in text:
    if user_input == 1: #encryption
        if ord(letter) <= 122 - shift:
            cypher_text += chr(ord(letter) + shift)
        else: 
            cypher_text += chr(ord(letter) + shift -122-1 + 97)
            #pass #insert execution
    else: #decryption
        if ord(letter) >= 97 + shift:
             cypher_text += chr(ord(letter) - shift)
        else: 
            cypher_text += chr(ord(letter) -shift + 122+1 - 97)
            #pass #insert execution
print(cypher_text)
        

# a-z is 97-122
# =============================================================================
#      ord(letter) + shift -122 + 97
#      ord(letter) -shift + 122 - 97
# =============================================================================
