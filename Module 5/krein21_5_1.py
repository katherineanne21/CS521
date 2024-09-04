"""
This program deals with integers and it's purpose is to not crash.

Author: Katherine Anne
Date: August 4, 2024
"""

def int_math(a,b,c,d):
    """ Compute a 4 int math problem """
    if d != 0:
        return ((a+b)*c)/d
    raise ZeroDivisionError("You can not have the fourth number be a 0.")

if __name__ == '__main__':
    
    while True:

        # Reset/define correct input to be true unless otherwise changed
        correct_input = True
        
        # Prompt user
        user_input = input("Please enter 4 non-zero integers separated by /: ")

        # Check backslashes
        if user_input.count('/') != 3:
            print("Please use 3 slashes to separate your 4 numbers.")
            correct_input = False
        
        # Split string into 4 numbers
        if correct_input:
        
            try:
                first, second, third, fourth = [
                    int(x) for x in user_input.split('/')
                    ]
            except ValueError:
                print("Ooops, value is not valid. Try again!")
                correct_input = False
            except IndexError:
                print("That seems to be out of the index. Try again!")
                correct_input = False
            except ZeroDivisionError:
                print("Oh no! You're dividing by zero. Try again!")
                correct_input = False
            
        # Invoke math function
        if correct_input:

            try:
                math_answer = int_math(first, second, third, fourth)
            except ValueError:
                print("Ooops, value is not valid. Try again!")
                correct_input = False
            except IndexError:
                print("That seems to be out of the index. Try again!")
                correct_input = False
            except ZeroDivisionError:
                print("Oh no! You're dividing by zero. Try again!")
                correct_input = False
        
        # Print out results 

        if correct_input:
            
            print(f"The result of (({first} + {second}) * {third}) / {fourth}"
                  f" is: {math_answer}.")

            # Quit if no exceptions were raised

            break
        
        
    
    
