# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:54:17 2021

@author: Inbar
"""

#w5_d3_xp
#1 - Built-In Functions & __doc__
# a program which prints the results of the following python built-in functions: 
# abs(), int(), input()

def result():
    '''
    function takes a user input, and because data from input is recieved as string the int() function casts it into an integer, finally the abs() function returns the absolute value of the negative int
    '''
    user_inp = int(input('enter negtive number: '))
    print(f'Absolute value of  {user_inp}  is: {abs(user_inp)}')

result()
print(result.__doc__)


#2

class Currency:
    def __init__(self, coin, value):
        self.coin = coin
        self.value = value
        
    def str(self):
        return f'{self.value} {self.coin}s'
    
    def int(self):
        return self.value
    
    def repr(self):
        return f'{self.value} {self.coin}s'
    
    def __add__(self, other_num):
        if isinstance(other_num, Currency):
            if self.coin == other_num.coin:
                 return self.value + int(other_num)
            else:
                raise TypeError('Cannot add between different Currency types')
        else:
            return self.value + int(other_num)

    def __iadd__(self, other):
        self.value += int(other)
        return self
    
    
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)
    


    