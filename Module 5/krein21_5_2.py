"""
This program deals with a file and the duplicated words in it.

Author: Katherine Anne
Date: August 4, 2024
"""

# Import Modules
from collections import Counter
import string


def word_counter(count, words_list):
    """ Count the number of words that repeat a certain number of times. """

    # Count the frequency of the words
    word_count = Counter(words_list)

    # Find the ones that occur count times
    count_words = {word for word, freq in word_count.items() if freq == count}

    # Return
    return tuple(count_words)

if __name__ == '__main__':

    # Define validity checker
    valid_input = True
    
    # Find file
    filename = input("Please enter the name of a file: ")

    try:
        
        # Read file
        text_file = open(filename, 'r', encoding='latin-1')
        content = text_file.read()

        # Split content into words
        words = content.split()

        # Remove punctuation and convert to lowercase
        translation_table = str.maketrans('', '', string.punctuation)
        cleaned_words = [word.translate(translation_table).lower()
                         for word in words]
            
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        valid_input = False
    except (IOError, UnicodeDecodeError):
        print(f"An error occurred while reading the file {filename}.")
        valid_input = False

    # Invoke function for 2-5

    if valid_input:
    
        for count in range(2, 6):
            our_tuple = word_counter(count, cleaned_words)

            print(f"Words occuring {count} times: {our_tuple}")
