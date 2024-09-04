"""
This program works with heart failure data.

Author: Katherine Anne
Date: August 4, 2024
"""

# Import modules
import csv
import random

def new_patient(patient_string):
    """ Process a patient record string into a dictionary. """
    
    # Define the keys corresponding to each field in the record
    keys = [
        'age', 
        'anaemia', 
        'creatinine_phosphokinase', 
        'diabetes', 
        'ejection_fraction', 
        'high_blood_pressure', 
        'platelets', 
        'serum_creatinine', 
        'serum_sodium', 
        'sex', 
        'smoking', 
        'time', 
        'DEATH_EVENT'
    ]
    
    # Split the record string into a list of values
    values = patient_string.split(',')
    
    # Create a dictionary of the values and keys
    patient_record = dict(zip(keys, values))
    
    return patient_record

if __name__ == '__main__':

    # Create list and dict
    PATIENT_RECORDS = dict()
    EXISTING_IDS = []

    try:
        # Read file
        FILENAME = 'heart_failure_clinical_records_dataset.csv'

        with open(FILENAME, 'r', encoding='latin-1') as file:
            reader = csv.reader(file)
            
            # Skip the header
            headers = next(reader)

             # Read in the rows and add in the unique patient ID
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

                # Convert the row to a comma-separated string
                row_str = ','.join(row)

                # Call function to create a dictionary for each patient
                new_patient_record = new_patient(row_str)
                PATIENT_RECORDS[patient_id] = new_patient_record
        
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        sys.exit()
    except (IOError, UnicodeDecodeError):
        print(f"An error occurred while reading the file {filename}.")
        sys.exit()

    # Print first and last record
    items_list = list(PATIENT_RECORDS.values())
    print(items_list[0])
    print(items_list[-1])
        
        
        
