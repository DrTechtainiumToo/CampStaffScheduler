from colorama import Fore, Style
import time
from contextlib import contextmanager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import datetime

#Time any block of code with time_block()

@contextmanager #NOTE allow to time ANY block of code, not just functions. I was learning about ocntext managers, still need to learn more.
def time_block(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        message = f"{label}: {end - start} seconds"
        with open("code_root/logs/program_times_log.txt", "a") as log_file:  # "a" opens the file in append mode
            log_file.write(message + "\n")    
                

        
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


#can disable in production enviroment
def timer(func):
    def time_analysis_wrapper(*args, **kwargs):  #IDK kinda get it, still confused
        start_time = time.time()
        result = func(*args, **kwargs) #IDK kinda get it
        end_time = time.time()
        
        #TODO make it only print if in terminal, else save to file or something
        #NOTE might really slow things down tho
        message = f"{func.__name__} run time length: {end_time - start_time} seconds."
        with open("code_root/logs/program_times_log.txt", "a") as log_file:  # "a" opens the file in append mode
            log_file.write(message + "\n")
        
        return result #IDK kinda get it
    return time_analysis_wrapper

def log_to_file(message: str, file_path: str = "code_root/logs/program_times_log.txt"):
    with open(file_path, "a") as log_file:  # "a" opens the file in append mode
            log_file.write(message + "\n")
            
def xyz_input_auto_completer(promptstring, refList): #TODO this might mess up multi-time input 
    """For terminal interfaces only! Does not require capitalization to auto suggest
    Args:
        promptstring (string): _description_
        refList (list): _description_
    """
    # Define a list of autocomplete words.
    try:
        completer = WordCompleter(refList, ignore_case=True) #WHY ignore_care=True, allowing case-insensitive input bc some ref list entries may be capitalized, but dont want to make user have to capitalize input to get auto suggestion    
        user_input = prompt(promptstring, completer=completer)
        return user_input
    except Exception as e:
        print("Error during prompt:", e)

# Selection sort
# time complexity O(n*n)
# sorting by finding min_index

@timer
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

#TODO rename this sometime
def end_time_log_cap():
    arg = str(time.time())
    with open("code_root/logs/program_times_log.txt", "a") as log_file:  # "a" opens the file in append mode
        log_file.write("\n\n" + arg + "-------End of UPDATED Program-------" + "\n\n")
        