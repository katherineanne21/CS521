"""
This program simulates an image slideshow using a singly-linked list.

Author: Katherine Anne
Date: July 29, 2024
"""

# Import modules
import random

# Generate number ids
image_ids = []

for i in range(25):
    image_ids.append(f"IMG_{random.randint(1000, 9999)}")

# Sort the list in descending order
sorted_image_ids = sorted(image_ids, reverse = True)

# Create a linked list of tuples
linked_list = []

for i in range(len(sorted_image_ids)):
    linked_list.append((
        sorted_image_ids[i], 
        sorted_image_ids[(i + 1) % len(sorted_image_ids)]
    ))

# Print the linked list
for image_id, next_id in linked_list:
    print(f"Image {image_id} (next: {next_id})")
