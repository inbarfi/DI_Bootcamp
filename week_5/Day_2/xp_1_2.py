# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:03:51 2021

@author: Inbar
"""

#w5_d2_xp
# =============================================================================
# #1
# 
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
# 
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
# 
# class Cat():
#     is_lazy = True
# 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def walk(self):
#         return f'{self.name} is just walking around'
# 
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# 
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#     
# #another cat bread
# class Persian(Cat):
#     def miau(self):
#         return f"{self.name} says: Miau!"
# 
#     #def fur(self, color):
#         #return self.color
#     
# c1 = Persian("mishmish", 3)
# print(c1.miau())
# c2 = Bengal("madona", 2)
# print(c2.name)
# my_cats = [c1, c2]
# my_pets = Pets(my_cats)
# print(my_pets.walk())  
# =============================================================================

#2
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking: waf!"
    def run_speed(self):
        return self.weight/self.age*10
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} won!"
        else:
            return f"{other_dog.name} won!"
    
dog1 = Dog('Rex', 1, 5)
dog2 = Dog('Pit', 4, 20)
dog3 = Dog('Duzo', 12, 6)
print(dog1.name)
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
#3 - new file





