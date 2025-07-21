"""
-------------------------------------------------------
Lab 3 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""

#Imports

from Queue_array import Queue

#Inputs 

q = Queue()

elements = [1,2,3,4]

#Output

print("Inserting elements into the queue:")
for element in elements:
    print(f"Inserting {element} into the queue.")
    q.insert(element)
    print(f"Queue now contains: {[val for val in q]}")
    