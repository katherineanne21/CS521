"""
This program is a menu order form.

Author: Katherine Anne
Date: July 23, 2024

Description:
This program takes the order from an individual via number or name (non-case
sensitive).

"""
        
# Create list
menu = ["ham", "eggs", "bacon", "fish", "toast", "spam", "fruit"]

menu = [item.lower() for item in menu]

while True:

    # Print out list
    print(f"Welcome to the breakfast buffet! We have {len(menu)} "
    "items available:")

    for idx, food in enumerate(menu):
        print(f"\t{idx + 1}. {food}")

    # Ask for order

    order = input("Please select a menu item: ")

    if order.isdigit():
        
        order = int(order)
        
        if 1 <= order <= len(menu):
            
            menu_item = menu[order - 1]
            print(f"A delicious order of {menu_item} has been put in for you!")
            break

        else:
            print("Please choose a number from the menu.")

    else:

        translation_table = str.maketrans('', '', '0123456789.,')
        string_order = order.translate(translation_table)
        string_order = string_order.strip().lower()

        if string_order in menu:
        
            menu_item = string_order
            print(f"A delicious order of {menu_item} has been put in for you!")
            break

        else:
            menu_item = string_order
            print(f"Sorry, I don't think we carry {menu_item}.")



        
