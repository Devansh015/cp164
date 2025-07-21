"""
-------------------------------------------------------
Assignment 3 Task 7
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""

from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

print(f"For the following maze '{maze}', the route is: ", end = "")
print(stack_maze(maze))