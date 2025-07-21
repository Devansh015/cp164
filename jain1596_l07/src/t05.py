"""
-------------------------------------------------------
Lab 7 Task 5
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
from List_linked import List

list1 = List()
list2 = List()

for value in [1, 3, 5, 7]:
    list1.append(value)

for value in [2, 4, 5, 6, 7]:
    list2.append(value)

union_list = List()

union_list.union_r(list1, list2)

print("Union of list1 and list2:")
current = union_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()