"""
-------------------------------------------------------
Assignment 1 Task 4
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
from functions import file_analyze

fv = open('testing.txt', 'r')
upp, low, dig, whi, rem = file_analyze(fv)
print(upp, low, dig, whi, rem)