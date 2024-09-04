"""
This program calculates 2D volumes.

Author: Katherine Anne
Date: July 15, 2024

Description:
This program takes the length and height of a shape and prints out the area of
a square, rectangle, and triangle using those measurements.

"""

# Get inputs
length = input('Please enter the length as a decimal (e.g., 4.0): ')
height = input('Please enter the height as a decimal (e.g., 4.0): ')

# Cast as ints
length = float(length)
height = float(height)

# Calculate areas
square = length * length
rectangle = length * height
triangle = 0.5 * rectangle

# Print out
print(f'You entered a length of {length} and a height of {height}')
print('Here are your shapes:')
print(f'\t Square: {square:.2f}')
print(f'\t Rectangle: {rectangle:.2f}')
print(f'\t Square: {triangle:.2f}')

