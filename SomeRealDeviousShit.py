
#region--------------------------- FILE HEADER COMMENTS

#Dunders
__author__ = "Andrew Dybala"
__copyright__ = "Copyright Restricted"
__credits__ = ["Andrew Dybala", "GPT4 as assistant"]
__license__ = "License Name and Info"
__version__ = "1.2.1"
__maintainer__ = "Andrew Dybala"
__email__ = "andrew@dybala.com"
__status__ = "status of the file"

#https://docs.python.org/3/c-api/intro.html


#TODO When developing, leave all gui stuff for after complete main program. Bc might have app take care ofall of that and the program just take the final type and ver of data and use it.
#So keep in mind when making inputs or conversion sequences that it has a clear final form and document it. That way can plug into api requests easy and stuff.

"""FOR later
hdiutil create -volname "SWATScheduler" -srcfolder /Users/andrewdybala/Desktop/SomeDeviousProjectcopy -ov -format UDZO ~/Desktop/SomeDeviousProjectcopy.dmg 
https://docs.python.org/3/py-modindex.html
https://wiki.python.org/moin/GuiProgramming
https://www.pythonguis.com/faq/which-python-gui-library/
https://www.bairesdev.com/blog/best-python-gui-libraries/

GUI toolkits:
https://flet.dev - fast, but not best way to learn as not well maintiable in the long run
https://www.youtube.com/watch?v=JJCjAUmNXBs


#WEB GUI
https://flask.palletsprojects.com/en/3.0.x/

#FLUTTER
https://flutter.dev - Free for commerical use, BRUH HAVE TO LEARN ANOTHER LANGUAGE (Dart language)
https://github.com/maxim-saplin/flutter_python_starter
https://docs.flutter.dev/get-started/install/macos/desktop
https://medium.com/@sudeshnb/to-connect-a-python-backend-to-a-flutter-mobile-app-a9f61f8d54f2#:~:text=78-,To%20connect%20a%20Python%20backend%20to%20a%20Flutter%20mobile%20app,for%20handling%20the%20app%27s%20state.


IMPORT Libraries Documentation: 
https://python-prompt-toolkit.readthedocs.io/en/master/

#MAC os shell application how to
https://mathiasbynens.be/notes/shell-script-mac-apps
https://gist.github.com/mathiasbynens/674099

https://flutter.gskinner.com/xd-to-flutter/


#Excel plugin-add in.
https://youtu.be/K6pRl7XHBAU?feature=shared
https://www.youtube.com/watch?v=G_Egf3oxghI #ribbon tutorial with python
 
https://www.youtube.com/watch?v=MwZwr5Tvyxo idk what this is



AT SOME POINT DOWNLOAD TKINTER DESINGN: https://github.com/ParthJadhav/Tkinter-Designer
also 
https://www.youtube.com/watch?v=9oaqCMwcoQ4

"""
#endregion

#region--------------------------------------- IMPORT STATEMENTS

#TODO consider multi threading/coreing imports to save time, espically for the first load.

import time
import datetime
from datetime import timezone
start_program_time = time.time()

import csv
#import prompt_toolkit CONFUSION why instead of jsut impoting whole library do i have to specify to import certain funcitons? otherwise wont work
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
#from flask import Flask, jsonify
from colorama import init, Fore, Style
import re #pattern matching module, regualr exspression
from contextlib import contextmanager
from scipy import stats
import random

#endregion

#region---------------- SWAT CLASS???
#interesting main class thing, idk why or how would use it, but will leave here
class SWATScheduler:
    def __init__(self):
        #self.schedule = Schedule() #Wut what would be the implications of this??, how would it effect the rest of the code
        #self.task_manager = TaskManager()
        pass
    def run(self):
        # Load data from CSV, adjust employee availability, add tasks, etc.
        pass

    def load_employees_from_csv(self, file_path):
        # Load employees from CSV and add them to the schedule
        pass

    def load_tasks_from_csv(self, file_path):
        # Load tasks from CSV and add them to the task manager
        pass
#endregion

#region--------------------------------- INTRO STUFF

"""LEARNING CONCEPT: If you find yourself repeatedly needing to time blocks of code, you can encapsulate this pattern in a context manager:
This approach allows you to easily measure the runtime of any block of code by simply wrapping it in a with time_block("Description"): statement, making your code cleaner and more readable."""

#Time any block of code with time_block()
@contextmanager #NOTE allow to time ANY block of code, not just functions. I was learning about ocntext managers, still need to learn more.
def time_block(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"{label}: {end - start} seconds")
        
#DEBUGGING / TESTING feature, turns off or on (most of) the printed feedback to console 
All_Feedback_Print_Statements_On = False #If true turns on all feedback print statements, otherwise it turns them off
def testOutput(input_string,input_variable, *args): #*args so that some print statements can have "\n" on the end
    global All_Feedback_Print_Statements_On
    if All_Feedback_Print_Statements_On == True:
        #Thanks GPT4 for getting the coloring and code for this part bc I was lazy 
        formatted_string = f"{Fore.RED}{Style.BRIGHT}{input_string}"
        formatted_variable = f"{Fore.LIGHTYELLOW_EX}{Style.DIM}{Style.NORMAL}{input_variable}"
        print(formatted_string, formatted_variable, *args, Style.RESET_ALL)
dateValue = "2022-01-01"
testOutput("TEST | dateValue:", dateValue)

def timer(func):
    def time_analysis_wrapper(*args, **kwargs):  #IDK kinda get it, still confused
        start_time = time.time()
        result = func(*args, **kwargs) #IDK kinda get it
        
        end_time = time.time()
        print(f"{func.__name__} run time length: {end_time - start_time} seconds.")
        return result # #IDK kinda get it
    return time_analysis_wrapper

def printIntroSequence():
    print("\n-----------------------------------------------------------------------------------------------\n\n\n\
                            LOADING...\n")
    print("            ::::::::  :::       :::     :::  ::::::::::")
    print("          :+:    :+: :+:       :+:   :+: :+:  :+:")
    print("        +:+        +:+       +:+  +:+   +:+  +:+")
    print("       +#++:++#++ +#+  +:+  +#+ +#++:++#++: +#+")
    print("             +#+ +#+ +#+#+ +#+ +#+     +#+ +#+")
    print("     #+#    #+#  #+#+# #+#+#  #+#     #+# #+#")
    print("     ########    ###   ###   ###     ### ###")
    print()
    print("           :::::::: ::::::::::: :::   ::: :::        ::::::::::  :::")
    print("         :+:    :+:    :+:     :+:   :+: :+:        :+:         :+:")
    print("        +:+           +:+      +:+ +:+  +:+        +:+         +:+")
    print("       +#++:++#++    +#+       +#++:   +#+        +#++:++#    +#+")
    print("            +#+    +#+        +#+     +#+        +#+         +#+")
    print("     #+#    #+#    #+#        #+#    #+#        #+#")
    print("     ########     ###        ###    ########## ##########  ###")
    print("\n\n         ---> [[[Hit enter to start the program!]]] <---")
    print("\nDedication:\nThis program is dedicated to my SWAT Coordinator: Slips (Abby Lucksinger),\nand all the SWATTIES of the summer of 2023 who I am glad to call my friends\n\nDeveloped by Yacht (Andrew Dybala)\nS.W.A.T. Session 1 and Session 2, Summer of 2023.\nBLHS & University of Colorado Boulder")
    print("\n-----------------------------------------------------------------------------------------------")
    #input() #DELAYS PROGRAM SO CAN SEE START SCREEN
    #time.sleep(0.5) #alt way to wait
printIntroSequence()
#endregion

#region ----------------------------------------- BASIC SAVED INFO, #GLOBAL #VARS, LISTS, DICTIONARIES, FUNCTIONS

#GLOBAL
#VARS, LISTS, DICTIONARIES
#Porb will use the lists with many functions, so I put them at the top
yesAnswers = ["Y","Yes","yes","y","YES","ye","Ye","YE"]
noAnswers = ["N","No","no","n",'NO']
maleAnswers = ["Male","male","men","Men","boys","Boys","Man","man","Boy","boy","Males","males"]
femaleAnswers = ["Female", "female", "Women","women","woman","Woman","Females", "females","Girl","girl","Girls","girls"]

dumbAndrewMemes1 = "Here dem lyrics!\n\n\n\
It's like I dont care about nothing man...\n\
Roll another blunt...\n\
Ooohh\n\
La da da da la da da la la da da\n\
I was gonna clean my room until I got high\n\
I was gonna get up and find the broom but then I got high\n\
My room is still messed up and I know why (why man?)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I was gonna go to class before I got high\n\
I could'a cheated and I could'a\n\
Passed but I got high (uh uh la la da da)\n\
I'm takin' it next semester and I know why (why man?) (hey hey)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I was gonna go to work but then I got high (ohh, ohh)\n\
I just got a new promotion but I got high (la da da da da)\n\
Now I'm selling dope and I know why (why man?)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I was gonna go to court before I got high\n\
I was gonna pay my child support but then I got high (no you wasn't)\n\
They took my whole paycheck and I know why (why man?)(yeah eh eh)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I wasn't gonna run from the cops but I was high (uh, I'm serious man)\n\
I was gonna pull right over and stop but I was high (uh)\n\
Now I'm a paraplegic (ha ha ha) and I know why (why man?)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I was gonna pay my car and note until I got high (say what say what?)\n\
I wasn't gonna gamble on the boat but then I got high (uh uh)\n\
Now the tow truck is pullin' away and I know why (why man)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I was gonna make love to you but then I got high (ooh) (I'm serious)\n\
I was gonna eat your **** too (ohhh) but then I got high\n\
Now I'm ****** off (ahh) and I\n\
Know why (turn this shit off, ha ha ha)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I messed up my entire life because I got high (go go go)\n\
I lost my kids and wife because I\n\
Got high (say what say what say what?)\n\
Now I'm sleepin' on the side walk and I know why (why man?)\n\
(Yeah yeah)\n\
'Cause I got high\n\
Because I got high\n\
Because I got high\n\
I'ma stop singing this song because\n\
I'm high (raise the ceiling... baby)\n\
I'm singing this whole thing wrong because I'm high (bring it back)\n\
And if I don't sell one copy, I'll know why (why man?) (yeah eh eh)\n\
Cause I'm high\n\
Cause I'm high\n\
Cause I'm high\n\
La la da da da da la da da da\n\
Shoobe do be do wa skibitty do da da da la\n\
Get jiggy with it scubbydooby wa 'cause\n\
I'm high, 'cause I'm high, 'cause I'm high\n\
Yo my name is Afroman and I'm from East Palmdale (east Palmdale)\n\
And all this jail weed I be smokin'\n\
Is bomb as hell (excellent delivery)\n\
I don't believe in hittin' that's what I said. Yes! (oh my goodness)\n\
So all of you skins please give me more head... muhwahahaha muh fuck,\n\
A E I O U (a e i o u) and sometimes W (hahahahaha)"

#GlobalVars
days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'mon': 1,
        'tues': 2, 'tue': 2, 'wed': 3, 'thurs': 4, 'thur': 4, 'fri': 5, 'sat': 6, 'sun': 7, 'm': 1, 'w': 3, 'f': 5,
        's': 6, 'su': 7}
daysKeyValueInverse = {1: "Monday", 2: "Tuesday", 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                       7: 'Sunday'}

#TODO depending on final program format / user interface implement these for ease of use
def xyz_input_auto_completer(promptstring, refList): #TODO this might mess up multi-time input 
    """does not require capitalization to auto suggest
    Args:
        promptstring (string): _description_
        refList (list): _description_
    """
    # Define a list of autocomplete words.
    xCompleter = WordCompleter(refList,ignore_case=True) #WHY ignore_care=True, allowing case-insensitive input bc some ref list entries may be capitalized, but dont want to make user have to capitalize input to get auto suggestion    
    user_input = prompt(promptstring, completer=xCompleter)
    return user_input
    #print('You entered:', user_input)
#endregion  

#region -------------------- Internal Mechanisms and Data Structures [Data Collection, Preparation and Formatting] (Plus some gobal functions)


