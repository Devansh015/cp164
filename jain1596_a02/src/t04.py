"""
-------------------------------------------------------
Assignment 02 Task 02
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""

from Food_utilities import read_foods, food_table

fh = open("foods.txt", "r")

foods = read_foods(fh)

food_table(foods)