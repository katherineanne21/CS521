"""
This program creates a Sentence class that evaluates and
manipulates an English sentence.

Author: Katherine Anne
Date: August 11, 2024
"""

# Import modules
import string
import random

class Sentence:
    """Evaluates and manipulates an English sentence"""

    def __init__(self, sent = ''):
        """Initializes the Sentence object with a given sentence"""
        
        self._sentence = sent

        # Convert to list with cleaned punctuation
        translation_table = str.maketrans('', '', string.punctuation)
        cleaned_sentence = self._sentence.translate(translation_table)
        self.words_list = cleaned_sentence.split()

    def __repr__(self):
        """Returns the sentence list as a single string,
            with a period at the end"""
        
        # Join the words list into a single string
        sentence_str = " ".join(self.words_list)
        
        # Add a period at the end
        return sentence_str + "."

    def get_all_words(self):
        """Counts the number of words in the list of words"""

        return len(self.words_list)

    def get_word(self, idx):
        """Gets a word at at specific index"""

        # Return word at a specific index
        # Handle exceptions
        if 0 <= idx < len(self.words_list):
            return self.words_list[idx]
        else:
            return ''

    def set_word(self, idx, new_word):
        """Changes the word at index location to a new word"""

        # Set new_word at the idx
        if 0 <= idx < len(self.words_list):
           self.words_list[idx] = new_word

    def scramble(self):
        """Scrambles the words in the sentence"""
        
        # Create a copy of the words_list
        scrambled_words = self.words_list[:]
        
        # Shuffle the copied list
        random.shuffle(scrambled_words)
        
        return scrambled_words

if __name__ == '__main__':

    # Run a unit test
    
    # Instantiate the class with a test sentence
    sentence = Sentence("This is a sentence: to test my code.")

    # Validate set_word
    sentence.set_word(2, "test")
    assert sentence.get_word(2) == "test", f"Error:"
    "expected 'test' but got '{sentence.get_word(2)}'"

    # Print success message and sentence versions
    print("Sentence unit test successful")
    print("Original Sentence: This is a sentence: to test my code.")
    print("Scrambled sentence:", " ".join(sentence.scramble()))
    print(f"Final sentence: {sentence}")
