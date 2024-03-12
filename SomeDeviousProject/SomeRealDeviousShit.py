#LEARNING - If broken check to make sure dont have something twice, like an input or variable if it is broken via search / find like Issac did
#TODO maybe make variables to repersent file pathways then use in all the funcitons that way only have to change once

"""FOR later
https://docs.python.org/3/py-modindex.html
https://wiki.python.org/moin/GuiProgramming
https://www.pythonguis.com/faq/which-python-gui-library/
https://www.bairesdev.com/blog/best-python-gui-libraries/

GUI toolkits:
https://flet.dev - fast, but not best way to learn as not well maintiable in the long run
https://www.youtube.com/watch?v=JJCjAUmNXBs


https://www.pysimplegui.com : Hobbyist subscriptions are NO COST
Commercial subscriptions start at $99/year

PySide & Qt
While PySide may be used in non-GPL applications without any additional fee.
However, note that both these libraries are separate from Qt itself which also has a free-to-use, open source version and a paid, commercial version.

Remi for webGUIs, but security and use drawbacks

https://flask.palletsprojects.com/en/3.0.x/
https://flutter.dev - Free for commerical use, BRUH HAVE TO LEARN ANOTHER LANGUAGE (Dart language)
https://github.com/maxim-saplin/flutter_python_starter


https://docs.flutter.dev/get-started/install/macos/desktop

After I make base code fully functional
DEF GONNA USE FLUTTER,
or if things get hard flask

PQT5?

"""
import time
start_program_time = time.time()

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
    input() #DELAYS PROGRAM SO CAN SEE START SCREEN
printIntroSequence()

#from collections import namedtuple
import csv
#import XlsxWriter
#import pandas
#from colorama import Fore, Style
from rich import print
from copy import deepcopy



#BASIC SAVED INFO ------------------------------------------------------------------------------------------------------  



#DefaultInfo
#Define names of employees
#Time Slots
#Lists of tasks
#Potentially swattie prefferences and count how many times do it to make equal balance


#REDO LATER------------------------------------
defaultInfo = {} #DICTIONARIES A dictionary is a collection which is ordered (in pyhton 3.7+), changeable and does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:
#print("\n CSV file results ----------------------------- \n")
"""#IS it even nessecary anymore??
with open('SWATBasicSavedInfoForScheduler.csv', newline='') as csvfile:

    # Create a csv.reader object
    csvreader = csv.reader(csvfile, dialect='excel')
    
    # Extract the first row to use as dictionary keys
    headers = next(csvreader)
    
    # Initialize a list for each header in columns
    for header in headers:
        defaultInfo[header] = []
    
    # Iterate over the rest of the rows and fill the dictionary lists
    for row in csvreader:
        for header, value in zip(headers, row):
            defaultInfo[header].append(value)
#print("test to print dicitionary"), print(defaultInfo)
"""

#LEARNING CONCEPT
    # add an extra backslash "\" to allow multi line wrap around for print, CANNOT HAVE TRAILING SPACES
    # use input to stop program 

def testPrintDefaultInfoDictionary():
    print("Test of key:value pair entries - in defaultInfo Dictionary \n")
    print("Employees: ")
    print(defaultInfo["\ufeffEmployee"])
    print()

    print("TimeSlots: ")
    print(defaultInfo["TimeSlots"])
    print()

    print("BasicTasks: ")
    print(defaultInfo["BasicTasks"])
    print()

    print("TaskDuration: ")
    print(defaultInfo["TaskDuration"])
    print()

    print("NightChore: ")
    print(defaultInfo["NightChore"])
    print()

    #https://www.geeksforgeeks.org/python-classes-and-objects/
    #https://www.w3schools.com/python/python_dictionaries_access.asp
#testPrintDefaultInfoDictionary()

#Additional Inputs? -----------------------------------------------------------------------------------------------  
dumbAndrewMemes1 = "It's like I dont care about nothing man...\n\
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
swatJokes = []

days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'mon': 1,
        'tues': 2, 'tue': 2, 'wed': 3, 'thurs': 4, 'thur': 4, 'fri': 5, 'sat': 6, 'sun': 7, 'm': 1, 'w': 3, 'f': 5,
        's': 6, 'su': 7}
daysKeyValueInverse = {1: "Monday", 2: "Tuesday", 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                       7: 'Sunday'}
def getUserEnteredDate():
    #Get date and stores it, will eventually use to see if need to schedule fixed event adn which ones (dance, bondfire, etc)
    wLoopBVar = 1
    while wLoopBVar < 6:
        if wLoopBVar == 5:
            print("\n----------------------------------------FINAL ERROR------------------------------------------------------")
            print("\nTROUBLESHOOT: Just go ask Andrew for help at this point. OR RESTART PROGRAM")
            print("For real man, you must be high as balls if you're struggling to type in a day of the week. Speaking about being high, that reminds me of this song I heard once.....")
            print("")
            print(dumbAndrewMemes1)
            wLoopBVar = 8
            #print("IF ONE: ",wLoopBVar)
            print("\n\nPROGRAM TERMINATING, its all your fault. Don't you have any sense of shame?")
            exit()
        dateUserEntered = "m"
        dateUserEntered = input("\nGenerate a schedule for which day of the week: ")
        if dateUserEntered.lower() in days: # "==" didn't work so used "in" recommended by stack overflow
            #dateUserEnteredInterpreted:
            print(f"Will generate a schedule for {daysKeyValueInverse[days[dateUserEntered.lower()]]}.\n")
            #print("IF TWO: ",wLoopBVar)
            wLoopBVar = 8
            #print("IF for user entered, AFTER ADD: ",wLoopBVar)
            break
        else:
            print("\n-----------------------------------------------------------------------------------------------\nERROR!\n\nMispellling or not a valid day, try again.\n-----------------------------------------------------------------------------------------------\n")
            #print("getUserEnteredDate ForLoop If (dateUserEntered input) ELSE check TEST")
            #print("ERROR Else: ",wLoopBVar)
        wLoopBVar = wLoopBVar + 1
    #print ("wLoopBVar out of loop ",wLoopBVar)
    #check which day to format schedule like sat or sunday and to for account for special events
    dateValue = days[dateUserEntered.lower()]
    return dateValue
dateValue = getUserEnteredDate()
print("TEST dateValue", dateValue)

  
# Internal Mechanisms [Data Collectoin, Preperation and Formatting]-----------------------------------------------------------------------------------------------------------



