"""
This file creates a Book class that can be used when organizing a library.

Author: Katherine Anne
Date: August 12, 2024
"""

class Book:
    """Used to organize books"""

    def __init__(self, title_a = '', author_first_a = '',
                 author_last_a = '', genre_a = '', rating_a = 0):
        """Initializes the Book object with the given variables"""

        # Prep attributes
        self.title = title_a
        self.author_first = author_first_a
        self.author_last = author_last_a
        self.genre = genre_a
        self.rating = rating_a

        # Add a book ID

        self.__book_id_num = self.book_id(self.title, self.author_first,
                                    self.author_last)

    def __repr__(self):
        """Returns the title and author"""

        return f"{self.title} by {self.author_first} {self.author_last}"

    def __eq__(self, other_book):
        """Delineates what is meant by two books being equal"""

        if isinstance(other_book, Book):
            return (self.__similar_str(self.title, other_book.title) and
                    self.author_first == other_book.author_first and
                    self.author_last == other_book.author_last)

        return False

    def __similar_str(self, str1, str2):
        """Checks to see if the strings are substrings of each other"""

        return (str1.lower() in str2.lower() or
                str2.lower() in str1.lower())
        
    def book_id(self, title, author_first, author_last):
        """Creates a new unique book ID number"""

        # Concatenate the variables
        name = title + author_first + author_last

        # Sum their ASCII values
        book_id = sum(ord(char.lower()) for char in
                      name if char.isalpha())

        return book_id

    def book_rating(self, rating):
        """Adds a rating out of 5 to the book"""

        rating = int(rating)

        if isinstance(rating, int) and 0 <= rating <= 5:
            self.rating = rating

            return (f"{self.title} by {self.author_first} {self.author_last}"
                " now has a rating of {rating}/5")
        
        return f"Opps! That's not an acceptable rating"


                
    

    

        

    
            
        
