import time
import datetime
from datetime import timezone, timedelta
from code_root.config.settings import (
    DAYS,
    DAYS_KEY_VALUE_INVERSE,
    DUMB_MEME_1,
    time_slots_data,
    time_slots_by_day
    )
from code_root.config.utility import timer
from colorama import Fore, Style
from typing import Dict, List, Any
import math
import bisect

#NOTE EXPERIIMENTAL CLASS for maybe later usage to simplify some clacs
class military_time:
    """returns values to the min"""
    
    def __init__ (self):
        
        def string_to_military(days_time_slots, dayTimeSlotsKeysList, numbers_to_strings, strings_to_numbers):
            numbers_to_strings
        def military_to_string(days_time_slots, dayTimeSlotsKeysList, numbers_to_strings, strings_to_numbers):
            return
        def military_time_subtract(time1, time2):
            return
        def military_time_between(time1, time2):
            """returns value in min"""
            return
        def military_time_add(time1, time2):
            return

def program_auto_get_date_value(get_next_day = False):
    """Returns a string with a full weekday's name. Dependecies: Uses datetime and timezone modules"""
    weekday = datetime.datetime.now(timezone.utc).astimezone().isoweekday() #WHY isoweekday() - returns weekday int mon =1 sun = 7, this aligns with pre hardcoded date code i put in 'days' dict, that way this func gives same output as the manual one and there is no need to adjust any other outputs
    if get_next_day: #WHY if get_next_day - if you want to make the schedule the night before, it knows to generate a schedule for the next day. Since the day values are int you just add +1 to get the next day
        if weekday == 7: #Sunday
            weekday = 1  #Monday, instead of addign +1 to sunday, which would equal 8 (not a valid day)
        else:
            weekday + 1 
    return weekday

def validate_user_date_input(dateUserEntered):
    """Checks if user input is acceptable
    Returns: int : date value"""
    try:
        
        if isinstance(dateUserEntered, str) and dateUserEntered.lower() in DAYS: #account for non-numeric input
            dateUserEntered = DAYS[dateUserEntered.lower()] #convert any string input into int
            return dateUserEntered   
        else:
            date_value = int(dateUserEntered) #int bc keys are int, but user input is not
            
            if date_value in DAYS_KEY_VALUE_INVERSE.keys(): #if numeric input, check if valid
                return date_value
            
            elif date_value in {int(k): v for k, v in DAYS_KEY_VALUE_INVERSE.items()}: #if numeric input, check if valid
                return date_value
            
            else:
                return False
    except ValueError: 
        #if conversion to integer fails, return False
        return False

def play_joke_on_user():
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
        print("")
        print(DUMB_MEME_1)
        print("\n\nPROGRAM TERMINATING, its all your fault.")
        exit()
     
def get_day_name(dateValue):
    if not isinstance(dateValue, str):
        dateValue = str(dateValue)
    dayName = DAYS_KEY_VALUE_INVERSE[dateValue]
    return dayName

def get_day_time_slots(dateValue):
    if not isinstance(dateValue, str):
        dateValue = str(dateValue)
    dayTimeSlots = time_slots_data[time_slots_by_day[dateValue]] #NOTE if break look here
    return dayTimeSlots

def list_schedule_times(day_time_slots):
    """takes the days time slots dict and retruns the times to the user. (since dict, only displays time keys and not values: t/f)
    Args:
        day_time_slots (Dict): _description_
    """
    times = list(day_time_slots[0].keys())
    return times

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

def remove_time_slot(day_time_slots, time_to_remove):
    """Remove a time slot from the day's schedule."""
    if time_to_remove in day_time_slots:
        del day_time_slots[time_to_remove]
    return day_time_slots

def timeSlotStandardizer(dayTimeSlotsKeysList: list[str]) -> tuple[dict[int, str], dict[str, int]]:
    """ Standardizes timeslots values and makes ref dictionaries from a list of time slots.
    Args:
        dayTimeSlotsKeysList (List[str]): Input should be a list of time slot strings.
    Returns:
        Tuple[Dict[int, str], Dict[str, int]]: A tuple containing two dictionaries:
            - First dictionary maps indices to time slot strings. (NtS)
            - Second dictionary maps time slot strings to indices. (StN)
    """
    
    num_of_time_slots: int = len(dayTimeSlotsKeysList) - 1 #WHY -1 len gives me one more than index number, aka no start at 0.
    
    # Maps indices to time slots (Number to String) (NtS)
    numbers_to_strings: dict[int, str] = {}
    for i in range(num_of_time_slots+1):
        numbers_to_strings.update({i:dayTimeSlotsKeysList[i]})

    # put numbers as values, and times as key (StN)- Strings to Numbers
    strings_to_numbers: dict[str, int] = {time: num for num, time in enumerate(dayTimeSlotsKeysList)}
    
    
    #experimental faster listslicerversion
    return numbers_to_strings, strings_to_numbers 

def fill_time_slots_inbetween_A_and_B(timeA,timeB,dayTimeSlotsStandardizedStN,dayTimeSlotsStandardizedNtS):
    #assumes args already all have valid time slots
    
    #1. take input times, find corresponding standardized number for position in the master ref times list. 
    timeAPeriod = dayTimeSlotsStandardizedStN[timeA]
    timeBPeriod = dayTimeSlotsStandardizedStN[timeB]
    
    #2. Make a list
    times = list(dayTimeSlotsStandardizedStN.keys())
    
    #3. Slice from start to end, including both endpoints (add 1 to end)
    return times[timeAPeriod:timeBPeriod+1]


