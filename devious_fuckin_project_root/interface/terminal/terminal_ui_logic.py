from backend.core.employees import (
    EmployeeManager,
    EmployeeAvailabilityLogic,
    Employee
)
from backend.core.tasks import (
    TaskManager,
    TaskDataConverter,
    TaskRecommender,
    user_adds_additonal_tasks,
    instantiate_tasks,
)
from backend.core.time_processes import (
    program_auto_get_date_value,
    validate_user_date_input,
    get_day_name,
    get_day_time_slots,
    play_joke_on_user,
    list_schedule_times,
    insert_time_slot_at_position,
    timeSlotStandardizer,
    remove_time_slot,
)
from config.settings import (
    get_next_day,
    get_date_auto,
    days,
    daysKeyValueInverse,
    noAnswers,
    yesAnswers,
    maleAnswers,
    femaleAnswers,
)
from backend.core.process import employeeNamesList, employeeGenderList
from config.utility import xyz_input_auto_completer
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore, Style
import re
from typing import Dict, Any, Type


def get_date_value_ui(get_date_auto=False, get_next_day=False, max_entry_attempts=int):
    """Gets the date value either from computer or by user input. Returns: (int) representing the weekday"""
    if get_date_auto:
        return program_auto_get_date_value(get_next_day=get_next_day)
    else:
        attempts = 0
        while attempts < max_entry_attempts:
            date_user_entered = input(
                "\nGenerate a schedule for which day of the week: "
            )
            date_value = validate_user_date_input(date_user_entered)
            if not date_value:  # if false
                print(
                    "\n-----------\nERROR!\n\n Not a valid day, try again.\n-----------------\n"
                )
                attempts += 1
            else:
                return date_value  # acceptable value found
        play_joke_on_user()

def employee_name_input_auto_completer(employeeNamesList, promptString):
    """
    Prints out whatever prompt is given in the prompt string, (if nothing given then prints nothing). Then auto completes the user input with an employee name from employeeNamesList.
    It then automatically capitalizes the employee name. Finally the function returns the employee name (capitalized).
    Does not have a "backslash n" in the print statment. CANNOT take strings with escape sequences in them
    
    Dependency: 
    Uses prompttoolkit

    Args:
        employeeNamesList (list): list of employee names
        promptString (string): Only insert one string of prompt strings you want printed, if none given then prints nothing
    """
    
    #if no text given to function, makes prompt blank
    if promptString == False: #WHY & CHECK IF ERROR: GPT4- python treats empty strings ("") as False and non-empty strings as True when evaluated in a Boolean context.
        promptString = ""
    
    # Define a list of autocomplete words.
    employee_Name_Completer = WordCompleter(employeeNamesList,ignore_case=True) #WHY ignore_care=True, allowing case-insensitive input bc employee names list is capitalized, but dont want to make user have to capitalize input to get auto suggestion
    # Use the completer in the prompt.
    user_input = prompt(promptString, completer=employee_Name_Completer)
    
    capitalized_input = user_input.capitalize() #WHY - have input auto convert to Capital case, bc names in employeeName list and other data structs are capitalized
    #print('You entered:', capitalized_input)
    return capitalized_input

