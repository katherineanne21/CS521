"""
This program details the top 10 funniest videos from a dataset.

Author: Katherine Anne
Date: July 29, 2024
"""

# Import needed modules
import os
from operator import itemgetter

# Define the filename and path
FILENAME = (
    '/Users/katherineanne/Desktop/College/Summer 2024/'
    'CS 521/Module 4/comedy_comparisons.train'
)

# Create a dictionary to store votes
VOTES = {}

# Read in the data
with open(FILENAME, 'r') as file:
    for row in file:
        # Split the row into IDs and vote
        video1, video2, vote = row.strip().split(',')
        
        # Determine the winning video
        if vote == 'left':
            winning_video = video1
        else:
            winning_video = video2
        
        # Increment the vote count for the winning video
        if winning_video in VOTES:
            VOTES[winning_video] += 1
        else:
            VOTES[winning_video] = 1

# Sort the dictionary by vote count in descending order
sorted_votes = sorted(VOTES.items(), key = itemgetter(1), reverse = True)

# Select the top 10 videos
top_10_videos = sorted_votes[0:10]

# Print the enumerated list of top 10 videos
print("Top 10 Funniest Videos:")
for idx, (video_id, vote_count) in enumerate(top_10_videos, start = 1):
    print(f"{idx:2}. {video_id}")
