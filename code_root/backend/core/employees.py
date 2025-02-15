from code_root.config.settings import UNAVAILABILITY_TASK, SWAT_EMPLOYEE_INFO_CSV
from code_root.config.utility import timer
from code_root.backend.core.time_processes import fill_time_slots_inbetween_A_and_B, seek_valid_time_slot
from typing import Any
import csv

class EmployeeManager:
    """"For operations that involve multiple employees or require knowledge about the entire collection of employees"""
    def __init__(self):
        self.employees = {} #stores name & instances of employee class

    #setsup everythign else, thing of as instantiator for employee objs

    def add_employee(self, employee_name, employee_inst, dayTimeSlotsKeysList): #employee instance, also idk if most efficent way to create these instances
        """Adds an employee to the system with the specified name and instance.
        Args:
            self: The reference to the current object.
            employee_name (str): The name of the employee to be added.
            employee_inst: The instance of the employee to be added.
            dayTimeSlotsKeysList: A list of day-time slot keys for setting default availability.
        """ 
        self.employees[employee_name] = employee_inst
        self.employees[employee_name].set_default_availability(dayTimeSlotsKeysList)
        
    def set_employee_availability(self, employee_name, unavailable_time_slots: list[str]):
        """Sets employee availbility
        Args:
            unavailable_time_slots (list): List of unavailable timeslots, they must be valid timeslots in the timeslots for the day tho...
        """
        employee = self.employees[employee_name]
        if employee:
            employee.set_unavailability(unavailable_time_slots)
            #For output, just directly assigns an employee a task defined by unavaibility constant, thus not have to go thru algo. (not a task obj, just puts a str named unavailable into assigned tasks)

    def set_and_assign_employee_availability(self, employee_name, unavailable_time_slots: list[str]):
        """Sets employee availbility, plus adds the unavailability task to assigned tasks for schedule ouput.
        Args:
            unavailable_time_slots (list): List of unavailable timeslots, they must be valid timeslots in the timeslots for the day tho...
        """
        employee = self.employees[employee_name]
        if employee:
            employee.set_unavailability(unavailable_time_slots) #Employee??????? 
            #For output, just directly assigns an employee a task named Unavailable, thus not have to go thru algo. (not a task obj, just puts a str named unavailable into assigned tasks)
            employee.assign_task(unavailable_time_slots, UNAVAILABILITY_TASK)

    def get_employee_by_name(self, name):
        return self.employees.get(name)

    def total_available_time_slots(self):
        return sum(employee.sum_available_time_slots() for employee in self.employees) 

    def get_available_employees(self, time_slot: str) -> set[str]:
        available_at_time: set = set()
        for employee in self.employees:
            if self.employees[employee].is_available(time_slot):
                available_at_time.add(employee)
        return available_at_time #NOTE changed from dict to set
    
    def get_employees_with_traits(self, **traits: dict) -> set[str]: #TODO need to write unit tests for all of these, very important
        """Currently get employees from pool of all registered employees"""
        #is a set, not a dictionary 
        eligible_employees = {
            employee for employee in self.employees
            if all(getattr(employee, trait, None) == value for trait, value in traits.items()) #WHY - none prevents attr error if employee doesnt have that trait
        }  # WHY ok so if no reqs traits = one how to include employees that may meet the traits, wait no do that seperatley this should only be if the task has cert reqs
        return eligible_employees
    
    def get_employees_in_pool_with_traits(self, pre_filtered_employees: dict, **traits: dict) -> set[str]: #TODO need to write unit tests for all of these, very important
        """Currently get searches master list to get only prespecified employees list, who also have the traits"""
        #is a set, not a dictionary
        eligible_employees = {
            employee for employee in pre_filtered_employees.keys()
            if all(getattr(self.employees[employee], trait, None) == value for trait, value in traits.items()) #WHY - none prevents attr error if employee doesnt have that trait
        }
        return eligible_employees
    
    def assign_task_to_employee(self,employee_name, task, time_slot: list[str]): 
        self.employees[employee_name].assign_task(time_slot, task)           

