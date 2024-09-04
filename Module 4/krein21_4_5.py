"""
This program manages orders for a breakfast café menu and calculates the total bill.

Author: Katherine Anne
Date: July 29, 2024
"""

# Define the menu items
MENU_ITEMS = {
    'ham': 1.99,
    'eggs': 3.50,
    'bacon': 4.23,
    'fish': 5.62,
    'toast': 2.45,
    'spam': 1.95,
    'fruit': 2.92
}

# Initialize the user's order
USER_ORDER = []

# Print the banner and menu
print("Welcome to the Breakfast Café!")
print("Here is our menu today:")
for idx, (item, price) in enumerate(MENU_ITEMS.items(), start=1):
    print(f" {idx}. {item} ${price:.2f}")

# Get order
while True:
    selection = input("Please enter your selection by name; "
                      "when finished ordering enter 'done': ").strip().lower()
    
    if selection == 'done':
        break
    elif selection in MENU_ITEMS:
        if selection not in USER_ORDER:
            USER_ORDER.append(selection)
            current_order = ", ".join(sorted(USER_ORDER))
            print(f"Current order: {current_order}")
        else:
            print("You already have selected that item")
    else:
        print("Sorry, that item is not on the menu. Please choose something else.")

# Calculate and print the bill
print("\nExcellent! Here is your bill:")
print("----------------------------------------")

total = 0
for item in sorted(USER_ORDER):
    price = MENU_ITEMS[item]
    total += price
    print(f"{item} ${price:.2f}")

print("----------------------------------------")
print(f"TOTAL: ${total:.2f}")