class EmployeeAvailabilityUI:
    def __init__(self, availability_logic):
        self.availability_logic = availability_logic

    def prompt_employee_unavailability(self):
        while True:
            print("\n\nWho is unavailable?\n")
            employee_name = employee_name_input_auto_completer("Enter employee name: ", employeeNamesList)
            if self.validate_employee_name(employee_name):
                break
            print("Invalid employee name. Please check and try again.")

        unavailable_times = self.collect_unavailability_times(employee_name)
        self.availability_logic.set_employee_unavailability(employee_name, unavailable_times)
        print(f"\nConfirmed: {employee_name} is unavailable at {unavailable_times}.\n")

    def validate_employee_name(self, name):
        # Implement validation logic, e.g., checking against a list of employee names
        return (
            name in employeeNamesList
        )  # This list would be part of your overall employee management system

    def collect_unavailability_times(self, employee_name, dayTimeSlotsKeysList):
        times = []
        print(
            f"\nWhen is {employee_name} unavailable? (Please use format: 7am, 7:00pm, etc.)"
        )
        while True:
            print("Enter times of unavailability or 'done' to finish: ")
            time_input = xyz_input_auto_completer("", dayTimeSlotsKeysList)

            if time_input.lower() == "done":
                break
            if self.validate_time_format(time_input):
                times.append(time_input)
            else:
                print("Invalid time format. Please try again.")
        return times

    def validate_time_format(self, time_str):
        # Validate time format here, returning True if valid
        return bool(re.match(r"\d{1,2}(:\d{2})?\s*(am|pm)", time_str, re.IGNORECASE))

    def user_input_employee_unavailabilities(self):
        anyoneUnavailable = input(
            "\nIs anyone unavailable today?\n\ny or n? \n\nUser: "
        )
        if anyoneUnavailable in noAnswers:
            print("\nConfirmed: No unavailabilites.")
        else:
            self.prompt_employee_unavailability()
            while True:
                print("\nIs anyone else unavailable?\n\nY or N?\n")
                anyoneElse = input("\nUser: ")
                if anyoneElse in noAnswers:
                    print("\nConfirmed: no one else is unavailable.\n")
                    break
                else:
                    self.prompt_employee_unavailability()


def user_decide_modify_times_ui(day_time_slots):
    # Asks if times for schedule are acceptable, returns the user response as either True or False. Then the false would be used to activate the modify_time_slots func
    print("Time periods for today's schedule:")
    print(list_schedule_times(day_time_slots), "\n")
    # TODO BUG RENABLE LATER: DIABLED FOR DEBUG
    # input("\nDo you want to change any? (y/n):")
    # response = input("User: ").strip()
    response = False
    return response


def modify_schedule_ui(day_time_slots):
    print("\n[Options for Editing Tasks]")
    print("1. Add a time from the list")
    print("2. Remove time from the list.")
    print("3. Back - Exits out of current command, to command list")
    print("4. Exit - Exits the editor, assuming you're done editing tasks.")
    print("5. Commands - Reprints commands")
    instruction_string = (
        "\nPlease enter a command ('add', 'remove', 'back', 'exit', 'commands'):\n"
    )
    time_editor_command_list = ["add", "remove", "back", "exit", "commands"]

    while True:
        user_command = input(instruction_string).strip().lower()
        if user_command == "add":
            new_time = input(
                f"\nEnter the new {Fore.GREEN}{Style.BRIGHT}time{Style.RESET_ALL} (HH:MM)(AM/PM): "
            ).strip()
            # TODO need regex to check if it is a valid time first

            print(
                f"\nDo you want to {Fore.YELLOW}{Style.BRIGHT}insert {new_time}{Style.RESET_ALL} {Fore.GREEN}{Style.BRIGHT}before{Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}after{Style.RESET_ALL} a specific time: "
            )
            position = (
                prompt("User: ", completer=WordCompleter(["before", "after"]))
                .strip()
                .lower()
            )

            print(
                f"\nInsert {Fore.YELLOW}{Style.BRIGHT}{new_time} {position}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} what scheduled time:{Style.RESET_ALL}"
            )
            reference_time = prompt(
                "User: ", completer=WordCompleter(list(day_time_slots[0].keys()))
            ).strip()

            day_time_slots = insert_time_slot_at_position(
                day_time_slots[0], new_time, reference_time, position
            )
            print("\nUpdated times:", list(day_time_slots[0].keys()))

        elif user_command == "remove":
            time_to_remove = input(
                f"\nEnter the new {Fore.GREEN}{Style.BRIGHT}time{Style.RESET_ALL} (HH:MM)(AM/PM): "
            ).strip()

            day_time_slots = remove_time_slot(day_time_slots, time_to_remove)
            print("\nUpdated times:", list(day_time_slots[0].keys()))

        elif user_command == "exit":
            break
        elif user_command == "commands":
            print("\n[Available Commands]")
            print("\n".join(time_editor_command_list))
        elif user_command == "back":
            continue

    print("Final schedule:", list(day_time_slots.keys()))
    return day_time_slots


