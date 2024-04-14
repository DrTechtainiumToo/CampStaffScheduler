from backend.data.file_manager import intialCSVToDataStructures
from config.settings import swat_employee_info_csv

employeeNamesList, employeeGenderList = intialCSVToDataStructures(swat_employee_info_csv)


