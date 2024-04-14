import time
import datetime
from datetime import timezone
from config.settings import days, daysKeyValueInverse, normalDayTimeSlots, wenSpecialTimeslots, friSpecialTimeslots, satSpecialTimeslots, sunSpecialTimeslots, dumbMeme1
from config.utility import timer
import re
from colorama import Fore, Style
from typing import Dict, List, Any

datesTimeSlots = {
    1:normalDayTimeSlots,
    4:normalDayTimeSlots,
    2:normalDayTimeSlots,
    3:wenSpecialTimeslots,
    5:friSpecialTimeslots,
    6:satSpecialTimeslots,
    7:sunSpecialTimeslots
    }


def program_auto_get_date_value(get_next_day = False):
    """Returns a string with a full weekday's name. Dependecies: Uses datetime and timezone modules"""
    weekday = datetime.datetime.now(timezone.utc).astimezone().isoweekday() #WHY isoweekday() - returns weekday int mon =1 sun = 7, this aligns with pre hardcoded date code i put in 'days' dict, that way this func gives same output as the manual one and there is no need to adjust any other outputs
    if get_next_day: #WHY if get_next_day - if you want to make the schedule the night before, it knows to generate a schedule for the next day. Since the day values are int you just add +1 to get the next day
        #WHY - if, else statment, check incase its sunday so knows to set weekday equal to 1 for monday. Bc sun = 7 and Mon = 1, otherwise you'd get 8. 8 = undefined
        if weekday == 7:
            weekday = 1 
        else:
            weekday + 1 
    return weekday

def validate_user_date_input(dateUserEntered):
    """Checks if user input is acceptable
    Returns: int : date value"""
    if dateUserEntered.lower() in days: #account for non-numeric input
        dateUserEntered = days[dateUserEntered] #convert any string input into int
        return dateUserEntered
    else:
        try: 
            date_value = int(dateUserEntered) #int bc keys are int, but user input is not
            if date_value in daysKeyValueInverse.keys(): #if numeric input, check if valid
                return date_value
            else:
                return False
        except ValueError: 
            # If conversion to integer fails, return False
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
        print(dumbMeme1)
        print("\n\nPROGRAM TERMINATING, its all your fault.")
        exit()
     
def get_day_name(dateValue):
    dayName = daysKeyValueInverse[dateValue]
    return dayName

def get_day_time_slots(dateValue):
    dayTimeSlots = datesTimeSlots[dateValue]
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

def timeSlotStandardizer(dayTimeSlotsKeysList: List[str]):
    """ Standardizes timeslots values and makes ref dictionaries. Takes the "dayTimeSlots" var. 
    Args:
        time_slots_of_the_day (Type: List): Input should be a list with dictionaries. Example: normalDayTimeSlots = [{'7:00': True, '7:45': True, '9:15': True, '9:50': True, '10:00': True, '11:00': True, '11:45': True, '1:45': True, '2:45': True, '3:45': True, '4:45': True, '5:20': True, '6:30': True, '7ish': 'NG', '8ish': 'Sweeting', '9ish': 'NightChore'}] #what do when have too special events at the same time??? such as NG and Playtime
    """
    
    #first have to make a ref book to convert the stuff into in, Makes a list of the times / keys of dayTimeSlots
    num_of_time_slots: int = len(dayTimeSlotsKeysList)-1 #WHY -1 len gives me one more than index number, so keep in mind when using len to go thru indexs

    #put times as values, and ascending number as key (NtS)- Numbers to Strings
    numbers_to_strings: Dict[int, str] = {}
    i: int = 0
    while i <= num_of_time_slots:
        numbers_to_strings.update({i:dayTimeSlotsKeysList[i]})
        i+=1

    # put numbers as values, and times as key (StN)- Strings to Numbers
    strings_to_numbers: Dict[str, int] = {}
    i:int = 0
    while i <= num_of_time_slots:
        strings_to_numbers.update({dayTimeSlotsKeysList[i]:i})
        i+=1
    return numbers_to_strings, strings_to_numbers 

def fill_time_slots_inbetween_A_and_B(timeA,timeB,dayTimeSlotsStandardizedStN,dayTimeSlotsStandardizedNtS):
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
                
