"""
-------------------------------------------------------
Lab 02 Task 2
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = [1, 2, 3, 4, 5]

print("Source array before transferring to stack:", source)

array_to_stack(stack, source)

print("Source array after transferring to stack:", source)

print("Elements in the stack from top to bottom:")
for element in stack:
    print(element)