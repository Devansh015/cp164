"""
-------------------------------------------------------
Assignment 5 Task 2
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List 
from Food import Food
from copy import deepcopy

list1 = Sorted_List()
list2 = Sorted_List()
list3 = Sorted_List()

def print_list1():
    print(f"Items in List1")
    print("-" * 15)
    for item in list1._values:
        print(item)
    print("")

def print_list2():
    print(f"Items in List2")
    print("-" * 15)
    for item in list2._values:
        print(item)
    print("")

def print_list3():
    print(f"Items in List3")
    print("-" * 15)
    for item in list3._values:
        print(item)
    print("")

#Making Sorted Lists sorted by calories
foods = [Food("Candy",None,True,120), Food("Lasagna",7,False,135), Food("Fried Rice",1,False,425),Food("Pepperoni Pizza",7,False,713)]

list1._values = deepcopy(foods)
list2._values = deepcopy(foods)
list3._values = deepcopy(foods)

list1._values.append(Food("Chip Butty",11,True,956))
list1._values.append(Food("Candy",None,True,120))

contains = Food("Candy",None,True,120) in list1

equal = list1 == list2

item = list1[0]

print_list1()
print_list2()
print_list3()

print(f"Is 'Candy' in list1: {contains}")

print(f"Are list1 and list2 equal: {equal}")

print(f"How the following code runs: list1[0] -> {item}")

count = list1.count(Food("Candy",None,True,120))

print(f"How many times did 'Candy' appear in list1: {count}")

list1.clean()

print("List1 after being cleaned...")

print_list1()

#list1._values = foods

#found = list1.find("Lasagna")

#print(f"Item found: {found}")

index = list1.index(Food("Candy",None,True,120))

print(f"The index of 'Candy' in list1 is: {index}")

list3.intersection(list1.copy(), list2.copy())

print(f"The intersected values of list1 and list2 are in list3...\n")

print_list3()

max = list1.max()
min = list1.min()

print(f"The max in list1 is {max} and min is {min}")

peeked = list1.peek()

print(f"First item in list1 is {peeked}")

list1.remove(Food("Lasagna",7,False,135))

print("List after 'Lasagna' is removed...")
print_list1()

list1.remove_front()
print("List after front is removed...")
print_list1()

list1.remove_many(Food("Pepperoni Pizza",7,False,713))

print("List after 'Pepperoni Pizza' is removed...")
print_list1()

list2, list3 = list1.split()

print("Reseting lists...")

list1._values = deepcopy(foods)
list2._values = deepcopy(foods)
list3._values = deepcopy(foods)

print_list1()
print_list2()
print_list3()

list2, list3 = list1.split()

print("Lists after being split...")

print_list1()
print_list2()
print_list3()

print("Reseting lists...")

list1._values = deepcopy(foods)
list2._values = deepcopy(foods)
list3._values = deepcopy(foods)

print_list1()
print_list2()
print_list3()

print("Splitting lists in an alternating order...")

list2, list3 = list1.split_alt()

print_list1()
print_list2()
print_list3()

print("Reseting lists...")

list1._values = deepcopy(foods)
list2._values = deepcopy(foods)
list3._values = deepcopy(foods)

print_list1()
print_list2()
print_list3()

print("Splitting lists from 1...")

list2, list3 = list1.split_key(1)

print_list1()
print_list2()
print_list3()

print("Reseting lists...")

list1._values = deepcopy(foods)
list2._values = deepcopy(foods)
list3._values = deepcopy(foods)

print_list1()
print_list2()
print_list3()

value = list1.find('Lasagna')

print(f"Running the following code: list1.find('Lasagna') -> \n{value}")