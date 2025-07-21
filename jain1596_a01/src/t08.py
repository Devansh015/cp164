"""
-------------------------------------------------------
Assignment 1 Task 8
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""

from functions import matrix_stats

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
small, large, total, average = matrix_stats(a)

print(small, large, total, average)