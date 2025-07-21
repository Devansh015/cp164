"""
-------------------------------------------------------
Lab 4 Task 5
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from List_array import List

my_list = List()

my_list.append(10)
my_list.append(20)
my_list.append(30)

#Outputs

second_item = my_list[1]
print(f"The second item in the list: {second_item}")

print("Setting the second item in the list to 25...")
my_list[1] = 25

try:
    print("Trying to access index out of range:")
    my_list[5]
except AssertionError as e:
    print(f"Error: {e}")

try:
    print("Trying to set index out of range:")
    my_list[5] = 50
except AssertionError as e:
    print(f"Error: {e}")