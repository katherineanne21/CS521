"""
This program works with depreciation of assets.

Author: Katherine Anne
Date: August 5, 2024
"""

def calc_dep_assets(term, initial_val, salvage):
    """Returns the annual depreciation of a tree. """
    
    annual_dep = (initial_val - salvage) / term
    return annual_dep

def gen_creator(initial_val, salvage, depreciation):
    """Returns the annual depreciation of a tree."""

    current_value = initial_val
    while current_value > salvage:
        current_value -= depreciation
        yield max(current_value, salvage)

def string_to_int(string):
    """Tests to see if a string can turn into an integer."""

    try:
        
        integer = int(string)
        return integer
    
    except ValueError:

        print("This is not an integer")
        return None

if __name__ == '__main__':

    # Prompt user for inputs
    while True:
        initial_val = input("Enter the initial integer value of the item: ")

        if string_to_int(initial_val) is not None:
            initial_val = string_to_int(initial_val)
            break

    while True:
        term = input("Enter the term in years as an integer: ")

        if string_to_int(term) is not None:
            term = string_to_int(term)
            break

    while True:
        salvage = input("Enter the integer salvage value of the item:  ")

        if string_to_int(salvage) is not None:
            salvage = string_to_int(salvage)
            break

    # Calculate annual depreciation
    annual_dep = calc_dep_assets(term, initial_val, salvage)
    
    # Print out results
    print(f"Depreciation schedule for ${initial_val} over {term} years:")

    # Print out year 0
    print(f"Year {0:<2}: | {initial_val:10.2f} |")

    # Create generator
    depreciation_generator = gen_creator(initial_val, salvage, annual_dep)

    # Print annual depreciation values
    for year in range(1, term + 1):
        try:
            current_value = next(depreciation_generator)
            print(f"Year {year:<2}: | {current_value:10.2f} |")
        except StopIteration:
            break


        
