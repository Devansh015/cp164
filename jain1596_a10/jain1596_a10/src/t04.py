"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-07-21"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()

vals = [11, 3, 54, 709, 6, 10, 68, 395, 96585, 456, 2312, 6059]

for l in vals:
    a.insert_rear(l)

print(Sorts.gnome_sort(a))

for i in a:
    print(i)