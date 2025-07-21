"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""

from Food_utilities import read_foods

fh = open("foods.txt", "r")

items = read_foods(fh)

for each in items:
    print(each)
    print()