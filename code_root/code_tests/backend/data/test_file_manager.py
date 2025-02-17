import csv
import tempfile
import os
import pytest

# Import the functions to test
from code_root.backend.data.file_manager import inital_csv_to_data_structures, read_csv

@pytest.fixture
def temp_csv_file():
    """
    Create a temporary CSV file with dummy employee data and yield its filename.
    After the test, remove the temporary file.
    """
    temp_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8-sig')
    fieldnames = ['Employee', 'Gender']
    writer = csv.DictWriter(temp_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Employee': 'Alice', 'Gender': 'female'})
    writer.writerow({'Employee': 'Bob', 'Gender': 'male'})
    temp_csv.close()
    yield temp_csv.name
    os.unlink(temp_csv.name)

def test_inital_csv_to_data_structures(temp_csv_file):
    # Call the function with our temporary CSV file.
    employee_names, employee_genders = inital_csv_to_data_structures(temp_csv_file)
    # Verify that the names and genders match what we wrote.
    assert employee_names == ['Alice', 'Bob']
    assert employee_genders == ['female', 'male']

def test_read_csv(temp_csv_file):
    """
    For read_csv, we need to simulate a 'self' since its signature expects one.
    We create a dummy class, bind the function to its instance, and then call it.
    """
    class DummyReader:
        pass

    dummy_instance = DummyReader()
    bound_read_csv = read_csv.__get__(dummy_instance, DummyReader)
    
    rows = bound_read_csv(temp_csv_file)
    expected_rows = [
        {'Employee': 'Alice', 'Gender': 'female'},
        {'Employee': 'Bob', 'Gender': 'male'}
    ]
    assert rows == expected_rows

