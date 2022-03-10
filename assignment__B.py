#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:16:34 2022

@author: Or Tzadok
"""

def reverse(sentence, reverse_word):
    if type(reverse_word) != str:
        return "invalid input"
    if sentence.find(reverse_word) == -1:
        return "The word was not found"
    return(sentence.replace(reverse_word, reverse_word[::-1],1))
                
          
print(reverse("I like apples and I also like bananas", "like")) 
print(reverse("I like apples and I also like bananas", "oranges"))
print(reverse("I like apples and I also like bananas", "Bananas")) 
print(reverse("I like apples and I also like bananas", 3)) 
