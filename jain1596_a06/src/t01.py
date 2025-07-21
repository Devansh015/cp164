"""
-------------------------------------------------------
Assignment 6 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
from Queue_linked import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.remove()

print(q._front._value, q._rear._value, q.is_empty())