def find_valid_time_slot(input_time_str, times_list, time_list_minutes, time_list_minutes_compiled = False): #WHY thing to help only compile list once in function, and then just ref it after that. Rather than recompile every time subfunction runs. Efficency thing
                        
    @timer
    def compile_time_list_minutes():
        nonlocal time_list_minutes  # Indicate that we're using the outer function's variable
        nonlocal time_list_minutes_compiled

        # Compile the list only if it hasn't been compiled yet
        if not time_list_minutes_compiled:
            time_list_minutes = sorted([time_to_minutes(time_str) for time_str in times_list])
            time_list_minutes_compiled = True  # Update the flag to prevent re-compilation

    @timer
    def time_to_minutes(time_str): #for intial conversion into min for comparison
        
        """Convert a hh:mm AM/PM time string to minutes since midnight."""
        time_str = time_str.upper() #makes AM/PM upper just incase
        
        #time_pattern = r'^\d{1,2}(:\d{2})?$' # This pattern matches a string that looks like a time (one or two digits for hour, optionally followed by ":" and one or two digits for minutes)
        """
        #TODO reasses and figure if still needed and a workaround later, prob use for front end
        if re.match(time_pattern, time_str) and not re.search(r'AM|PM', time_str, re.IGNORECASE): #Returns true if valid time, but no AM/PM, returns false if am/pm in it
            while True:
                    #print(f"\n{Fore.RED}{Style.BRIGHT}WARNING: {time_str} is missing an am/pm designator.{Style.RESET_ALL}")
                    #am_pm = input(f"Please enter if {time_str} is am or pm: ").strip().upper() #WHY - for datetime module functions to work am/pm must be uppercase: Am/PM
                    
                    if am_pm  == 'AM' or am_pm == 'PM':
                        time_str = time_str+" "+am_pm
                        break # Exit loop on successful parse
                    else: 
                        
                        print("Invalid input, try again.")"""  
                        
        time_formats = [
            "%I:%M %p", # Format 1: 08:25 PM # Note the use of %I for hour and %p for AM/PM
            "%I %p", # Format 2: 7 PM
            "%I:%M%p", # Format 3: 08:25AM <-- WHY needed because when try to convert ref list to min before midnight, the values come in as 7:00am etc, with no space between time and am/p,
            "%I%p", # #Format 4: 7PM  
            ]
        
        for fmt in time_formats:
            try:
                time_val = datetime.datetime.strptime(time_str, fmt) #ref datetime twice, once for the module, once for the class
                successful_parse = True 
                break # Parsing succeeded; exit the loop
            except:
                continue #Try the next format
        
        # If no format matched, handle the failure: #IDK #TODO figure how to integrate into front end
        if not successful_parse:
            error_message =  f"\n\n{Fore.RED}{Style.BRIGHT}Your time input:'{time_str}', does not match any known format.{Style.RESET_ALL}\n\n"
            return error_message
        return time_val.hour * 60 + time_val.minute
    
    @timer
    def minutes_to_time(minutes): #for conversion from minutes back to 12Am/Pm time after sequence has been run and found a valid times
        """Convert minutes since midnight back to a hh:mm AM/PM string."""
        # Convert minutes back to a datetime object to leverage strftime formatting
        hours, minutes = divmod(minutes, 60)
        time_val = datetime.datetime(year=1, month=1, day=1, hour=hours, minute=minutes)
        # Note the use of %I for hour, %M for minutes, and %p for AM/PM
        return time_val.strftime("%-I:%M%-p").lower() # WHY Format the time without leading zeros, spaces between time and am/pm, and lowercase am/pm, bc in master ref list its "9:25am" not "09:25 AM" and the time will later be checked against it at some point, plus good to keep uniformity.

    # Converts both the input time and the master ref list of times to minutes since midnight
    input_time_minutes = time_to_minutes(input_time_str)
    compile_time_list_minutes()

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
        return minutes_to_time(time_list_minutes[left])
    else:
        error_message = "ERROR | multi time converter, finding valid time slot to calc diff | No matching timeslot found. Check input, or timeSlots list, see if AM/PM issue or formatting"
        return error_message
