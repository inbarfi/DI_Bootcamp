# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:27:28 2021

@author: Inbar
"""
#Class_exercise 
user_number = int(input('choose a number between 1 t0 100: '))
if user_number % 3 == 0 and user_number % 5 == 0:
    print('FizzBuzz')
elif user_number % 3 == 0 :
    print('Fizz')
elif user_number % 5 == 0:
    print('Buzz')



#W4_D1_XP

#1
print('Hello World' +'\n' + 'Hello World' +'\n' + 'Hello World' +'\n' + 'Hello World' +'\n')
print('Hello World ' '\n' * 4)

#2
print((99^3) * 8)

#3 
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
#print("3" > 3) #'>' not supported between instances of 'str' and 'int'
print("Hello" == "hello") #False

#4
computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer")

#5
name = "Lori"
age = 24
shoe_size = 37
info = f"I'm {name}, I'm {age} years old..."
print(info)

#6 
a = 5
b = 4
if a > b :
    print('hello world')

#7
input_num = int(input('type in a number: '))
if input_num % 2 == 0:
    print('even')
else: 
    print('odd')


#8 
fun_name = "inbar"
name = input('what\'s your name?: ')
if fun_name == name:
    print('funny! I got the same name here!')
else: print('na, not the same name :\(')

#9
height = int(input('whats your height in inches?: '))
height_cm = height * 2.54
print(f"your height in cm is: {height_cm}")
if height_cm > 145:
    print("tall enough to ride")
else: print("need to grow some more to ride")

