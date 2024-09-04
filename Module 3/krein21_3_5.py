"""
This program tests the Birthday Paradox.

Author: Katherine Anne
Date: July 23, 2024

Description:
This program creates random rooms of a certain size and sees how many matching
birthdays there are.

"""

# Import modules

import random

# Set constants

TESTS = 50
SIZE = 30

# Generate collections

collections = []

for i in range(TESTS):
    collection = [random.randint(1, 365) for q in range(SIZE)]
    collections.append(collection)

# Count how many have matching

matching = 0

for test in collections:
    if len(test) != len(set(test)):
        matching += 1

# Find percentage

perc_matching = (matching/TESTS) * 100

# Print results

print(f"Of {TESTS} rooms of {SIZE} people each, there were "
      f"{matching} matching birthdays")
print(f"This is a matching percentage of {perc_matching}%")

