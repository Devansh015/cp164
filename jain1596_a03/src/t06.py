"""
-------------------------------------------------------
Assignment 3 Task 6
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""


from functions import postfix

string = "4 5 + 12 * 2 3 * -"

print(f"For the postfix '{string}', the answer is: ", end = "")
print(postfix(string))