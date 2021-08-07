# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:08:43 2021

@author: Inbar
"""

#w5_d4_daily_challenge

#1)
class Text: 
    def __init__(self, text):
        self.text = text.lower().replace("\n", " ")
        self.word_list = self.text.split(" ")
        self.all_words_count = {} 
        self._count_words() #_the first underscore indicates it shoudn't be available for the users,  class itself uses it.
    
    #class method
    @ classmethod    #automatically gets the class Text indise cls parameter
    def from_file(cls, file_path): 
        with open(file_path, "r") as f:
            file_contents = f.read()
        
        return cls(file_contents) 
        # same as: 
        # return Text(file_contents)
            
    
    def _count_words(self): #_the first underscore indicates it shoudn't be available for the users, class itself uses it.
        distinct_words = set(self.word_list)
        for word in distinct_words:
            self.all_words_count[word] = self.word_list.count(word)
    
    def get_frequency_of_word(self, word):
        return self.all_words_count[word].get(word) or 0 #with get code wont crush if word doesn't exist
    
    def get_most_common_word(self):
        biggest_entry = ('', 0)
        for entry in self.all_words_count.items():
            #entry[1] is count (the value in the dictionary)
            if entry[1] > biggest_entry[1]:
                biggest_entry = entry
                
        return biggest_entry
    
    def get_unique_words(self):            
        unique_words = []
        for entry in self.all_words_count.items():
            if [entry] == 1:
                unique_words.append(entry[0])
        return unique_words
            
        
        
        
            
t = Text("The sun is yellow, the sky is blue. I love you")
print(t.word_freq('the'))
print(t.word_freq('sun'))
print(t.common_word())

t = Text.from_file("")


#2)
#TextModification that inherits from Text
class TextModification(Text):
    super().__init__(text)
    self.word_list = self.remove_stopwords
    self.remove_special_chars()
    self._count_words()
    
    stopwords = ("ha", "the", "a", "an") #set (more efficient than a list) of example of stopwords in English
    special_chars = ("*", ".", ",")
    def remove_stopwords(self):
        return list(filter(lambda word: word not in self.stopwords, self.word_list))
                    #filter is a function that takes a function
    def remove_special_chars(self):
        for char in self.special_chars:
            self.text = self.text.replace(char, "")
        
t = TextModification.from_file("")
print(t.word_list)
print(t.remove_stopwords())

#the lambda is same as:
def is_not_a_stopword(self, word):
    if word not in self.stopwords: 
        return True
    return False

