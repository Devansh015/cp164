"""
-------------------------------------------------------
Assignment 3 Task 2
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack

source1 = Stack()
source2 = Stack()
target = Stack()

for a in [1,3,5]:
    source1.push(a)

for a in [2,4,6]:
    source2.push(a)
    
target.combine(source1, source2)

for item in target._values:
    print(item, end = " ")