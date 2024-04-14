
import csv
from config.utility import timer
from config.settings import swat_night_chores_info_csv, swat_scheduler_special_tasks_list_csv, swat_employee_info_csv, swat_basic_tasks_list_for_scheduler_csv
#hmmm should this be done in main / interface or????

@timer
def intialCSVToDataStructures(employee_details_filepath = str):
    #take names and put into list
    employeeNamesList = []
    with open(swat_employee_info_csv, encoding='utf-8-sig', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            # Use the names in the 'Employee' column as values
            name = row['Employee'] #TODO LEARNING CONCEPT - SOLVED (looked at another csv without \ufeff) Its because I needed to give a encoding parameter to the open() func. why is \ufeff a thing.
            employeeNamesList.append(name) #add names to list
            
    #take gender and put into lsit
    employeeGenderList = []
    with open(swat_employee_info_csv, newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            gender = row['Gender']
            employeeGenderList.append(gender) #add names to list
    return employeeNamesList, employeeGenderList

def read_csv(self, file_path, dialect='excel', encoding='utf-8-sig'):
        with open(file_path, newline='', encoding=encoding) as csvfile:
            reader = csv.DictReader(csvfile, dialect=dialect)
            return [row for row in reader]
