"""
-------------------------------------------------------
Assignment 3 Task 3
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_reverse

source = Stack()

for a in [1,2,3,4,5]:
    source.push(a)

stack_reverse(source)

for a in source._values:
    print(a, end = " ")