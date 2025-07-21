"""
-------------------------------------------------------
Lab 7 Task 3
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)

print("Original List:")
current = my_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

even_list, odd_list = my_list.split_alt_r()

print("Even List:")
current = even_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

print("Odd List:")
current = odd_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()