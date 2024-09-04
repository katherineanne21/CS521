"""
This program calculates the GCD.

Author: Katherine Anne
Date: August 5, 2024
"""

def calc_GCD(a, b):
    """Calculates the GCD of two numbers."""

    if a % b == 0:
        return b
    else:
        return calc_GCD(b, a%b)
    

def string_to_int(string):
    """Tests to see if a string can turn into an integer."""

    try:
        
        integer = int(string)
        return integer
    
    except ValueError:

        print("This is not an integer")
        return None


if __name__ == '__main__':

    while True:
        first = input("Enter first non-zero integer value: ")

        if string_to_int(first) is not None:
            first = string_to_int(first)

            if first != 0:
                break
            else:
                print("No zeros!")

    while True:
        second = input("Enter second non-zero integer value: ")

        if string_to_int(second) is not None:
            second = string_to_int(second)

            if second != 0:
                break
            else:
                print("No zeros!")

    # Calculate GCD
    GCD = calc_GCD(first, second)

    # Print out GCD
    print(f"The GCD of {first} and {second} is {GCD}")

        
