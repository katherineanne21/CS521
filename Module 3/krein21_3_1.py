"""
This program is a gift wrap calculator.

Author: Katherine Anne
Date: July 23, 2024

Description:
This program lets us see how much wrapping paper we need
for a gift box of different sizes.

"""

# Print banner
print("-------------------------------------")
print("Welcome to the gift wrap calculator!")
print("Type 'quit' when you are done")
print("-------------------------------------")
print()

values = ''

# Ensure user still wants to run program
while True:
    
    # Get values
    values = input("Please enter the box dimensions separated"
            " with an x, e.g. 10x20x15: ")
    values = str(values)

    if values.lower() == 'quit':
        break

    # Split string into a list
    values_list = values.split(sep = 'x')

    # Assign values to length, height, width
    length = values_list[0]
    height = values_list[1]
    width = values_list[2]

    # Ensure they are numbers
    length = float(length)
    height = float(height)
    width = float(width)

    # Calculate surface area
    side1 = height * length
    side2 = length * width
    side3 = width * height
    
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    
    # Find the smallest side and add to surface area
    box_sides = [side1, side2, side3]
    min_side = min(box_sides)

    surface_area += min_side

    print(f"You will need {surface_area} cm of wrapping paper")
    print()


# Close out the program
print()
print("Thank you for using the gift-wrap calculator!")
          

    

    

    