class Employee:
    """For operations that involve manipulating an employee's attributes
    BTW need dayTimeSlotsKeysList to be predefined, bc in class method and can't pass argument if makes any sense, WUT???"""
    
    """#default times for taks assigned to - based on previous user input. #rename var later???? idk
    default_assigned_to_times = None

    @classmethod
    def define_default_assigned_to_times(cls, dayTimeSlotsKeysList):
        cls.default_assigned_to_times = {time_slot: None for time_slot in dayTimeSlotsKeysList}
        
    if Employee.default_assigned_to_times is None:
        raise ValueError("Default assigned times not defined. Call Employee.define_default_assigned_to_times() first.")
        self.name = name
        
    Employee.default_assigned_to_times.copy() # Pre-populate each employee's assigned times with defaults (copied) so that:
    #   - Every timeslot is represented (even if no task is assigned, ensuring consistent Excel output).
    #   - Changes to the defaults later don't affect already instantiated employees.
    # Future work: streamline default assignment, possibly sourcing defaults externally.

    """

    def __init__(self, name, gender, default_assigned_to_times, preferences=None, certifications=None, position=None, off_week=None):
        #TODO LOAD IN LISTS N STUFF FOR ALL EMPLOYEE DETAILS
        self.name = name
        self.gender = gender
        self.preferences = preferences if preferences else []
        self.availability = {}
        self.assigned_to = default_assigned_to_times
        self.certifications = None
        
        # All for counsler version
        self.village = None #for later
        self.cabin = None #for later
        self.personal_time_schedule = None #for later
        self.co = None #for later

    def set_default_availability(self, time_slots: list[str]) -> None:
        for time_slot in time_slots:
            self.availability[time_slot] = True
            
    def set_unavailability(self, unavailable_times: list[str]) -> None:
        #modifies availability list, and 
        for time_slot in unavailable_times:
            if time_slot in self.availability:
                self.availability[time_slot] = False
            else:
                response = f"Time slot {time_slot} not recognized."

    def is_available(self, time_slot: str) -> str:
        """Defaults to false"""
        return self.availability.get(time_slot, False)

    def sum_available_time_slots(self):
        return sum(1 for available in self.availability.values() if available)
    
    def get_available_time_slots(self):
        return list(self.availability.keys())
    
    def assign_task(self, time_slot: Any, task: str) -> None:
        """adds the task to the employees dict of times and tasks assigned at time
        Args:
            time_slot (str): 7:00am etc
            task (str): TaskVarName
        """
        
        #DONE fix later for multiple for times assign to timeslot
        if isinstance(time_slot, list):
            for slot in time_slot:
                self.assigned_to.update({slot: task})
        else:
            self.assigned_to[time_slot] = task

class EmployeeAvailabilityLogic:
    def __init__(self, employee_manager):
        self.employee_manager = employee_manager

    def set_employee_availability(self, employee_name, unavailable_times, time_slot_to_index_map, index_to_time_slot_map):
        """Sets the unavailability times for a specified employee."""
        self.employee_manager.set_and_assign_employee_availability(employee_name, unavailable_times)

                      
    def multi_time_input_detector_and_converter_employee_unavailability(self, input_str: list[str], times_list: list[str], time_slot_to_index_map, index_to_time_slot_map) -> list[str]: #dayTimeSlotsKeysList
        # Why did i have it called before???
        # seek_valid_time_slot(time_list_minutes, time_list_minutes_compiled = time_list_minutes_compiled)
        
        #BUG NOTE watch parameters and args here
        def time_range_handler(input_val: list[str], times_list: list[str], time_slot_to_index_map, index_to_time_slot_map):
            #all come in list, need to get ride of list to use some methods in time rang handler

            timePair = input_val[0].split("-") #list obj has no value split
            for item in timePair:
                item.strip().lower() #This is just so the am/pm is lowercase to match the master time ref list (dayTimeSlots, which formatted like 8:00am etc) in the if statments below.
            if not timePair[0] in times_list: #Time1
                #how to propagate out to interface?? problematic_time_input_warning(timePair[0],dayTimeSlotsKeysList)
                timePair[0] = seek_valid_time_slot(timePair[0], times_list)
            if not timePair[1] in times_list: #Time2
                #problematic_time_input_warning(timePair[1],dayTimeSlotsKeysList)
                timePair[1] = seek_valid_time_slot(timePair[1], times_list)

            #now have valid timeslot refs, I can find all the values betwen the two and can mark all the times inbetween unavailable for the employee
            inbetween_slots_list_inclusive = fill_time_slots_inbetween_A_and_B(timePair[0],timePair[1], time_slot_to_index_map, index_to_time_slot_map)
            return inbetween_slots_list_inclusive
        
        #Actual logic process --------------------
        SecondListExpandedValues = [] #BEWARE this is to prevent runaway loops, bc im paranoid that ill wind up with a loop if it goes through and keeps expanding as it append in a for loop
        
        #Parser
        
        #TODO figure out how to incorperate this error: ['9:15am-1:45pm,']
        if any("," in item for item in input_str): #generator so can check inside each string value for character, and stop as soon as evaluates to True
            #so can input stuff as 6am, 7pm, 4:45am then split into indvs in list
            
            try: #prevent split() error for '9:15am-1:45pm,'
                split_times_list = input_str.split(",") #string.split(separator, maxsplit) default = -1 is as many as occur
            except:
                split_times_list = input_str #just goes as 9:15am-1:45pm and processed like normal
                
            for item in split_times_list:
                item.strip().lower() #Remove trailing whitespace
                if "-" in item:
                    SecondListExpandedValues.extend(time_range_handler(item, times_list, time_slot_to_index_map, index_to_time_slot_map))
                else: #Incase value isnt "-" but ","
                    if not item in times_list: #incase not a valid time.
                        SecondListExpandedValues.append(seek_valid_time_slot(item, times_list))
                        #problematic_time_input_warning(item,dayTimeSlotsKeysList) #NOTE REMOVE I/O make detaches
                    else: 
                        SecondListExpandedValues.append(item)
                #put "-" in here so can make multiple multi values if put in list form
        elif any("-" in item for item in input_str):
            #WUT - #WHY - bc maybe user input 7-8am, 10-11am. if put "-" then would trigger, but wouldnt realize is part of larger list
                #assuming just one 7:00am-8:00pm type
                SecondListExpandedValues.extend(time_range_handler(input_str, times_list, time_slot_to_index_map, index_to_time_slot_map))
        #TODO what about single times??????
        else:
            SecondListExpandedValues.extend(input_str) #3:45pm extend() so doesn't double list [[]] the single time, bc the variable is a list
        return SecondListExpandedValues
        #WHY should return a list, then at the place called i can decide how it will be joined / added to other vars based on circumstance.
        
        #TODO this one def need a unit test
        """
        #make handle inputs such as 7am-9:15am, 7-9:15am, give an error if 7am-AnyNumberWithout AM/PM, raise and exception if impossible calc such as TimeB starts before A, make cycle if invalid time. Make a exit emergency statement to exit the loop?????
        #TODO do that calcs gap or goes to nearest one, then calcs difference and inputs it.
        #iterates up and down until it reaches closest value. well checks if has :, and not 00, or
        # maybe then iterates thru and finds the cloest one. Could at :00 to 8am then iterate until match see which takes list iteraiton. then find lengths idk
        """


