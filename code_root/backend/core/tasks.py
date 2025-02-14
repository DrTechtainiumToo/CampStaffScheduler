from code_root.config.settings import SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV, SWAT_NIGHT_CHORES_INFO_CSV
from code_root.config.utility import timer
import csv
from typing import Any, ParamSpec, Concatenate #LEARN
from collections.abc import Callable
import re


def try_convert_to_int(value): #TODO figure out try/excpet and how to deal with none args
    """Use when have csv values that ur assigning to function attr but need them to be ints, instead of the standard string.
    If unconvertable, None for instances, sets value = 0"""
    try:
        return int(value)
    except ValueError:
        return 0  #IF ERROR, check this, sets to 0

class TaskManager:
    """Describe"""
    def __init__(self, defaultTasksDictionary):
        if not isinstance(defaultTasksDictionary, dict):
            raise TypeError("defaultTasksDictionary must be a dictionary")
        self.tasks = {**defaultTasksDictionary} # A list to hold all tasks, add specialTasksDict later **specialTasksDict
    
    def add_task(self, task_identifier, task):
        self.tasks[task_identifier] = task

    def delete_task(self, task_identifier):
        if task_identifier in self.tasks:
            del self.tasks[task_identifier]
              
    def total_tasks_for_today(self):
        # Similarly, this is a placeholder. You need to add logic to count today's tasks specifically.
        return len(self.tasks)

    #NOTE NOT IN USE
    def assign_to(self, time_slot, employee_name):
        """assign employee to what task, this is confusing on task instances vs employee and who adds to who"""
    # maybe it is smart to just update per all of them that go thru, faster than having to recalc, can just do -1 or whatever, keep in mind if need to optimize, it was dumb of me to delete all those functions
    
    
    
    def get_task_cert_reqs(self, task_name) -> dict:
        certs_req = self.tasks[task_name].certs_required
        if certs_req is not None and certs_req != "No": #change No(s) later
            return certs_req

    def get_task_gender_reqs(self, task_name) -> dict[str, str]:
        """Return: dict{gender name : # req}"""
        
        # {'male': 'only'} {'female': 'only'} only males or females for task #would look like female:only in csv or or female only, female 2, or male only or male 2
        # {'male': 2, 'female': 3} 2 males and 3 females for the task
        gender_reqs = self.tasks[task_name].gender_required
        if gender_reqs is not None and gender_reqs != "No": #only inlcude req if there is a req inputted if empty, dont return anything - is a simpler system than checking
            return gender_reqs 
            
    
    def recalculate_distance_to_deadline(self, task_name: str, current_time: str, dayTimeSlotsStandardizedStN: dict[str, int]) -> int:
        """updates the distance to deadline for task, by recalculating what it would be for the current period, returns (int) distance"""
        current_timeslot: int = dayTimeSlotsStandardizedStN[current_time]
        deadline: int = dayTimeSlotsStandardizedStN[self.tasks[task_name].due_by]
        distance: int = deadline - current_timeslot
        return distance
    
    class Task():
        task_attribute_guide = {
        "task_name": "The name of the task.",
        "frequency": "Frequency indicates the number of time periods a task is available for scheduling in a day, not the total number of times it will be scheduled. The actual number of task instances is determined by multiplying this frequency by the min_num_people_needed, which specifies how many people are required for each instance. Essentially, the task's total daily instances equal its frequency times the minimum people required.",
        "start_time": "Primary start time for the task. Additional start times can be specified in start_time2 to start_time6 attributes.",
        "duration": "The expected duration of the task. Enter an integer (1,2,3,4 etc). NOTE: Each duration increment is equal to one time period on the schedule",
        "min_num_people_needed": "The minimum number of people required to complete the task.",
        "importance": "The importance level of the task, which might affect scheduling priority.",
        "task_cost": "Calculated based on various factors such as frequency and duration. Represents the 'cost' or effort of the task, is mainly for the algorithim to figure out how to priortize things and see if a solution is possible",
        "preassigned_to": "The person or group preassigned to the task. Optional, may be decided during task scheduling.",
        "chosen": "Indicates if the task has been chosen to be performed. Can be True/False.",
        "task_tier": "The tier or level of the task, which might categorize its priority or type.",
        "gender_required": "Specifies the gender required for gender-specific tasks.",
        "preassigned": "Indicates if the task is pre-assigned to someone specific.",
        "window": "Wether or not the task has a time window in which it must occur. In contrast to \"static\" tasks that occur according to their start times",
        "time_preferred": "Alternative or additional preferred start times for the task.",
        "earliest_start": "The earliest time the task should start (assumes task has a window).",
        "due_by": "When the task is due",
        "scheduledoccurance": "Specifies if the task has a scheduled occurrence, potentially overriding other timing preferences.",
        "occurs_every_n_days": "For repeating tasks, specifies the interval in days between each occurrence.",
        "spawn_days": "Specifies on which days of the week the task is applicable, allowing for weekly scheduling patterns."
        # Add additional attributes as needed.
        }
        
        #class attr bc don't want to be dealing with this constant for every instantiation
        
        dayTimeSlotsKeysList = None
        
        @classmethod
        def define_default_assigned_to_times(cls, dayTimeSlotsKeysList):
            """Define default times in day"""
            cls.dayTimeSlotsKeysList = dayTimeSlotsKeysList
        
        def __init__(self, task_name, task_frequency, start_time, duration, min_num_people_needed, importance, pre_assigned_to, certs_required, gender_required, task_tier = None, **kwargs):
            #WHY **args, was gettign confused abotu KWARGS and assignment with csv converter rows, bc this one kwarg wasnt working, and was consulting GPT4
            #GPT4 reccomended that i use kwargs for optional ones to simplify the func call and i thought it was a good idea.
            
            #WUT????? - maybe so can have master converter so that no matter what in csv can assign it to that value and funct arent depenet on specific words???
            #ALL NEGATIVES IN CSV NEED TO CHANGE
            #1.1 = userInput
            #1.21 = allMales
            #1.22 = allFemales
            #1.6 for playtime: sum of timeslots btwn breakfast and lunch or lunch and dinner
            #1.7 number of employees / (num sum of timeslots btwn breakfast and lunch or lunch and dinner) (unless a counsler, then include night off, but more complicated cus vilbo and other stuff)
            #1.8 remainder_of_unassigned_slots
            #1.9 unassigned_employeess
            #4 Last
            #5 Very last
            #NOTE DONT USE FLOATS, ints are faster
                        
            def safe_int_conversion(value):
                """WHY - Use when have csv values that ur assigning to function attr but need them to be ints, instead of the standard string. Returns 1, if error"""
                try:
                    return int(value)
                except (ValueError, TypeError):
                    return 1 
            self.tier = safe_int_conversion(task_tier)
            #WHY - task_tier is not included in the **kwargs & assignment loop below bc i need to explicity make it a int, and simpler to do it this way.
             
            self.task_name = task_name
            self.frequency = task_frequency
            self.duration = duration
            self.min_num_people_needed = min_num_people_needed
            self.importance = importance
            
            def process_gender_text(input_text) -> dict[str, str | int]:
                if not input_text:
                    # Handle the case where the input is None or empty
                    return {}
    
                segments = input_text.split(', ')
                result = {}
        
                # Regex to extract key and value
                pattern = re.compile(r"(male|female)(\d+|only|all)")

                for segment in segments:
                    match = pattern.match(segment)
                    if match:
                        key = match.group(1)
                        value = match.group(2)

                        if value.isdigit():
                            # Convert digit strings to integers and sum them
                            result[key] = result.get(key, 0) + int(value)
                        else:
                            # Assign non-digit values directly, overwriting any previous numbers
                            result[key] = value
                return result
                    
            def process_pre_assigned(name_string, delimiter=',') -> tuple[str]:
                #Mock: "Alice, Bob, Charlie, Diana"
                
                # Split the string by the specified delimiter and strip whitespace from each name
                if not name_string: #removed the strip
                    return ()
                names = [name.strip() for name in name_string.split(delimiter)]
                return names
                
            def process_certifications(input_text) -> dict[str, int]:
                #Mock: "Silver1,Gold2,Silver1,Platinum3,Bronze1"
                
                if not input_text:
                    return {}
                
                # Regex to extract certification name and the number
                pattern = re.compile(r"(\w+)(\d+)")

                result = {}
                segments = input_text.split(',')
                
                for segment in segments:
                    match = pattern.match(segment)
                    if match:
                        cert_name = match.group(1)
                        num_required = int(match.group(2))

                        # Sum the numbers for each certification
                        result[cert_name] = result.get(cert_name, 0) + num_required
                
                return result

            self.pre_assigned_to: list[str] = process_pre_assigned(pre_assigned_to, delimiter=',')
            self.certs_required: dict[str, int] = process_certifications(certs_required)
            self.gender_required: dict[str, int] = process_gender_text(gender_required)
            
            # Assign all additional parameters
            for key, value in kwargs.items():
                setattr(self, key, value)
                #NOTE make key in kwargs what you want the attr name to be, so func can use consistently
    
            #Interally calcualted attributes
                # WHY - assigned after additional **kwargs para, so have all the data needed from other attrs.
            self.start_time: list[str] = [time for time in [start_time, self.start_time2, self.start_time3, self.start_time4, self.start_time5, self.start_time6, self.start_time7]] #Thanks GPT4 
            self.start_times_iter = 0
            self.assigned_to: dict[str, list[str]] = {key: [] for key in TaskManager.Task.dayTimeSlotsKeysList} #Time, and who assigned to (in list) #when, who
            self.task_cost = "To be caculated at assignment time in algorith with calc_task_cost()"
              
        def calc_task_cost(self):
            self.task_cost = self.task_frequency*len(self.start_time) #what if for multiple durations??
            #TODO idk if work but can call during althorithm to calc exact freq 
            #worry about later
        
        #NOTE DEPRECIATED - being split into two methods which will be acessed at employee manager level, will keep for now tho
        def get_task_requirements(self): #TODO make check more dynamic with settings 
            """Should return with requirments or empty if None"""
            req_dict = {}
            if self.gender_specific is not None and self.gender_specific != "No": #only inlcude req if there is a req inputted if empty, dont return anything - is a simpler system than checking
                req_dict["gender"] = self.gender_required #or gender specific #WHY - so the keys should be the attr names of the mpoyees bc it will use the key name to see it employee has that attr then compares the .self val to the employee val to see if match
            if self.certs_required is not None and self.certs_required != "No": #change No(s) later
                req_dict["certifications"] = self.certs_required
                #may have to figure out to include how many eventually and make that work with the serch algo, also may have to use an "OR"
                #FUTURE, evantually maybe make this a dict comprehension??? so can jsut edit the names / reqs in a list?
            return req_dict
        
        def assign_employee_to_task(self,time_slot,employee_name):
            """(list) time_slot, must be valid slot from days timeslot list"""
            if isinstance(time_slot, list): #TODO maybe at some point make these to take dictionaries so would be smaller adn more efficent??
                for slot in time_slot:
                    self.assigned_to[slot].append(employee_name)
            else:
                self.assigned_to[time_slot].append(employee_name) #IDK if will work #QUESTION - should be extend or append idk what if not pre exisitng lists
            #TODO make sure doesnt override and stuff, figure out later
        
        def describe_var_name_times(self): 
           return self.task_variable_name, self.start_time 

        #DONE fix up later
        def describe_verbose(self) -> list[list[str], list[str], str]:
            attributes = []
            for attr_name, attr_value in vars(self).items(): #use pythons introspection abilites to help with this, can use vars(), get the vars of the obj, using dir() would have to filter out built in attr and use getattr() method
                if attr_name in ['start_time2','start_time2','start_time3','start_time4','start_time5','start_time6']:
                    continue #skip attributes
                attributes.append(f"{attr_name.replace('_', ' ').title()}: {attr_value}")
            
            # Weekday spawns
            weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
            spawns = [self.spawn_sunday, self.spawn_monday, self.spawn_tuesday, self.spawn_wensday, self.spawn_thursday, self.spawn_friday, self.spawn_saturday]
            spawn_days = [day for day, spawn in zip(weekdays, spawns) if spawn]
            task_var_name = self.task_variable_name
            return attributes, spawn_days, task_var_name
         
