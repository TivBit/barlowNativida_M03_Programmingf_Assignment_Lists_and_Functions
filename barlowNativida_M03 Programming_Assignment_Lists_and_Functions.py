# -*- coding: utf-8 -*-
"""
Created on %(Date: 05 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M03 Programming Assignment - Lists and Functions
"""

############################################################################
#This program is designed to print out a list of things.  Some items on
#the list are to print out capitalized.

things = ['mozzarella', 'cinderella', 'salmonella']
print(things)
for i in range(len(things)):
    things[i] = things[i].upper()
print(things[1])
for i in range(len(things)):
    things[i] = things[i].upper()
    print(things[0])
for i in range(len(things)):
    things[i] = things[i].upper()
print(things[2])

print()

############################################################################
#This program is designed to define a function and then print out the names
#on a list when the function "good" is called.

names = ['Harry', 'Ron', 'Hermione']

def good():
    print (names)

good()

print()

############################################################################
#This program is designed with a generator function that returns the odd numbers
#from range(10). Use a for loop to find and print the third value returned.


def odd_numbers( max=0 ):
   n = 1
   while n < max:
       yield 1 * n
       n += 2

a = odd_numbers(10)

for i in a:
   print(i)

############################################################################