#WHY FIGURE OUT WHAT TO DO WITH and why no return
def add_employees_from_csv(self, file_name=SWAT_EMPLOYEE_INFO_CSV, file_dialect = 'excel', new_line_value = '', encoding_value = 'utf-8-sig'):
    """Converts a CSV file of standard tasks into a dictionary where keys are task identifiers and values are Task objects.
    Args:
    csvfile (str): Path to csv file
    file_dialect (str): Dialect of file, defaults to 'excel'. WHY - csv module has dialect option idk if make diff, also i make my csvs in excel."""
    
    with open(file_name, newline=new_line_value, encoding=encoding_value) as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect=file_dialect)  
        
        for row in csvreader:
            # Use the column headers as keys the rows as values
            #Second have auto cycle through and popualte all class attribtues with data from CSV) # Create a new Task instance and store it with the user-defined name as the key
            
            employee_details = {
                #TODO eventually figure out how to modularize
                #NOTE the keys are attr names, so don't fuck with them as other function rely on them
                    'task_name': row.get('TaskName'),
                    'task_frequency': row.get('Frequency'),
                    'start_time': row.get('StartTime'),
                    'duration': row.get('TaskDuration'),
                    'min_num_people_needed': row.get('MinNumPeopleNeeded'),
                    'importance': row.get('Importance', None),  
                }

def define_default_assigned_to_times(time_slot_labels: list) -> dict[Any, None]:
        """Define default times for tasks assigned to. 
        All times start start with None / Blank assigned because the algo hasnt assigned anything yet. 
        #NOTE may be a prob in future depending if and how i do preassigned tasks"""
        
        default_assigned_to_times = {time_slot: None for time_slot in time_slot_labels}
        return default_assigned_to_times

@timer        
def instantiate_employees(employee_manager, time_slot_labels: list, employee_names, employee_genders) -> EmployeeManager:
    default_assigned_to_times = define_default_assigned_to_times(time_slot_labels)
    for name, gender in zip(employee_names, employee_genders): #can add any number of args, returns results as a tuple 
        employee_instance = Employee(
            name,
            gender,
            default_assigned_to_times
            )
        
        employee_manager.add_employee(name, employee_instance,time_slot_labels)
    return employee_manager