class TaskDataConverter:
    def __init__ (self):
        self.tasks_dict = {}
        self.task_variable_names = []
        
    @timer
    def add_tasks_from_csv(self, file_name=SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV, file_dialect = 'excel', new_line_value = '', encoding_value = 'utf-8-sig'):
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
                task_details = {
                    #TODO eventually figure out how to modularize
                    #NOTE the keys are attr names, so don't fuck with them as other function rely on them
                        'task_name': row.get('TaskName'),
                        'task_frequency': row.get('Frequency'),
                        'start_time': row.get('StartTime'),
                        'duration': row.get('TaskDuration'),
                        'min_num_people_needed': row.get('MinNumPeopleNeeded'),
                        'importance': row.get('Importance', None),
                        'pre_assigned_to': row.get('PreassignedTo', None), #TODO Note for error checks, not yet implemented yet
                        'certs_required': row.get('CertificationsRequired', None),
                        'gender_required': row.get('GenderReq', None),
                        'task_cost': row.get('TaskCost', None),  # Calculated later, default set here if needed
                        'chosen': row.get('WillSpawnTodayChosen', None),
                        'task_tier': row.get('Tier', None),
                        'window': row.get('Window', None),
                        'time_preferred': row.get('TimePreferred', None),
                        'earliest_start': row.get('EarliestStart', None),
                        'due_by': row.get('DueBy', None),
                        'start_time2': row.get('StartTime2', None),
                        'start_time3': row.get('StartTime3', None),
                        'start_time4': row.get('StartTime4', None),
                        'start_time5': row.get('StartTime5', None),
                        'start_time6': row.get('StartTime6', None),
                        'start_time7': row.get('StartTime7', None),
                        'scheduled_occurance': row.get('ScheduledOccurance', None),
                        'occurs_every_n_days': row.get('OccursEveryNDays', None),
                        'spawn_sunday': row.get('SpawnSunday', None),
                        'spawn_monday': row.get('SpawnMonday', None),
                        'spawn_tuesday': row.get('SpawnTuesday', None),
                        'spawn_wensday': row.get('SpawnWensday', None),
                        'spawn_thursday': row.get('SpawnThursday', None),
                        'spawn_friday': row.get('SpawnFriday', None),
                        'spawn_saturday': row.get('SpawnSaturday', None),
                        'task_variable_name': row.get('TaskVariableName2'),
                        'category': row.get('Category', None),
                        'auto_schedule': row.get('AutoSchedule', None), #Wether to allow something to be auto suggested / added to schcedule.  
                        #lets say they only want the scheduler to only do certain tasks. For exmaple only schedule KSWAT periods for day and use can do everything else manual
                        'anti_co_concurrent': row.get('AntiCoCounselorConcurrent', None),
                        'anti_sequential': row.get('AntiSequential', None),
                        'at_least_once_per_person': row.get('AtLeastOncePerPerson', None)
                        
                    }
                #create dict with VarName as key and the object as the value
                self.tasks_dict[row['TaskVariableName']] = TaskManager.Task(**task_details)
                self.task_variable_names.append(row['TaskVariableName'])
                
    #from determine_eligible_task_types, give eligible files or something idk or give to csv converte and within those files only choose certain ones
    
    def process_files(self, file_names):
        """Runs TaskDataConverter functions on files to convert csv files of tasks into dictionary where keys are task identifiers and values are Task objects."""
        for file_name in file_names:
            self.add_tasks_from_csv(file_name=file_name)
        return self.tasks_dict, self.task_variable_names

    def determine_eligible_task_types(defaultTasksDictionary, dateValue): #- UNESSECARY - finish the MVP - what if someone just puts in into one giant file, might need backup system to sort them into categories so have same funcitonality 
        #region--------------------------- Special Task System #TODO MAKE THIS
            
        #TODO create special task system
        #TODO make a converter for special tasks csv sheet, integrate into converter class.
        #TODO somehow standardize these into time slots - see intial time section and make a function, think about time stand sys.
        #TODO integrate into converter class, and make work with night chores, so load in only tasks needed for day, besides the basic dictionary.

        wenSpecialTaskList = {'Clean Up Pizza Night': "TIME DOES NOT EXIST", 'Pac Chair Set Up -> Dance ->': "TIME DOES NOT EXIST",'Adoration -> Pac Chair Takedown': "TIME DOES NOT EXIST", "NightChore":'9:30ish Maybe'}
        tuesSpecialTaskList = {'Mens Sesh': "7ish",'Womens Sesh': "7ish",'Night Game': "sometime", 'Sweeting': "9ish", 'Pizza Run Leave At 4:05Pm': "3:45"}
        friSpecialTaskList = {}
        satSpecialTaskList = {}
        sunSpecialTaskList = {}

        specialTasksDict = {
            3: wenSpecialTaskList,
            5: friSpecialTaskList,
            6: satSpecialTaskList,
            7: sunSpecialTaskList
                            }
        if dateValue in specialTasksDict:
            daySpecialTasks = specialTasksDict[dateValue]
        else:
            daySpecialTasks = 0 #WHY I PROGRAMMED IT LIKE THIS: all these key = 0, is so that when counting the len of dict it doesnt return error if dateValue represents / is a normal day, and thus it knows there are no special tasks. For use comparing total time avail to total tasks needed to be done.
            
            #TODO later when making master task list see what I should have this as, none or something else
        if dateValue == 7 or dateValue == 6: #BIG LEARNING CONCEPT: if dateValue == 7 or 6: This condition does not check if dateValue is either 7 or 6. Instead, it checks if dateValue is 7, or if 6 is true. Since non-zero integers are considered truthy in Python, 6 is always true, making the condition always evaluate to true.
            defaultTasksDictionary.clear() #WHY- because special schedule for these dates and it is easier just to preprogram in, faster than searching through.
        #endregion

