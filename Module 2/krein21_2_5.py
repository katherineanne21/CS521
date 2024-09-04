"""
This program is similar to the typical fizz-buzz problem.

Author: Katherine Anne
Date: July 15, 2024

Description:
This program details which numbers are divisible by 2, 3, or 5. It prints the
label on the same line.

"""

# Declare MAXVAL
MAXVAL = 30

# Deliniate which values are divisible by 2, 3, or 5
for i in range(1,MAXVAL + 1):
    print(f'{i}: ', end = " ")
    
    if i % 2 == 0:
        print('two', end = " ")
    if i % 3 == 0:
        print('three', end = " ")
    if i % 5 == 0:
        print('five', end = " ")

    print()
        
print('-------------')    
