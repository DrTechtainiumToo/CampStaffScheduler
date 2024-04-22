from datetime import datetime, timezone

# TODO maybe make seocnd file once complete and name it 'defaults' 
#Gobal Variables and Basic Information + any future settings
#TODO name and make system later, plus converter for different types and universal storage, retrieval and update system

# Settings for application behavior
INTERFACE_TYPE = "terminal" #option 2 is web
MAX_ENTRY_ATTEMPTS = 3 #Max user input attempts for day in getting day value sequence, else goes to meme
GET_NEXT_DAY = False
GET_DATE_AUTO =  True
WEEK_COUNT_START_REF_DAY = '4/21'
"""must be m/d, must be a sunday, allow user to set a base datetime object, will be used as a date for the program to reference what week of camp it is."""

# Output config settings
#TODO add here

#Settings for internal behavior
UNAVAILABILITY_TASK = 'Unavailable' #The value of the 'unavailable task
#Note the unavailability value cant be int, gets changed in the program for some reason
#maybe bc its a constant?

#TODO maybe in the future
#ATTR var names & behaviors???
#Excel/Data file headers so can have conversion program easily be able to deal with hcnage to names and stil map correctly????



# File locations and paths
PROJECT_ROOT = "devious_fuckin_project_root/backend/data" #path to project
CSV_DATA_FOLDER = "CSV Data Folder"
SWAT_NIGHT_CHORES_INFO_CSV = f"{PROJECT_ROOT}/{CSV_DATA_FOLDER}/SWATNightChoresInfo.csv"
SWAT_SCHEDULER_SPECIAL_TASKS_LIST_CSV = f"{PROJECT_ROOT}/{CSV_DATA_FOLDER}/SWATSchedulerSpecialTasksList.csv"
SWAT_EMPLOYEE_INFO_CSV = f"{PROJECT_ROOT}/{CSV_DATA_FOLDER}/SWATEmployeeInfo.csv"
SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV = f"{PROJECT_ROOT}/{CSV_DATA_FOLDER}/SWATBasicTasksListForScheduler.csv"

# Response constants ----------------------
YES_ANSWERS = ["Y","Yes","yes","y","YES","ye","Ye","YE"]
NO_ANSWERS = ["N","No","no","n",'NO']
MALE_ANSWERS = ["Male","male","men","Men","boys","Boys","Man","man","Boy","boy","Males","males"]
FEMALE_ANSWERS = ["Female", "female", "Women","women","woman","Woman","Females", "females","Girl","girl","Girls","girls"]

# Mapping days to numerical identifiers and vice versa
DAYS = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'mon': 1,
        'tues': 2, 'tue': 2, 'wed': 3, 'thurs': 4, 'thur': 4, 'fri': 5, 'sat': 6, 'sun': 7, 'm': 1, 'w': 3, 'f': 5,
        's': 6, 'su': 7}
DAYS_KEY_VALUE_INVERSE = {1: "Monday", 2: "Tuesday", 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

# Time slot configurations
NORMAL_DAY_TIME_SLOTS = [{'7:00am': True, '7:45am': True, '9:15am': True, '9:50am': True, '10:00am': True, '11:00am': True, '11:45am': True, '1:45pm': True, '2:45pm': True, '3:45pm': True, '4:45pm': True, '5:30pm': True, '6:30pm': True, '7:00pm': False, '8:00pm': False, '9:00pm': False}] #'7ishpm': False, '8ishpm': False, '9ish': False #'7ish': 'NG', '8ish': 'Sweeting', '9ish': 'NightChore' #what do when have too special events at the same time??? such as NG and Playtime
WEN_SPECIAL_TIMESLOTS = ['7:00', '7:45', '9:15', '9:50', '10:00', '11:00', '11:45', '1:45', '2:45', '3:45', '4:45', '5:20', 'TIME DOES NOT EXIST', 'TIME DOES NOT EXIST',  'TIME DOES NOT EXIST', '9is MAYBE'] #'TIME DOES NOT EXIST', 'TIME DOES NOT EXIST',  'TIME DOES NOT EXIST', '9is MAYBE' #can merge TIME DOES NOT EXIST and fromatting later, this is mainly all just formatted so the ;ogram can interpret it, will format for export seperatley
TUES_SPECIAL_TIMESLOTS = ['7:00', '7:45', '9:15', '9:50', '10:00', '11:00', '11:45', '1:45', '2:45', '3:45', '4:45', '5:30', '6:30', '7:15',  '8ish', '9:00']
FRI_SPECIAL_TIMESLOTS = [] # type: ignore
SAT_SPECIAL_TIMESLOTS = [] # type: ignore
SUN_SPECIAL_TIMESLOTS = [] # type: ignore

# Other constants (humorous placeholder text)
DUMB_MEME_1 = "Here dem lyrics!\n\n\n\
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