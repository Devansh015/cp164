"""
-------------------------------------------------------
Lab 6 Task 1
-------------------------------------------------------
Author: Devansh Jain    
ID:        169061596
Email:   jain1596@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""

from List_linked import List

playlist = List()

playlist.prepend("Baby - Justin Bieber")

playlist.append("Freestyle - Lil Baby")

playlist.insert(1, "Best Part - Daniel Caesar")

for each in playlist:
    print(each)