#region--------------------------------------- Tasks User Input
 
# --------------------- Additional Tasks #TODO refine this later to be more elegant and standalone as backend
def user_adds_additonal_tasks(taskDictLocal, userTaskVariableName, userTaskName, userFrequency, userStartTime, userDuration, userMinManpower, 
                              userImportance, userGenderSpecific, userAssignees, user_windowed_task, userTimePreferred, user_earliest_start, user_due_by, task_tier=1):
    #Insert ability to make custom tasks...   
    task_name = userTaskName  # This could be any user-defined string
    
    taskDictLocal[task_name] = Task( # Create a new Task instance and store it with the user-defined name as the key, # type: ignore
        task_variable_name = userTaskVariableName, #DONE need code to prevent creation of multiple tasks with same variable name,
        task_tier = task_tier, #CHECK IF ERROR, may need to change later, MAYBE make upmost importance??
        task_name = userTaskName,
        task_frequency = userFrequency,
        # = userStartTime[0] #- idk if nessecary but since i now have start time and starttimes list, tho idk if needed, maybe was better earlier
        start_time = userStartTime, #List, so if multiple times can just use one var and iterate through
        duration = userDuration, #TODO make Auto convert if user enters time range etc
        min_num_people_needed = userMinManpower,
        importance = userImportance,
        gender_specific = userGenderSpecific,
        preassigned = userAssignees,
        window = user_windowed_task,
        time_preferred = userTimePreferred, 
        earliest_start = user_earliest_start,  #TODO fix some bulltshit later, #CHECK IF ERROR, standard fale input = NONE, WHY = because will use timeslot standardized periods which will include 0
        due_by = user_due_by,  #CHECK IF ERROR, standard fale input = NONE
        chosen = 1, #set to yes by default, bc user #CHECK IF ERROR, may have to change default data rep
        task_cost = (userFrequency*userDuration)
        )
    return taskDictLocal
