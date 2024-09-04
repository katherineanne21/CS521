"""
This program finds the longest word in a text file.

Author: Katherine Anne
Date: July 23, 2024

Description:
This program reads in a file and then finds the longest word(s) in it.

"""

# Import modules
import os
import string
import re
        
# Set filename
FILENAME = 'cs521_assign_3_4.txt'

if not os.path.exists(FILENAME):
    print(f"The file {FILENAME} does not exist.")
    sys.exit()

# Read in text file

text_file = open(FILENAME, 'r', encoding='latin-1')
text_str = text_file.read()

# Separate words into a list

word_list = re.split(r'\s+', text_str.strip())

# Clean words

translation_table = str.maketrans('', '', string.punctuation)
cleaned_words = [word.translate(translation_table).lower()
                 for word in word_list]

# Find longest word(s)

long_word = []
length = 0

for word in cleaned_words:
    if len(word) == length:
        long_word.append(word)
    if len(word) > length:
        long_word = []
        length = len(word)
        long_word.append(word)

# Print out the longest word(s)

if len(long_word) == 1:
    print(f"The longest word in {FILENAME} is {long_word[0]} at "
          f"{len(long_word[0])} letters.")
else:
    print(f"The longest words in {FILENAME} are {', '.join(map(str, long_word))}"
          f" at {len(long_word[0])} letters.")




