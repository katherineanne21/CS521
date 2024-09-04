"""
This program finds the 25th record of patient data.

Author: Katherine Anne
Date: July 29, 2024
"""

# Import modules
import csv
import random

# Create list and dict
PATIENT_RECORDS = {}
EXISTING_IDS = []

# Read file
FILENAME = 'heart_failure_clinical_records_dataset.csv'

with open(FILENAME, 'r') as file:
    
    reader = csv.DictReader(file)
    
    for row in reader:
        
        # Generate a unique patient ID
        while True:
            patient_id = (
                f"{random.randint(0, 999):03}-"
                f"{random.randint(1000, 9999):04}"
            )

            if patient_id not in EXISTING_IDS:
                EXISTING_IDS.append(patient_id)
                break
            
        # Add to patient records
        PATIENT_RECORDS[patient_id] = row

# Print out 25th record
print(PATIENT_RECORDS[list(PATIENT_RECORDS.keys())[24]])
