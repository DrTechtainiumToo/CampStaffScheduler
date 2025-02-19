from typing import Union
import json
from pathlib import Path

# Load configuration data from JSON, file should be structured with keys like "settings", "paths".
CONFIG_PATH = Path(__file__).parent / "settings_config.json"
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

# ================================
# Global Variables and Basic Information + any future settings
# ================================

# Settings for application behavior
settings_data: dict = config.get("settings", {})

SCHEDULER_MODE: str = settings_data.get("scheduler_mode", "SWAT")
"""what type of scheduling you will be doing, mainly just changes the files names for now"""
INTERFACE_TYPE: str = settings_data.get("interface_type", "terminal") 
"""option 1 is terminal, option 2 is web, option 3 is textual"""
MAX_ENTRY_ATTEMPTS: int = settings_data.get("max_entry_attempts", 3)
"""Max user input attempts for day in getting day value sequence, else goes to meme"""
GET_NEXT_DAY: bool = settings_data.get("get_next_day", False)
GET_DATE_AUTO: bool = settings_data.get("get_date_auto", True)
WEEK_COUNT_START_REF_DAY: str = settings_data.get("week_count_start_ref_day", "5/20")
"""must be m/d, must be a sunday, allow user to set a base datetime object, will be used as a date for the program to reference what week of camp it is."""

# Settings for internal behavior
UNAVAILABILITY_TASK: str = settings_data.get("unavailability_task", "Unavailable")
"""The value of the 'unavailable task"""
# NOTE WHAT DOES THIS MEAN? -> #WHY #BUG the unavailability value cant be int, gets changed in the program for some reason


# ================================
# File Locations and Paths
# ================================
paths_data = config.get("paths", {})

project_root = Path(paths_data.get("project_root", "code_root"))
backend_folder: str = paths_data.get("backend_folder")
core_folder: str = paths_data.get("core")
data_folder: str = paths_data.get("data_folder")
interface_folder: str = paths_data.get("interface_folder")
config_folder: str = paths_data.get("config_folder")
csv_data_folder = paths_data.get("csv_data_folder", "CSV Data Folder")
logs_folder = paths_data.get("logs_folder", "logs")
files: dict = paths_data.get("files", {})

program_time_log: str = project_root / logs_folder / "program_times_log.txt"
SWAT_NIGHT_CHORES_INFO_CSV: str = project_root / backend_folder / data_folder / csv_data_folder / files.get("swat_night_chores_info_csv")
SWAT_SCHEDULER_SPECIAL_TASKS_LIST_CSV: str = project_root / backend_folder / data_folder / csv_data_folder / files.get("swat_scheduler_special_tasks_list_csv")
SWAT_EMPLOYEE_INFO_CSV: str = project_root / backend_folder / data_folder / csv_data_folder / files.get("swat_employee_info_csv")
SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV: str = project_root / backend_folder / data_folder / csv_data_folder / files.get("swat_basic_tasks_list_for_scheduler_csv")

# Response constants ----------------------
responses_data = config.get("responses", {})

YES_ANSWERS: list[str] = responses_data.get("yes_answers", [])
NO_ANSWERS: list[str] = responses_data.get("no_answers", [])
MALE_ANSWERS: list[str] = responses_data.get("male_answers", [])
FEMALE_ANSWERS: list[str] = responses_data.get("female_answers", [])


# Time Values ----------------------

# Mapping days to numerical identifiers and vice versa
days_data = config.get("days", {})

DAYS: dict[str, int] = config.get("days", {})
DAYS_KEY_VALUE_INVERSE: dict[Union[str, int], str] = config.get("days_key_value_inverse", {})

# Time slot configurations
time_slots_data: dict[str,list[dict[str,bool]]] = config.get("time_slots", {})
time_slots_by_day = config.get("time_slots_by_day", {})

# Misc ----------------------
DUMB_MEME_1: str = config["misc"]["dumb_meme_1"]

# ================================
# Excel Output Settings
# ================================
EXCEL_CONFIG_PATH = Path(__file__).parent /"excel_output_settings.json"
with open(EXCEL_CONFIG_PATH, "r") as f:
   excel_config=json.load(f)

#NOTE WHY - Im using dictionaries bc Now, instead of importing each variable separately in my output module, I can simply import EXCEL_OUTPUT_SETTINGS.

#Excel Text Values Settings:
excel_text_values_settings = excel_config.get("excel_text_values_settings", {})

# -----------------------------------------------------------------------------
# Excel Formatting Settings (create formats later using workbook.add_format()) 
# -----------------------------------------------------------------------------
excel_formatting_settings = excel_config.get("excel_formatting_settings", {})

# -----------------------------------------------------------------------------
# Task Formatting Settings
# -----------------------------------------------------------------------------
task_format_dict = excel_config.get("task_format", {})
