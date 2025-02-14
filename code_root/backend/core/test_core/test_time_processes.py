import unittest
from time_processes import *
from datetime import datetime

class TestTimeProcesses(unittest.TestCase):
    
    def program_auto_get_date_value(self):
        """Test the auto date value determination."""
        today = datetime.datetime.now(timezone.utc).astimezone().isoweekday()
        if today == 7: #Sunday
            expected = 1  # Monday
        else:
            expected = today + 1
        self.assertEqual(program_auto_get_date_value(get_next_day=True), expected, "Should return next day's date")
    
    def test_validate_user_date_input(self): 
        self.assertEqualself.assertEqual(validate_user_date_input('Monday'), 1, "Should return 1 for Monday")
        self.assertEqual(validate_user_date_input('monday'), 1, "Should handle case insensitivity")
        self.assertEqual(validate_user_date_input('monday'), 1, "Should handle shortcut abbrv for days")
        self.assertEqual(validate_user_date_input('8'), False, "Should return False for invalid numeric input")
        self.assertEqual(validate_user_date_input(3), 3, "Should validate and return integer for valid weeekdays")
        self.assertEqual(validate_user_date_input('March 33'), False, "Should return False for non-existent date string")

    def test_get_day_name(self): 
        self.assertEqual(get_day_name(1), "Monday", "Should return 'Monday' for 1")
        self.assertEqual(get_day_name(7), "Sunday", "Should return 'Sunday' for 7")
    
    def test_insert_time_slot_at_position(self): #TODO important to write a test for this
        pass
    
    def test_timeSlotStandardizer(self):
        """Tests the correct creation of reference dictionaries from a list of time slots."""
        time_slots = ['9:00am', '10:00am', '11:00am']
        expected_numbers_to_strings = {0: '9:00am', 1: '10:00am', 2: '11:00am'}
        expected_strings_to_numbers = {'9:00am': 0, '10:00am': 1, '11:00am': 2}
        
        nts, stn = timeSlotStandardizer(time_slots)

        self.assertEqual(nts, expected_numbers_to_strings, "Numbers to strings mapping should match expected")
        self.assertEqual(stn, expected_strings_to_numbers, "Strings to numbers mapping should match expected")
    
    def test_fill_time_slots_inbetween_A_and_B(self): #TODO important to write a test for this
        """Tests the correct identification of time slots between two given times."""
        time_slots = ['9:00am', '10:00am', '11:00am']
        nts, stn = timeSlotStandardizer(time_slots)  # Reusing the standardizer function to get StN dictionary

        # Using the dictionary from the standardizer to test filling times
        results = fill_time_slots_inbetween_A_and_B('9:00am', '11:00am', stn, nts)
        expected_results = ['9:00am', '10:00am', '11:00am']

        self.assertEqual(results, expected_results, "Should correctly list all time slots between 9:00am and 11:00am, inclusive")

        # Testing boundary conditions
        boundary_results = fill_time_slots_inbetween_A_and_B('9:00am', '9:00am', stn, nts)
        self.assertEqual(boundary_results, ['9:00am'], "Should handle the case where A and B are the same")

        # Testing input where A > B should logically return an empty list if implemented, or handle as per function design
        inverse_results = fill_time_slots_inbetween_A_and_B('11:00am', '9:00am', stn, nts)
        self.assertEqual(inverse_results, [], "Should return an empty list if A is later than B")

    
    def test_seek_valid_time_slot(self): #TODO important to write a test for this
        pass
    
    def test_get_current_week(self):
        test_date = '03/01'
        result = get_current_week(test_date, False)
        self.assertTrue(result.startswith('Week '), "Should return a week string")

if __name__ == '__main__':
    unittest.main()