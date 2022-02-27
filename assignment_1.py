#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:04:42 2022

@author: Or Tzadok

"""
#a
#Python Program to Check If a String Is a Number (Float)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#math function

def my_func(x1, x2, x3):
    
    for num in (x1 ,x2 ,x3):
        if not isfloat(num): #check if float
            return("Error: parameters should be float") 
    s = x1+x2+x3
    if  s == 0 : #check if possible to calculate
        return("Not a number – denominator equals zero")
    else:
        return((s*(s-x1)* x3) / s) #calc
    

#b

def convert(hours, minutes):
    for hm in (hours, minutes):
        if not isfloat(hm): #check if float
            return("input error") 
    return(hours*3600 + minutes*60)