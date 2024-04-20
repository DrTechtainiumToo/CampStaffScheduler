from backend.data.file_manager import inital_csv_to_data_structures
from config.settings import SWAT_EMPLOYEE_INFO_CSV

#TODO reasses this intermediate file later
employee_names, employee_genders = inital_csv_to_data_structures(SWAT_EMPLOYEE_INFO_CSV)