#TODO fix       
def seek_valid_time_slot(input_time_str: str, times_list: list[str]) -> str: #WHY thing to help only compile list once in function, and then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
    """Finds the next valid time slot in a list of time slots after a given input time."""      
    

    @timer
    def time_to_minutes(time_str): #for intial conversion into min for comparison
        
        """Convert a hh:mm AM/PM time string to minutes since midnight."""
        time_str = time_str.upper() #WHY - makes AM/PM upper just incase, bc datetime modules functions to work
        
        #time_pattern = r'^\d{1,2}(:\d{2})?$' # This pattern matches a string that looks like a time (one or two digits for hour, optionally followed by ":" and one or two digits for minutes) 
                        
        time_formats = [
            "%I:%M %p", # Format 1: 08:25 PM # Note the use of %I for hour and %p for AM/PM
            "%I %p", # Format 2: 7 PM
            "%I:%M%p", # Format 3: 08:25AM <-- WHY needed because when try to convert ref list to min before midnight, the values come in as 7:00am etc, with no space between time and am/p,
            "%I%p", # #Format 4: 7PM  
            ]
        
        for fmt in time_formats:
            try:
                time_val = datetime.datetime.strptime(time_str, fmt) #WHY - ref datetime twice, once for the module, once for the class
                successful_parse = True 
                break # Parsing succeeded; exit the loop
            except:
                successful_parse = False
                continue #Try the next format
        
        # If no format matched, handle the failure: #IDK #TODO figure how to integrate into front end
        if not successful_parse:
            error_message =  f"\n\n{Fore.RED}{Style.BRIGHT}[ERROR]: Your time input:'{time_str}', does not match any known time format. \n Formats: 08:25 PM, 7 PM, 08:25AM, 7PM. \n ADIVCE: Prehaps you are missing an am/pm designator?.{Style.RESET_ALL}\n\n"
            raise ValueError(error_message)
        return time_val.hour * 60 + time_val.minute
    
    @timer
    def minutes_to_time(minutes): #for conversion from minutes back to 12Am/Pm time after sequence has been run and found a valid times
        """Convert minutes since midnight back to a hh:mm AM/PM string."""
        # Convert minutes back to a datetime object to leverage strftime formatting
        hours, minutes = divmod(minutes, 60)
        time_val = datetime.datetime(year=1, month=1, day=1, hour=hours, minute=minutes)
        # Note the use of %I for hour, %M for minutes, and %p for AM/PM
        return time_val.strftime("%-I:%M%-p").lower() # WHY Format the time without leading zeros, spaces between time and am/pm, and lowercase am/pm, bc in master ref list its "9:25am" not "09:25 AM" and the time will later be checked against it at some point, plus good to keep uniformity.
    
    #ROUNDS UP? 
    def find_next_time(input_time_minutes, time_list_minutes):
        left, right = 0, len(time_list_minutes)-1
        while left < right:
            middle = (left + right) // 2
            if time_list_minutes[middle] < input_time_minutes:
                left = middle + 1
            else:
                right = middle - 1
        return left
    
    # Convert input time and master list times to minutes
    input_time_minutes = time_to_minutes(input_time_str)
    time_list_minutes = sorted([time_to_minutes(time_str) for time_str in times_list])
    
    # Use binary search to find the insertion point
    index = find_next_time(input_time_minutes, time_list_minutes)

    # Check if we found a match
    if index < len(time_list_minutes):
        return minutes_to_time(time_list_minutes[index])
    else:
        error_message: str = "ERROR | multi time converter, finding valid time slot to calc diff | No matching timeslot found. Check input, or timeSlots list, see if AM/PM issue or formatting"
        return error_message
    
def get_current_week(m_d_ref_date: str, GET_NEXT_DAY: bool) -> str:
    """Returns a string indicating the number of full weeks since the given 'month_day_ref_date' of the current year until today.
    Assumes weeks start on Sunday. If today is Saturday and get_next_day is true, calculates from the next day (Sunday).
    The first week is counted as 'Week 1'.
    
    Args:
    month_day_ref_date (str): The reference date in 'MM/DD' format, e.g., '03/31'.
    GET_NEXT_DAY (bool): Flag to adjust calculation start if today is Saturday.

    Returns:
    str: A string in the format 'Week X', where X is the number of full weeks"""

    todays_date = datetime.datetime.now()
    #Create the reference date string by appending the current year to the given month and day
    ref_date_string = m_d_ref_date + "/" + str(todays_date.year)
    ref_date = datetime.datetime.strptime(ref_date_string, "%m/%d/%Y")

    if GET_NEXT_DAY and todays_date.weekday() == 5: # Saturday
        todays_date = todays_date + timedelta(days=1) # Move to sunday

    dist_btwn =  todays_date - ref_date

    # To adjust the week start to Sunday: (python thinks they start on monday)
    day_adjustment = (ref_date.weekday() + 1) % 7 #calc days to add to make it sunday
    dist_btwn += datetime.timedelta(days=day_adjustment)

    # Calculate full weeks and adjust for week count starting at 1
    week =  math.floor(dist_btwn.total_seconds() / 604800) + 1

    return f'Week {week}'