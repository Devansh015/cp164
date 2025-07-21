"""
-------------------------------------------------------
Assignment 3 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_combine

stack1 = Stack()
stack2 = Stack()

for a in [1,3,5]:
    stack1.push(a)

for a in [2,4,6]:
    stack2.push(a)

combined_stack = stack_combine(stack1, stack2)

for item in combined_stack._values:
    print(item, end = " ")