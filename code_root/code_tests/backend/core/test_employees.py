import csv
import tempfile
from typing import Dict
import io
import pytest

from code_root.backend.core.employees import (
    EmployeeManager,
    Employee,
    define_default_assigned_to_times,
    instantiate_employees,
    add_employees_from_csv  # Note: This function uses file I/O.
)
from code_root.backend.core.time_processes import (
    fill_time_slots_inbetween_A_and_B,
    seek_valid_time_slot
)
from code_root.config.settings import SWAT_EMPLOYEE_INFO_CSV, UNAVAILABILITY_TASK


###############################
# Tests for Utility Function(s)
###############################

def test_define_default_assigned_to_times():
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_dict = define_default_assigned_to_times(time_slots)
    assert default_dict == {"9:00am": None, "9:30am": None, "10:00am": None}


###############################
# Tests for Employee class
###############################

def test_employee_methods():
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Alice", "Female", default_assigned.copy())
    
    # Set default availability.
    emp.set_default_availability(time_slots)
    for t in time_slots:
        assert emp.availability[t] is True

    # Mark one time slot as unavailable.
    emp.set_unavailability(["9:30am"])
    assert emp.availability["9:30am"] is False
    assert emp.is_available("9:00am") is True
    assert emp.is_available("9:30am") is False

    # Sum of available times should be 2 out of 3.
    assert emp.sum_available_time_slots() == 2

    # Test task assignment.
    emp.assign_task("9:00am", "Task1")
    assert emp.assigned_to["9:00am"] == "Task1"
    # Test assigning a task to multiple time slots.
    emp.assign_task(["9:30am", "10:00am"], "Task2")
    assert emp.assigned_to["9:30am"] == "Task2"
    assert emp.assigned_to["10:00am"] == "Task2"


###############################
# Tests for EmployeeManager class
###############################

def test_employee_manager_add_and_get():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Bob", "Male", default_assigned.copy())
    manager.add_employee("Bob", emp, time_slots)
    # Verify that get_employee_by_name returns the correct instance.
    retrieved = manager.get_employee_by_name("Bob")
    assert retrieved is emp

def test_employee_manager_set_availability():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Carol", "Female", default_assigned.copy())
    manager.add_employee("Carol", emp, time_slots)
    # Set "9:30am" as unavailable.
    manager.set_employee_availability("Carol", ["9:30am"])
    assert emp.availability["9:30am"] is False

def test_employee_manager_set_and_assign_availability():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Dave", "Male", default_assigned.copy())
    manager.add_employee("Dave", emp, time_slots)
    # This method should both mark "9:30am" unavailable and assign the unavailability task.
    manager.set_and_assign_employee_availability("Dave", ["9:30am"])
    assert emp.availability["9:30am"] is False
    assert emp.assigned_to["9:30am"] == UNAVAILABILITY_TASK

def test_employee_manager_get_available_employees():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp1 = Employee("Eve", "Female", default_assigned.copy())
    emp2 = Employee("Frank", "Male", default_assigned.copy())
    manager.add_employee("Eve", emp1, time_slots)
    manager.add_employee("Frank", emp2, time_slots)
    # Make Frank unavailable at "9:30am"
    emp2.set_unavailability(["9:30am"])
    available = manager.get_available_employees("9:30am")
    assert "Eve" in available
    assert "Frank" not in available

def test_employee_manager_get_employees_in_pool_with_traits():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp1 = Employee("Grace", "Female", default_assigned.copy())
    emp1.position = "Manager"
    emp2 = Employee("Heidi", "Female", default_assigned.copy())
    emp2.position = "Staff"
    manager.add_employee("Grace", emp1, time_slots)
    manager.add_employee("Heidi", emp2, time_slots)
    # Use the full employees dictionary as the pre-filter.
    pre_filtered = manager.employees
    eligible = manager.get_employees_in_pool_with_traits(pre_filtered, position="Manager")
    assert "Grace" in eligible
    assert "Heidi" not in eligible

def test_employee_manager_assign_task_to_employee():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Ivan", "Male", default_assigned.copy())
    manager.add_employee("Ivan", emp, time_slots)
    manager.assign_task_to_employee("Ivan", "TaskX", "9:00am")
    assert emp.assigned_to["9:00am"] == "TaskX"


###############################
# Tests for instantiate_employees
###############################

def test_instantiate_employees():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    employee_names = ["Judy", "Ken"]
    employee_genders = ["Female", "Male"]
    new_manager = instantiate_employees(manager, time_slots, employee_names, employee_genders)
    # Verify that both employees have been added.
    assert "Judy" in new_manager.employees
    assert "Ken" in new_manager.employees
    # Also, each employee’s availability should be set to True for all time slots.
    for name in employee_names:
        emp = new_manager.employees[name]
        for t in time_slots:
            assert emp.availability.get(t) is True


###############################
# Tests for EmployeeAvailabilityLogic
###############################

def test_employee_availability_logic_set_employee_availability():
    manager = EmployeeManager()
    time_slots = ["9:00am", "9:30am", "10:00am"]
    default_assigned = define_default_assigned_to_times(time_slots)
    emp = Employee("Laura", "Female", default_assigned.copy())
    manager.add_employee("Laura", emp, time_slots)
    avail_logic = EmployeeAvailabilityLogic(manager)
    avail_logic.set_employee_availability("Laura", ["9:30am"], None, None)
    assert emp.availability["9:30am"] is False
    assert emp.assigned_to["9:30am"] == UNAVAILABILITY_TASK

@pytest.fixture
def dummy_time_mappings():
    # Create a dummy times list and mapping dictionaries.
    times_list = ["9:00am", "9:30am", "10:00am", "10:30am"]
    time_slot_to_index_map = {time: i for i, time in enumerate(times_list)}
    index_to_time_slot_map = {i: time for i, time in enumerate(times_list)}
    return times_list, time_slot_to_index_map, index_to_time_slot_map

def test_multi_time_input_detector(monkeypatch, dummy_time_mappings):
    # Define dummy versions of the time–processing functions.
    def dummy_fill_time_slots_inbetween_A_and_B(start, end, ts_map, index_map):
        start_index = ts_map[start]
        end_index = ts_map[end]
        return [index_map[i] for i in range(start_index, end_index + 1)]
    def dummy_seek_valid_time_slot(slot, times_list):
        return slot if slot in times_list else times_list[0]

    # Patch the imported functions in the employees module.
    # (Assuming your employees module imported them at top level.)
    import employees
    monkeypatch.setattr(employees, "fill_time_slots_inbetween_A_and_B", dummy_fill_time_slots_inbetween_A_and_B)
    monkeypatch.setattr(employees, "seek_valid_time_slot", dummy_seek_valid_time_slot)

    times_list, ts_map, index_map = dummy_time_mappings
    dummy_manager = EmployeeManager()
    avail_logic = EmployeeAvailabilityLogic(dummy_manager)

    # Test with a range input.
    input_range = ["9:00am-10:00am"]
    result = avail_logic.multi_time_input_detector_and_converter_employee_unavailability(
        input_range, times_list, ts_map, index_map
    )
    expected = ["9:00am", "9:30am", "10:00am"]
    assert result == expected

    # Test with a list of individual times.
    input_single = ["9:30am", "10:30am"]
    result_single = avail_logic.multi_time_input_detector_and_converter_employee_unavailability(
        input_single, times_list, ts_map, index_map
    )
    # Since there’s no comma or dash, it should simply return the input list.
    assert result_single == input_single
