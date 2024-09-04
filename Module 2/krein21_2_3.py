"""
This program divides two user inputted integers.

Author: Katherine Anne
Date: July 15, 2024

Description:
This program takes two user inputted integers and divides them. It prints
out the answer as a decimal and a remainder.

"""
# Recieve ints from user
first_int = input('Please enter an integer: ')
second_int = input('Please enter a second integer: ')

# Convert to int
first_int = int(first_int)
second_int = int(second_int)

# Calculate float and remainder
float_ans = first_int / second_int
whole_num = first_int // second_int
remainder = first_int % second_int

# Print out results
print(f'The result of {first_int} divided by {second_int} is:')
print(f'\t {float_ans:.2f} as a floating-point value')
print(f'\t {whole_num} remainder {remainder}')
