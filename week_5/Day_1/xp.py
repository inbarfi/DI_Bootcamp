# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:58:31 2021

@author: Inbar
"""

#w5_d1_xp
#1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Roger", 4)
print(cat1.name)
cat2 = Cat("Ragina", 5)
cat_list = [cat1, cat2]
def find_oldest(cat_list):
    max_age = max(cat1.age, cat2.age)
    for cat in cat_list:
        if max_age == cat.age:
            return f"Oldest cat name is {cat.name}, and is {max_age} years old."


print(find_oldest(cat_list))   

#2
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        return f"{self.name} goes woof!"
    def jump(self):
        return f"jumps {self.height*2} cm high!"
davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height, "cm")

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.bark(), "and", sarahs_dog.jump())

def highest_dog():
    max_height = max(davids_dog.height, sarahs_dog.height)
    for dog in [davids_dog, sarahs_dog]:
        if max_height == dog.height:
            return(f"{dog.name} is {max_height} cm high")
    
print(highest_dog())     
#or shortly:
biggest_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name
print(biggest_dog)
        
        
#3
class Song():
    def __init__(self, lyrics): #lyrics is a list
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
        
stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#print(type(stairway)) #class '__main__.Song'
# How can I join stairway? join doesn't work, as stairway isn't a list
#print(''.join(stairway)) # doesn't work

print(stairway.sing_me_a_song()) #why returns none at the end?
#stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]).sing_me_a_song()

# 4
from itertools import groupby
from operator import itemgetter

class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        self.new_animal = new_animal
        if self.new_animal not in self.animals:
            self.animals.append(self.new_animal)
        else:
            print(f"{self.new_animal} is already in the Animals list")
    def get_animals(self):
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} not in the list")
# =============================================================================
#     #continue
#     def sort_animals(self):
#         sorted_animals = sorted(self.animals)
#         for sorted_animals[0] in sorted_animals:
# =============================================================================
    #review:        
    def sort_animals(self):
        new_dict = {}
        self.animals.sort()
        x = [list(word) for letter, word in groupby(self.animals, key=itemgetter(0))]
        for index, word in enumerate(x):
            if len(word) < 2:
               word = "".join(word)
            new_dict[index + 1] = word
        print(new_dict)
        return new_dict
    
    def get_groups(self):
        d = self.sort_animals()
        for animal in d.values():
            print(animal)
            
ramat_gan_safari = Zoo('Ramat gan')
ramat_gan_safari.add_animal('Panda')
ramat_gan_safari.add_animal('Leopard')
ramat_gan_safari.add_animal('hypo')
ramat_gan_safari.add_animal('pinguin')
ramat_gan_safari.add_animal('elephant')
ramat_gan_safari.add_animal('baboon')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('monkey')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()




