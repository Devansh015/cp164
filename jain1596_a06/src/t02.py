"""
-------------------------------------------------------
[Assignment 6 Task 2]
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

pq = Priority_Queue()

pq.insert('a')
pq.insert('b')
pq.insert('c')

print(pq._front._value, pq._count)