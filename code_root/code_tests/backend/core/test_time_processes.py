import datetime
from datetime import timezone
import pytest

# Import the functions and constants from your modules.
from code_root.backend.core.time_processes import (
    program_auto_get_date_value,
    validate_user_date_input,
    get_day_name,
    timeSlotStandardizer,
    fill_time_slots_inbetween_A_and_B,
    seek_valid_time_slot,
    get_current_week,
)
from code_root.config.settings import GET_NEXT_DAY

def test_program_auto_get_date_value():
    """Test the auto date value determination."""
    today = datetime.datetime.now(timezone.utc).astimezone().isoweekday()
    if today == 7:  # Sunday
        expected = 1  # Monday
    elif GET_NEXT_DAY:
        expected = today + 1
    else:
        expected = today
    result = program_auto_get_date_value(get_next_day=GET_NEXT_DAY)
    assert result == expected, "Should return next day's date"

def test_validate_user_date_input():
    assert validate_user_date_input('monday') == 1, "Should return 1 for 'monday'"
    assert validate_user_date_input('Monday') == 1, "Should handle case insensitivity"
    # Assuming the function accepts an abbreviation (if implemented)
    # For example, if 'mon' is accepted as Monday:
    # assert validate_user_date_input('mon') == 1, "Should handle shortcut abbreviation for days"
    assert validate_user_date_input(8) is False, "Should return False for invalid numeric input"
    assert validate_user_date_input('8') is False, "Should return False for invalid numeric input"
    assert validate_user_date_input(3) == 3, "Should validate and return integer for valid weekday"
    assert validate_user_date_input('3') == 3, "Should validate and return integer for valid weekday"
    assert validate_user_date_input('March 33') is False, "Should return False for non-existent date string"

def test_get_day_name():
    assert get_day_name(1) == "Monday", "Should return 'Monday' for 1"
    assert get_day_name(7) == "Sunday", "Should return 'Sunday' for 7"

@pytest.mark.skip(reason="insert_time_slot_at_position not implemented yet")
def test_insert_time_slot_at_position():
    # TODO: Write tests once insert_time_slot_at_position is implemented.
    pass

def test_timeSlotStandardizer():
    """Tests the correct creation of reference dictionaries from a list of time slots."""
    time_slots = ['9:00am', '10:00am', '11:00am']
    expected_numbers_to_strings = {0: '9:00am', 1: '10:00am', 2: '11:00am'}
    expected_strings_to_numbers = {'9:00am': 0, '10:00am': 1, '11:00am': 2}
    
    nts, stn = timeSlotStandardizer(time_slots)
    assert nts == expected_numbers_to_strings, "Numbers to strings mapping should match expected"
    assert stn == expected_strings_to_numbers, "Strings to numbers mapping should match expected"

def test_fill_time_slots_inbetween_A_and_B():
    """Tests the correct identification of time slots between two given times."""
    time_slots = ['9:00am', '10:00am', '11:00am']
    expected_results = ['9:00am', '10:00am', '11:00am']
    nts, stn = timeSlotStandardizer(time_slots)  # nts: number->string, stn: string->number

    results = fill_time_slots_inbetween_A_and_B('9:00am', '11:00am', stn, nts)
    assert results == expected_results, "Should list all time slots between 9:00am and 11:00am, inclusive"

    boundary_results = fill_time_slots_inbetween_A_and_B('9:00am', '9:00am', stn, nts)
    assert boundary_results == ['9:00am'], "Should handle the case where A and B are the same"

    inverse_results = fill_time_slots_inbetween_A_and_B('11:00am', '9:00am', stn, nts)
    assert inverse_results == [], "Should return an empty list if A is later than B"

def test_seek_valid_time_slot():
    """Test seeking valid time slots with various inputs."""
    time_slots = ['9:00am', '10:00am', '11:00am', '8:00pm']
    with pytest.raises(ValueError):
        seek_valid_time_slot('invalid', time_slots)
    assert seek_valid_time_slot('9:25am', time_slots) == '9:00am', "Should return correct index for '9:25am'"
    assert seek_valid_time_slot('10:30am', time_slots) == '11:00am', "Should return correct index for '10:30am'"
    assert seek_valid_time_slot('10:45am', time_slots) == '11:00am', "Should return correct index for '10:45am'"
    assert seek_valid_time_slot('3:45pm', time_slots) == '8:00pm', "Should return correct index for '3:45pm'"

def test_get_current_week():
    """Test week calculation functionality."""
    test_date = '03/01'
    result = get_current_week(test_date, False)
    assert result.startswith('Week '), "Should return a week string"