#VARS, LISTS, DICTIONARIES
#Porb will use the lists with many functions, so I put them at the top
yesAnswers = ["Y","Yes","yes","y","YES","ye","Ye","YE"]
noAnswers = ["N","No","no","n",'NO']
maleAnswers = ["Male","male","men","Men","boys","Boys","Man","man","Boy","boy","Males","males"]
femaleAnswers = ["Female", "female", "Women","women","woman","Woman","Females", "females","Girl","girl","Girls","girls"]
#timesSlotAnswers = []
#defaultTaskAnswers = []

def intialCSVToDataStructures():

    def try_convert_to_int(value):
        try:
            return int(value)
        except ValueError:
            return 0 #IF ERROR, check this, maybe set to None.

    #Assign default task info to default task dictionary
    #Assign task duration to default tasks via dictionary
    defaultTasksList = []
    defaultTasksDictionary = {}
    defaultTaskDurationsDict = {}
    with open('SWATBasicTasksListForScheduler.csv', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        #for row in csvreader:

            #defaultTasksDictionary[task] = y
        for row in csvreader:
            # Use the 'BasicTasks' column as keys and 'TaskDuration' column as values
            task = row['TaskName']
            duration = row['TaskDuration'].strip() #LEARNING CONCEPT: strip(), Return a copy of the string with leading and trailing whitespace removed.
            converted_duration = try_convert_to_int(duration)
            defaultTaskDurationsDict[task] = converted_duration

            #print("TEST | converted duration type", type(converted_duration))
        """
        newTaskDict = {'TaskName': userTask,
                       'StartTime': userStartTime,
                       'Duration': userDuration, #TODO make Auto convert if user enters time range etc
                       'NumPeopleNeeded': userManpower,
                       'Importance': userImportance,
                       'GenderSpecific': userGenderSpecific,
                       'Preassigned': userAssignees,
                       #TODO add other stuff like cert needed and type of cert needed, employee type too
                       }
        """

    #print("\n Task durations:\n",defaultTaskDurationsDict,"\n")

    #take names and put into list
    employeeNamesList = []
    with open('SWATBasicSavedInfoForScheduler.csv', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            # Use the names in the '\ufeffEmployee' column as values
            name = row['\ufeffEmployee']
            employeeNamesList.append(name) #add names to list
    #print("TEST employeeNamesList:", employeeNamesList)

    #take gender and put into lsit
    employeeGenderList = []
    with open('SWATBasicSavedInfoForScheduler.csv', newline='') as csvfile:
        # Create a csv.reader object
        csvreader = csv.DictReader(csvfile, dialect='excel')
        for row in csvreader:
            # Use the names in the '\ufeffEmployee' column as values
            gender = row['Gender']
            employeeGenderList.append(gender) #add names to list
    #print("TEST employeeGenderList:", employeeGenderList)
    return defaultTaskDurationsDict, employeeNamesList, employeeGenderList
defaultTaskDurationsDict, employeeNamesList, employeeGenderList = intialCSVToDataStructures()

print("TEST new intial csv load function resulting vars: ", defaultTaskDurationsDict,employeeNamesList,employeeGenderList)





# Selection sort
# time complexity O(n*n)
# sorting by finding min_index
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

#TODO move activites/tasks further down, can merge all together later.
#MAKE SPECIAL TASKS LATER ---- Get full schedule
##Special task duration and time????
#special tasks indv

normalDayTimeSlots = [{'7:00': True, '7:45': True, '9:15': True, '9:50': True, '10:00': True, '11:00': True, '11:45': True, '1:45': True, '2:45': True, '3:45': True, '4:45': True, '5:20': True, '6:30': True, '7ish': 'NG', '8ish': 'Sweeting', '9ish': 'NightChore'}] #what do when have too special events at the same time??? such as NG and Playtime
wenSpecialTimeslots = ['7:00', '7:45', '9:15', '9:50', '10:00', '11:00', '11:45', '1:45', '2:45', '3:45', '4:45', '5:20', 'TIME DOES NOT EXIST', 'TIME DOES NOT EXIST',  'TIME DOES NOT EXIST', '9is MAYBE'] #can merge TIME DOES NOT EXIST and fromatting later, this is mainly all just formatted so the ;ogram can interpret it, will format for export seperatley
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


#Set preferences so that it is a list for all the acitivties that they prefer
#TODO import and use savedInfo alt thingy, maybe rename it too.


print("\n---------------------------------------------------------------------------------------------------------------\n") 




# Employees ---------------------------------------------------------------------------------------------------




#pretty much takes all the data we have been formatting, collecting, or importing and rearrangng it and applying it to the availableEmployees list that has all their details. So algo can use later
def employeeAdjustmentSection():

    #LESSON LEARNED I made it expect a keword argument with **, but didn't give it one. Argument needed to be all lowercase?
    """
    FOR LATER WHEN I WILL REQRITE THE CLUSTERFUCK ABOVE:
    Dictionary Comprehensions from Lists:,
    Create a dictionary with indexes as keys and list elements as values
    hobby_dict = {i: hobby for i, hobby in enumerate(person["hobbies"])}
    """

    #I AM SO SICK OF THE WORD UNAVAILABILITES, AND PRETTY SOON EMPLOYEE, VALUE, AND VARIABLE TOO.

    noUnavailabilites = True  # Default state used for if funciton
    unavailableEmployees = {}
    # TODO still gives error and say confirmed no unaviailbilties when there are, infact, unavailibilties
    # TODO have input for names capitalized so can work, maybe can also have check list to see if that is a valid entry. WOULD IMMENSELY COMPLICATE THO
    # TODO Maybe try to rewrtie this more efficent sometime, maybe even using functions, be inspired by additional task assignment group.
    # People Available for day (Check for exceptions), *also find out partial avialibilites*, prompted earlier to see who is out, Ask if anyone is out.
    def employeeAvailabilityInput(noUnavailabilites):
        avialLoopX = True
        firstLoopIteration = True
        while avialLoopX == True:
            if firstLoopIteration == True:
                unavailableEmployeeName = input("\nIs anyone unavailable today, or partially? \n \nY or N? \n \nUser: ")
                if unavailableEmployeeName in noAnswers:
                    #print(unavailableEmployees)
                    print("\nConfirmed: no unavailabilites.\n")
                    avialLoopX = False
                else:
                    #TODO PROB COULD BE MADE INTO A REUSABLE FUNCTION
                    unavailableEmployeeName = input("\nWho is unavailable?\n\nUser: ")
                    #print("BEFORE CAPITAL",unavailableEmployeeName)
                    unavailableEmployeeName.capitalize() # LEARNED LESSION Strings in Python are immutable, so methods like capitalize() dont modify, just creat a new string
                    #print("AFTER CAPITAL", unavailableEmployeeName)
                    tempTime = input("\nWhen are they unavailable?\n\nUser: ") #TODO Y/N SHOULD AKS IF ALL DAY FIRST, maybe make enter between two dates
                    unavailableEmployees.update({unavailableEmployeeName:[tempTime]}) #UPGRADE: use enumerate and append #dict. ??????

                    print("1 unavailableEmployees dict", unavailableEmployees)

                    #loop so can insert as many time slots as needed.
                    multipleUnavailbilites = input("\n\nIs that the only time, or are they unavailable at other times, Y or N? \n \nUser: ") #LOOP THIS unitl Y/N
                    #print("TEST lol:",lol)
                    if multipleUnavailbilites in yesAnswers:
                        needMore = True
                        while needMore == True:
                            newTime = input("\nWhen are they unavailable?\n\nUser: ")
                            unavailableEmployees[unavailableEmployeeName].append(newTime)
                            multipleUnavailbilites2 = input("\n\nIs that the only time, or do you need to enter more, Y or N? \n \nUser: ")
                            if multipleUnavailbilites2 in noAnswers:
                                needMore == False #TODO REEXAMINE needMore=False changed from == to = and i think might be effecting code and make it loop one mroe time.
                                break
                            print("2 unavailableEmployees dict", unavailableEmployees)
                    else:
                        needMore = False
                        print("TEST Else thingy past lol")
                        print("\nConfirmed:",unavailableEmployeeName,"is unavailable.\n")
                        print("3 unavailableEmployees dict", unavailableEmployees)
                        firstLoopIteration = False
                        noUnavailabilites = False
            else:
                #print(" -1 TEST noUnavailabilites var: ", noUnavailabilites)
                print("\nAnyone else?\n\nY or N?\n")
                anyoneElse = input("\nUser: ")
                if anyoneElse in noAnswers:
                    print("\nConfirmed: no one else is unavailable.\n")
                    avialLoopX = False
                else:
                    unavailableEmployeeName = input("\nWho?\n\nUser: ")
                    unavailableEmployeeName.capitalize() #maybe change var later????
                    #ref dict and #find out time when unavailable later *********************
                    print("\nConfirmed:",unavailableEmployeeName,"is unavailable.\n")
                    tempTime = input("\nWhen are they unavailable?\n\nUser: ") #TODO Y/N SHOULD AKS IF ALL DAY FIRST, maybe make enter between two dates
                    unavailableEmployees.update({unavailableEmployeeName:[tempTime]}) #USE enumerate and append #dict. ??????
                    print("1 unavailableEmployees dict", unavailableEmployees)
                    #loop so can insert as many time slots as needed.
                    lol = input("\n\nIs that the only time, or are they unavailable at other times, Y or N? \n \nUser: ") #LOOP THIS unitl Y/N
                    print("TEST lol:",lol)
                    if lol in yesAnswers:
                        needMore = True
                        while needMore == True:
                            newTime = input("\nWhen are they unavailable?\n\nUser: ")
                            unavailableEmployees[unavailableEmployeeName].append(newTime)
                            oof = input("\n\nIs that the only time, or do you need to enter more, Y or N? \n \nUser: ")
                            if oof in noAnswers:
                                needMore = False
                                break
                            print("2 unavailableEmployees dict", unavailableEmployees)

        return noUnavailabilites #still dont understand function arguments verywell
    noUnavailabilites = employeeAvailabilityInput(noUnavailabilites) #calls function, duh
    #print("TEST noUnavailabilites var: ", noUnavailabilites)


    #check if unavialable employees, if not then ignore the following
    if noUnavailabilites == False: #CHECKING IF UNAVAILABILITES CORRECT
        #then have it go over and confirm everyone who is out by printing it
        #ask if mistake and want to repeat
        print("List of Unavailable Employees & Time unavailable at")
        print(unavailableEmployees)
        userEmployeeAvailabilityListFeedback = input("\nIs the list correct?\nYes or No?\n\nUser: ")
        if userEmployeeAvailabilityListFeedback in yesAnswers: #ALL INFO CORRECT
            print("\n\nConfirmed, employee availability data correct!\n\nContinuing to task inputs...\n\n")
        else: #NEED TO CORRECT INFO
            userEmployeeAvailabilityListFeedback = input("\n\nFixing the mistake(s) requires reentering all of the availability data.\n\nProceed? Yes or No\n\nUser: ")
            if userEmployeeAvailabilityListFeedback in yesAnswers: #CONFIRM WANT TO RESTART PROCESS TO CORRECT INFO
                print("\nConfirmed, restarting process...\n\n")
                employeeAvailabilityInput(noUnavailabilites) #TODO#
    else: #ALL INFO CORRECT
        print("\nContinuing to task inputs...\n")
        print("List of Unavailable Employees & Time unavailable at")
    return None
unavailableEmployees = employeeAdjustmentSection()
#print("Test avail employees", availableEmployees)

# Complicatedly reformats and adds data to unavailableEmployee dictionary so that it can then edit/update the availableEmployee Data to reflect the unavailabilites
unavailableEmployees = {'Yacht': ['7:45', "9:50"], 'Shazam': ['3:45'],
                        'Fenway': ["5:20", "10:00", "11:00", "11:45", "1:45"]}  # POTENTIAL TYPE ISSUE, program put inputs in as strings,
#TODO NEEED TO SOORT LIST OF TIMES SO THAT IN INCREASIG ORDER OTHERWISE ASSIGNMETN FUNCTION WONT WORK

availabilitesToChangeForEmployees = []
lengthOfUnavailableEmployees = len(unavailableEmployees)
print("0 lengthOfUnavailableEmployees TEST: ", lengthOfUnavailableEmployees)
numberOfEmployeesInUnavailableEmployeesDict = lengthOfUnavailableEmployees
global listOfOrderOfUEOfIndexesOfAE
listOfOrderOfUEOfIndexesOfAE = []
availability_timesSum = []
iWUEV = 0
employeeOrderInUnavailableEmployeesDict = 0
while lengthOfUnavailableEmployees > 0:
    employeeNameTemp = list(unavailableEmployees.keys())[iWUEV]
    employeeNameTempValue = iWUEV
    iWUEV += 1
    #print("0.5, TEST iWUEV value: ", iWUEV)
    # employeeNameTemp = keyToListTempUE[0]

    #print("1, TEST employeeNameTemp: ", employeeNameTemp)
    # print("TEST unavailableEmployees: ", unavailableEmployees)

    indexValueX = employeeNamesList.index(employeeNameTemp)
    listOfOrderOfUEOfIndexesOfAE.append(indexValueX)
    #print("2, name index value for employeeNamesList TEST: ", indexValueX)

    availability_times = unavailableEmployees[employeeNameTemp]
    print("3, test PRINT availability_times: ", availability_times)
    availability_timesSum.append(availability_times)

    # miniDict = {employeeNameTemp: indexValueX}
    # for time in availability_times:
    # miniDict[time] = False #availability_list [{[time] = False}] for time in availability_times]
    # print("mini dict TEST", miniDict)

    availability_list = [{time: False} for time in availability_times]
    #print("4, availability_list TEST:  ", availability_list)

    availabilitesToChangeForEmployeesTemp = [
        {employeeNameTempValue: employeeNameTemp, employeeNameTemp: indexValueX, "availability": availability_list}]
    #print("5, test PRINT availabilitesToChangeForEmployeesTemp[]: ", availabilitesToChangeForEmployeesTemp)

    availabilitesToChangeForEmployees.extend(availabilitesToChangeForEmployeesTemp)
    print("6, test availabilitesToChangeForEmployees{}: ", availabilitesToChangeForEmployees)

    # maybe make availabilitesToChangeForEmployees really availabilitesToChangeForEmployees, and have the getting of the order and the pair values seperate? Or rename, idk and i dont really care.
    lengthOfUnavailableEmployees -= 1
    #print("7, TEST lengthOfUnavailableEmployees", lengthOfUnavailableEmployees)

    #print("8,----- END OF ITERATION OF FOR LOOP -----\n\n")
print("TEST listOfOrderOfUEOfIndexesOfAE: ", listOfOrderOfUEOfIndexesOfAE)
print("TEST availability_timesSum: ", availability_timesSum)
print("test avial time sums call",availability_timesSum[0][1])
#print("config print", listOfOrderOfUEOfIndexesOfAE[0])

#Criticism, in feel like my variables are too long, but better to be discriptive and be able to easily tell what they are and apart from eachother than being to short.
#PURPOSE: To make sure the info from unavailable employees is assigned to the right person in the for assignment loop, have to pre sort listOfOrderOfUEOfIndexesOfAE to be in same order as employeeList


#TODO NEEED TO SORT LIST OF TIMES SO THAT IN INCREASIG ORDER OTHERWISE ASSIGNMETN FUNCTION WONT WORK, may need to rework after data format standarizaton
#TODO STANDARDIZING DATA FOR TIME, INT REF, IN LISTS / KINDA DO I WANT TO DI IT HERE OR LATER
# TODO multi time converter idea, what about multi time stuff?, maybe make a function for that? search for times in stirng answer then split up, convert to int. Then subtract to find diff, then be like oh all these times are invalid and then insert all those times into list so all those slots are invalid.

sortedListOfOrderOfUEOfIndexesOfAE = listOfOrderOfUEOfIndexesOfAE #need for fr loop to continue working properly
unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict = {}
iterAAFY = 0
for x in listOfOrderOfUEOfIndexesOfAE:
    unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict.update({listOfOrderOfUEOfIndexesOfAE[iterAAFY]:availability_timesSum[iterAAFY]})
    iterAAFY+=1
print(" TEST unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict: ", unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict)

#first have to make a ref book to convert the stuff into in, Makes a list of the times / keys of dayTimeSlots
lengthDayTimeSlots = len(dayTimeSlots[0])-1 #LEARNING CONCEPT,, & KEY POINT - len gives me one more than index number, so keep in mind when using len to go thru indexs
#print("TEST lenghtdayTimeSlots: ", lengthDayTimeSlots)
iterDayTimeSlotsStandardizer = 0
while iterDayTimeSlotsStandardizer <= lengthDayTimeSlots:
    tempKeyListForDayTimeSlotsStandardizer = list(dayTimeSlots[0])
    iterDayTimeSlotsStandardizer += 1
print("TEST 1 tempKeyListForDayTimeSlotsStandardizer: ", tempKeyListForDayTimeSlotsStandardizer)

# put times as values, and ascending number as key (NtS)- Numbers to Strings
dayTimeSlotsStandardizedNtS = {}
iterDayTimeSlotsStandardizerA = 0
while iterDayTimeSlotsStandardizerA <= lengthDayTimeSlots:
    dayTimeSlotsStandardizedNtS.update({iterDayTimeSlotsStandardizerA:tempKeyListForDayTimeSlotsStandardizer[iterDayTimeSlotsStandardizerA]})
    iterDayTimeSlotsStandardizerA+=1
    #print("[TEST 2, IN LOOP] new dict dayTimeSlotsStandardizedNtS: ", dayTimeSlotsStandardizedNtS)
print("[TEST 3, OUT OF LOOP] new dict dayTimeSlotsStandardizedNtS: ", dayTimeSlotsStandardizedNtS)

# put numbers as values, and times as key (StN)- Strings to Numbers
dayTimeSlotsStandardizedStN = {}
iterDayTimeSlotsStandardizerB = 0
while iterDayTimeSlotsStandardizerB <= lengthDayTimeSlots:
    dayTimeSlotsStandardizedStN.update({tempKeyListForDayTimeSlotsStandardizer[iterDayTimeSlotsStandardizerB]:iterDayTimeSlotsStandardizerB})
    iterDayTimeSlotsStandardizerB+=1
    #print("[TEST 2, IN LOOP] new dict dayTimeSlotsStandardizedNtS: ", dayTimeSlotsStandardizedNtS)
print("[TEST 3, OUT OF LOOP] new dict dayTimeSlotsStandardizedStN: ", dayTimeSlotsStandardizedStN)

#TODO find better way to cycle thru the keys and update values
#TODO make a uni function for splitting dicts and stuff writing data and put back together like DNA modification
#TODO maybe maek so can edit times for day and add or subtract any if needed, then would need to use the dynamic script

# TODO STAND DATA FORMAT BEOFRE SORTING, CANNOT US TRAD DATE, MAKE 2ND TIMESLOT DICT, ONE FOR TIMES & T/F, OTHER FOR DATA REF INT & STR TIME

timeListToSortAlgo = []
tempTransferDict1 = {}
timeListToSortAlgoDefault = deepcopy(timeListToSortAlgo)
iterAAAH = 0
for person in unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict:
    
    #Step 1 - Detach from dictionary, and convert to int
    timeListToSortAlgo.extend(unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[person])
    print("TEST timeListToSortAlgo :", timeListToSortAlgo)
    sizeL = len(timeListToSortAlgo)

    #def convertTimeListStrToInt(list,sizeOfList):
    for index, timeStr in enumerate(timeListToSortAlgo):  #index = index, timeStr = corresponding value
        timeListToSortAlgo[index] = dayTimeSlotsStandardizedStN[timeStr]
        print("TEST Thingy may be working", timeListToSortAlgo)
        # LEARNING CONCEPT if getting "dict_keys" at beginning of list, cus trying to get the keys, then call list() on the dictionary instead:
        """timeListToSortAlgo[index] = int(timeStr.replace(":","")) #LEARNING CONCEPT - strings are immutable so have to specifically assign shit to them
        #LEARNING CONCEPT - can use (string name).replace("thing to replace", "thing to replace with") to replace stuff in a string
        print("TEST update per for timeListToSortAlgo :", timeListToSortAlgo)
        #sizeL0+=1"""

    """LEARNING CONCEPT -
    ChatGPT
    The use of enumerate in a for loop is a common Python idiom for iterating over a sequence when you need both the index and the value of each item in the sequence. 
    The function enumerate takes an iterable (like a list, tuple, or string) as an input and returns an iterator that produces pairs of indexes and values from the iterable.
    
    enumerate(timeListToSortAlgo): This call to enumerate takes the list timeListToSortAlgo as an argument. 
    timeListToSortAlgo is assumed to be a list of strings, where each string represents a time (e.g., "12:30", "09:45").
    enumerate Functionality: For each item in timeListToSortAlgo, enumerate generates a pair consisting of an index (starting from 0) and the value at that index in the list. 
    So, if timeListToSortAlgo is ["12:30", "09:45", "23:59"], enumerate(timeListToSortAlgo) would produce (0, "12:30"), (1, "09:45"), and (2, "23:59") in successive iterations.
    for index, timeStr in enumerate(timeListToSortAlgo): This unpacks each pair generated by enumerate into index and timeStr. In the first iteration, index would be 0 and timeStr would be "12:30", in the second iteration, index would be 1 and timeStr would be "09:45", and so on. 
    This allows you to use both the index of each item (to access or modify items in the list by their position) and the value of each item (to work with the content directly) within the loop.
    """

    #Step 2 - Sort the list to ascending order
    # Selection sort
    # time complexity O(n*n)
    # sorting by finding min_index
    selectionSort(timeListToSortAlgo, sizeL)
    print('The array after sorting in Ascending Order by selection sort is:')
    print(timeListToSortAlgo)

    #Step 3 - Convert back to str
    for index, timeInt in enumerate(timeListToSortAlgo):  #index = index, timeStr = corresponding value
        timeListToSortAlgo[index] = dayTimeSlotsStandardizedNtS[timeInt]
        print("TEST REconversion may be working", timeListToSortAlgo)

    #Step 4 - Reattach to dictionary
    unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[listOfOrderOfUEOfIndexesOfAE[iterAAAH]] = timeListToSortAlgo
    #print("TEST tempTransferDict1 FINAL END", tempTransferDict1)
    print("TEST unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict FINAL END", unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict)
    #IF LINE ABOVE BREAKS, might be because of this: var & usage eslewhere listOfOrderOfUEOfIndexesOfAE

    #END

    #print("TEST timeListToSortAlgo (BEFORE) reset: ", timeListToSortAlgo)
    timeListToSortAlgo = deepcopy(timeListToSortAlgoDefault) #using a .clear method fucks things up, idk why tho
    #print("TEST timeListToSortAlgo (AFTER) reset: ", timeListToSortAlgo)
    iterAAAH+=1
#unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict = deepcopy(tempTransferDict1)

#print("TEST newly sorted & formatted unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict: ", unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict)
#print("TEST (INDV) unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict: ", unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[2][0])
#print("TEST length of new dict: ", len(unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict))



# TODO - shit DATA STRUCTURE, need to make time dict so can set to false??? ALSO how take multiple, SOLUTION if entered as 6-7 then all good can interpret that
availableEmployees = []
availEmpCollectiveIter = 0
unavailableEmpNumberIter = 0
unavailableEmpsTimeUnavailableIter = 0
dayTimeSlotsIter = 0 #TODO make csv file for defining timeslots, also counsler ones per village, make column title the day / value, and then the slots numbers.
dayTimeSlotsTemp = deepcopy(dayTimeSlots)  #to hold to reset values that unavail employee changed, but don't nessecarily want changed for nxt employee

for employees in employeeNamesList: #names list keeps them in same order too??
    dayTimeSlots = deepcopy(dayTimeSlotsTemp)
    if dayTimeSlotsIter in listOfOrderOfUEOfIndexesOfAE:  # LEARNING QUESTION what are other ways of saying this?
        for slot in dayTimeSlots:
            for key in list(slot.keys()):
                    if unavailableEmpsTimeUnavailableIter < len(unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[availEmpCollectiveIter]):
                        if key in unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[availEmpCollectiveIter][unavailableEmpsTimeUnavailableIter]: #BUG FIXED, unavailableEmpNumberIter &  listOfOrderOfUEOfIndexesOfAE, not line up in order the for loop goes through the employeeNamesList, so I pre sort it before the for loop, alt fix is to make adictionary have this loop go off that but can do later.
                            #print("TEST tripwire, unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[unavailableEmpNumberIter][unavailableEmpsTimeUnavailableIter]", unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[availEmpCollectiveIter][unavailableEmpsTimeUnavailableIter]) #KEy error 0 = key does not exist
                            print("Slot key caught: ", [key])
                            slot[key] = False
                            #print("TEST unavailableEmpsTimeUnavailableIter / The list index/number of the current unavailable time in the list of unvailiable times for the current unavailable employee: ", unavailableEmpsTimeUnavailableIter)
                            unavailableEmpsTimeUnavailableIter += 1
                            #print("For loop if", slot)
                            #TODO See what more efficent for runtime this try and except things, or just doing an if to make sure the unavailableEmpsTimeUnavailableIter is less / equal to the number of absences /len(unavailableEmpNumberIter) of that employee
                    #except:
                        #unavailableEmpsTimeUnavailableIter = len(unavailableEmployeesIndexInEmployeeNameListAndUnavailableTimesDict[unavailableEmpsTimeUnavailableIter]) #why did I add this again???
        #print("test ITEMS", slot)
        unavailableEmpsTimeUnavailableIter = 0
        #print("TEST TWO unavailableEmpsTimeUnavailableIter", unavailableEmpsTimeUnavailableIter)
        unavailableEmpNumberIter+=1
        #print("TEST unavailableEmpNumberIter / The total number (NOT THE INDEX VALUE) of current unavailable employees cycled: ", unavailableEmpNumberIter)
        #print("end of IF dayTimeSlotsIter in listOfOrderOfUEOfIndexesOfAE statment")

    newEmployeeDict = ({
    'Name': employeeNamesList[availEmpCollectiveIter],
    'Gender': employeeGenderList[availEmpCollectiveIter],
    'Preferences': ['TrashWater'],
    'Availability': dayTimeSlots,
    })

    availEmpCollectiveIter+=1
    #print("TEST availEmpCollectiveIter", availEmpCollectiveIter)
    dayTimeSlotsIter+=1
    dayTimeSlots = dayTimeSlotsTemp
    #print("test loop",newEmployeeDict)
    availableEmployees.append(newEmployeeDict)
dayTimeSlots = deepcopy(dayTimeSlotsTemp)

#This Function was written by chat GPT4, bc I was  curious what a table outlook might look like & i was tried from 2 hours of coding. Thanks Chat GPT 4!
def print_employee_table(employee_dict):
    if not isinstance(employee_dict, dict):
        print("Error: Expected a dictionary as input.")
        return

    key_width = max(len(key) for key in employee_dict.keys()) + 2
    value_width = 50

    print("-" * (key_width + value_width + 3))
    print("Employee Information")
    for key, value in employee_dict.items():
        if isinstance(value, list):
            if key == 'Preferences':
                value_str = ', '.join(value)
            elif key == 'Availability':
                    # Assuming 'Availability' contains a list of dictionaries
                    # Count how many timeslots are True
                if value:  # Check if the list is not empty
                    available_slots = sum(1 for time, available in value[0].items() if available is True)
                    value_str = f"Total Slots: {available_slots}, Details Omitted for Brevity"
                else:
                    value_str = "No Availability Data"
            print(f"{key:>{key_width}} : {value_str:<{value_width}}")
        else:
            print(f"{key:>{key_width}} : {value:<{value_width}}")
    print("-" * (key_width + value_width + 3))

# Iterate through each employee dictionary and print its information
"""for employee_dict in availableEmployees:
    print_employee_table(employee_dict)
    print()"""
#print(len(availableEmployees[0]["Availability"][0]))


def employeeAvailableTimeSlotsSummer(employee_dict): #TODO take into calculations the 7:00am slots and other depenencies, maybe make diff betwen fire water and such
    """takes the availableEmployees Dict & Returns totalTimeSlots, (that are true)"""
    totalTimeSlots = 0
    if not isinstance(employee_dict, list):
        print("Error: Expected a list as input.")
    for employee_dict in availableEmployees:
        if not isinstance(employee_dict, dict):
            print("Error: Expected a dictionary as secondary layer input.")
        for key, value in employee_dict.items():
            if key == "Availability":
                    # Assuming 'Availability' contains a list of dictionaries
                    # Count how many timeslots are True
                if value:  # Check if the list is not empty
                    available_slots = sum(1 for time, available in value[0].items() if available is True)
                    totalTimeSlots += available_slots
                else:
                    value_str = "No Availability Data"
    return totalTimeSlots





# TASKS -------------------------------------------------------------------------------



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
#print("TEST value daySpecialTasks", daySpecialTasks)

#TODO be able to assign addtional tasks to certain people
#TODO be able to say when task is and use multi-duration

#UNDER CONSTRUCTION ------------------------------------------------------------------------
additionalTasks = []
#REALLY GOOD IMPLEMENTATION OF LOOPS AND INs AND APPENDING DICTIONARIES HERE
#Insert ability to make custom tasks...

#TODO remove AFTER DEBUGGING | additionalTasksTF = input("\nAre there any additional tasks you want to add for the day? Y or N? ")
additionalTasksTF = "N" #TODO remove after debugging
while additionalTasksTF in yesAnswers:
        userTask = input("Task Name: ")
        userStartTime = input("Start time: ") #make it so it standardizes time or give list to choose from
        userDuration = input("Duration: ") #FIX LATER to be blocks or time date, or give options. also mkae smart function to calc distance btwn two numbers to get duration
        userManpower = input("Number of People Needed: ")
        userImportance = input("Importance (1-10): ") # Figure out importance scale and how will work
        userAssignees = input("Is the task preassigned to someone(s)? Y/N: ")
        if userAssignees in yesAnswers:
            userAssignees = input("To whom: ") #TODO make it compatible with multiple names
        elif userAssignees in noAnswers:
            userAssignees = "No"
        userGenderSpecific = input("Is the task Gender Specific? Y/N: ")
        if userGenderSpecific in yesAnswers:
            userGenderSpecific = input("To which gender: ") #DONE: able to have list to take diff spellings of male or female and standardize the result
            if userGenderSpecific in maleAnswers:
                userGenderSpecific = "Male"
            elif userGenderSpecific in femaleAnswers:
                userGenderSpecific = "Female"
        elif userGenderSpecific in noAnswers:
            userGenderSpecific = "none"

        additionalTasksTF = input("Are there any additionally tasks you want to add for the day? Y or N?\n\nUser: ")

        newTaskDict = {'TaskName': userTask,
                       'StartTime': userStartTime,
                       'Duration': userDuration, #TODO make Auto convert if user enters time range etc
                       'NumPeopleNeeded': userManpower,
                       'Importance': userImportance,
                       'GenderSpecific': userGenderSpecific,
                       'Preassigned': userAssignees,
                       #TODO add other stuff like cert needed and type of cert needed, employee type too
                       }
        additionalTasks.append(newTaskDict)
if additionalTasksTF in noAnswers:
    print("No extra tasks! YIPPIE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#print("TEST FINAL additionalTasks DICT ",additionalTasks)

#Generate total tasks & special tasks depending on dateValue (date)

#TODO make a way to insert like a list of things you need done for the day more eaisly like a row in a csv or spreadsheet - could maybe come from default tasks, just be like any default taks yo uwant done, and ask if so when(or if predetermined time is acceptable, for special ones))
#daysTasks = additionalTasks + needToDoTasks(could maybe come from default tasks, just be like any default taks yo uwant done, and ask if so when(or if predetermined time is acceptable, for special ones)) + specialTasks + NightChore

print("TEST daySpecialTasks type check", daySpecialTasks)
if dateValue == 7 or dateValue == 6: #BIG LEARNING CONCEPT: if dateValue == 7 or 6: This condition does not check if dateValue is either 7 or 6. Instead, it checks if dateValue is 7, or if 6 is true. Since non-zero integers are considered truthy in Python, 6 is always true, making the condition always evaluate to true.
    defaultTaskDurationsDict.clear() #WHY- because special schedule for these dates and it is easier just to preprogram in

#TODO create nightchore list and data structures
nightChores = []
daysTasks = [daySpecialTasks, additionalTasks, defaultTaskDurationsDict, "Standard Tasks", nightChores]
#TaskRank1, TaskRank2,TaskRank3 can add other lists into them??
#tasks: {'TaskName': 'Clean Windows', "StartTime" : "7:45" 'Duration': 2 , 'NumPeopleNeeded': 1, 'Importance': 5, 'GenderSpecific': None, CertNeeded: "Yes/N", RelevantCert: "Lifeguard" TaskValue: taskValueVar}

#tasks per timeslot etc
#tasks # of ppl needed




#TODO Generate special tasks depending on Day
#TODO  for a (special) task day need to know the tasks, then for a task the day, the time the tasks take place+duration, how many ppl on tasks (aka # of certain task).
#Timeslot
#TODO Tasks due in timeslot & number of people per task
#TODO IMPORTANCE SYSTEM - Rank tasks in importance, HOW DO I RANK IMPORTANCE???





#Start of algorithm / assignment sequence --------------------------------


#Calc total task for the day and timeslots available to see if enough room.
#might have to change later depending on how structure data
totalAvailEmpTimeSlots = employeeAvailableTimeSlotsSummer(availableEmployees)
#print("TEST sum of avail emp timeslots: ", totalAvailEmpTimeSlots)

def sum_duration_values(data):
    total_duration = 0
    def search(data):
        tempDuration = 0
        tempFreq = 0
        print("TEST | data in search(data): ", data)
        nonlocal total_duration #LEARNING CONCPET: nonlocal, allows use of outerscope variable in functions
        if isinstance(data,dict):
            for key, value in data.items():
                #print("TEST | for key, value in data.items(): ", data.items())
                if key == "Duration":
                    tempDuration +=(value)
                if key == "Frequency":
                    tempFreq =+ (value)
                elif key in defaultTaskDurationsDict: #IF ERROR, check this. to handle and count the basic task csv file dict
                    #TODO maybe standardize all taks formats even ones imported from CSV
                    total_duration +=(value)
                search(value)
        elif isinstance(data, list):
            for item in data: #NOT for item in list
                search(item) #recursive call search function so goes thru every item in list, of every list
        elif data == 0: #item neither dict or list, so prob integer or basic value which means no task (prob), so set to 0
            total_duration += 0 #IF ERROR, check this
        #print("TEST total duration in search(data): ", total_duration)

    search(data)
    return total_duration

sum_Day_Duration_Values = sum_duration_values(daysTasks)

print("TEST numOfTasksForDay: ", sum_Day_Duration_Values)

#FOR TASKS CREAT taskCost var? so task duration*num of people / freq?????
print("\n--------------------------------------------------------\n")
print("QUESTION: Calculating if a scheduling solution is possible.....")
totalAvailEmpTimeSlots -= (4+(1*2)+(1*3)) #IF ERROR CHECK, total swatties -4 on kswat and waterun for 7am, then account for am and pm flagup overlap #TODO take into calculations the 7:00am slots and other depenencies (KSWAT etc)
#TODO give option to see how calc??
print("Total employee time periods available: ", totalAvailEmpTimeSlots)
sum_Day_Duration_Values -= ((1*2)+(1*3)) #IF ERROR CHECK, KSWAT AM overlap * * num of people/freq & PM shift overlap * * num of people/freq
#TODO take into calc the depenencies (KSWAT etc) overlaps. account for overlaps
print("Total time periods needed to complete all of today's tasks: ", sum_Day_Duration_Values)
if totalAvailEmpTimeSlots >= sum_Day_Duration_Values:
    print("ANSWER: Scheduling solution is probably possible.\nContinuing to task scheduling and assignment...")
if totalAvailEmpTimeSlots <= sum_Day_Duration_Values:
    print("ANSWER: Scheduling solution probably not possible. See diagnostics & suggestions?, Edit Task load / reconfigure?")
    #TODO Make see diagnostics, solution suggestions, edit task load / reconfigure inputs tools? Maybe break down and show stats of each task?, can do fancy stuff later once the sum functions are fully compelted and main program is complete
print("--------------------------------------------------------\n")






#----- Program Code snippets may need to reuse
""""
OBSELETE?, until later when need to update stuff?
# Assigns names from names list to the availableEmployeesList
employeeNamesListTempModded = list(employeeNamesList)  # so it doesnt jack up the og values list in case i need to use it. The for loop fucks up the list so its not reusable
for employeeNamesListTempModded, new_name in zip(availableEmployees,employeeNamesListTempModded):  # wut is zip? BEWARE MAY BRAKE IF UNEVEN?
    employeeNamesListTempModded['Name'] = new_name

# Assigns genders from genders list to the availableEmployeesList
employeeGenderListTemp = list(employeeGenderList)  # so it doesnt jack up the og values list in case i need to use it. The for loop fucks up the list so its not reusable
for employeeGenderListTemp, new_name in zip(availableEmployees, employeeGenderListTemp):  # wut is zip? BEWARE MAY BRAKE IF UNEVEN?
    employeeGenderListTemp['Gender'] = new_name
"""


"""DIDNT WORK, NEED TO UNDERSTAND BETTER --> gpt output bleow it better
print("TEST availableEmployeesList INDV VER: \n")
y = 1
for i in availableEmployees:
    print(availableEmployees[y],"\n")
    y = y + 1"""

""""#TEST availableEmployees print each persons name and number
for i, employee in enumerate(availableEmployees, start=0):  # start=1 if you want indexing to start at 1
    name = employee['Name'] #is retrieving the value associated with the key 'Name' from the dictionary employee and storing it in the variable name.
    print(name, "#", i, "\n")"""

#TEST availableEmployees print all of each persons information
"""for i, employee in enumerate(availableEmployees, start=0):
    print(availableEmployees[i],"\n")"""

"""
#LEARNING - I keep accidentally doing == evaluator operator # instead of = assignment operator when I use T/F for loops and then I wonder why the loop doesn't work

Some examples on how to use lists in dics and dics in lists and so forth.
# Update Alice's age
people[0]["age"] = 31
# Add a new hobby to Bob
people[1]["hobbies"].append("cycling")
print(people)

Y/N Confirmation & Continuing Input Loop Cycle Template
Basic Y/N confirmation & input cycle loop I find I keep using, so I am going to make a template for it

ogVariableTF = input("Are there any additionally tasks you want to add for the day? Y or N?\n\nUser: ")
if ogVariableTF in yesAnswers:
    inputTF == True
    ix = 0
    while inputTF == True
        descriptionVariable1 = input("description: ") #however many inputs and variables you need
        dictName.update({NameOfKeyThing:[var that replaces value]}) #add var to list or whatever
        descriptionVariable2 = input("description: ")
        additionalTasks[ix]["TaskName"] = userTask #or replace dict in list value
        #add them into something if you want like a dict or list below
        tasks: {'TaskName': 'Clean Windows', 'Duration': 2, 'NumPeopleNeeded': 1, 'Importance': 5, 'GenderSpecific': None}
        inputTF = input("Are there any additionally tasks you want to add for the day? Y or N?\n\nUser: ")
        if inputTF in yesAnswers:
            inputTF == True
            ix+=1
        else:
            inputTF == False
            break 
if ogVariableTF in noAnswers:
    pass
    #something else happens
#they way i have the while loop done makes it a little harder to understand with the var names, but is more efficnet code wise than repeating stuff
"""


""""


#PROGRAM OVERVIEW --------------------------------------------------
#load in default info, employee gender info & nickname, basic tasks & stand duration, timeslots, & nightchore
#Ask for special tasks for the day and relevant info, also determine based on date user inputs what are some routinly occuring speical events that need to be accounted for.
#Generate Total Tasks
#People Avialable for day (Check for exceptions), *also find out partial avialibilites*
#Timeslot
#Tasks due in timeslot & number of people per task
#Rank tasks in importance
#See how many ppl avail in timeslot, then check if enough people  to complete tasks for that timeslot -> throw exception if isnt list shortage amount, 
#then base on importance list find how many task you can fill and then state what tasks cannot be filled, maybe in final log
#then take that list and save it in new variable to be used in the assignment loop for that slot???? idk, that way dont have to re calc in loop. (Could hurt multi timeslot assignments maybe??)
#(Req people task preferences???)
# MAKE THIS A LOOP, Assign tasks  until all needed tasks are assigned or no room / people to complete all task in slot (make sure (idk when in program) to define when task need done by / deadlines  
    #How to implement the assignment loop? 
    #Take list of tasks that we determined earlier can be filled, then start with most important task, but first check if it is a mulit hour / timeslot task if it is then (Nested loop?) take the pool of avialible employees and randomly select one, 
    #this probbaility can be modifyied by a pref variable which can make it more liely for certain employees to get certain tasks if they prefer them, this information would be stored somewhere in the program and could be modified by the user.
    #See if the selected employee is avialiable for next time slots or as long as needed for the long task, if not then cycle to next until find one? If it is not a long task then just randomly select from the available employee pool and employee, 
    #Also some tasks are gender dependent: but really only matters for specific special events that happen at a routine time every week: men-womans sessions & nightchores such as clenaing men or womens bathroom etc.
    #Randomly select person (Based on "people power" (lol) pool calc probbability of person recieving each task) #loop by person or task? does it matter??? -Person bc assigning it to a person
    #Then if can't assign all tasks in timeslot give error and add to final report what couldnt be assigned what was moved and why, and if able to fit into the schudle someowhere else maybe dont notify in final report?
#Print final scheudle output and error logs in console, also write resutls to CSV so can be the formatted or manually modified in excel or google sheets. Maybe if adapated as a google workspace add in it could directly output the information into the sheet then user made final adjsutments.


GPT SUGGESTION:
Tasks:
Each task could be represented as a dictionary with its properties.
tasks: {'TaskName': 'Clean Windows', 'Duration': 2, 'NumPeopleNeeded': 1, 'Importance': 5, 'GenderSpecific': None}
Employees:
A list where each employee is a dictionary with their details and availability.
Example: {'Name': 'Alice', 'Gender': 'F', 'Preferences': ['Task1', 'Task2'], 'PartialAvailability': {'Morning': True, 'Afternoon': False}}
Timeslots:
You could use a list if timeslots are fixed and ordered or a dictionary for more flexibility.
Example: [{'Timeslot': '08:00-10:00', 'AvailableEmployees': ['Alice', 'Bob']}] or {'Morning': {'StartTime': '08:00', 'EndTime': '12:00', 'AvailableEmployees': ['Alice', 'Bob']}}
Task Assignments:
A dictionary to hold which tasks are assigned in which timeslots and to whom.
Example: {'08:00-10:00': {'Task1': ['Alice'], 'Task2': ['Bob']}}


#ADDITONAL IDEAS
#idea to make more user friendly, make a final program that takes the csv file and converts it to an excel file that can be modified & styled by the user. Idk maybe even get it able to format the excel file - prob to complicated tho.
#resources for conversion and then formatting excel file: 
#***https://blog.devgenius.io/how-to-produce-beautiful-well-formatted-excel-reports-using-python-fd87146a1e0e
#https://www.geeksforgeeks.org/convert-csv-to-excel-using-pandas-in-python/
#**https://www.cybrosys.com/blog/how-to-convert-csv-to-excel-using-pandas-in-python#:~:text=In%20python%2C%20we%20convert%20CSV,labeled”%20information%20handy%20and%20intuitive.



#PROBLEMS
#problems how to do multi hour tasks, pre assign peopl stuff or intentionally leaving part of the scheudle blank. Other concerns: efficency, and overcomplication, how easy would it be to modify and make user friendly? Also how easy to port to google workspace addon to google sheets
"""


#TODOLIST bc my dumbass has 1mb of working memory ----------------------------------------------------------------------------------------------------------------
#TODO Redo defaultInfo csv file, storage, retrevial, and interpetation system. Now need to ad gender column too
#TODO Create save system for preferential stuff that you dont want to type in repeatedly but cant be in defaultInfo, will have to maeke csv readers & converters tho
#TODO Finish getting all the time and special events listed
#TODO Create master task list (just add some stuff some like 80% there)
#TODO Preferences system
#TODO Time system, how work? its input blocks or time date, or give options. also make smart function to calc distance btwn two numbers to get duration, will have to maeke csv readers & converters too tho
#TODO Importance system
#TODO Multi-timeblock system
#TODO Merge all input data into master roster for algorithm
#TODO Actually devlop algorithm - will be a pain in the ass week long affair probbably
    #TODO Probability system
    #TODO Sort system and arrange data for selectioin
    #TODO Anti Overlap System
    #TODO A bunch of other algorithim stuff
    #TODO Error Log, Exceptions, & Final Error Report System
    #TODO prob a bunch of other shit I forgot
#TODO Format Console Output (Potentially scrapped)
#TODO Format CSV / Excel Output --> Core Feature
#TODO Decide if format for google sheets or app plugin (Somewhat likely)
#TODO Decide if format for web application deployment via Flask and Google Cloud (Highly Likely)
#TODO Potentially make gui to make input easier??? DO AFTER Decide on output format
#TODO Final review of entire system for user friendly-ness changes and bugs
#TODO Review to ensure scalability
#TODO Documentation
#TODO Bug Reporting and Diagnostic Mechanism - maybe make an internal log that saves each time you use and had a toon of data so if there is a glitch, or at the end fo the program it asks the user any glitches, if yess then saves to log which i can look at later and user can also make comments on messsup.
#TODO Clean up comments and consolidate learning experience and examples maybe at the end to show what learned?
#TODO Cry
#TODO Get user feedback, incoperate feedback & iterate
#TODO Finalize & Deploy

end_program_time = time.time()
elapsed_time = end_program_time - start_program_time
print("Elapsed time:", elapsed_time, "seconds")