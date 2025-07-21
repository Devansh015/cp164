"""
-------------------------------------------------------
Lab 02 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""

from Stack_array import Stack

stack = Stack()

print("Stack empty: ", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print("After pushing: ", stack.is_empty())  

top_element = stack.peek()
print("Top element (peek): ", top_element)

popped_element = stack.pop()
print("Popped element: ", popped_element) 

new_top_element = stack.peek()
print("New top element after popping: ", new_top_element)

print("Elements in the stack from top to bottom:")

for element in stack:
    print(element)
