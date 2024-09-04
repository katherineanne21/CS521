"""
This program is for my final project. It creates a library search and update
system.

Author: Katherine Anne
Date: August 13, 2024
"""

# Constants
GENRES = {'romance', 'fantasy', 'general fiction',
          'non-fiction', 'historical fiction', 'childrens'}

# Import modules
import csv
import sys
import os
from book_class import Book

# Functions

def find_user(accounts_list, value, types):
    """Looks for a username or password in a list of tuples"""

    if types == 'username':
        types = 0
    elif types == 'password':
        types = 1
    
    for tup in accounts_list:
        if tup[types].lower() == value.lower():
            return True

    return False

def current_user(accounts_list):
    """Finds which account is correlated with a username"""

    username = input("Please enter your username: ")

    if find_user(accounts_list, username, 'username'):

        while True:

            password = input("Please enter your password: ")

            if find_user(accounts_list, password, 'password'):
                print(f"Welcome {username}!")
                return username
            else:
                tryagain = input(f"That doesn't match your username of"
                                 f" {username}. Please choose an option"
                                 f" below.\n1. Try again\n2. Enter new "
                                 f"username\n3. Create new account\n"
                                 f"Choice: ")

                if tryagain == '1':
                    print()
                elif tryagain == '2':
                    username = current_user(accounts_list)
                    return username
                elif tryagain == '3':
                    username = new_user_account(accounts_list)
                    return username
                else:
                    print("No valid number was entered. You will now have"
                          " the opportunity to enter your password again.")
                
    else:
        while True:
            new_account = input("I can't seem to find that one."
                                " Would you like to create a new account?"
                                " (Y/N): ")

            if new_account.lower() == 'y':
                username = new_user_account(accounts_list)
                return username
            elif new_account.lower() == 'n':
                username = current_user(accounts_list)
                return username
            else:
                print("Please enter either a y for yes or an n for no")

def new_user_account(accounts_list):
    """Creates a new user account"""

    # Get username and password
    username = input("Please enter your new account username: ")

    if find_user(accounts_list, username, 'username'):

        while True:
            
            tryagain = input("That username already exists. Would you like"
                             " to log into that existing account? (Y/N) ")

            if tryagain == 'y':
                username = current_user(accounts_list)
                return username
            elif tryagain == 'n':
                username = new_user_account(accounts_list)
                return username
            else:
                print("Please enter either a y for yes or an n for no")

    password = input("Please input your password: ")

    # Create a tuple for the username and password
    new_account = (username, password)
    
    # Append tuple
    with open('accounts.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(new_account)

    # Create the user csv

    file_name = f"{username}.csv"

    if os.path.exists(file_name):
        os.remove(file_name)

    headers = ['Title', 'Author First', 'Author Last', 'Genre', 'Rating']

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
    # Return the username

    return username

def create_book():
    """To simplfy process of getting data about the book"""

    title = input("Title: ")
    author_first = input("Author First Name: ")
    author_last = input("Author Last Name: ")
    print("We have 6 genre sections available:")
    print("1. Romance\n2. Fantasy\n3. General Fiction\n4. Non-Fiction"
          "\n5. Historical Fiction\n6. Childrens")

    while True:
        genre = input("Please choose one of the above genres: ")

        if genre.lower() in GENRES:
            break

        print("That is not one of the 6 genres. Please check your spelling")
    
    return Book(title, author_first, author_last, genre)

def add_book(username):
    """Adds a book to a users csv"""

    print("Please insert the book details below")

    new_book = create_book()

    # Add to CSV

    file_name = f"{username}.csv"

    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([new_book.title, new_book.author_first,
                          new_book.author_last, new_book.genre,
                          new_book.rating])

def readin_books(username):
    """Read in all of the books that a user has saved"""

    file_name = f"{username}.csv"

    # Assert statements
    assert os.path.exists(file_name), (f"File {file_name} needs"
                                       f" to be created")
    assert os.path.getsize(file_name) > 0, (f"File {file_name}"
                                            f"can not not be empty")
    
    books_list = []

    # Read in books
    with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                books_list.append(row)

    # Use dictionary to help create book objects
    book_objects = []
    
    for book_dict in books_list:
        rating = book_dict.get('Rating', 0)
        
        book = Book(
            title_a = book_dict['Title'],
            author_first_a = book_dict['Author First'],
            author_last_a = book_dict['Author Last'],
            genre_a = book_dict['Genre'],
            rating_a = book_dict['Rating']
        )
        
        book_objects.append(book)
    
    return book_objects

def search_book(username):
    """Find a book based on title and author"""

    print("Insert the details of the book")

    other_book = create_book()

    books_list = readin_books(username)

    for book in books_list:
        if book == other_book:
            return book

    return None

def rate_book(username):
    """Add a rating to a book"""

    print("Enter the details for the book you would like to rate")

    rating_book = create_book()
    books_list = readin_books(username)
    found_book = None

    for book in books_list:
        if book == rating_book:
            found_book = book

    if found_book is None:
        print("That book doesn't exist in your library")
    else:
        rating = input("Enter your rating as an integer between 0 and 5: ")

        found_book.book_rating(rating)

        assert found_book.rating == int(rating), ("Book rating did not"
                                             "update correctly")

        file_name = f"{username}.csv"
        
        # Prepare data for writing to CSV
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write headers
            writer.writerow(['Title', 'Author First', 'Author Last',
                             'Genre', 'Rating'])
            
            # Write book data
            for book in books_list:
                writer.writerow([book.title, book.author_first,
                                 book.author_last, book.genre, book.rating])


def menu(username):
    """Displays the main menu for the library system."""
    while True:
        print("\nLibrary Menu")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Rate a book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(username)
        elif choice == '2':
            book = search_book(username)

            if book is None:
                print("No book found")
            else:
                print(f"We found {book} in your library")
                
        elif choice == '3':
            rate_book(username)
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':

    # Get the current usernames and passwords
    user_csv = 'accounts.csv'
    current_accounts = []

    try:
        with open(user_csv, 'r',encoding='latin-1') as file:
            
            reader = csv.reader(file)

            # Read in the rows and add to list
            current_accounts = [tuple(row) for row in reader]

    except FileNotFoundError:
        
        # Create an empty CSV file if it does not exist
        with open(user_csv, 'w', newline='', encoding='latin-1') as file:
            writer = csv.writer(file)

        print("Hello! Welcome to your personal library.")

    else:

        print("Welcome back!")

    # Create or Find account

    while True:

        new_user = input("Do you already have an account? (Y or N): ")

        if new_user.lower() == 'y':
            username = current_user(current_accounts)
            break
        elif new_user.lower() == 'n':
            username = new_user_account(current_accounts)
            break
        else:
            print("Please enter either a y for yes or an n for no")
    
    # Menu

    menu(username)

    
    

        
