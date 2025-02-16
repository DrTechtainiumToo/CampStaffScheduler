import time
from contextlib import contextmanager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
from code_root.config.settings import program_time_log

@contextmanager
def time_block(label, log_file_path = None):
    """with time_block("Example Task"): Code to be timed"""
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        message = f"{label}: {end - start} seconds"
        log_file_path = log_file_path if log_file_path else program_time_log
        with open(log_file_path, "a") as log_file:  # "a" opens the file in append mode
            log_file.write(message + "\n")    


#can disable in production enviroment
def timer(func):
    def time_analysis_wrapper(*args, **kwargs):
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        message = f"{func.__name__} run time length: {end_time - start_time} seconds."
        with open(program_time_log, "a") as log_file:  # "a" opens the file in append mode
            log_file.write(message + "\n")
        return result
    return time_analysis_wrapper

def log_to_file(message: str, log_file_path = None):
    log_file_path = log_file_path if log_file_path else program_time_log
    with open(log_file_path, "a") as log_file: 
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

#DONE rename this sometime -> log_conclusion_text()
def log_conclusion_text(log_file_path = None):
    log_file_path = log_file_path if log_file_path else program_time_log
    arg = str(time.time())
    with open(log_file_path, "a") as log_file:  # "a" opens the file in append mode
        log_file.write("\n\n" + arg + "-------End of UPDATED Program-------" + "\n\n")

def clear_log_file(log_file_path = None):
    """"# Check if the file exists and clear its contents."""
    # Check if the file exists and clear its contents.
    log_file = log_file_path if log_file_path else program_time_log
    if os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.truncate(0)  # This step is optional since "w" already clears the file.