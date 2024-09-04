"""
This program reads in 2 integers and computes the product.

Author: Katherine Anne
Date: July 15, 2024

Description:
This program is able to read in the two integers and compute their product.
Additionally, the product gets displayed in multiple different formats.

"""

# Recieve ints from user
first_int = input('Please enter an integer: ')
second_int = input('Please enter a second integer: ')

# Convert to int
first_int = int(first_int)
second_int = int(second_int)

# Calculate product
product = first_int * second_int

# Convert into different formats
binary = bin(product)
octal = oct(product)
hexadecimal = hex(product)

# Print out results
print(f'You entered the numbers {first_int} and {second_int} - their product is {product}.')
print('Here is that product in different formats:')
print(f'\t Binary:{binary}')
print(f'\t Octal:{octal}')
print(f'\t Decimal:{product}')
print(f'\t Hexadecimal:{hexadecimal}')
