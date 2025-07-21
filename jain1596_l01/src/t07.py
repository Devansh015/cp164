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

from Food_utilities import get_vegetarian, read_foods

from Food import Food

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

veggies = get_vegetarian(foods)

for each in veggies:
    print(each)
    print()