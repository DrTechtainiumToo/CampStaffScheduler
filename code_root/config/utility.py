from colorama import Fore, Style
import time
from contextlib import contextmanager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os

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

#DONE rename this sometime
def log_conclusion_text():
    arg = str(time.time())
    with open("code_root/logs/program_times_log.txt", "a") as log_file:  # "a" opens the file in append mode
        log_file.write("\n\n" + arg + "-------End of UPDATED Program-------" + "\n\n")

def clear_log_file(file_path: str = "code_root/logs/program_times_log.txt"):
    """"# Check if the file exists and clear its contents."""
    log_file_path = "code_root/logs/program_times_log.txt"
    # Check if the file exists and clear its contents.
    if os.path.exists(log_file_path):
        with open(log_file_path, "w", encoding="utf-8") as f:
            f.truncate(0)  # This step is optional since "w" already clears the file.