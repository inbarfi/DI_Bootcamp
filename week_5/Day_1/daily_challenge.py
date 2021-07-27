# -*- coding: utf-8 -*-
"""
@author: Inbar
"""

#w5_d1_daily challenge - Old MacDonald’s Farm
class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}
    def add_animal(self, animal_type, quantity = 1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
            print('print:', self.animals[animal_type])
        else: 
            self.animals[animal_type] = quantity
    def get_info(self):
        print(f"{self.name}'s Farm")
        for key, value in self.animals.items():
            print(f"{key}\t\t\t: {value}")
        print("\tE-I-E-I-0!")
    def get_animal_types(self):
        animals = list(self.animals.keys())
        animals.sort()
        return animals
    def get_short_info(self):
        return f"{self.name}'s farm has: {self.get_animal_types()}"


f1 = Farm("McDonald")
f1.add_animal('cow',5)
f1.add_animal('sheep')
f1.add_animal('sheep')
f1.add_animal('goat', 12)
f1.get_info()
print(f1.name)
print(f1.get_animal_types())
print(f1.animals)
print(f1.get_short_info())
 