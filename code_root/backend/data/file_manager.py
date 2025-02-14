import csv
from code_root.config.utility import timer
from code_root.config.settings import SWAT_NIGHT_CHORES_INFO_CSV, SWAT_SCHEDULER_SPECIAL_TASKS_LIST_CSV, SWAT_EMPLOYEE_INFO_CSV, SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV
#hmmm should this be done in main / interface or????

@timer
def inital_csv_to_data_structures(swat_employee_info_csv):
    #take names and put into list
    import os
    employee_names = []

    with open(swat_employee_info_csv, encoding='utf-8-sig', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            # Use the names in the 'Employee' column as values
            name = row['Employee']
            employee_names.append(name) 
            
            
    #take gender and put into lsit
    employee_genders = []
    with open(swat_employee_info_csv, newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            gender = row['Gender']
            employee_genders.append(gender)
    return employee_names, employee_genders

def read_csv(self, file_path, dialect='excel', encoding='utf-8-sig'):
        with open(file_path, newline='', encoding=encoding) as csvfile:
            reader = csv.DictReader(csvfile, dialect=dialect)
            return [row for row in reader]
