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
from Sorts_List_linked import Sorts
from List_linked import List

list = List()
list.append(55)
list.append(45)
list.append(3)
list.append(289)
list.append(213)
list.append(1)
list.append(288)
list.append(53)
list.append(2)


Sorts.radix_sort(list)

l = list._front

while l != None:
    print(l._value)

    l = l._next