class TaskRecommender():
    """Tasks Editor and Selector (Special and Default), Generate total tasks & special tasks depending on dateValue (date). 
    Returns a master task dict, and has user fill in any missing task detials"""
    #TODO be able to assign addtional tasks to certain people
    #TODO be able to say when task is and use multi-duration
    #TODO make a way to insert like a list of things you need done for the day more eaisly like a row in a csv or spreadsheet - could maybe come from default tasks, just be like any default taks yo uwant done, and ask if so when(or if predetermined time is acceptable, for special ones))
    #TODO merge the special, default, and night chore tasks together into once list. Then calcualte and make list that is auto then diplay the auto reccomended

    def __init__ (self, dayName):
        self.selected_tasks_dict = {}
        self.selected_tasks_var_names_list = []
        self.dayName = dayName

    @timer
    def recommend_tasks(self, master_task_dict):    
        """Auto-Recommended tasks algorithm"""
        #NOTE this spawn thing could be a problem if refactor in the future
        attribute_name = 'spawn_'+ self.dayName.lower() #WHY .lower to create name value? It refs dateValue num to corresponding dictionary values which are day names, and the day names are capitalized. However the obj attribute daynames are not, so we lowercase this name.
        for task_name, instance in master_task_dict.items(): 
            attr_value = getattr(instance, attribute_name)
            #WHY check for Yes"?  bc looking at SpawnMonday etc attributes, so checking if it occurs on those days
            if attr_value.capitalize().strip() == 'Yes': #WHY - .upper() bc comparison value is upper case, and its just incase someones puts a lowercase 'yes' on the csv they wont screw everyhting up. #TODO(later also look for "depends' for scheduled basis tasks such as water flowers)
                self.selected_tasks_dict[task_name]=instance
        self.selected_tasks_var_names_list = list(self.selected_tasks_dict)
         #assume faster if just generate list from dict keys after, instead of appending values along with the dict #OPTIMIZATION QUESTION

    #NOTE not in use, for creating a schedule like rep of when stuff will happen
    def get_recommended_tasks_verbose(self):
        data = []
        for task_name, instance in self.selected_tasks_dict.items():
            pass
        return data
        #TODO SIMPLE, GOOD, IDEA!!! CHECK IF ERROR, in future update may later change from "yes" to True, will be faster too?
        #- 2nd reminder, add in reoccuring scheduled tasks later (like ones that occur every x days ex: Water flowers)
    
    # ----------------------- Fill in any missing data for the tasks.
    #TODO make better transition and explain now filling in data for previously selected tasks that need user Input
    #NOTE from a UI perspective this part is terribly confusing but will leave it as is bc IDGAF. I dont want ohave to write 250 more lines of code that wont probbaly be used in the final GUI.
    
    #TODO have if startimes blank and jsut fill freq / min num ppl or something to ask you want assign a startime, or have computer do it? Have computer do it between X&Y
    #TODO NOTE will have to move most of this to front end prob eventually

    #new seperate validation and collection version        
    
    def validate_details(self, obj):
        missing_details = {}
        for attr in vars(obj):
            if not attr.startswith('__') and not callable(getattr(obj, attr)):
                value = getattr(obj, attr)
                #make this to complex and might have neg performance
                if (isinstance(value, str) and "userInput" in value) or (isinstance(value, list) and any(item in ["userInput"] for item in value)): #Note if ur going to have it look for blank timeslot lists or "" or None,
                #make sure it doesn't already have a normal value in there. Otherwise will put all tasks in there bc not all have 6 start times 
                    missing_details[attr] = value
                elif "Yes" == getattr(obj, "window"): #for windowed tasks
                    if getattr(obj, "due_by") is None: #need to make sure only ACTIVATES FOR THE BLANKS
                        if not getattr(obj, "start_time"):
                            missing_details["start_time"] = "userInput" #BUG WUT AM I DOING WITH THIS???? #need to assume no starttime yet
                        missing_details["due_by"] = "userInput"
        return missing_details
    
    #TODO this can also be usefull for filling in stuff that the computer needs to do, such as Calc et cetra, or do at assignment
    def handle_missing_details(self, collect_missing):
        """args: (function)collect_missing: a function to use as a call back to the front end, which 
        fills in missing detials for that task"""
        for task_name, obj in self.selected_tasks_dict.items():
            missing_details = self.validate_details(obj)
            if missing_details:
                collect_missing(task_name, obj, missing_details)
                
            #NOTE DEF CAN OPTIMIZE THIS LATER
            #Use this to do any final corrections needed before assignment since already iterating thru the values
            #quick patch bc don't want to do in front end or at assignment(again)

            #NOTE can speed up by looking this up once then ref - in the if statement current_list
            start_window = getattr(obj, "earliest_start") #this wont always eval to true, bc if empty string, list, or None then will be false
            if start_window or getattr(obj, "due_by"): #NOTE Why should i check for due_by?? need to re look at this #NOTE ASSUMES ONLY ONE START TIME FOR WINDOW DURATIONS
                start_times_list = getattr(obj, "start_time")
                start_times_list[0] = start_window
                setattr(obj,"start_time", start_times_list)  #NOTE change later once move list stuff
            #make convert certifications and gender lists shit
            
                #TODO in future, idk how work with web version, but to make more independent
                #make a return value, then have it sort thru return values and assign stuff.
                #So work better with web
                #NOTE so im thinking it just give the filled ut value back in a specific format 
                # then this backend updates stuff as needed - but more code tho :\
                    
    def return_selected_tasks_for_day(self):
        return self.selected_tasks_dict, self.selected_tasks_var_names_list

def instantiate_tasks(additionalTasks: dict[str, TaskManager.Task], dayTimeSlotsKeysList: list[str]) -> tuple[TaskManager, dict[str, object], list[str]]:
    """Return object, dict, list"""
    
    TaskManager.Task.define_default_assigned_to_times(dayTimeSlotsKeysList) #bc need it for all creations
    
    task_data_converter = TaskDataConverter()
    csv_tasks_files = [SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV, SWAT_NIGHT_CHORES_INFO_CSV] #maybe add this to the args eventually
    
    #WHY - create the defaultTasksVarNamesList list so the autoComplete can use in menus and stuff
    defaultTasksDictionary, defaultTasksVarNamesList = task_data_converter.process_files(csv_tasks_files)
    
    defaultTasksDictionary = defaultTasksDictionary | additionalTasks #note if duplicates bc of union operater tasks in additionalTasks will overwrite defaultTasksDictionary, which is good because probbaly want specificed tasks.

    task_manager = TaskManager(defaultTasksDictionary) 

    return task_manager, defaultTasksDictionary, defaultTasksVarNamesList
