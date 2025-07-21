"""
-------------------------------------------------------
Lab 02 Task 5
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food

s = Stack()

fh = open("foods.txt", "r", encoding="utf-8")

for line in fh:
    food = read_food(line)
    s.push(food)
    
stack_test(s)