"""
This program is a message encoder.

Author: Katherine Anne
Date: July 23, 2024

Description:
This program takes a string and encodes by using a predefined shift.

"""

# Import modules
import string

# Declare constants
SHIFT = 6
MESSAGE = "O, that this too too solid flesh would melt, \
Thaw and resolve itself into a dew!"

# Define lower and upper case
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
        
# Check the letters of the message
encoded_string = ''

for idx, char in enumerate(MESSAGE):

    if char.isalpha():
        
        if char.islower():
            new_pos = (lowercase.index(char) + SHIFT) % 26 
            shifted_char = lowercase[new_pos]
            encoded_string = encoded_string + shifted_char
        
        if char.isupper():
            new_pos = (uppercase.index(char) + SHIFT) % 26 
            shifted_char = uppercase[new_pos]
            encoded_string = encoded_string + shifted_char        
        
    else:
        encoded_string = encoded_string + char

print(f"Your cleartext message was: {MESSAGE}")
print(f"The new encoded message is: {encoded_string}")   

    

        
        
