
from config.settings import noAnswers, yesAnswers, femaleAnswers, maleAnswers
from config.utility import timer
from backend.core.time_processes import fill_time_slots_inbetween_A_and_B, find_valid_time_slot
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from typing import Dict, List, Any


def get_employee_name_gender_list_from_csv():
    pass
#TOOD eventually make it so that get employee info from here then pass it into the main file???

class EmployeeManager:
    """"For operations that involve multiple employees or require knowledge about the entire collection of employees"""
    def __init__(self):
        self.employees = {} #stores name & instances of employee class

    #setsup everythign else, thing of as instantiator for employee objs

    def add_employee(self, employee_name, employee_inst,dayTimeSlotsKeysList): #employee instance, also idk if most efficent way to create these instances
        """Adds an employee to the system with the specified name and instance.
        Args:
            self: The reference to the current object.
            employee_name (str): The name of the employee to be added.
            employee_inst: The instance of the employee to be added.
            dayTimeSlotsKeysList: A list of day-time slot keys for setting default availability.
        """ 
        self.employees[employee_name] = employee_inst
        self.employees[employee_name].set_default_availability(dayTimeSlotsKeysList)
        #note typically the function runtime for 23 employees on a monday is around 0.000029 seconds. 
        #Or 0.00000126086sec per employee.

    def set_employee_availability(self, employee_name, unavailable_time_slots):
        """Sets employee availbility
        Args:
            unavailable_time_slots (list): List of unavailable timeslots, they must be valid timeslots in the timeslots for the day tho...
        """
        employee = self.employees[employee_name]
        if employee:
            employee.set_unavailability(unavailable_time_slots) #Employee??????? 


    def get_employee_by_name(self, name):
        return self.employees.get(name)

    def total_available_time_slots(self):
        return sum(employee.sum_available_time_slots() for employee in self.employees) 

    def get_available_employees(self, time_slot):
        available_at_time = {}
        for employee in self.employees:
            if self.employees[employee].is_available(time_slot):
                available_at_time[employee] = None
        return available_at_time
    
    def get_employees_with_traits(self, **traits):
        #TODO idk how if even possible to make into dictionary comprehension
        #TODO need to understand better
        eligible_employees = {
            employee for employee in self.employees
            if all(getattr(employee, trait, None) == value for trait, value in traits.items()) #WHY - none prevents attr error if employee doesnt have that trait
        }  # WHY ok so if no reqs traits = one how to include employees that may meet the traits, wait no do that seperatley this should only be if the task has cert reqs
        return eligible_employees
    
    def assign_task_to_employee(self,employee_name, task, time_slot): 
        self.employees[employee_name].assign_task(time_slot, task)           

class Employee:
    """For operations that involve manipulating an employee's attributes
    BTW need dayTimeSlotsKeysList to be predefined, bc in class method and can't pass argument if makes any sense"""
    
    #default times for taks assigned to - based on previous user input. #rename var later???? idk
    default_assigned_to_times = None

    @classmethod
    def define_default_assigned_to_times(cls, dayTimeSlotsKeysList):
        """Define default times for tasks assigned to."""
        cls.default_assigned_to_times = {time_slot: None for time_slot in dayTimeSlotsKeysList}

    def __init__(self, name, gender, preferences=None, certifications=None, position=None, off_week=None):
        self.name = name
        self.gender = gender
        self.preferences = preferences if preferences else []
        self.availability = {} #time_slot: True for time_slot in get_all_time_slots(), i think benifit of making timeSlots a dicitonary is that dont have to iterate and assign true to each one, but then have to use all those funcitons on it which complicates things. hmmmmmmmm
        self.assigned_to = Employee.default_assigned_to_times.copy() #Time: Task. #WHY set times ahead of time, timeslots for day are already set at this point, so if a employee doesn't get assgined a task for a slot it will report as none, that way it doesn't mess up the output order (by having a gap) when printed to excel or such. Tasks can still be assigned as needed. Better way to implement?
        #TODO review this later #WHY -  .copy() This creates a shallow copy of default_assigned_to_times and assigns it to self.assigned_to, ensuring that changes to self.assigned_to do not affect the class variable default_assigned_to_times or those in other instances. - GPT Reccomendaition 
        self.availabile_time_list = None #so can ref this list once rather than having to figure out available times via loop over and over again.
        
        #will have to make a way to easily insert these from other sources
        self.developerbonus = None #will actuallly need to be an if statement in the main code, #prob unethical to include this but lol, i can set my task pref to have maybe 10% more weight
        self.certifications = None
        self.village = None #for later
        self.cabin = None #for later
        self.personal_time_schedule = None #for later
        self.co = None #for later

    def set_default_availability(self, time_slots):
        for time_slot in time_slots:
            self.availability[time_slot] = True
            
    def set_unavailability(self, unavailable_times):
        for time_slot in unavailable_times:
            if time_slot in self.availability: #adds some time to program, plus dont know if really nessecary with accoutning for it in multi times func
                self.availability[time_slot] = False
            else:
                print(f"Time slot {time_slot} not recognized.")

    def is_available(self, time_slot):
        return self.availability.get(time_slot, False) #WAIT IS THIS RIGHT? need to initalize first, maybe upoun creation, butthen order dependent. #NEED A CHECK BEFORE ALGO THAT ALL THINGS ARE INITALIZED???

    def sum_available_time_slots(self):
        return sum(1 for available in self.availability.values() if available)
    
    def get_available_time_slots(self):
        return list(self.availability.keys())
    
    def assign_task(self, time_slot: Any, task: str):
        """adds the task to the employees dict of times and tasks assigned at time
        Args:
            time_slot (str): 7:00am etc
            task (str): TaskVarName
        """
        #TODO DONE fix later for multiple for times assign to timeslot
        if isinstance(time_slot, list):
            for slot in time_slot:
                self.assigned_to.update({slot: task})  #LEARNING CONCEPT update() is like the dictionary equivlent of the list extend() method, dont forget curly braces {}! self.assigned_to.update({time_slot: task})
        else:
            self.assigned_to[time_slot] = task

