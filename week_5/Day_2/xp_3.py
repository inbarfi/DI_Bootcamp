# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:29:55 2021

@author: Inbar
"""

#w5_d2_xp 
# 3
from xp_1_2 import Dog
from random import choice

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False): #adding trained
        super().__init__(name, age, weight)
        self.trained = trained
    #train method: prints the output of bark and switches the trained boolean to True
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *args):
        print(f'{self.name}, {", ".join(args)} all play together!')
    def do_a_trick(self):
        tricks_list = ['does a barrel roll','stands on his back legs','shakes your hand','plays dead']
        if self.trained == True:
            print(f'{self.name} {choice(tricks_list)}')
        else:
            print(f"This dog {self.name} isn't trained")
            
dog1 = PetDog('Puppy', 5, 10)
dog2 = PetDog('Blacky', 10, 20)
dog3 = PetDog('Toby', 15, 30)
print(dog1.train())
dog1.play(dog2.name, dog3.name) 
dog3.do_a_trick()


