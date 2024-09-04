"""
This program calculates the Jaccard Index between two strings.

Author: Katherine Anne
Date: July 29, 2024
"""

# Get two strings from the user
while True:
        string1 = input(
            "Please enter a string of at least 40 characters: ")
        
        if len(string1) >= 40:
            break
        
        print("The string must be at least 40 characters long.")

while True:
        string2 = input(
            "Please enter another string of at least 40 characters: ")
        
        if len(string2) >= 40:
            break
        
        print("The string must be at least 40 characters long.")

# Convert strings to lists of lowercase letters
list1 = [char.lower() for char in string1 if char.isalpha()]
list2 = [char.lower() for char in string2 if char.isalpha()]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Calculate the intersection and union of the sets
intersection = set1.intersection(set2)
union = set1.union(set2)

# Compute the Jaccard Index
jaccard_index = len(intersection) / len(union) * 100

# Print the result
print(f"The Jaccard Index value for your two strings is {jaccard_index:.4f}%.")