class EmployeeAvailabilityLogic:
    def __init__(self, employee_manager):
        self.employee_manager = employee_manager

    def set_employee_unavailability(self, employee_name, unavailable_times):
        """Sets the unavailability times for a specified employee."""
        self.employee_manager.set_employee_availability(employee_name, unavailable_times)
    
    @timer                   
    def multi_time_input_detector_and_converter_employee_unavailability(input_str, times_list, dayTimeSlots, dayTimeSlotsKeysList):
        
        time_list_minutes_compiled = False #WHY thing to help only compile list once in function, and then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
        time_list_minutes = []
        #NOTE BUG check this inner outer scope, thing prob will cause problems
        find_valid_time_slot(time_list_minutes,time_list_minutes_compiled = time_list_minutes_compiled)
        
        @timer #BUG NOTE watch parameters and args here
        def time_range_handler(input_val, dayTimeSlots, times_list):
            timePair = input_val.split("-")
            for item in timePair:
                item.strip().lower() #This is just so the am/pm is lowercase to match the master time ref list (dayTimeSlots, which formatted like 8:00am etc) in the if statments below.
            if not timePair[0] in dayTimeSlots[0]: #Time1
                #how to propagate out to interface?? problematic_time_input_warning(timePair[0],dayTimeSlotsKeysList)
                timePair[0] = find_valid_time_slot(timePair[0],times_list)
            if not timePair[1] in dayTimeSlots[0]: #Time2 
                #problematic_time_input_warning(timePair[1],dayTimeSlotsKeysList)
                timePair[1] = find_valid_time_slot(timePair[1],times_list)

            #now have valid timeslot refs, I can find all the values betwen the two and can mark all the times inbetween unavailable for the employee
            inbetween_slots_list_inclusive = fill_time_slots_inbetween_A_and_B(timePair[0],timePair[1])
            return inbetween_slots_list_inclusive
        
        #Actual logic process --------------------
        SecondListExpandedValues = [] #BEWARE this is to prevent runaway loops, bc im paranoid that ill wind up with a loop if it goes through and keeps expanding as it append in a for loop
        
        #Parser
        if "," in input_str: #so can input stuff as 6am, 7pm, 4:45am then split into indvs in list
            split_times_list = input_str.split(",") #string.split(separator, maxsplit) default = -1 is as many as occur
            
            for item in split_times_list:
                item.strip().lower() #Remove trailing whitespace
                
                if "-" in item:
                    SecondListExpandedValues.extend(time_range_handler(item))
                
                else: #Incase value isnt "-" but ","
                    if not item in dayTimeSlots[0]: #incase not a valid time.
                        SecondListExpandedValues.append(find_valid_time_slot(item,times_list))
                        #problematic_time_input_warning(item,dayTimeSlotsKeysList) #NOTE REMOVE I/O make detaches
                    else: 
                        SecondListExpandedValues.append(item)
                #put "-" in here so can make multiple multi values if put in list form
        else: #WHY - bc maybe user input 7-8am, 10-11am. if put "-" then would trigger, but wouldnt realize is part of larger list
            if "-" in input_str:
                SecondListExpandedValues.extend(time_range_handler(input_str))
        return SecondListExpandedValues
        #WHY should return a list, then at the place called i can decide how it will be joined / added to other vars based on circumstance.
        
        """
        #make handle inputs such as 7am-9:15am, 7-9:15am, give an error if 7am-AnyNumberWithout AM/PM, raise and exception if impossible calc such as TimeB starts before A, make cycle if invalid time. Make a exit emergency statement to exit the loop?????
        #TODO do that calcs gap or goes to nearest one, then calcs difference and inputs it.
        #iterates up and down until it reaches closest value. well checks if has :, and not 00, or
        # maybe then iterates thru and finds the cloest one. Could at :00 to 8am then iterate until match see which takes list iteraiton. then find lengths idk
        """

@timer        
def instantiate_employees(employee_manager,dayTimeSlotsKeysList,employeeNamesList,employeeGenderList):
    Employee.define_default_assigned_to_times(dayTimeSlotsKeysList)
    for name, gender in zip(employeeNamesList, employeeGenderList): #can add any number of args, returns results as a tuple 
        employee_instance = Employee(
            name,
            gender
            ) #wierd dict dup thing gonna be a prob?
        employee_manager.add_employee(name, employee_instance,dayTimeSlotsKeysList)
    return employee_manager
    