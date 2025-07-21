"""
-------------------------------------------------------
Assignment 02 Task 01 
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""

from Food_utilities import read_foods, by_origin, food_table

fh = open("foods.txt", "r")

foods = read_foods(fh)

Can_foods = by_origin(foods, 0)

print("Showing all Canadian foods:\n")

food_table(Can_foods)