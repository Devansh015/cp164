"""
-------------------------------------------------------
Assignment 3 Task 4
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack
stack = Stack()

for a in [1,2,3,4,5]:
    stack.push(a)

stack.reverse()

for a in stack._values:
    print(a, end = " ")