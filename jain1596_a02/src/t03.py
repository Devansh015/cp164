"""
-------------------------------------------------------
Assignment 02 Task 03
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""

from Food_utilities import read_foods, calories_by_origin

fh = open("foods.txt", "r")

foods = read_foods(fh)

avg_Can = calories_by_origin(foods, 0)

print(f"The average calories in Canadian food is: {avg_Can:.5}")
