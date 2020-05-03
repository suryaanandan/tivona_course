# Question 5

import collections
import re
class  Linguist(object):
    
    # about_given_string dict to store all the details about given string
    about_given_string = {}

    def __init__(self, testing_string, length = "", total_words= "", total_unique_words = "", total_characters = "", total_unique_characters = ""):
        self.testing_string = testing_string
        self.length = length
        self.total_words = total_words
        self.total_unique_words = total_unique_words
        self.total_characters = total_characters
        self.total_unique_characters = total_unique_characters

    def analyze_text (self, testing_string):
        """Module level function to compute length, total_words, total_unique_words, total_characters, total_unique_characters of given string

        """    
        self.length = len(self.testing_string)
        self.total_words = (self.testing_string).split()
        self.total_unique_words = set(self.total_words)

        self.total_characters = (int)(0)
        for ch in self.testing_string :
            if(ch.isspace() != True):
               self.total_characters = self.total_characters + 1 

        self.total_unique_characters = set(self.testing_string)
        
        Linguist.about_given_string["Length"] = self.length
        Linguist.about_given_string["Total_words"] = len(self.total_words)
        Linguist.about_given_string["Total_unique_words"] = len(self.total_unique_words)
        Linguist.about_given_string["Total_characters"] = self.total_characters
        Linguist.about_given_string["Total_unique_characters"] = len(self.total_unique_characters)

    def is_english (self, testing_string):
        """Module level function return true if text contain english characters only otherwise return false

        """   
        try:
            self.testing_string.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True

    def __str__(self):
        key_list = ("Length", "Total_words", "Total_unique_words", "Total_characters", "Total_unique_characters")

        for list_item in key_list :
            print("\n{} = {}".format(list_item, Linguist.about_given_string[list_item]))  
            

name = input("Enter a string : ")
name = name.upper()
linguist_obj = Linguist(name)
linguist_obj.analyze_text(name)
linguist_obj.__str__()
contain_english_only = linguist_obj.is_english(name)
print("\nText contains only English characters : {}".format(contain_english_only))