class TaskUI: #NOTE ah this is the UI counterpart to task manager logic?
    @classmethod
    def print_help(cls, topic):  # LEARNING CONCEPT, .cls is similar to .self
        """Prints help information for a given topic related to a task attributes=."""
        info = cls.task_attribute_guide.get(topic, "Help topic not found.")
        print(f"\n{topic}:\n {info}\n")

    def __init__(self, task_manager):
        self.task_manager = task_manager

    # TODO complete later
    def print_var_name_time(task_var_name, start_time):
        print(
            f"Task var name: {Fore.BLUE}{Style.BRIGHT}{task_var_name}{Style.RESET_ALL} at {start_time}"
        )

        # TODO eventually find out how to pass arugments to make if statments in these so i can tell it to be verbose or not

    def display_all_tasks(self):
        # Iterate through the task instances in the dictionary values
        for task in self.tasks.values():
            task.describe_var_name_times()  # Call the describe method on each task instance

    def task_info(self, taskVarName, defaultTasksDictionary):
        defaultTasksDictionary[taskVarName].describe_verbose()

    """def print_task_verbose(task_name, spawn_days):
        print("---------------------------------------------")
        print(f"Task var name: {Fore.BLUE}{Style.BRIGHT}{task_name}{Style.RESET_ALL}")
        
        for attribute in attributes:
            print()
         
        print("----------------------------------------------\n")"""    

