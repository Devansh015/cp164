"""
-------------------------------------------------------
Assignment 5 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
from List_array import List
from Food import Food

list = List()
list1 = List()
list2 = List()

def print_lists():
    print("First List:")
    print("-" * 15)
    for food in list1:
        print(food)
    print("\nSecond List:")
    print("-" * 15)
    for food in list2:
        print(food)

def print_main_list():
    print("Main List")
    print("-" * 15)
    for food in list:
        print(food)

foods = [Food("Candy",None,True,120), Food("Lasagna",7,False,135), 
         Food("Fried Rice",1,False,425),Food("Pepperoni Pizza",7,False,713)]

for food in foods:
    list1.append(food)
    list2.append(food)

print_lists()

equal = list1 == list2

print(f"\nAre the lists equal: {equal}")


list1.append(Food("Candy",None,True,120))

print("Duplicate Appended...\n")

print_lists()

list1.clean()

print("List Cleaned...\n")

print_lists()

list.combine(list1.copy(), list2.copy())

print("Two list combined to one...\n")

print_main_list()

list1.append(Food("Greek Salad",5,True,185))

print_lists()

list.intersection(list1.copy(), list2.copy())

print("Intersection of Two Lists...\n")

print_main_list()

print("Prepending the food 'Pavlova'...")

list2.prepend(Food("Pavlova",10,True,272))

print_lists()

list2.remove_front()

print("Front Removed...")

print_lists()

list1.append(Food("Candy",None,True,120))

print_lists()

print("All 'Candy' items removed...")

list1.remove_many(Food("Candy",None,True,120))

print_lists()

print_main_list()

print("List split...")

list1, list2 = list.split()

print_lists()

print_main_list()

print('Lists Combined...')

foods = [Food("Candy",None,True,120), Food("Lasagna",7,False,135), 
         Food("Fried Rice",1,False,425),Food("Pepperoni Pizza",7,False,713)]

for food in foods:
    list1.append(food)
    list2.append(food)

list.union(list1, list2)

print_lists()

print_main_list()

print("Lists Split in an alternating order...")

list1, list2 = list.split_alt()

print_lists()

print_main_list()