#LOAD DATA CLASS, or encapsulation??? really need for information on
def intialCSVToDataStructures():
    #take names and put into list
    employeeNamesList = []
    with open('CSV Data Folder/SWATEmployeeInfo.csv', encoding='utf-8-sig', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            # Use the names in the '\ufeffEmployee' column as values
            name = row['Employee'] #TODO LEARNING CONCEPT - SOLVED (looked at another csv without \ufeff) Its because I needed to give a encoding parameter to the open() func. why is \ufeff a thing.
            employeeNamesList.append(name) #add names to list
    #testOutput("TEST | employeeNamesList:", employeeNamesList) #\ufeff

    #take gender and put into lsit
    employeeGenderList = []
    with open('CSV Data Folder/SWATEmployeeInfo.csv', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            gender = row['Gender']
            employeeGenderList.append(gender) #add names to list
    testOutput("TEST | employeeGenderList:", employeeGenderList)
    return employeeNamesList, employeeGenderList

employeeNamesList, employeeGenderList = intialCSVToDataStructures()
testOutput("TEST | new intial csv load function resulting vars: ", employeeNamesList,employeeGenderList)

# Selection sort
# time complexity O(n*n)
# sorting by finding min_index
def selectionSort(array, size,setting=None):
    """Settings = how to sort, either ascending, descending.
        DEFAULTS TO ASCENDING order sort

    Args:
        array (_type_): _description_
        size (_type_): _description_
        setting (_type_): How to sort, either ascending, descending
    """
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if setting == 'descending':
                if array[j] > array[min_index]:
                    min_index = j
            else:
                if array[j] < array[min_index]:
                    min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
#endregion

#region------------------------------------------ TIME FUNCTIONS & PROCESSES

class ScheduleTime:
    def __init__(self) -> None:
        pass
    pass

@timer
def program_auto_get_date(get_next_day = False):
    """Returns a string with a full weekday's name. Dependecies: Uses datetime and timezone modules"""
    weekday = datetime.datetime.now(timezone.utc).astimezone().isoweekday() #WHY isoweekday() - returns weekday int mon =1 sun = 7, this aligns with pre hardcoded date code i put in 'days' dict, that way this func gives same output as the manual one and there is no need to adjust any other outputs
    if get_next_day: #WHY if get_next_day - if you want to make the schedule the night before, it knows to generate a schedule for the next day. Since the day values are int you just add +1 to get the next day
        #WHY - if, else statment, check incase its sunday so knows to set weekday equal to 1 for monday. Bc sun = 7 and Mon = 1, otherwise you'd get 8. 8 = undefined
        if weekday == 7:
            weekday = 1 
        else:
            weekday + 1 
    return weekday
    
def user_enter_date():
    """Allows the user to manually enter a day of the week, and returns the integer representationl
    Returns: int : date value"""
    attempts = 0
    while attempts < 3:
        dateUserEntered = input("\nGenerate a schedule for which day of the week: ")
        if dateUserEntered.lower() in days: #Why - account for non-numeric input
            dateUserEntered = days[dateUserEntered] #convert any string input into int
            return dateUserEntered
        elif dateUserEntered in daysKeyValueInverse.keys(): #Why - if numeric input, check if valid
            return int(dateUserEntered)
        else:
            print("\n-----------\nERROR!\n\nMispellling or not a valid day, try again.\n-----------------\n")
            attempts +=1    
    import webbrowser
    print("\n---> To many invalid attempts, exiting... <----\n")
    time.sleep(2.5)
    print("For real man, you must be high as balls if you're struggling to type in a day of the week. Speaking about being high, that reminds me of this song I heard once.....")
    print("\n\nHey, lemme open up youtube real quick so you can sing along!!!")
    webbrowser.open("https://www.youtube.com/watch?v=WeYsTmIzjkw") #LEARNING CONCEPT how to use webbrowser module
    time.sleep(4)
    print("\nALMOST LOADED!!!, 25% there\n")
    print("\nALMOST LOADED!!!, 50% there\n")
    time.sleep(10)
    print("\nALMOST LOADED!!!, 70% there\n")
    time.sleep(10)
    print("\nJK! I'm just making you wait!\n")
    time.sleep(1) 
    print("") #LEARNING CONCEPT - HOW TO MAKE PYHTON WAIT BEFORE EXECUTING SOMETHING, import time, then time.sleep(x)
    print(dumbAndrewMemes1)
    print("\n\nPROGRAM TERMINATING, its all your fault.")
    exit()

@timer
def get_date(get_date_auto = False, get_next_day = False):
    """Gets the date value either from computer or by user input. Returns: (int) representing the weekday"""
    if get_date_auto:
        return program_auto_get_date(get_next_day=get_next_day)
    else:
       return user_enter_date()
        
#TODO settings-ize this if want manual or auto-also see how end user does it. Have a setup mode.
get_date_auto = True
get_next_day = False
dateValue = get_date(get_date_auto = get_date_auto, get_next_day = get_next_day) 
dateValue = 1 #TODO DISABLE ONCE DONE DEBUGGING #NOTE Global vars
dayName = daysKeyValueInverse[dateValue]
print(f"Will generate a schedule for {dayName}.\n")

testOutput("TEST |  dateValue", dateValue)

#region-------------------------- SAVED TIME DATA & GlobalVars
#TODO END GAME UPDATES
#TODO how tf does this work again with employees and taks, why do i have the trues and shit in there again?
#TODO figure out if these need to be lists or not and then go through and edit according. Note to self: need more why comments for code.

#NOTE ONLY USE PURE TIMES, NO TIMES WITH LETTERS, can make label times for printing later
#VERY IMPORTANT OTHERWISE MULTI UNAVAILABILITY AUTO DURATION PARSING WONT WORK
normalDayTimeSlots = [{'7:00am': True, '7:45am': True, '9:15am': True, '9:50am': True, '10:00am': True, '11:00am': True, '11:45am': True, '1:45pm': True, '2:45pm': True, '3:45pm': True, '4:45pm': True, '5:30pm': True, '6:30pm': True, '7:00pm': False, '8:00pm': False, '9:00pm': False}] #'7ishpm': False, '8ishpm': False, '9ish': False #'7ish': 'NG', '8ish': 'Sweeting', '9ish': 'NightChore' #what do when have too special events at the same time??? such as NG and Playtime
wenSpecialTimeslots = ['7:00', '7:45', '9:15', '9:50', '10:00', '11:00', '11:45', '1:45', '2:45', '3:45', '4:45', '5:20', 'TIME DOES NOT EXIST', 'TIME DOES NOT EXIST',  'TIME DOES NOT EXIST', '9is MAYBE'] #'TIME DOES NOT EXIST', 'TIME DOES NOT EXIST',  'TIME DOES NOT EXIST', '9is MAYBE' #can merge TIME DOES NOT EXIST and fromatting later, this is mainly all just formatted so the ;ogram can interpret it, will format for export seperatley
tuesSpecialTimeslots = ['7:00', '7:45', '9:15', '9:50', '10:00', '11:00', '11:45', '1:45', '2:45', '3:45', '4:45', '5:30', '6:30', '7:15',  '8ish', '9:00']
friSpecialTimeslots = []
satSpecialTimeslots = []
sunSpecialTimeslots = []

datesTimeSlots = {
    1:normalDayTimeSlots,
    4:normalDayTimeSlots,
    2:tuesSpecialTimeslots,
    3:wenSpecialTimeslots,
    5:friSpecialTimeslots,
    6:satSpecialTimeslots,
    7:sunSpecialTimeslots
    }

dayTimeSlots = datesTimeSlots[dateValue]
#dayTimeSlots_lenght #so can be more memory efficent
#endregion

# ------------ Confirm if timeslots for the day are acceptable to user and allow modification


#region---------------------------------- Time Schedule Modificaiton 

print("----------------------------------------------------------------------------\n")



@timer
def display_schedule_times(dayTimeSlots):
    """takes the days time slots dict and displays the times to the user. (since dict, only displays time keys and not values: t/f)
    Asks if times for schedule are acceptable, returns the user response as either True or False. Then the false would be used to activate the modify_time_slots func
    Args:
        day_time_slots (Dict): _description_
    """
    
    print("Time periods for today's schedule:")
    print(list(dayTimeSlots[0]))
    print("\nDo you want to change any? (y/n):")
    response = False #TODO RENABLE LATER: DIABLED FOR DEBUG
    #response = input("User: ").strip() #TODO RENABLE LATER: DIABLED FOR DEBUG
    return response # #TODO RENABLE LATER: #TODO look at this again, makes no sense, Disabled FOR DEBUG in yesAnswers #returns as TRUE if yesAnswer, else FALSE cus then is a negative answer

@timer
def insert_time_slot_at_position(day_time_slots, new_time, reference_time, position='after'): #TODO should i remove 'after', do i need keyword args???
    """
    GPT4 assist on this one bc im lazy.
    Inserts a new time slot relative to a reference time slot in an ordered dictionary.
    
    Args:
    day_time_slots (dict): The original dictionary of time slots.
    new_time (str): New time slot to insert (e.g., '10:30').
    reference_time (str): Reference time slot to base the insertion on (e.g., '9:15').
    position (str): Specifies whether to insert before or after the reference time ('before' or 'after').
    """
    
    new_day_time_slots = {}
    inserted = False

    for time, available in day_time_slots.items():
        if time == reference_time and position == 'before':
            new_day_time_slots[new_time] = True  # Assuming the new time slot is available
            inserted = True
        new_day_time_slots[time] = available
        if time == reference_time and position == 'after':
            new_day_time_slots[new_time] = True  # Insert after the current item
            inserted = True

    # If reference_time was not found or new_time is to be added at the end
    if not inserted:
        new_day_time_slots[new_time] = True

    return new_day_time_slots

def modify_schedule_times(day_time_slots):
    print("\n[Options for Editing Tasks]") #Thanks to GPT4 for making my command instructions more concise
    print("1. Add a time from the list")
    print("2. Remove time from the list.")
    print("3. Back - Exits out of current command, to command list")
    print("4. Exit - Exists the editor, assuming your done editing tasks.")
    print("5. Commands - Reprints commands")
    instructionString = "\nPlease enter a command ('add', 'remove', 'back', 'exit', 'commands'):\n"
    timeEditorCommandList = ['add', 'remove', 'back', 'exit', 'commands']
    
    while True:
        userCommand = xyz_input_auto_completer(instructionString,timeEditorCommandList).strip() #WHY - makes it lower case bc the commands in the command list are lowercase, and we are assigning the return value to the userCommand var which represents which command the user wants to run
        if userCommand ==  'add' or userCommand ==  'remove':
            #print(f"\nSelect a {Fore.GREEN}{Style.BRIGHT}time{Style.RESET_ALL} to preform the {Fore.YELLOW}{Style.BRIGHT}{userCommand}{Style.RESET_ALL} command on.")
            while True:
                if userCommand ==  'add':
                    NewTime = input(f"\nEnter the new {Fore.GREEN}{Style.BRIGHT}time{Style.RESET_ALL} (HH:MM)(AM/PM): ").strip()
                    
                    while True: #loops until input is right / spell before or after correctly
                        print(f"\nScheduled times: {list(day_time_slots[0].keys())}")
                        xCompleterP = WordCompleter(["before","after"])
                        print(f"\nDo you want to {Fore.YELLOW}{Style.BRIGHT}insert {NewTime}{Style.RESET_ALL} {Fore.GREEN}{Style.BRIGHT}before{Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}after{Style.RESET_ALL} a specific time: ")
                        Position = prompt("User: ", completer=xCompleterP).strip().lower()
                        if Position == 'before' or Position == 'after':
                            break
                    
                    while True: #loops until input is right / inputs a valid ref time
                        print(f"\n{Fore.GREEN}{Style.BRIGHT}Scheduled times: {list(day_time_slots[0].keys())}{Style.RESET_ALL}")
                        xCompleterR = WordCompleter(list(day_time_slots[0].keys()))
                        print(f"\nInsert {Fore.YELLOW}{Style.BRIGHT}{NewTime} {Position}{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} what scheduled time:{Style.RESET_ALL}")
                        RefTime = prompt("User: ", completer=xCompleterR).strip()
                        if RefTime in list(day_time_slots[0].keys()):
                            break
                    
                    datesTimeSlots = insert_time_slot_at_position(day_time_slots[0],NewTime,RefTime,Position)
                    #print("1.1 pre updated slots", datesTimeSlots)
                    datesTimeSlots = [datesTimeSlots] #turn it back into orignal format as a dict within a one item list
                    #print("1.2 pre updated slots", datesTimeSlots)
                    #print("\n\n1.3 UPDATED SLOmTS: ", list(datesTimeSlots[0].keys()),"\n\n")
                    
                    print("\nUpdated times:\n", list(datesTimeSlots[0].keys()))
                    
                elif userCommand ==  'remove': #if not 'add' then must be 'remove'
                    print("Scheduled times: ", list(day_time_slots[0].keys()))
                    userCommand = xyz_input_auto_completer(userCommand, list(day_time_slots[0].keys())).strip()
                    day_time_slots[0].remove(userCommand)
                    print("\nTimes remaining: ", list(day_time_slots[0].keys()))
                print("\nType 'back' to exit section")
                print(f"[Press enter] to continue {userCommand}")
                userContinueQuestion = input().strip().lower()
                if userContinueQuestion == 'back':
                  break
        if userCommand == "exit":
            break
    print("Times confirmed.")
    return datesTimeSlots
    
if display_schedule_times(dayTimeSlots):
    dayTimeSlots = modify_schedule_times(dayTimeSlots)

# -------- standardize the timeslots
@timer
def timeSlotStandardizer(dayTimeSlotsKeysList):
    """ Standardizes timeslots values and makes ref dictionaries. Takes the "dayTimeSlots" var. 
    Args:
        time_slots_of_the_day (Type: List): Input should be a list with dictionaries. Example: normalDayTimeSlots = [{'7:00': True, '7:45': True, '9:15': True, '9:50': True, '10:00': True, '11:00': True, '11:45': True, '1:45': True, '2:45': True, '3:45': True, '4:45': True, '5:20': True, '6:30': True, '7ish': 'NG', '8ish': 'Sweeting', '9ish': 'NightChore'}] #what do when have too special events at the same time??? such as NG and Playtime
    """
    
    #first have to make a ref book to convert the stuff into in, Makes a list of the times / keys of dayTimeSlots
    lengthDayTimeSlots = len(dayTimeSlotsKeysList)-1 #WHY -1 len gives me one more than index number, so keep in mind when using len to go thru indexs
    testOutput("TEST | lengthdayTimeSlots: ", lengthDayTimeSlots)
    iterDayTimeSlotsStandardizer = 0
    while iterDayTimeSlotsStandardizer <= lengthDayTimeSlots:
        iterDayTimeSlotsStandardizer += 1
    testOutput("TEST | 1 time_slot_keys: ", dayTimeSlotsKeysList)

    # put times as values, and ascending number as key (NtS)- Numbers to Strings
    dayTimeSlotsStandardizedNtSLocal = {}
    iterDayTimeSlotsStandardizerA = 0
    while iterDayTimeSlotsStandardizerA <= lengthDayTimeSlots:
        dayTimeSlotsStandardizedNtSLocal.update({iterDayTimeSlotsStandardizerA:dayTimeSlotsKeysList[iterDayTimeSlotsStandardizerA]})
        iterDayTimeSlotsStandardizerA+=1
        testOutput("[TEST | 2.1, IN LOOP] new dict dayTimeSlotsStandardizedNtSLocal: ", dayTimeSlotsStandardizedNtSLocal)
    testOutput("[TEST | 3.1, OUT OF LOOP] new dict dayTimeSlotsStandardizedNtSLocal: ", dayTimeSlotsStandardizedNtSLocal)

    #TODO #ALSO INCLUDE IN MASTER CONVERTER - wut
    # put numbers as values, and times as key (StN)- Strings to Numbers
    dayTimeSlotsStandardizedStNLocal = {}
    iterDayTimeSlotsStandardizerB = 0
    while iterDayTimeSlotsStandardizerB <= lengthDayTimeSlots:
        dayTimeSlotsStandardizedStNLocal.update({dayTimeSlotsKeysList[iterDayTimeSlotsStandardizerB]:iterDayTimeSlotsStandardizerB})
        iterDayTimeSlotsStandardizerB+=1
        testOutput("[TEST | 2.2, IN LOOP] new dict dayTimeSlotsStandardizedStNLocal: ", dayTimeSlotsStandardizedStNLocal)
    testOutput("[TEST | 3.2, OUT OF LOOP] new dict dayTimeSlotsStandardizedStNLocal: ", dayTimeSlotsStandardizedStNLocal)
    return dayTimeSlotsStandardizedNtSLocal,dayTimeSlotsStandardizedStNLocal 

dayTimeSlotsKeysList = list(dayTimeSlots[0].keys())  #for when i just want to diplay the keys / dates. will make easier to change stuff later too. BEWARE: Is static tho and does not updates with the acutaly DICT
dayTimeSlotsStandardizedNtS, dayTimeSlotsStandardizedStN = timeSlotStandardizer(dayTimeSlotsKeysList)

#endregion
#endregion

#region------------------------------------------------- EMPLOYEES 2.0 - CLASS BASED


"""Keep the Single Responsibility Principle in mind: a class should have one, and only one, reason to change. 
This can help in deciding what functionality belongs where.
"""

class EmployeeManager:
    """"For operations that involve multiple employees or require knowledge about the entire collection of employees"""
    def __init__(self):
        self.employees = {} #stores name & instances of employee class

    #setsup everythign else, thing of as instantiator for employee objs
    @timer
    def add_employee(self, employee_name, employee_inst,dayTimeSlotsKeysList): #employee instance, also idk if most efficent way to create these instances
        self.employees[employee_name] = employee_inst
        self.employees[employee_name].set_default_availability(dayTimeSlotsKeysList)
        #also make set default availability!!
        

    @timer
    def set_employee_availability(self, employee_name, unavailable_time_slots):
        """_summary_
        Args:
            employee_name (string): _description_
            unavailable_time_slots (list): List of unavailable timeslots 
        """
        #employee = self.find_employee_by_name(employee_name) #finds employee instance, but honestly no need to iterate thru can just give name to find.
        employee = self.employees[employee_name]
        if employee:
            employee.set_unavailability(unavailable_time_slots) #Employee??????? 

    def get_employee_by_name(self, name):
        return self.employees.get(name)

    @timer
    def total_available_time_slots(self):
        return sum(employee.sum_available_time_slots() for employee in self.employees) 

    @timer
    def get_available_employees(self, time_slot):
        available_at_time = {}
        for employee in self.employees:
            if self.employees[employee].is_available(time_slot):
                available_at_time[employee] = None
        return available_at_time
    @timer
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
    

class AvailabilityManager:  #IDK, pointless for now until I make frontend???. Fuck idk
    def __init__(self, employee_manager):
            self.employee_manager = employee_manager
    
    def run(self):
        def employeeUnavailabilityUserInputPrompt():
            """_summary_
                REQS: xyz_input_auto_completer, multi_time_input_detector_and_converter_employee_unavailability
                ALSO REFS: employeeNamesList, dayTimeSlotsKeysList, noAnswers, yesAnswers
                RETURNS: unavailableEmployeeName, tempListOfUnavailabilites 
            Args: None
            """
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
            
            @timer    
            def multi_time_input_detector_and_converter_employee_unavailability(input_str, times_list):
                
                #CHECK IF ERROR, dont feel like passing as an argument in all these functions 10 times
                time_list_minutes_compiled = False #WHY thing to help only compile list once in function, and then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
                time_list_minutes = []
                
                @timer
                def find_valid_time_slot(input_time_str, times_list): #WHY thing to help only compile list once in function, and then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
                    
                    @timer
                    def compile_time_list_minutes():
                        nonlocal time_list_minutes  # Indicate that we're using the outer function's variable
                        nonlocal time_list_minutes_compiled

                        # Compile the list only if it hasn't been compiled yet
                        if not time_list_minutes_compiled:
                            time_list_minutes = sorted([time_to_minutes(time_str) for time_str in times_list])
                            time_list_minutes_compiled = True  # Update the flag to prevent re-compilation
                            print("COMPILER: Not compiled yet")
                        print("COMPILER: Sucessfully excuted compile checker thingy")

                    
                    #nonlocal time_list_minutes
                    #nonlocal time_list_minutes_compiled
                    
                    @timer
                    def time_to_minutes(time_str): #for intial conversion into min for comparison
                        #nonlocal time_list_minutes
                        #nonlocal time_list_minutes_compiled
                        
                        print("TEST | indv time string:", time_str)
                        """Convert a hh:mm AM/PM time string to minutes since midnight."""
                        time_str = time_str.upper() #makes AM/PM upper just incase
                        
                        #check if without am/pm and asks to input to avoid errors before proceeding with the rest of the code.
                        time_pattern = r'^\d{1,2}(:\d{2})?$' # This pattern matches a string that looks like a time (one or two digits for hour, optionally followed by ":" and one or two digits for minutes)
                        if re.match(time_pattern, time_str) and not re.search(r'AM|PM', time_str, re.IGNORECASE): #Returns true if valid time, but no AM/PM, returns false if am/pm in it
                            while True:
                                    print(f"\n{Fore.RED}{Style.BRIGHT}WARNING: {time_str} is missing an am/pm designator.{Style.RESET_ALL}")
                                    am_pm = input(f"Please enter if {time_str} is am or pm: ").strip().upper() #WHY - for datetime module functions to work am/pm must be uppercase: Am/PM
                                    if am_pm  == 'AM' or am_pm == 'PM':
                                        time_str = time_str+" "+am_pm
                                        break # Exit loop on successful parse
                                    else: 
                                        print("Invalid input, try again.")            
                        time_formats = [
                            "%I:%M %p", # Format 1: 08:25 PM # Note the use of %I for hour and %p for AM/PM
                            "%I %p", # Format 2: 7 PM
                            "%I:%M%p", # Format 3: 08:25AM <-- WHY needed because when try to convert ref list to min before midnight, the values come in as 7:00am etc, with no space between time and am/p,
                            "%I%p", # #Format 4: 7PM  
                            ]
                        
                        successful_parse = False
                        for fmt in time_formats:
                            try:
                                time_val = datetime.datetime.strptime(time_str, fmt) #ref datetime twice, once for the module, once for the class
                                successful_parse = True 
                                break # Parsing succeeded; exit the loop
                            except:
                                continue #Try the next format
                        
                        # If no format matched, handle the failure:
                        if not successful_parse:
                            print(f"\n\n{Fore.RED}{Style.BRIGHT}Your time input:'{time_str}', does not match any known format.{Style.RESET_ALL}\n\n")
                        
                        #print("TEST time. val : ", time_val)
                        #print("TEST time_to_minutes final result: ", time_val.hour * 60 + time_val.minute)
                        return time_val.hour * 60 + time_val.minute
                    
                    @timer
                    def minutes_to_time(minutes): #for conversion from minutes back to 12Am/Pm time after sequence has been run and found a valid times
                        """Convert minutes since midnight back to a hh:mm AM/PM string."""
                        # Convert minutes back to a datetime object to leverage strftime formatting
                        hours, minutes = divmod(minutes, 60)
                        time_val = datetime.datetime(year=1, month=1, day=1, hour=hours, minute=minutes)
                        # Note the use of %I for hour, %M for minutes, and %p for AM/PM
                        #print("TEST | minutes_to_time final [time_val]: ", time_val.strftime("%I:%M %p").lower())
                        return time_val.strftime("%-I:%M%-p").lower() # WHY Format the time without leading zeros, spaces between time and am/pm, and lowercase am/pm, bc in master ref list its "9:25am" not "09:25 AM" and the time will later be checked against it at some point, plus good to keep uniformity.

                
                    # Converts both the input time and the master ref list of times to minutes since midnight
                    input_time_minutes = time_to_minutes(input_time_str)
                    compile_time_list_minutes()
                    
                    """
                    #IDk if need to make a funciton works fine as is, plus idk if time_to_minutes() call would work if i put it under the parent
                    #thing to help only compile list once in function, adn then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
                    if not time_list_minutes_compiled:
                        time_list_minutes = sorted([time_to_minutes(time_str) for time_str in times_list]) #WHY Sort and convert into minutes the master time list for ref
                        #CHECK IF ERROR, dont feel like passing as an argument in all these functions 10 times
                        time_list_minutes_compiled = True
                    else:
                        time_list_minutes
                    """
                    
                    #print("TEST | input_time_minutes: ",input_time_minutes)
                    #print("TEST | time_list_minutes: ",time_list_minutes)
                    
                    # Binary search for the next time greater than or equal to the input time
                    left, right = 0, len(time_list_minutes) - 1
                    while left <= right:
                        mid = (left + right) // 2
                        if time_list_minutes[mid] < input_time_minutes:
                            left = mid + 1
                        else:
                            right = mid - 1        
                    # Check if we found a match
                    if left < len(time_list_minutes):
                        print("TEST | Binary search final results:", minutes_to_time(time_list_minutes[left]))
                        return minutes_to_time(time_list_minutes[left])
                    else:
                        # If no time is found that is greater, consider the list circular or return an error/indicator
                        print("ERROR | multi time converter, finding valid time slot to calc diff | No matching timeslot found. Check input, or timeSlots list, see if AM/PM issue or formatting")
                
                @timer
                def fill_time_slots_inbetween_A_and_B(timeA,timeB):
                    #1, take input times, find corresponding standardized number for position in the master ref times list. 
                    timeAPeriod = dayTimeSlotsStandardizedStN[timeA]
                    timeBPeriod = dayTimeSlotsStandardizedStN[timeB]
                    #2, Calculate the positional difference between inputs within the master reference times list. This difference reveals the count of time periods separating Time A and Time B. Each timeslot in this master list is uniquely identified by an ascending whole number, indicating its sequence
                    #number_of_slots_between_times = timeBPeriod - timeAPeriod #Assumes Time B is later than Time A (e.g., 8am to 12pm). This ensures a positive duration/range, as Time B must be greater than Time A.
                    #3 Find the times that are between A and B and add to a list, includes A and B in the list
                    
                    times = []
                    for number in range (timeAPeriod,timeBPeriod+1): #WHY +1? #LEARING CONCEPT - range (timeAPeriod,timeBPeriod+1) why +1, because the range funciton is sort of like a list where it starts at 0, so to have it include the end digit you have to give it+1
                        times.append(dayTimeSlotsStandardizedNtS[number])
                    return times
                
                def problematic_time_input_warning(time_var,masterTimesList):
                    print(f"\n{Fore.RED}{Style.BRIGHT}You entered {time_var}, which doesn't line up with the start of a schedule window:{Style.RESET_ALL}\n{masterTimesList}.\n{Fore.LIGHTMAGENTA_EX}Oh well, I'll just have to guess which time slot it should start at. You might of just forgotten to include am/pm, so you might be good. But keep your fingers crossed homie. I got a 1 on the AP Computer Science exam.{Style.RESET_ALL}\n")

                @timer
                def time_range_handler(input_val):
                    timePair = input_val.split("-")
                    print("Test| input_val post split: ", timePair)
                    for item in timePair:
                        item.strip().lower() #This is just so the am/pm is lowercase to match the master time ref list (dayTimeSlots, which formatted like 8:00am etc) in the if statments below.
                    if not timePair[0] in dayTimeSlots[0]: #Time1
                        problematic_time_input_warning(timePair[0],dayTimeSlotsKeysList)
                        timePair[0] = find_valid_time_slot(timePair[0],times_list)
                        #print("TEST | find_valid_time_slot(timePair[0],times_list) -> timePair[0]", timePair[0])
                    if not timePair[1] in dayTimeSlots[0]: #Time2 
                        problematic_time_input_warning(timePair[1],dayTimeSlotsKeysList)
                        timePair[1] = find_valid_time_slot(timePair[1],times_list)
                        #print("TEST | find_valid_time_slot(timePair[1],times_list) -> timePair[1]", timePair[1])

                    #now have valid timeslot refs, I can find all the values betwen the two and can mark all the times inbetween unavailable for the employee
                    inbetween_slots_list_inclusive = fill_time_slots_inbetween_A_and_B(timePair[0],timePair[1])
                    return inbetween_slots_list_inclusive
                
                #Actual logic process --------------------
                
                #TODO make clearer??? also expand on this later to include if they put "and" in etc
                SecondListExpandedValues = [] #BEWARE this is to prevent runaway loops, bc im paranoid that ill wind up with a loop if it goes through and keeps expanding as it append in a for loop
                if "," in input_str: #so can input stuff as 6am, 7pm, 4:45am then split into indvs in list
                    #print("TEST TIRGGERED MAIN IF")
                    split_times_list = input_str.split(",") #string.split(separator, maxsplit) default = -1 is as many as occur
                    #print("TEST post "," split - og input_str list ", split_times_list)
                    for item in split_times_list:
                        item.strip().lower() #Remove trailing whitespace
                        if "-" in item:
                            SecondListExpandedValues.extend(time_range_handler(item))
                            #print("TEST TIRGGERED main if, for, if")
                        else: #Incase value isnt "-" but ","
                            if not item in dayTimeSlots[0]: #incase not a valid time.
                                SecondListExpandedValues.append(find_valid_time_slot(item,times_list))
                                problematic_time_input_warning(item,dayTimeSlotsKeysList)
                                #print("TEST TIRGGERED main if, for, if,else->if ")
                            else: 
                                SecondListExpandedValues.append(item)
                                #print("TEST TIRGGERED main if, for, if,else,if-> else")
                        #put "-" in here so can make multiple multi values if put in list form
                    #IDK see if needs this:
                else: #WHY - bc maybe user input 7-8am, 10-11am. if put "-" then would trigger, but wouldnt realize is part of larger list
                    print("TEST TIRGGERED BASE ELSE")
                    if "-" in input_str:
                        SecondListExpandedValues.extend(time_range_handler(input_str))
                print("TEST | final func output SecondListExpandedValues", SecondListExpandedValues)
                return SecondListExpandedValues
                #WHY should return a list, then at the place called i can decide how it will be joined / added to other vars based on circumstance.
                
                #make handle inputs such as 7am-9:15am, 7-9:15am, give an error if 7am-AnyNumberWithout AM/PM, raise and exception if impossible calc such as TimeB starts before A, make cycle if invalid time. Make a exit emergency statement to exit the loop?????
                
                """
                #TODO do that calcs gap or goes to nearest one, then calcs difference and inputs it.
                #iterates up and down until it reaches closest value. well checks if has :, and not 00, or
                # maybe then iterates thru and finds the cloest one. Could at :00 to 8am then iterate until match see which takes list iteraiton. then find lengths idk
                """
            
            while True: #WHY - to make sure user inputs name correctly
                unavailableEmployeeName = 'str'
                tempListOfUnavailabilites = []
                print("\n\nWho?\n")
                unavailableEmployeeName = employee_name_input_auto_completer(employeeNamesList, "User: ") #TODO Y/N SHOULD AKS IF ALL DAY FIRST, maybe make enter between two dates
                if unavailableEmployeeName in employeeNamesList:
                    break
                else:
                    print("ERROR | They don't work here silly. | Not a valid employee name, check your capitalization and spelling.")
                    
            print("\nWhen is "+unavailableEmployeeName+" unavailable? (Please affix am/pm to end of the times. Example: 7am, 7:00pm, 11:45am-2pm, 6pm-9pm)\n") #LEARNING CONCEPT - input takes 1 arguments, so if need to put vars in output text concatente the string, use f strings, or str.format(). DON'T do this: tempTime = input("\nWhen is",unavailableEmployeeName,"unavailable?\n\nUser: ")
            tempTime = xyz_input_auto_completer("User: ", dayTimeSlotsKeysList)
            tempTime = multi_time_input_detector_and_converter_employee_unavailability(tempTime,dayTimeSlotsKeysList)

            #####TODO REALLY IMPORTANT MAKE AN EXCEPTION DN TRY AGAIN IF THEY ENTER TIME IN WRONG ORDER, OR LIKE ENTER THE START TIME BEFORE END TIME WHICH IS INCOMPUTABLE
            tempListOfUnavailabilites.append(tempTime) #UPGRADE: use enumerate and append #dict. ??????
            print("Unavailabilities updated: ", tempListOfUnavailabilites)

            #loop - WHY? so can insert as many time slots as needed.
            multipleUnavailbilites = input("\n\nIs that the only time, or is " + unavailableEmployeeName +" unavailable at other times, y or n? \n\nUser: ") #LOOP THIS unitl Y/N
            if multipleUnavailbilites in yesAnswers:
                addEntries = True
                while addEntries == True:
                    print("Current unavailable times: ", tempListOfUnavailabilites)
                    print("\nWhen is",unavailableEmployeeName,"unavailable? (Please affix am/pm to end of the times. Example: 7am, 7:00pm, 11:45am-2pm, 6pm-9pm. Also 12Hr time values only)\n")
                    #while True: #so can cycle thru if fucked up #TODO fix error cycle and functionality later
                    newTime = xyz_input_auto_completer("User: ", dayTimeSlotsKeysList)
                    newTime = newTime.replace(" ","")#WHY incase they put a " " between the time and am/pm. Example: 7:00 am, this would cause problems because the master time list doesnt have spaces, just 8am or 11:45am. 
                        #Also later when ordering/prepping and integrating with main data unavailable emp times are compared to the daysTimes dict whose keys / times are all formated as 8:00pm without spaces. CHECK IF ERROR
                        #try: #incase they enter something that fucks everything up    
                    newTime = multi_time_input_detector_and_converter_employee_unavailability(newTime,dayTimeSlotsKeysList)
                        #except Exception as e:
                            #print(f"{Fore.RED}{Style.BRIGHT}ERROR {e}|\nYou probbaly messedup up the unavailbility time input so badly that I couldnt fix it,{Fore.GREEN}{Style.BRIGHT} its okay tho, i'll just restart the input sequence.{Style.RESET_ALL}\nRemember the input needs to be a valid 12hr standard time.\n\nBtw, here is what you inputted that messed it up so badly: ",newTime)
                            #continue #TODO learn more about exceptions, errors, and raises and type up in document then come back and redo this
                        #else:
                            #break
                    tempListOfUnavailabilites.append(newTime)
                    print("Unavailabilities updated: ", tempListOfUnavailabilites)
                    
                    enterMoreUnavailableTimes = input("\n\nDo you need to enter more times? (Y/N)\n\nUser: ")
                    if enterMoreUnavailableTimes in noAnswers:
                        addEntries = False
                        break
                    testOutput("2 tempListOfUnavailabilites list", tempListOfUnavailabilites)
            else:
                testOutput("TEST | Else thingy past lol",None)
                print(f"\nConfirmed: {unavailableEmployeeName} is unavailable at {tempListOfUnavailabilites}.\n")
                testOutput("3 tempListOfUnavailabilites list", tempListOfUnavailabilites)
            
            return unavailableEmployeeName, tempListOfUnavailabilites 
        employee_name, times = employeeUnavailabilityUserInputPrompt()
        self.employee_manager.set_employee_availability(employee_name, times)
      
class Employee:
    """For operations that involve manipulating an employee's attributes"""
    
    #default times for taks assigned to - based on previous user input. #rename var later???? idk
    default_assigned_to_times = {time_slot: None for time_slot in dayTimeSlotsKeysList}
 
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
        
    def assign_task(self,time_slot,task):
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
    

#instantiate employees
employee_manager = EmployeeManager() #TODO Go here if break
availability_manager = AvailabilityManager(employee_manager) #could or should i move instantiation into the class method func def???

#make it depend on type of data file, eventually make usable with SQL, and JSON formats
#create stuff from data
numberOfaemployeeInstances = 0
for name, gender in zip(employeeNamesList, employeeGenderList): #can add any number of args, returns results as a tuple 
    employee_instance = Employee(
        name,
        gender
        ) #wierd dict dup thing gonna be a prob?
    employee_manager.add_employee(name, employee_instance,dayTimeSlotsKeysList)



#Employee Info Input
def user_Input_Employee_Unavailbilites(Backend=None):
    """
        Sub def employeeUnavailabilityUserInputPrompt reqs: 
            REQS: xyz_input_auto_completer, multi_time_input_detector_and_converter_employee_unavailability
            ALSO REFS: employeeNamesList, dayTimeSlotsKeysList
    Args:
        Backend (_type_, optional): _description_. Defaults to None.
    """
    
    anyoneUnavailable = input("\nIs anyone unavailable today?\n\ny or n? \n\nUser: ")
    if anyoneUnavailable in noAnswers:
        print("\nConfirmed: No unavailabilites.")
    else:
        availability_manager.run()
        while True:     
            print("\nIs anyone else unavailable?\n\nY or N?\n")
            anyoneElse = input("\nUser: ")
            if anyoneElse in noAnswers:
                print("\nConfirmed: no one else is unavailable.\n")
                break
            else:
                availability_manager.run()

user_Input_Employee_Unavailbilites()

print("\n---------------------------------------------------------------------------------------------------------------\n") 

#endregion

#region----------------------------------------------- TASKS

#region----------------------------- Tasks import data and basic data structures
#TODO maybe need to check if multi start times then go thru start times, also how to integrate with premade lsit for startTime one in additional tasks function, also see if can do something / same thing for frequency

class TaskManager:
    def __init__(self, defaultTasksDictionary, **kwargs):
        self.tasks = {**defaultTasksDictionary} # A list to hold all tasks, add specialTasksDict later **specialTasksDict
    
    def add_task(self, task_identifier, task):
        self.tasks[task_identifier] = task

    def delete_task(self, task_identifier):
        if task_identifier in self.tasks:
            del self.tasks[task_identifier]

    #TODO eventually find out how to pass arugments to make if statments in these so i can tell it to be verbose or not
    def display_all_tasks(self):
        # Iterate through the task instances in the dictionary values
        for task in self.tasks.values():
            task.describe_var_name_times()  # Call the describe method on each task instance
        
    def task_info(self, taskVarName):
        defaultTasksDictionary[taskVarName].describe_verbose()
              
    def total_tasks_for_today(self):
        # Similarly, this is a placeholder. You need to add logic to count today's tasks specifically.
        return len(self.tasks)

    def assign_to(self,time_slot,employee_name):
        pass
        #TODO SOLVE THIS FIRST, PROBLEM I HAVE MULTIPLE TASK DICTIONARIES HOW WILL I FIX THIS?? WTF???
        #I think just how to mkae all the naming things non confucing has discuraged me from doing this.
    
    class Task:
        task_attribute_guide = {
        "task_name": "The name of the task.",
        "frequency": "Frequency indicates the number of time periods a task is available for scheduling in a day, not the total number of times it will be scheduled. The actual number of task instances is determined by multiplying this frequency by the min_num_people_needed, which specifies how many people are required for each instance. Essentially, the task's total daily instances equal its frequency times the minimum people required.",
        "start_time": "Primary start time for the task. Additional start times can be specified in start_time2 to start_time6 attributes.",
        "duration": "The expected duration of the task. Enter an integer (1,2,3,4 etc). NOTE: Each duration increment is equal to one time period on the schedule",
        "min_num_people_needed": "The minimum number of people required to complete the task.",
        "importance": "The importance level of the task, which might affect scheduling priority.",
        "task_cost": "Calculated based on various factors such as frequency and duration. Represents the 'cost' or effort of the task, is mainly for the algorithim to figure out how to priortize things and see if a solution is possible",
        "preassigned_to": "The person or group preassigned to the task. Optional, may be decided during task scheduling.",
        "reccomended": "Indicates if the task is recommended based on certain criteria. Can be True/False.",
        "chosen": "Indicates if the task has been chosen to be performed. Can be True/False.",
        "task_tier": "The tier or level of the task, which might categorize its priority or type.",
        "gender_specific": "Indicates if the task is gender-specific, requiring a specific gender to perform.",
        "gender_required": "Specifies the gender required for gender-specific tasks.",
        "preassigned": "Indicates if the task is pre-assigned to someone specific.",
        "overlap_problem_task_cost_offsetter": "Used to offset the cost of tasks that overlap, ensuring efficient scheduling.",
        "pref_time": "The preferred time for the task to start. This is considered during scheduling to optimize task assignments.",
        "time_preferred": "Alternative or additional preferred start times for the task.",
        "not_before_time": "The earliest time the task should start.",
        "not_after_time": "The latest time the task should start.",
        "scheduledoccurance": "Specifies if the task has a scheduled occurrence, potentially overriding other timing preferences.",
        "occurs_every_n_days": "For repeating tasks, specifies the interval in days between each occurrence.",
        "spawn_days": "Specifies on which days of the week the task is applicable, allowing for weekly scheduling patterns."
        # Add additional attributes as needed.
        }

        @classmethod
        def print_help(cls,topic): #LEARNING CONCEPT, .cls is similar to .self
            """Prints help information for a given topic related to a task attributes=."""
            info = cls.task_attribute_guide.get(topic, "Help topic not found.")
            print(f"\n{topic}:\n {info}\n")
        
        def __init__(self, task_name, task_frequency, start_time, duration, min_num_people_needed, importance, task_cost, preassigned_to=None, reccomended=None, chosen=None, task_tier=None, gender_specific=None, gender_required=None, preassigned=None, overlap_problem_task_cost_offsetter=None, pref_time=None, time_preferred=None, not_before_time=None, not_after_time=None, start_time2=None, start_time3=None, start_time4=None, start_time5=None, start_time6=None, scheduledoccurance=None, occurs_every_n_days=None, spawn_sunday=None, spawn_monday=None, spawn_tuesday=None, spawn_wensday=None, spawn_thursday=None, spawn_friday=None, spawn_saturday=None, task_variable_name=None, certs_required=None, requires_certs=None):
            
            #-2
            #WUT?????
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
            
            
            #TODO maybe make specialStringVar Versions
            self.tier = task_tier   # Initialize as 0, may change later based on your TODO note
            self.task_name = task_name
            self.frequency = task_frequency
            self.duration = duration
            self.min_num_people_needed = min_num_people_needed
            self.importance = importance
            self.gender_specific = gender_specific
            self.gender_required = gender_required
            self.preassigned = preassigned
            self.pref_time = pref_time  # Optional, based on your TODO note
            self.time_preferred = time_preferred  # Optional, based on your TODO note
            self.not_before_time =  not_before_time
            self.not_after_time = not_after_time
            self.start_time2 = start_time2
            self.start_time3 = start_time3
            self.start_time4 = start_time4
            self.start_time5 = start_time5
            self.start_time6 = start_time6
            self.start_time = [time for time in [start_time, start_time2, start_time3, start_time4, start_time5, start_time6] if time.strip()] #Thanks GPT4            
            #DONE find way to get rid of unsed timeslot whitespace
            self.scheduledoccurance = scheduledoccurance
            self.occurs_every_n_days = occurs_every_n_days
            self.spawn_sunday = spawn_sunday
            self.spawn_monday = spawn_monday
            self.spawn_tuesday = spawn_tuesday
            self.spawn_wensday = spawn_wensday
            self.spawn_thursday = spawn_thursday
            self.spawn_friday = spawn_friday
            self.spawn_saturday = spawn_saturday
            self.chosen = chosen
            self.reccomended = reccomended
            self.task_cost = "To be caculated at assignment time in algorith with calc_task_cost()"
            self.overlap_problem_task_cost_offsetter = overlap_problem_task_cost_offsetter
            self.preassigned_to = preassigned_to #TODO MAYBE REMOVE that way can look up task to see who is assigned to it and when (when part might be more complicated)
            self.assigned_to = {key: [] for key in dayTimeSlotsKeysList} #Time, and who assigned to ( in list)#when, who #TODO GENERATE APON SCHEDULING
            self.task_variable_name = task_variable_name
            self.start_time_iter = 0
            self.requires_certs = requires_certs
            self.certs_required = certs_required #List the cert req, maybe set to dict by default? so easy to call up?? and can = 0 if none of type req. like {} for none or {None:None} or {Lifegaurd:2}
            #TODO add this to csv file, and file converter program
            #self.order
            
        def calc_task_cost(self, **kwargs):
            self.task_cost = task_frequency*len(self.start_time)
            #TODO idk if work but can call during althorithm to calc exact freq 
            #worry about later
        
        def describe_var_name_times(self,**kwargs): #
            print(f"Task var name: {Fore.BLUE}{Style.BRIGHT}{self.task_variable_name}{Style.RESET_ALL} {self.start_time}")

        def describe_verbose(self,**kwargs): #
            print("---------------------------------------------")
            print(f"Task var name: {Fore.BLUE}{Style.BRIGHT}{self.task_variable_name}{Style.RESET_ALL}")
            #if kwargs.get('verbose', False): #This approach does not actually check verbose to be false; rather, it provides a default value (False) to use in case verbose is not specified when the 
            print(f"Task name: {self.task_name}")
            print(f"Tier: {self.tier}")
            print(f"Frequency: {self.frequency}")
            print(f"Start Times: {self.start_time}")
            print(f"Duration: {self.duration}")
            print(f"Minimum Number of People Needed: {self.min_num_people_needed}")
            print(f"Importance: {self.importance}")
            print(f"Task Cost: {self.task_cost}")
            print(f"Assigned To: {self.preassigned_to if self.preassigned_to else 'Not Assigned'}")
            print(f"Recommended: {self.reccomended}")
            print(f"Chosen: {self.chosen}")
            print(f"Gender Specific: {self.gender_specific}")
            print(f"Gender Required: {self.gender_required}")
            print(f"Preassigned: {self.preassigned}")
            print(f"Overlap Problem Task Cost Offsetter: {self.overlap_problem_task_cost_offsetter}")
            print(f"Preferred Time: {self.pref_time}")
            print(f"Time Preferred: {self.time_preferred}")
            print(f"Not Before Time: {self.not_before_time}")
            print(f"Not After Time: {self.not_after_time}")
            # Assuming start_time2 to start_time6 are additional optional start times
            #additional_start_times = [self.start_time2, self.start_time3, self.start_time4, self.start_time5, self.start_time6]
            #print("Additional Start Times: ", [time for time in additional_start_times if time is not None])
            print(f"Scheduled Occurrence: {self.scheduledoccurance}")
            print(f"Occurs Every N Days: {self.occurs_every_n_days}")
            # Weekday spawns
            weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
            #TODO fix this shit so actually represent what is yes / no. IMPORTANT
            spawns = [self.spawn_sunday, self.spawn_monday, self.spawn_tuesday, self.spawn_wensday, self.spawn_thursday, self.spawn_friday, self.spawn_saturday]
            print("Spawn Days: ", [day for day, spawn in zip(weekdays, spawns) if spawn]) 
            print("----------------------------------------------\n")
        
        def get_task_requirements(self): #LEARNING CONCEPT - DICTIONARY COMPREHENSIONs {key_expression: value_expression for item in iterable}
            req_dict = {}
            if self.gender_specific is not None and self.gender_specific != "No": #only inlcude req if there is a req inputted if empty, dont return anything - is a simpler system than checking
                req_dict["gender"] = self.gender_required #or gender specific #WHY - so the keys should be the attr names of the mpoyees bc it will use the key name to see it employee has that attr then compares the .self val to the employee val to see if match
            if self.certs_required is not None and self.certs_required != "No": #change No(s) later
                req_dict["certifications"] = self.certs_required
                #may have to figure out to include how many eventually and make that work with the serch algo, also may have to use an "OR"
                #FUTURE, evantually maybe make this a dict comprehension??? so can jsut edit the names / reqs in a list?
            return req_dict
        
        def assign_employee_to_task(self,time_slot,employee_name):
            if isinstance(time_slot, list): #TODO maybe at some point make these to take ditionaries so would be smaller adn more efficent??
                for slot in time_slot:
                    self.assigned_to[slot].append(employee_name)
            else:
                self.assigned_to[time_slot].append(employee_name) #IDK if will work #QUESTION - should be extend or append idk what if not pre exisitng lists
            #TODO make sure doesnt override and stuff, figure out later           
                        
def try_convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value  #IF ERROR, check this, maybe set to None.


#TODO take remaining slots and ones that require user input off the diplay / desribe list and edit list???? idk how to deal with them. atleast take cusotm ones off, can ask what they want spare slots to be.

defaultTasksDictionary = {}
defaultTasksVarNamesList = []

@timer
def defaultTasksListCSVToDictConverter(): #consider renaming this later
    with open('CSV Data Folder/SWATBasicTasksListForScheduler.csv', newline='', encoding='utf-8-sig') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        #for row in csvreader:
        
        #1, First create dict with VarName as key and the object as the value
        for row in csvreader:
            # Use the 'a' column as keys and 'b' column as values
            #task_name = row['TaskVariableName']    
            
            """
            # Convert frequency and min_num_people_needed to integers
            frequency = try_convert_to_int(row['Frequency'])
            min_num_people_needed = try_convert_to_int(row['MinNumPeopleNeeded'])
            duration = try_convert_to_int(row['TaskDuration'])
            #print("min_num_people_needed", type(min_num_people_needed),min_num_people_needed)
            #print("frequency", type(frequency),frequency)
            #print("duration", type(duration),duration)"""


            tier = try_convert_to_int(row['Tier'])
            #print("tier", type(tier),tier)

            #task_cost = frequency * (min_num_people_needed * duration)
            #print("task_cost", type(task_cost),task_cost)
            

            #1.8 put every TaskVariableName in a list so the autoComplete can use in menus and stuff
            defaultTasksVarNamesList.append(row['TaskVariableName'])
            
            #2, Second have auto cycle through and popualte all class attribtues with data from CSV) # Create a new Task instance and store it with the user-defined name as the key
            defaultTasksDictionary[row['TaskVariableName']] = TaskManager.Task(
            #row['\ufeffTaskVariableName'], #TODO evaluate if need or find work around ERROR i think because dict cannot have any duplicate values
            row['TaskName'],
            row['Frequency'],
            row['StartTime'],
            row["TaskDuration"],
            row['MinNumPeopleNeeded'],
            None, #row['Importance'] idk if will acutally wind up using this
            None, #task cost, calc later during algo bc of strings and dynamic stuff
            None, #will not inlcuding preassigned_to mess it up?
            row['Recommended'],
            None, #row['WillSpawnTodayChosen'] selected by an algorithm
            tier,
            row['GenderSpecific'],
            row['GenderReq'],
            None, #ADD preassigned to csv file, for like checkin / checkout tasks 
            row['OverlapProblemTaskCostOffsetter'],
            row['PrefTime'],
            row['TimePreferred'],
            row['NotBeforeTime'],
            row['NotAfterTime'],
            row['StartTime2'],
            row['StartTime3'],
            row['StartTime4'],
            row['StartTime5'],
            row['StartTime6'],
            row['ScheduledOccurance'],
            row['OccursEveryNDays'],
            row['SpawnSunday'],
            row['SpawnMonday'],
            row['SpawnTuesday'],
            row['SpawnWensday'],
            row['SpawnThursday'],
            row['SpawnFriday'],
            row['SpawnSaturday'],
            row['TaskVariableName2'] #Made a 2nd column in the csv file and TaskVariableName2 bc i think since i made the key TaskVariableName, i cant use that column again when defining var names in the class because it would have duplicate names and values and duplicates aren't allowed in dicitonaries.
            )
            #TODO this will probbably be a problem later
            #duration = row['TaskDuration'].strip() 
            #converted_duration = try_convert_to_int(duration)
            #defaultTasksDictionary[task] = converted_duration
    testOutput("TEST | new func csv task converter", defaultTasksDictionary)
    #defaultTasksDictionary['DH'].describe_verbose()

    #testOutput("TEST | converted duration type", type(converted_duration))
    #testOutput("\n Task durations:\n",defaultTasksDictionary, "\n")
    
defaultTasksListCSVToDictConverter()
#endregion

#region---------------------------- NightChore System #TODO MAKE THIS
#TODO create nightchore list and data structures
nightChores = []
#make seperate csv file for it? That way wont have to do nightchore? if so yes, idk may be better on algo. for now can just put on the main list IG.
#endregion

#region--------------------------- Special Task System #TODO MAKE THIS

#TODO somehow standardize these into time slots - see intial time section and make a function, think about time stand sys.
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
#testOutput("TEST | value daySpecialTasks", daySpecialTasks)

testOutput("TEST | daySpecialTasks type check", daySpecialTasks)
if dateValue == 7 or dateValue == 6: #BIG LEARNING CONCEPT: if dateValue == 7 or 6: This condition does not check if dateValue is either 7 or 6. Instead, it checks if dateValue is 7, or if 6 is true. Since non-zero integers are considered truthy in Python, 6 is always true, making the condition always evaluate to true.
    defaultTasksDictionary.clear() #WHY- because special schedule for these dates and it is easier just to preprogram in
#endregion

#region--------------------------------------- Tasks User Input

task_manager = TaskManager(defaultTasksDictionary) #add specialTasksDict later

#Generate total tasks & special tasks depending on dateValue (date)
#TODO be able to assign addtional tasks to certain people
#TODO be able to say when task is and use multi-duration
#TODO give current tasks loaded for day and let choose from default, so they can see if they need to add more.
#TODO make reccommended algo???????? --------------
#TODO make a way to insert like a list of things you need done for the day more eaisly like a row in a csv or spreadsheet - could maybe come from default tasks, just be like any default taks yo uwant done, and ask if so when(or if predetermined time is acceptable, for special ones))
#daysTasks = additionalTasks + needToDoTasks(could maybe come from default tasks, just be like any default taks yo uwant done, and ask if so when(or if predetermined time is acceptable, for special ones)) + specialTasks + NightChore

#------------------- Tasks Editor and Selector (Special and Default)

selected_default_basic_tasks_dict = {}
selected_default_basic_tasks__var_names_list = []


#-------------Auto-Recommended tasks algorithm
#merge the special, default, and night chore tasks together into once list. Then calcualte and make list that is auto then diplay the auto reccomended
@timer
def default_selected_tasks_recommendation_algorithm(defaultTasksDictionary,dayName,selected_default_basic_tasks__var_names_list,selected_default_basic_tasks_dict):
    #first get the day,  then actual day/time for repeating tasks.
    #TODO - far future - would be good if could pre compile which occcur on what day. That way could just load in, all this looping through cant be good for efficency
    
    attribute_name = 'spawn_'+dayName.lower() #WHY .lower to create name value? It refs dateValue num to corresponding dictionary values which are day names, and the day names are capitalized. However the obj attribute daynames are not, so we lowercase this name.
    for task_name, instance in defaultTasksDictionary.items(): 
        attr_value = getattr(instance,attribute_name)
        #print("TEST| get attr value, type, length",attr_value,type(attr_value),len(attr_value)) #since attr are named by day, and only looking for todays attr. Can copy attr name style and just append todays Name to end and then get the data for it.
        if attr_value.capitalize().strip() == 'Yes': #WHY - .upper() bc comparison value is upper case, and its just incase someones puts a lowercase 'yes' on the csv they wont screw everyhting up. #TODO(later also look for "depends' for scheduled basis tasks such as water flowers)
            selected_default_basic_tasks__var_names_list.append(task_name)
            #print("TEST| selected_default_basic_tasks__var_names_list IN IF",selected_default_basic_tasks__var_names_list)
            selected_default_basic_tasks_dict[task_name]=instance
            #print("TEST| selected_default_basic_tasks_dict IN IF",selected_default_basic_tasks_dict)      
    #TODO SIMPLE, GOOD, IDEA!!! CHECK IF ERROR, in future update may later change from "yes" to True, will be faster too?
     #- 2nd reminder, add in reoccuring scheduled tasks later (like ones that occur every x days ex: Water flowers)

default_selected_tasks_recommendation_algorithm(defaultTasksDictionary,dayName,selected_default_basic_tasks__var_names_list,selected_default_basic_tasks_dict)
#print("TEST| selected_default_basic_tasks__var_names_list POST IF",selected_default_basic_tasks__var_names_list)
#print("TEST| selected_default_basic_tasks_dict POST IF",selected_default_basic_tasks_dict)      

#print("TEST default var names list", defaultTasksVarNamesList)
#TODO copy all tasks that are reccomend or meet criteria into this list????

def default_selcted_tasks_confirmation_and_editor(selected_default_basic_tasks_dict,selected_default_basic_tasks__var_names_list,defaultTasksVarNamesList,defaultTasksDictionary):
    print("\n----------------------------------------------------------------------------\n")
    print("Here are today's selected default basic tasks (auto-recommended by algorithm):")
    print(selected_default_basic_tasks__var_names_list)
    
    #print("\n Printed above: today's selected default basic tasks (auto-recommended).\n")
    decision = input("\nWould you like to edit them? y/n\n(Note: You can add custom tasks later): ")
    if decision.strip() in yesAnswers:
        def print_default_selcted_tasks_editior_commands():
            print("\n[Options for Editing Tasks]") #Thanks to GPT4 for making my command instructions more concise
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
        taskEditorCommandList = ['add', 'remove', 'info', 'display all tasks', 'display selected tasks', 'clear all tasks', 'back','exit', 'commands']
        #TODO maybe later make it be able to edit the selected tasks characteristics, that way can edit it if it is off
        #TODO make it put out list of taks and times they at, even better if go by time. IDK stuff for long term
        
        #Loop to continually prompt the user until they're done editing.
        continueEditing = True
        while continueEditing:
            userCommand = xyz_input_auto_completer(instructionString, taskEditorCommandList).strip().lower()
            match userCommand:
                case 'add' | 'remove' | 'info':
                    print(f"Type a {Fore.YELLOW}{Style.BRIGHT}task{Style.RESET_ALL} to use the {Fore.GREEN}{Style.BRIGHT}{userCommand}{Style.RESET_ALL} command on.\n", end="")
                    userCommandModedPrompt = f"{userCommand} "
                    while True:
                        if userCommand in ['add', 'info']:
                            while True:
                                userTaskSelected = xyz_input_auto_completer(userCommandModedPrompt, defaultTasksVarNamesList)
                                if userTaskSelected in defaultTasksVarNamesList: break
                            if userTaskSelected == 'back': break
                            #userTaskSelected = userTaskSelected.upper() #CHECK IF ERROR, just incase it wasnt in caps already. Task names in master dict and lists are in Caps so trying to keep it consistent
                            #TODO idk maybe just make it loop if invalid input.
                            #TODO maybe hould make if reject if doesnt enter a valid task name from the dict, / check to see if it is in it
                            #TODO add nightchore and special to this eventually actually, well maybe ill just integrate them in
                            if userCommand == 'add':
                                selected_default_basic_tasks__var_names_list.append(userTaskSelected)
                                selected_default_basic_tasks_dict.update({userTaskSelected: defaultTasksDictionary[userTaskSelected]})
                                print("Updated selected tasks list: ", selected_default_basic_tasks__var_names_list, selected_default_basic_tasks_dict)
                            else:  # 'info'
                                task_manager.task_info(userTaskSelected)
                        
                        elif userCommand == 'remove':
                            print("Tasks: ", selected_default_basic_tasks__var_names_list)
                            while True:
                                userTaskSelected = xyz_input_auto_completer(userCommandModedPrompt, selected_default_basic_tasks__var_names_list)
                                if userTaskSelected in defaultTasksVarNamesList: break
                            if userTaskSelected == 'back': break
                            selected_default_basic_tasks__var_names_list.remove(userTaskSelected)
                            selected_default_basic_tasks_dict.pop(userTaskSelected, None)  # Use pop with None to avoid KeyError
                            print("Selected tasks remaining: ", selected_default_basic_tasks__var_names_list, selected_default_basic_tasks_dict)

                        print(f"\ntype {Fore.RED}{Style.BRIGHT}'back'{Style.RESET_ALL} to {Fore.RED}{Style.BRIGHT}exit section{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}to continue using {userCommand} [press enter]{Style.RESET_ALL}")
                        userContinueQuestion = input().strip().lower()
                        if userContinueQuestion == 'back':
                            break
                
                case 'display all tasks':
                    task_manager.display_all_tasks()
                
                case 'display selected tasks':
                    print(selected_default_basic_tasks__var_names_list)
                
                case 'clear all tasks':
                    selected_default_basic_tasks__var_names_list.clear()
                    selected_default_basic_tasks_dict.clear()
                    #IDK implement later once figure how will format the selected tasks list

                case 'commands':
                    print_default_selcted_tasks_editior_commands()
                    print("\n\nList of commands:")
                    print(taskEditorCommandList)
                
                case 'exit':
                    continueEditing = False
                    print("Selected basic tasks confirmed.")
                
                case _:  # This acts like an 'else' to handle unexpected commands
                    continueEditing = True
                    #So since the user command at this point can only be 'back' we let the loop iterate back to the beginning.
    else:
        print("Selected basic tasks confirmed.\n\n") 
        
default_selcted_tasks_confirmation_and_editor(selected_default_basic_tasks_dict,selected_default_basic_tasks__var_names_list,defaultTasksVarNamesList,defaultTasksDictionary)

#print("TEST EDITOR OUTPUT: - selected_default_basic_tasks__var_names_list ", selected_default_basic_tasks__var_names_list)
#print("TEST EDITOR OUTPUT - selected_default_basic_tasks_dict", selected_default_basic_tasks_dict,"\n")

#TODO SERIOUS, MAKE  AHELP GUIDE / DICTIONARY DESCRIBING WHAT EACH OF THE ATRRIBUTES REPRESENT. SO THAT WAY USER CAN TYPE HELP AND IT WILL PULL UP THE DEFINITON.
#TODO make transition and explain now filling in data for previously selected tasks that need user Input
# ----------------------- Fill in any missing data for the tasks.
#TODO now that selected, make user input data for certain attributes of tasks that ask for user input, that way have all the nessecay info. Maybe make a need user completion attribute????
def check_for_user_input(obj,taskName):
    for attr in dir(obj):
        # Ignore special attributes and methods
        if not attr.startswith('__') and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            #print("TEST2 what is obj & attr = ", value) #NOTE LEARN MORE: Still confused about what its cycling thru a bit, like i get what dir does, but the print statments make it seem like it goes thru all instances attr and not just the classes once idk
            # Assuming the attributes we care about are strings or lists, you might need to adjust this
            if isinstance(value, str) and "userInput" in value:
                print(f"{taskName} task {attr} needs userInput.\n{Fore.YELLOW}{Style.BRIGHT}If you are confused about what needs input-ing, type 'help' to get more information about the data your're supposed to enter.{Style.RESET_ALL}\nSeperatley if no value is needed, enter None\n")
                while True: 
                    userData = input(f"Input {attr} for {taskName}: ")#.upper() idk why have this here
                    if userData.lower().strip() == 'help':
                        TaskManager.Task.print_help(attr)
                    else: 
                        break
                setattr(obj, attr, userData)
                print(f"TEST | Result for {attr}: ", getattr(obj, attr))
            elif isinstance(value, list):
                autoEnter = False 
                for index, item in enumerate(value):
                    if "userInput" in item: 
                            print(f"\n{taskName} {attr} needs userInput. If done entering or no more values then enter 'exit'\n{Fore.YELLOW}{Style.BRIGHT}If you are confused about what needs input-ing, type 'help' to get more information about the data your're supposed to enter.{Style.RESET_ALL}\n")
                            if autoEnter == True:
                                print(f"Exiting {taskName} {attr} input sequence, filling remaining userInput values for {attr} with 'None'")
                                value[index] = None
                            else:
                                while True: 
                                    userData = input(f"Input {attr} for {taskName}: ")
                                    if userData.lower().strip() == 'help':
                                        TaskManager.Task.print_help(attr)
                                    elif userData == "exit":
                                        autoEnter = True
                                        break
                                    else: 
                                        break
                                value[index] = userData
                                print(f"TEST | Result for {attr}[{index}]: ", value[index])

#NOTE from a UI perspective this part is terribly confusing but will leave it as is bc IDGAF. I dont want ohave to write 250 more lines of code that wont probbaly be used in the final GUI.
for tasks, instance in selected_default_basic_tasks_dict.items():
    check_for_user_input(instance,tasks)
    

# --------------------- Additional Tasks
def user_PromptXY_YesOrNo_If_So_PromptABC_Template(variable,stringprompt):
    pass 
def user_Adds_Additonal_Tasks():
    #UNDER CONSTRUCTION ------------------------------------------------------------------------
    #REALLY GOOD IMPLEMENTATION OF LOOPS AND INs AND APPENDING DICTIONARIES HERE
    #Insert ability to make custom tasks...
    #TODO ADD AFTER DEBUGGING | additionalTasksTF = input("\nAre there any additional tasks you want to add for the day? Y or N? ")
    additionalTasksTF = "N" #TODO remove after debugging
    taskDictLocal = {}
    while additionalTasksTF in yesAnswers:
            print("(SYSTEM LIMITATION) PLEASE NOTE: The all instances of this task will have the same duration and min number of people required. If this is a problem create a seperate task for each instance where the min number of people or the duration changes.\nUnfortunately there is no solution for this yet.")
            input("I understand, (Press Enter)")
            userTaskName = input("Task Name: ") #make var name +1 etc if multiple times or similar name
            #WHY: Prevents duplicate variable names, may get rid of later, restrict what can put in, maybe use classes???
            #TODO MIGHT BREAK WHEN I CHANGE TO DICT
            if userTaskName in taskDictLocal:  #no matter what they put in, ts not the same Varname as anything in list so we are good. IF ERROR CHECK
                taskNameOccuranceCount = 0 
                for tasks in taskDictLocal:
                    if userTaskName in taskDictLocal: 
                        taskNameOccuranceCount += 1
                userTaskVariableName = userTaskName + str(taskNameOccuranceCount) #Adds a number to the name to differentiate from other vars. #LEARNING CONCEPT concatenate an int with a string
            else:
                userTaskVariableName = userTaskName
                
            print("If multiple start times, seperate each with a comma.")
            userStartTime = list(input("Start time(s): ")) #TODO NEED TO STANDARDIZE AND CONVERT START TIMES MAKE FUNCTION SO CAN USE WHEN IMPORT DATA TOO #make it so it standardizes time or give list to choose from
            userDuration = input("Duration: ") #FIX LATER to be blocks or time date, or give options. also mkae smart function to calc distance btwn two numbers to get duration
            userMinManpower = input("Number of People Needed: ")
            userImportance = input("Importance (1-10): ") # Figure out importance scale and how will work
            
            userAssignees = input("Is the task preassigned to someone(s)? y/n: ")
            if userAssignees in yesAnswers:
                print("Seperate each with a comma.\nExample: Terry, Bevis, Butthead, Jacob, ThatAssholeOverThere")
                userAssignees = list(input("To whom: ")) #TODO make it compatible with multiple names, CHECK IF ERROR IN ALGO, maybe need to make it a list by default
            elif userAssignees in noAnswers:
                userAssignees = 0 #TODO may need to change data value type
            
            userGenderSpecific = input("Is the task Gender Specific? y/n: ")
            if userGenderSpecific in yesAnswers:
                userGenderSpecific = input("To which gender: ") #DONE: able to have list to take diff spellings of male or female and standardize the result
                if userGenderSpecific in maleAnswers:
                    userGenderSpecific = "Male"
                elif userGenderSpecific in femaleAnswers:
                    userGenderSpecific = "Female"
            elif userGenderSpecific in noAnswers:
                userGenderSpecific = 0 #TODO may need to change data value type

            userPrefTime = input("Is there a preferred time to schedule this y/n?: ")
            if userPrefTime in yesAnswers:
                userPrefTime = 1
                userTimePreferred = input("What time:")
                userPrefTimeAdditionalParametersTF = input("Do you want to input additional parameters such as, don't schedule before x time, and don't schedule after x time?")
                if userPrefTimeAdditionalParametersTF in yesAnswers:
                    userNot_before_time = input("don't schedule before x time, if none then type NONE")
                    userNot_after_time = input("don't schedule after x time?, if none then type NONE")
            else:
                userPrefTime = 0
                userTimePreferred = 0
                userNot_before_time = None
                userNot_after_time = None
            userFrequency = 0
            for times in userStartTime: #Calc freq from number of start times
                userFrequency += 1
            
            #confused how can I independetly name them???
            # Dictionary to hold task instances
            task_name = userTaskVariableName  # This could be any user-defined string
            taskDictLocal[task_name] = Task( # Create a new Task instance and store it with the user-defined name as the key
                task_variable_name = userTaskVariableName, #DONE need code to prevent creation of multiple tasks with same variable name,
                task_tier = 0, #CHECK IF ERROR, may need to change later, MAYBE make upmost importance??
                task_name = userTaskName,
                task_frequency = userFrequency,
                start_time = userStartTime, #List, so if multiple times can just use one var and iterate through
                duration = userDuration, #TODO make Auto convert if user enters time range etc
                min_num_people_needed = userMinManpower,
                importance = userImportance,
                gender_specific = userGenderSpecific,
                preassigned = userAssignees,
                pref_time = userPrefTime,
                time_preferred = userTimePreferred, 
                not_before_time = userNot_before_time,  #TODO fix some bulltshit later, #CHECK IF ERROR, standard fale input = NONE, WHY = because will use timeslot standardized periods which will include 0
                not_after_time = userNot_after_time,  #CHECK IF ERROR, standard fale input = NONE
                chosen = 1, #set to yes by default, bc user #CHECK IF ERROR, may have to change default data rep
                task_cost = (userFrequency*userDuration)
                )
            """# Accessing a task instance by its user-defined name
            print("Here is a list of the acessible task names: ", list(taskListLocal.keys())) #LEARNING CONCEPT - #In Python, when you call the .keys() method on a dictionary, it doesn't return a list directly. Instead, it returns a dict_keys object. which is a view object that displays a live view of all the keys in the dictionary. When you wrap my_dict.keys() with list(), it converts the dict_keys object into a list, and printing it will result in just the list of keys  
            task_to_access = input("Enter the name of the task you want to access: ") 
            if task_to_access in taskListLocal:
                print(f"Accessing task: {taskListLocal[task_to_access].task_name}")
            else:
                print("Task not found.")"""
            #taskListLocal.append(taskObject)
            #print("TEST | taskListLocal:", taskListLocal)
            additionalTasksTF = input("Are there any additionally tasks you want to add for the day? Y or N?\n\nUser: ")
    if additionalTasksTF in noAnswers:
        print("No extra tasks! YIPPIE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #testOutput("TEST | FINAL taskDictLocal List ", taskDictLocal)
    return (taskDictLocal) 
additionalTasks = user_Adds_Additonal_Tasks() #TODO re add once done debugging
testOutput("TEST |  NEW additionalTasks List ", additionalTasks)
#-----------------------------------------------------------------


# ------------------------------ Master Task List
daysTasks = [additionalTasks, defaultTasksDictionary, nightChores]
#TODO maybe at some point - maybe also make a days tasks dict, that way for algo only have to use that. would allow speeration of night chore and special dict, but speical dict honestly is kidna, well eh never mind idk about performance improvement
#TaskRank1, TaskRank2,TaskRank3 can add other lists into them??

#TODO give total tasks loaded for day, so they can see if they are satisfied. Make and option to delete or add more tasks (ugg more coding).
#TODO for a (special) task day need to know the tasks, then for a task the day, the time the tasks take place+duration, how many ppl on tasks (aka # of certain task).
#TODO Tasks due in timeslot & number of people per task
#TODO IMPORTANCE SYSTEM - Rank tasks in importance, HOW DO I RANK IMPORTANCE???

#endregion
#endregion

#region---------------------------------------------------------- Start of algorithm / assignment sequence 

start_mainAlgo_time = time.time()
#--------------------------------------------------- Check if solution is possible 
#TODO reimplement?????? to check if solution possible???????? DO LATER after i get algorithm completely finished???
#IDEA! - can ask if they want to calc, it will speed up time(time how long it tasks and if shorter than their decision), but if alot of tasks risks not finding a solution until after calc

print("\n--------------------------------------------------------")

#Calc total task for the day and timeslots available to see if enough room.
#might have to change later depending on how structure data
#TODO redo logic on this eventually to take into account weird stuff like overlap, flagup, and 7:00 am no wakeup
#SCRAP THAT IDEA NOTE work around for times when everyone else is asleep is just for that task to randomly select x amount of employees and make them available for that time and then assign them. WAIT NOT NEEDED
#TODO, if everyone it TRUE availbility by default. It will just assign the tasks needed for that period and leave everyone else alone. Can have default None assigned in a thing to show as blank on final output. idk easy to fix

#SOLVING THE OVERLAP PROB can make an computationally exspensive,(well could only do ones that are duration 1+, bc well we would know there is overlap bc the times are same(lets say for ones that have yet computed its the value of all tasks in that period - total num of employees give the amount of instances take up. can use ahead of time for algo. dont want to compute to many thigns ahead.
#hmmmmmmmmm. Or could just calc ahead of tie on certian days knwo will be overlap and account that way. EASIER ))
#min_num_of_people_equal_remaining_times

#FK really need to go over how classes work again and global var overshadowing

#TODO make update so that can do generate in between times a min num of people, also if have some reqs but want remaining stuff like all females idl
#TODO develop this out more when decde what to do with nightchores

class Schedule:
    def __init__(self,timeSlotsStandardizedDictStn,timeSlotsStandardizedDictNtS,dayTimeSlotsKeysList,daysTasks) -> None:
        self.dynamicTimeSlotQueuesDict = {}
    
    def generate_schedule(self): #would having lenght of day be predefined actually give notacible improv???? no 
        schedule.generate_dynamic_time_slot_qeues_for_day(dayTimeSlotsStandardizedStN,dayTimeSlotsStandardizedNtS,dayTimeSlotsKeysList,daysTasks)
        for qeue in self.dynamicTimeSlotQueuesDict:
            testOutput("test main for loop | slot: ", qeue)
            schedule.dynamicTimeSlotQueuesDict[qeue].populate_queue()
            schedule.dynamicTimeSlotQueuesDict[qeue].assign_tasks()    
        #run all the queues until finished

    def generate_dynamic_time_slot_qeues_for_day(self,timeSlotsStandardizedDictStn,timeSlotsStandardizedDictNtS,dayTimeSlotsKeysList,daysTasks):
        #original generation of timeslots and assign to dict, #INITALIZATION OF VALUES
        for time_slot in dayTimeSlotsKeysList:
            #print("TEST (for key) |", key)
            self.dynamicTimeSlotQueuesDict[time_slot] = Schedule.dynamicTimeSlotQueue(timeSlotsStandardizedDictStn,timeSlotsStandardizedDictNtS,dayTimeSlotsKeysList,time_slot)
        #print("\n\nTEST| dynamicTimeSlotQueuesDict[item]",self.dynamicTimeSlotQueuesDict.items())    
        #print("\n\nTEST| 2", self.dynamicTimeSlotQueuesDict["7:00am"])
        #print("\nTEST| dayTimeSlotsStandardizedNtS: ", dayTimeSlotsStandardizedNtS)
    
    def describe_dynamic_time_slot_qeues(self):
        print("\nA list of dynamic time slot qeues and their associated tasks:\n")
        for queue in self.dynamicTimeSlotQueuesDict.keys():
            print(queue)
            self.dynamicTimeSlotQueuesDict[queue].print_tasks() #WHY - LEARNING CONCEPT dont need to put in a print statment as methods prints values, if i did it would print none, as there is nothing being explicity returned so it returns none by default
            print() #serves as a nexline seperator sort of thing.
    
    class dynamicTimeSlotQueue:
        def __init__(self,timeSlotsStandardizedDictStn,timeSlotsStandardizedDictNtS,dayTimeSlotsKeysList,time_slot_name):
            self.queue = []
            self.daysTasks = daysTasks #TODO QUESTION, WILL THIS CAUSE PROBLEMS BC SHADOW GLOBALS VARS???
            self.time_slot = time_slot_name #maybe for later so instead of ref slot can just use this?????????
            
        def print_tasks(self):
            print(self.queue)
            
        @timer
        def populate_queue(self): #maybe change to generate later idk, semantics            
            
            @timer
            def searchStartTimePeriodTasks(daysTasks,searchVal):
                activitesThatMeetCriteria = []
                for dataGrouping in daysTasks:
                    if isinstance(dataGrouping, dict):
                        #print("TEST -2 what datagrouping", dataGrouping)
                        for key, instance in dataGrouping.items():
                            #print("TEST| Instance: ", instance)
                            #print("TEST| instance.start_time_iter += 1: ", instance.start_time_iter)

                            if hasattr(instance, 'start_time') and hasattr(instance, 'start_time_iter'):
                            # Assuming each value has a 'start_time' list and a 'start_time_iter' attribute
                                
                                if instance.start_time and  0 <= instance.start_time_iter < len(instance.start_time): #WUT??? #to account for the fact that there may be multiple start tiems and are comparing to the right startime.
                                    # Compare searchVal with the current start_time value
                                    #print("TEST searchVal", searchVal)
                                    #print("INSTANCE test: start_time", instance.start_time)
                                    if searchVal == instance.start_time[instance.start_time_iter]:
                                        instance.start_time_iter += 1  # Increment the iterator
                                        #print("TEST| instance.start_time_iter += 1: ", instance.start_time_iter)
                                        activitesThatMeetCriteria.append(key)
                                        #print("TEST| activitesThatMeetCriteria.append(key)", activitesThatMeetCriteria)
                                        #print("\n\nTEST internal 0", instance.start_time,"\n\n")
                                    #else:
                                        #print("ERROR | time not in activity, IDK ")
                                #else:
                                    #print("ERROR | len instance.start_time_iter: ", instance.start_time_iter)
                                    #print("ERROR | prob an empty list or startime is out of bounds")
                                    
                            #print("TEST | INTERNAL", dataGrouping.items())
                    #else: 
                        #print("ERROR | datagrouping in daysTaskList not a dict")
                return activitesThatMeetCriteria
            tasks_that_meet_start_time_criteria = searchStartTimePeriodTasks(daysTasks,self.time_slot)
            
            #PROBLEM, what if the duration or num of people is dynamically generated at assignment bc it depends on what other things have been added. in part what tier is for too
            @timer
            def searchQuereDurationPeriodTasks(tasks_meet_prev_criteria):
                tasks_sorted_by_duration = []
                refDurationList = []
                
                #1. get durations from object attrbutes and put into an ordered list
                #for task in tasks_meet_prev_criteria: #is this line nessecary?
                for task in tasks_meet_prev_criteria:
                    refDurationList.append(defaultTasksDictionary[task].duration)
                    #print("TEST For | TASK = ", task)
                #IDK about usinga selection sort, but this is an easy way for me to do this
                
                #2. selection sort the durations list (reverse to do max instead of min)
                #refDurationListLength = len(refDurationList) #need lenght for selection sort algo
                selectionSort(refDurationList,len(refDurationList), setting = 'descending') #WHY (setting=ascending)? - because we want the tasks with the largest durations to be first
                #print("test refDurationList", refDurationList)
                
                    #TODO maybe make selection sort work with funcitons so don't have to do this recombine thing???
                    #idk if this is faster, tho prob in long hall rather than having to do loops
                
                #3. Then loop through the tasks list plus get the duration attribute value for each task, then compare using an if statment that
                # if first duratin value in the sorted duration list is equal to that objects duration value. 
                
                for index, taskName in enumerate(tasks_meet_prev_criteria):
                    #print("TEST index val", index)
                    #print("TEST IF | Duration:Index", defaultTasksDictionary[taskName].duration, refDurationList[index])
                    if defaultTasksDictionary[taskName].duration == refDurationList[index]:
                        #4. If so then add to the tasks sorted by duration list, then move on and search for the object that equals the 2nd value
                        # in the sorted durations list and so on until all tasks have been added in the order of their values Min to 
                        # max(aka the order of the tasks duration list).
                        tasks_sorted_by_duration.append(taskName)
                        #print("TEST IN FOR LOOP tasks_sorted_by_duration", tasks_sorted_by_duration)
                #5. then return the tasks_sorted_by_duration list for use by the next function / to be assigned to the variable
                return tasks_sorted_by_duration
            tasks_stage2_now_sorted_by_duration = searchQuereDurationPeriodTasks(tasks_that_meet_start_time_criteria)
            #print("DONE searchQuereDurationPeriodTasks -------------------")
            #print("TEST | tasks_stage2_now_sorted_by_duration", tasks_stage2_now_sorted_by_duration)

            #Sort by tier last, bc some large tasks may have to be scheduled last but by dur they wouldn't
            @timer
            def sortTierPeriodTasks(prev_sorted_tasks_local):
                tasks_sorted_by_tier = []
                tierRefList = []
                
                for prev_sorted_tasks in prev_sorted_tasks_local:
                    tierRefList.append(defaultTasksDictionary[prev_sorted_tasks].tier)
                    #TODO eventually, maybe - make error log thing here, should have caught everyone in input tho...... maybe make master error input tofix functin. plus would be useful for http req???
                
                #selection sort the tierRefList list (reverse to do max instead of min)
                tierRefListLength = len(tierRefList) #need lenght for selection sort algo
                selectionSort(tierRefList,tierRefListLength) #LEARNING CONCEPT - MY select sort function doesnt return a value so you can assign it to anything. You give it the list, and since lists are mutable it mdofies it and doesnt need to return anyhting. Sodont do this: tierRefList = selectionSort(tierRefList,tierRefListLength)

                for index, taskName in enumerate(prev_sorted_tasks_local):
                    if defaultTasksDictionary[taskName].tier == tierRefList[index]:
                        tasks_sorted_by_tier.append(taskName)
                return tasks_sorted_by_tier
            tasks_final_sorted = sortTierPeriodTasks(tasks_stage2_now_sorted_by_duration)
            #print("TEST | tasks_final_sorted: ", tasks_final_sorted)
            #print("DONE sortTierPeriodTasks -------------------")
            
            #TODO consider making match-reorder-reassign function for above 2 function, idk if will help with readability tho   
            self.queue = tasks_final_sorted
            #print("TEST | dynamicSlotQueue | tasks for time Period/Slot:" , tasks_final_sorted)
                    
        def assign_tasks(self,employee_info=None):
            avail_employees_in_period = employee_manager.get_available_employees(self.time_slot)
            #maybe make an inverse for checking??????
            #maybe use duplication to get rid of ones that are already deleted
            #pointless if go to class to get attributes??
            #PART 2 - now for part 2 of the algo sequence which is assigning tasks to an employee
            
            def assign_task(task_name):
                #TODO if leave stuff blank have it assume none or "", esp for tasks and stuff
                #TODO evantually redo this and figure out how to implement how many certs you need. Also maybe make a table with prelisted number of people with certs, might be faster       
                
                assigned_people = {}
                def generate_list_of_eligible_employees(): #need to rename this
                    task_reqs = task_manager.tasks[task_name].get_task_requirements() #should be *task employee req
                    #TODO FOR NOW - justs assigns all the min number of people with things that meet reqs, even after reqs have technically been filled
                    if task_reqs: #truthy if contain at least one item, Falsey if empty. If checks if true.
                        employees_with_req_traits = employee_manager.get_employees_with_traits(**task_reqs) #QHY & LEANRING CONCEPT **unpack dictionary into keyword arguments bc function expects them
                    else: #then no employees with special traits needed, can pick any
                        employees_with_req_traits = {}
                    #get_personnel_with_task_critical_traits
                    #get who is available first -- do this first or get qualified people??? hmmm, This first cus have to search multiple for qualis and better to have to search less
                
                    #then do the rest of these if nessecary
                    
                    #Then do normal people, skip if amount from special has been filled alread]
                    return employees_with_req_traits
                    
                def generate_assignment_probabilities(removeLater):
                    assignment_probbability = {} #employee | base prob value | modifiers ??? how implement???
                    #Figure shit out later
                    #should return employee chosen
                    #lower probbs if certs in other things and tasks with those certs are needed in the period
                    return removeLater
                
                def update_data(name, time_slot):
                    #assigned_people[name] = None #TODO fix #POTENTIAL TO  CAUSE BUG hmm is this working right? so doesn't assing same people twice?? #ok if do this first, but then do total unavail. Proab could optimize here
                    #for multi duration tasks - rethink how to efficently implement this later.
                    employee_manager.set_employee_availability(name, time_slot) #IMPORTANT fix this and incorperate multi time assignment relevant_time_slots. #LEARNING CONCEPT - Issue was iteration over characters in value / str,list(self.time_slot) how to prevent#TODO INSPECT THIS, think this has to be a list??? TODO CHECK HTIS LATER, need better type checkers and descs in program
                    employee_manager.assign_task_to_employee(name, task_name, time_slot) #TODO see if can take list like for employee availability, for multi duration args
                    task_manager.tasks[task_name].assign_employee_to_task(time_slot, name) 
                    del avail_employees_in_period[name]
                    if employees_with_req_traits: #bc otherwise will delete an empty dict and cause an error
                        del employees_with_req_traits[name]
                    #print("UPADTE FUNCTION OUTPUT | +1")
                     
                #Put outside update funciton so onyl have to calculate once, and not everytime need to assign task to someone
                def calculate_time_slots_for_duration(task_name):
                    # Get the task object (assuming you have a way to access it via task_name)

                    #thanks chatGPT, bc i was to lazy / tired, its 8:42pm to write this out myself, easier to just describe, well I actually did end up have to make a decent amount of changes
                    
                    duration = int(task_manager.tasks[task_name].duration) # WHY int - Ensure duration is an integer bc dictionary to convert value will onyl take integer
                    
                    if duration > 1:
                    # Check the duration of the task
                        
                        #FORGET FOR NOW - think unessecary WHY - subtract one, subtracting 1 from the task's duration accounts for including the starting time slot as part of the duration. This adjustment helps to ensure the task is scheduled for the correct number of time slots, starting from the initial slot.
                        #duration -= 1
                        
                        # Get the numeric value for the current time slot
                        current_slot_numeric = dayTimeSlotsStandardizedStN[self.time_slot]

                        # Calculate numeric values for the duration of the task
                        duration_slots_numeric = [current_slot_numeric + i for i in range(duration)] #good list comprehension

                        # Convert numeric values back to string representations
                        duration_slots_strings = [dayTimeSlotsStandardizedNtS[num] for num in duration_slots_numeric if num in dayTimeSlotsStandardizedNtS]

                        return duration_slots_strings
                    else:
                        # If duration is 1, return the current time slot in a list
                        return [self.time_slot]
                time_slot = calculate_time_slots_for_duration(task_name)
                    
                def assign_employees_to_task(employees_with_req_traits_local, task_name, time_slot):
                    #TODO write logic for TASKS THAT ARE DEPENDENT ON NUMBER OF EMPLOYEES BASED ON OTHER TASKS
                    #TODO once get code for how many certs to assign, then make it count until it has fulfilled it.
                    
                    #first assign special trait employees first
                    employees_with_req_traits = employees_with_req_traits_local
                    
                    def choose1():
                        chosen_name_local = random.choice(list(employees_with_req_traits.keys())) #idk if the .keys is most efficent but, is it redundant IDK
                        return chosen_name_local
                    
                    #also interesting employees_with_req_traits = set(employees_with_req_traits_local.keys()) & set(avail_employees_in_period.keys()) - set(assigned_people.keys())

                    if employees_with_req_traits:
                        
                        #check if already assigned or unavailable
                        while True:
                            chosen_name = choose1()  #find someone who isn't been assigned or unavailable
                            if chosen_name not in assigned_people and chosen_name not in avail_employees_in_period: #use all??
                                break #Break the loop if a suitable / available employee is found, #TODO implent find someone with right reqs???
                        update_data(chosen_name, time_slot)
                        
                    else:
                        attribute = getattr(task_manager.tasks[task_name], 'min_num_people_needed') #IMPORTANT, #COULD SET THIS TO STAND VAR, THEN HAVE FUNCTION NEAR IMPORTS THAT GETS A LIST OF CODE WORDS AND CONVERTS THEM TO STAND VALUE
                        #WHY - convert if input string / csv data is anything but a number tha can convert to int.
                        if attribute == "unassigned_employees":
                           attribute = len(avail_employees_in_period)
                        ppl_needed = int(attribute) # need to check if an if or not
                        while ppl_needed > 0: #faster maybe? # WHY: not For loop bc cannot iterate over integers
                            while True:
                                chosen_name = random.choice(list(avail_employees_in_period.keys())) #IMPLEMENT prob #would be faster to have seperate list once, and del values in it to instead of remaking it each time.
                                if chosen_name not in assigned_people:
                                    break
                            update_data(chosen_name, time_slot)
                            ppl_needed -= 1
                               
                        #HMM this is also an interesting implementation: available_candidates = set(avail_employees_in_period.keys()) - set(assigned_people.keys())
                        #check if already assigned or unavailable
                        #update with anti-cert-use-up code later
                        #normal random assignment
                    #then do the normal
                    #check if in avail employees for period, would slow down if didnt have to but dict means fast look up.
                    #temp prinout to see if assigning to tasks:
                    #print(f"{task_name} is assigned to: {assigned_people}.") #still not working???
                employees_with_req_traits = generate_list_of_eligible_employees()
                assign_employees_to_task(employees_with_req_traits, task_name, time_slot)
                
            for task in self.queue:
                assign_task(task)

#need to then reorder selected tasks by TIER and duration, how to make sure stuff does not get overwritten twice???????
#Then go to next criteria or assign to people and set durations. once done set all other durations to blank???? idk
#recursive function to look through all the lists and shit in the daysTasks and find those that start at time, next duration, then do by tiers            
        
schedule = Schedule(dayTimeSlotsStandardizedStN,dayTimeSlotsStandardizedNtS,dayTimeSlotsKeysList,daysTasks)
schedule.generate_schedule()
schedule.describe_dynamic_time_slot_qeues()

end_mainAlgo_time = time.time()
elapsed_mainAlgo_time = round(end_mainAlgo_time - start_mainAlgo_time, 5)
print("Elapsed time for main algorithim:", elapsed_mainAlgo_time, "Seconds")

#endregion

#region -------------------------------- Schedule Output
# ------------------ output stuff
class OutputSchedule():
    
    #TODO FIGURE OUT LATER
    
    output_settings_var = {}
    excel_formatting_settings = {}

    def update_settings(self, new_settings):
        # Modifying the class variable
        OutputSchedule.output_settings_var = new_settings
        # Or equivalently, but less commonly used
        # self.__class__.output_settings_var = new_setting
        
    def __init__(self, day_time_slots_list, employee_list, employee_instances) -> None: #employee_list may be unessecarybut want to make sure in order same time, everytime.
        self.day_time_slots_list = day_time_slots_list
        self.length_time_slots = len(self.day_time_slots_list)
        self.employee_list = employee_list
        self.length_employee_list = len(employee_list)
        self.employee_instance = employee_instances
    
    def csv():
        pass
    
        assigned = {"7:00am": "KSWAT1", "7:45am": "KSWAT1", "9:15am": "KSWAT1", "9:50am": "KSWAT1", "10:00am": "HALFSTAFF", "11:00am": None, "11:45am": "Something", '1:45pm': 'Something'}
        task_durs = {"KSWAT1": 4, "HALFSTAFF": 1, "Something": 2}
        employee_list = ["Huey", "Granddad", "Wuncler"]
    
    @timer
    def excel(self):
        import xlsxwriter
        
        #TODO MEDIUM - PRIORITY !! make system which able to input week, or starting week and will put what week it is, also let it choose between week or formal date         
        #TODO HARD - FOR FUTURE make formate setting system # FOURTH PRIORITY, for now just code into csv value - could do a bunch of pre made styles and have choose from them - hmm, but include a system that allows to make new styles easily
        #TODO MEDIUM HARD - figure out how to do up down stuff and diff style things SECOND PRIORITY
        #TODO make a standard font size and style for all tasks, make auto size and fit #THIRD PRIORITY
        #TODO make times_slot cubes a lil bigger, find out hwo sheets print and let that determine
        #TODO make quote autosize and fit
        #TODO make standard color fill for the borders and stuff
        #TODO MEDIUM - HARD (2-3horus) figure out prinitng paramteres and let it adjust box size based on that FIRST PRORITY
        #TODO make quote of the day prompt before all of this, and be able to turn on or off etc - make larger part of settings
        
        #NOTE REMEMBER to print it has to be assigned to each period and have the proper duration, will help with #Debuging
       
        #formatted_date_Month_Day = str(datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A, %m:%s")) #TODO LEARNING CONCEPT memorize reg-ex and the date-time exspressions
        formatted_date_month_day_weekday = datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A") #WHY - Str(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
        file_title = f"SWAT Schedule {formatted_date_month_day_weekday}.xlsx" #%b - abrv month, %d -num date in month, %a - weekday abr name (depedns on region)
        title = 'SCHEDULE'
        quote_of_day = "Quote of the day"
        
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(file_title)
        worksheet = workbook.add_worksheet(f"SWAT Schedule {formatted_date_month_day_weekday}")
        
        # Define formats
        schedule_axis_fill_color ='#404040'
        schedule_axis_label_color ='#FFFFFF'
        tasks_and_employee_cell_height = ''
        #task_default_font_color ='#333333'
        
        date_label_format = workbook.add_format({ #CASE text is set to capital by .upper() at the write function
            'bold': True, 
            'align': 'left',
            'valign': 'vcenter',
            #'fg_color': '#FFD3D3D3',
            'font_size': 10,
            'border': 1
        })
        #colors are specified using a Html style #RRGGBB value.
        title_format = workbook.add_format({ #TODO UPDATE
            'bold': True, 
            'align': 'center',
            'valign': 'vcenter',
            'font_color': schedule_axis_label_color,
            'fg_color': schedule_axis_fill_color,
            'font_size': 30,
            #'border': 1
        })
        time_slot_format = workbook.add_format({
            'bold': True, 
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D3D3D3',
            'font_size': 12,
            'border': 1
        })
        employee_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': schedule_axis_fill_color,
            'font_color': schedule_axis_label_color
            #TODO make it shrink the text to auto fit
        })
        corner_gap_fill_format = workbook.add_format({
            'fg_color': schedule_axis_fill_color
        })
        quote_format = workbook.add_format({ #TODO UPDATE??
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': schedule_axis_fill_color,  # Background color
            'font_color': schedule_axis_label_color,  # Font color
            'font_size': 30,
            'bold': True,
            #'border': 1
        })
        #make a .CSV and autoconver values, also find work around for KSWAT and such.
        
        task_format = {
        'SERVE': workbook.add_format({
            'bg_color': '#FFFFCC'
        }),
        'HALF STAFF': workbook.add_format({
            'bg_color': '#C6EFCE'
        }),
        'SEE R00SKI': workbook.add_format({
            'bg_color': '#FFD9B3'
        }),
        'SEE JESUS': workbook.add_format({
            'bg_color': '#FFF2CC'
        }),
        'MAIL': workbook.add_format({
            'bg_color': '#DDEBF7'
        }),
        'DISH': workbook.add_format({
            'bg_color': '#FFEB9C'
        }),
        'PLAYTIME': workbook.add_format({
            'bg_color': '#B6D7A8'
        }),
        'SEE SLIPS': workbook.add_format({
            'bg_color': '#D9D9D9'
        }),
        'BALLOONS': workbook.add_format({
            'bg_color': '#EAD1DC'
        }),
        'PHONES': workbook.add_format({
            'bg_color': '#DBDBDB'
        }),
        'CAMP STORE': workbook.add_format({
            'bg_color': '#C9DAF8'
        }),
        'PIZZA': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'DH': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'WATER RUN': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'BALLOONS': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'FLAG UP': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'SEE EAGLE': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'FLAG UP': workbook.add_format({
            'bg_color': '#F4CCCC'
        }),
        'KSWAT1' : workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#FFB6C1',
            'font_color': '#333333',
            'border': 1
        }),
        'KSWAT2' : workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#FFB6C1',
        'font_color': '#333333',
        'border': 1
        }),
        'KSWAT3' : workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#FFB6C1',
        'font_color': '#333333',
        'border': 1
        })
        }

        #Write Date Label - Always in the top left corner
        worksheet.write(0, 0, formatted_date_month_day_weekday.upper(), date_label_format)
        
        # Column and Row indexes ----------------
        #NOTE - REMEMBER: Excel Rows/Columns are Zero based
        column_index = 1 #first column beyond the employee label column, aka the first column to put stuff into
        row_index = 4 #first row beyond the time slots label

        #Fill in corner gap between employees and title & time
        worksheet.write(1, 0, None, corner_gap_fill_format,)
        worksheet.write(2, 0, None, corner_gap_fill_format,)
        worksheet.write(3, 0, None, corner_gap_fill_format,)
    
        # Write time headers
        time_slot_column_index = column_index
        for time_slot in self.day_time_slots_list:
            worksheet.write(row_index-1, time_slot_column_index, time_slot, time_slot_format)
            worksheet.set_column(time_slot_column_index-1, 70) #NOTE #TODO adjs height, find way to make consistent for all cells, read docs
            time_slot_column_index += 1
        
        # Write employee names
        emp_row_index = row_index
        for employee in self.employee_list:
            worksheet.write(emp_row_index, 0, employee, employee_format)
            emp_row_index += 1
        
        # Fill in the data
        row = row_index
        for employee in self.employee_list:
            column = 1
            multi_period_task_name_counter = 0
            for time_slot, task in employee_manager.employees[employee].assigned_to.items(): #NOTE if error check here, lol that rhymes. maybe give these props to output class, make simpler??[] 
                if task:
                    duration = int(task_manager.tasks[task].duration) #why int = attr is assigned from csv sheet so need to convert it from string to int. #LEARNING use get get attr?? learn more. need to update my learning google doc. 
                    #TODO error gaurding - WHAT if task doesn't have a duration, how should i guard against this error, what would ouput look like?
                    
                    # If task spans multiple columns
                    if duration > 1:
                        multi_period_task_name_counter += 1
                        if multi_period_task_name_counter == duration:
                            start_col = column - (duration-1) #minus one bc duration count is inclusive, we have to account for timeslot we are in as part of it
                            worksheet.merge_range(row, start_col, row, column, task, task_format[task])
                            multi_period_task_name_counter = 0
                        column += 1
                    else:
                        worksheet.write(row, column, task, task_format[task])
                        column += 1
                else:
                    worksheet.write(row, column, task)
                    column += 1  # Skip if no task
            row += 1
        
        #Write Title    #merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
        worksheet.merge_range(row_index-3, column_index,row_index-2,self.length_time_slots, title)
        worksheet.write(row_index-3, column_index, title, title_format)
        
        #Write Quote
        # Calculate the row to insert the quote based on the number of employees
        quote_row = self.length_employee_list + row_index # WHY +row_index, row_index = the amount of gaps / rows between the first employee and top of the page. #Accounts for the rows that the date label, title, and timeslots take up so that the quote can be correctly positioned at the bottom of the page
        worksheet.merge_range(quote_row, 0, quote_row, self.length_time_slots, quote_of_day)
        # Apply the format to the merged cells with the quote
        worksheet.write(quote_row, 0, quote_of_day, quote_format)
        workbook.close()
            
    def console():
        pass
    
output_schedule = OutputSchedule(dayTimeSlotsKeysList,employeeNamesList,employee_manager.employees)
output_schedule.excel()
#endregion

end_program_time = time.time()
elapsed_time1 = round(end_program_time - start_program_time, 2)
print("Elapsed time for program:", elapsed_time1, "sec")

#GUI - API - SERVER STUFF
'''
def run_cli():
    pass
#command line interface

if __name__ == "__main__":
    run_cli()
#app_backend.py

from flask import Flask, jsonify,request
app = Flask(__name__)

#@app.route
#HTTP endpoint logic

#star server
if __name__ == "__main__":
    app.run(debug=True, port='0.0.0.0', port=5000)

"""POST = send new data
GET = retreive
PUT or PATCH to update existing data
DELETE to remove data"""


myDict = {}
x = len(myDict)
if x > 7:
    print("okay")
else:
    print("small")
'''
