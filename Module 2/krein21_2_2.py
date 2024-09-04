"""
This program prints out a numbered list of breakfast items.

Author: Katherine Anne
Date: July 15, 2024

Description:
This program is able to take a list and turn it into a numbered list

"""

# Create list
menu = ["ham", "eggs", "bacon", "fish", "toast", "spam", "congee", "fruit"]

# Print out list
print('Welcome to the breakfast buffet! We have 8 items available:')

for idx, food in enumerate(menu):
    print(f'\t{idx + 1}. {food}')