def user_adds_additonal_tasks_ui(): #TODO GO THRU AND FIX
    # Insert ability to make custom tasks...

    # NOTE will probbably break first
    # BUG ADD FUNCTIONALITY IN AFTER DEV | additionalTasksTF = input("\nAre there any additional tasks you want to add for the day? Y or N? ")
    additionalTasksTF = "N"  # TODO remove after dev
    taskDictLocal = {}
    while additionalTasksTF in yesAnswers:
        print(
            "(SYSTEM LIMITATION) PLEASE NOTE: The all instances of this task will have the same duration and min number of people required. If this is a problem create a seperate task for each instance where the min number of people or the duration changes.\nUnfortunately there is no solution for this yet."
        )
        input("I understand, (Press Enter)")
        userTaskName = input(
            "Task Name: "
        )  # make var name +1 etc if multiple times or similar name
        # WHY: Prevents duplicate variable names, may get rid of later, restrict what can put in, maybe use classes???
        # TODO MIGHT BREAK WHEN I CHANGE TO DICT
        if (
            userTaskName in taskDictLocal
        ):  # no matter what they put in, ts not the same Varname as anything in list so we are good. IF ERROR CHECK
            taskNameOccuranceCount = 0
            for tasks in taskDictLocal:
                if userTaskName in taskDictLocal:
                    taskNameOccuranceCount += 1
            userTaskVariableName = userTaskName + str(
                taskNameOccuranceCount
            )  # Adds a number to the name to differentiate from other vars. #LEARNING CONCEPT concatenate an int with a string
        else:
            userTaskVariableName = userTaskName

        print("If multiple start times, seperate each with a comma.")
        userStartTime = list(
            input("Start time(s): ")
        )  # TODO NEED TO STANDARDIZE AND CONVERT START TIMES MAKE FUNCTION SO CAN USE WHEN IMPORT DATA TOO #make it so it standardizes time or give list to choose from
        userDuration = input(
            "Duration: "
        )  # FIX LATER to be blocks or time date, or give options. also mkae smart function to calc distance btwn two numbers to get duration
        userMinManpower = input("Number of People Needed: ")
        userImportance = input(
            "Importance (1-10): "
        )  # Figure out importance scale and how will work

        userAssignees = input("Is the task preassigned to someone(s)? y/n: ")
        if userAssignees in yesAnswers:
            print(
                "Seperate each with a comma.\nExample: Terry, Bevis, Butthead, Jacob, ThatAssholeOverThere"
            )
            userAssignees = list(
                input("To whom: ")
            )  # TODO make it compatible with multiple names, CHECK IF ERROR IN ALGO, maybe need to make it a list by default
        elif userAssignees in noAnswers:
            userAssignees = 0  # TODO may need to change data value type

        userGenderSpecific = input("Is the task Gender Specific? y/n: ")
        if userGenderSpecific in yesAnswers:
            userGenderSpecific = input(
                "To which gender: "
            )  # DONE: able to have list to take diff spellings of male or female and standardize the result
            if userGenderSpecific in maleAnswers:
                userGenderSpecific = "Male"
            elif userGenderSpecific in femaleAnswers:
                userGenderSpecific = "Female"
        elif userGenderSpecific in noAnswers:
            userGenderSpecific = 0  # TODO may need to change data value type

        user_time_window = input("Is there a time window to schedule this y/n?: ")
        if user_time_window in yesAnswers:
            user_time_window = "Yes"
            #earliest_start = input( - 
                #"don't schedule before x time, if none then type NONE"
            #)
            user_due_by = input(
                "don't schedule after x time?, if none then type NONE"
            )
        else:
            user_time_window = None
            userTimePreferred = 0
            user_earliest_start = None
            user_due_by = None
        userFrequency = 0
        
        #NOTE THIS IS IMPORTANT AND COULD CAUSE BUGS IN THE FUTURE
        #freq only matters if windowed, otherwise just basically basing it off of starttimes, will keep around for now but could be cut for optimization in the future, but also might be useful if times ref changes
        for times in userStartTime:  # Calc freq from number of start times
            userFrequency += 1

        taskDictLocal | (
            #TODO  make kwarg??? for clarity
            user_adds_additonal_tasks(
                taskDictLocal,
                userTaskVariableName,
                userTaskName,
                userFrequency,
                userStartTime,
                userDuration,
                userMinManpower,
                userImportance,
                userGenderSpecific,
                userAssignees,
                user_time_window,
                userTimePreferred,
                user_earliest_start,
                user_due_by,
                task_tier=1, #might need to reasses
            )
        )

        additionalTasksTF = input(
            "Are there any additionally tasks you want to add for the day? Y or N?\n\nUser: "
        )
    if additionalTasksTF in noAnswers:
        print("No extra tasks! YIPPIE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return taskDictLocal

class TaskRecommendationUI:
    def __init__(self, recommendation_logic, dayTimeSlotsKeysList):
        self.recommendation_logic = recommendation_logic
        self.dayTimeSlotsKeysList = dayTimeSlotsKeysList

    def modify_tasks_interface(self, master_task_dict_names_list, master_task_dict, task_manager):
        def print_default_selcted_tasks_editior_commands():
            print("\n[Options for Editing Tasks]")  # Thanks to GPT4 for making my command instructions more concise
            print("1. Add <TaskName> a tasks from the basic tasks dictionary.")
            print("2. Remove <TaskName> a task from the selected list.")
            print("3. Info <TaskName> - Know more about the parameters of a selected task, or any preprogrammed task.")
            print("4. Display all tasks - Get a list of available preprogrammed tasks.")
            print("5. Display selected tasks - Redisplay the tasks selected for the day.")
            print("6. Clear all tasks - Remove all tasks from the selected list.")
            print("7. Back - Exits out of current command, to command list")
            print("8. Exit - Exists the editor, assuming your done editing tasks.")
            print("7. Commands - Reprints commands")

        print_default_selcted_tasks_editior_commands()

        instructionString = "\nPlease enter your choice ('add', 'remove', 'info', 'display all tasks', 'display selected tasks', 'clear all tasks', 'back', 'exit', 'commands'):\n"
        taskEditorCommandList = [
            "add",
            "remove",
            "info",
            "display all tasks",
            "display selected tasks",
            "clear all tasks",
            "back",
            "exit",
            "commands",
        ]
        # TODO maybe later make it be able to edit the selected tasks characteristics, that way can edit it if it is off
        # TODO make it put out list of taks and times they at, even better if go by time. IDK stuff for long term

        # Loop to continually prompt the user until they're done editing.
        continueEditing = True
        while continueEditing:
            userCommand = (
                xyz_input_auto_completer(instructionString, taskEditorCommandList)
                .strip()
                .lower()
            )
            match userCommand:
                case "add" | "remove" | "info":
                    print(
                        f"Type a {Fore.YELLOW}{Style.BRIGHT}task{Style.RESET_ALL} to use the {Fore.GREEN}{Style.BRIGHT}{userCommand}{Style.RESET_ALL} command on.\n",
                        end="",
                    )
                    userCommandModedPrompt = f"{userCommand} "
                    while True:
                        if userCommand in ["add", "info"]:
                            # User selects the task to preform either command on first
                            while True:
                                userTaskSelected = xyz_input_auto_completer(
                                    userCommandModedPrompt, master_task_dict_names_list
                                )
                                if userTaskSelected in master_task_dict_names_list:
                                    break

                            if userTaskSelected == "back":
                                break
                            # userTaskSelected = userTaskSelected.upper() #CHECK IF ERROR, just incase it wasnt in caps already. Task names in master dict and lists are in Caps so trying to keep it consistent
                            # TODO idk maybe just make it loop if invalid input.
                            # TODO maybe hould make if reject if doesnt enter a valid task name from the dict, / check to see if it is in it
                            # TODO add nightchore and special to this eventually actually, well maybe ill just integrate them in

                            if userCommand == "add":
                                self.recommendation_logic.selected_tasks_var_names_list.append(userTaskSelected)
                                self.recommendation_logic.selected_tasks_dict.update(
                                    {userTaskSelected: master_task_dict[userTaskSelected]} #TODO oh boy gonna need to fix this all manually
                                )
                                print(
                                    "Updated selected tasks list: ",
                                    self.recommendation_logic.selected_tasks_var_names_list,
                                    self.recommendation_logic.selected_tasks_dict,
                                )
                            else:  # 'info'
                                task_manager.task_info(userTaskSelected)

                        elif userCommand == "remove":
                            print("Tasks: ", self.recommendation_logic.selected_tasks_var_names_list)
                            while True:
                                userTaskSelected = xyz_input_auto_completer(
                                    userCommandModedPrompt,
                                    self.recommendation_logic.selected_tasks_var_names_list,
                                )
                                if userTaskSelected in master_task_dict_names_list:
                                    break
                            if userTaskSelected == "back":
                                break
                            self.recommendation_logic.selected_tasks_var_names_list.remove(userTaskSelected)
                            self.recommendation_logic.selected_tasks_dict.pop(
                                userTaskSelected, None
                            )  # Use pop with None to avoid KeyError
                            print(
                                "Selected tasks remaining: ",
                                self.recommendation_logic.selected_tasks_var_names_list,
                                self.recommendation_logic.selected_tasks_dict,
                            )

                        print(
                            f"\ntype {Fore.RED}{Style.BRIGHT}'back'{Style.RESET_ALL} to {Fore.RED}{Style.BRIGHT}exit section{Style.RESET_ALL}"
                        )
                        print(
                            f"{Fore.GREEN}{Style.BRIGHT}to continue using {userCommand} [press enter]{Style.RESET_ALL}"
                        )
                        userContinueQuestion = input().strip().lower()
                        if userContinueQuestion == "back":
                            break

                case "display all tasks":
                    task_manager.display_all_tasks() #NOTE what to do about this?
                    #TODO integrate this into task manager UI

                case "display selected tasks":
                    print(self.recommendation_logic.selected_tasks_var_names_list)

                case "clear all tasks":
                    self.recommendation_logic.selected_tasks_var_names_list.clear()
                    self.recommendation_logic.selected_tasks_dict.clear()
                    # IDK implement later once figure how will format the selected tasks list

                case "commands":
                    print_default_selcted_tasks_editior_commands()
                    print("\n\nList of commands:")
                    print(taskEditorCommandList)

                case "exit":
                    continueEditing = False
                    print("Selected basic tasks confirmed.")

                case _:  # This acts like an 'else' to handle unexpected commands
                    continueEditing = True
                    # So since the user command at this point can only be 'back' we let the loop iterate back to the beginning.

    def edit_selected_tasks(self, master_task_dict_names_list):
        print(
            "\n----------------------------------------------------------------------------\n"
        )
        print(
            "Here are today's selected default basic tasks (auto-recommended by algorithm):"
        )
        print(self.recommendation_logic.selected_tasks_var_names_list)

        decision = input("\nWould you like to edit them? y/n\n(Note: You can add custom tasks later): ")
        if decision.strip() in yesAnswers:
            self.modify_tasks_interface(master_task_dict_names_list)
        else:
            print("Selected basic tasks confirmed.\n\n")

    #NOTE WIP - prob will get rid of
    def display_selected_tasks_as_schedule(self):
        data = self.recommendation_logic.get_recommended_tasks_verbose
        
    
    #NOTE depreciated for now
    def request_missing_input(task_name: str, attribute: str = "attribute"):
    # This function could be part of the front-end
        return input(f"{task_name} task {attribute} needs userInput.\n{Fore.YELLOW}{Style.BRIGHT}If you are confused about what needs input-ing, type 'help' to get more information about the data your're supposed to enter.{Style.RESET_ALL}\nSeperatley if no value is needed, enter None\n")

    #NOTE depreciated for now
    def warning_missing_input(task_name: str, data_structure_type: type, attribute: str = "attribute"):
    # This function could be part of the front-end
        if data_structure_type is str:
            return input(f"{task_name} task {attribute} needs userInput.\n{Fore.YELLOW}{Style.BRIGHT}If you are confused about what needs input-ing, type 'help' to get more information about the data your're supposed to enter.{Style.RESET_ALL}\nSeperatley if no value is needed, enter None\n")
        elif data_structure_type is list:
            print(f"\n{task_name} {attribute} needs userInput. If done entering or no more values then enter 'exit'\n{Fore.YELLOW}{Style.BRIGHT}If you are confused about what needs input-ing, type 'help' to get more information about the data your're supposed to enter.{Style.RESET_ALL}\n")

    def collect_missing_details(self, task_name, obj, missing_details):
        def print_help(attr):
            print(f"\n{attr} = {TaskManager.Task.task_attribute_guide[attr]} \n")
        
        #TODO Def could make this cleaner, esp as attributes get more complex but will leave for now.
        print(f"{task_name} is missing some parameters, let's fill them in.\n{Fore.YELLOW}{Style.BRIGHT}Confused about what to input for a parameter? Type 'help' to get information about the data your're supposed to enter.{Style.RESET_ALL}\nSeperatley if no value is needed enter None, if you are done entering values for a sequence hit exit\n")
        for attr, value in missing_details.items():
            if isinstance(value, str):
                while True: #TODO make sure validate time input, #BUG fix whatever is going on here
                    if (attr == "earliest_start" and value) or (attr == "start_time" and value): #NOTE only cheking for userinput flag not emptyness
                        #so can put in time autocompleter
                        userData = xyz_input_auto_completer(f"Input {attr} for {task_name}: ", self.dayTimeSlotsKeysList)
                        if userData.lower().strip() == 'help':
                            print_help(attr)
                            continue
                        elif userData not in userData: continue
                        else:
                            setattr(obj, attr, userData)
                            print(f"Confirmed | Task {attr} = {userData}\n") 
                            break
                    else:
                        userData = input(f"Input {attr} for {task_name}: ")
                        if userData.lower().strip() == 'help':
                            print_help(attr)
                            continue
                        else:
                            setattr(obj, attr, userData)
                            print(f"Confirmed | Task {attr} = {userData}\n")
                            break
                                #check if valid time
                            

            elif isinstance(value, list): #pretty much just for start times list,
                autoEnter = False
                for index, item in enumerate(value):
                        if autoEnter:
                            print(f"Exiting {task_name} {attr} input sequence, filling remaining values for {attr} with 'None'")
                            value[index] = None
                        else: 
                            print(f"If done entering or no more values then enter 'exit'")
                            userData = xyz_input_auto_completer(f"Input {attr} for {task_name}: ", self.dayTimeSlotsKeysList)
                            if userData.lower().strip() == 'help':
                                print_help(attr)
                            elif userData.lower().strip() == 'exit':
                                autoEnter = True
                                break
                            else:
                                value[index] = userData

def describe_dynamic_time_slot_qeues(dynamicTimeSlotQueuesDict:dict):
    """will have to acess the schedule class first to get the dict"""
    print("\nA list of dynamic time slot qeues and their associated tasks:\n")
    for time_slot in dynamicTimeSlotQueuesDict.keys():
        print(time_slot)
        print(dynamicTimeSlotQueuesDict[time_slot].queue) #WHY - LEARNING CONCEPT dont need to put in a print statment as methods prints values, if i did it would print none, as there is nothing being explicity returned so it returns none by default
        print() #serves as a nexline seperator sort of thing.

