# for formatting, black {source_file_or_directory}

# aslo very interesting
# https://github.com/Textualize/textual

#https://www.youtube.com/watch?v=JrGFQp9njas

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
from config.utility import (
    end_time_log_cap, 
    timer
)
from backend.core.time_processes import (
    get_day_name,
    get_day_time_slots,
    timeSlotStandardizer,
)
from backend.core.process import employeeNamesList, employeeGenderList
from backend.core.employees import (
    EmployeeManager,
    EmployeeAvailabilityLogic,
    Employee,
    instantiate_employees,
)
from backend.core.tasks import (
    TaskManager,
    TaskDataConverter,
    TaskRecommender,
    instantiate_tasks,
)
from interface.terminal.terminal_ui_logic import (
    TaskUI,
    user_adds_additonal_tasks_ui,
    TaskRecommendationUI,
    get_date_value_ui,
    modify_schedule_ui,
    user_decide_modify_times_ui,
    EmployeeAvailabilityUI,
    describe_dynamic_time_slot_qeues
)
from backend.core.scheduler import instantiate_and_run_scheduler
from backend.core.output_schedule import OutputSchedule
import time
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
    
def display_menu(options):
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

def get_user_input(prompt):
    return input(prompt)


#make a loop & menu where can edit settings and shit up here.
# TODO make settings interface - in UI

# ---------------------------- main program

@timer
def printIntroSequence():
    print(
        "\n-----------------------------------------------------------------------------------------------\n\n\n\LOADING...\n"
    )
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
    print(
        "\nDedication:\nThis program is dedicated to my SWAT Coordinator: Slips (Abby Lucksinger),\nand all the SWATTIES of the summer of 2023 who I am glad to call my friends\n\nDeveloped by Yacht (Andrew Dybala)\nS.W.A.T. Session 1 and Session 2, Summer of 2023.\nBLHS & University of Colorado Boulder"
    )
    print(
        "\n-----------------------------------------------------------------------------------------------"
    )
    # time.sleep(0.5) #alt way to wait

printIntroSequence()

# Get day ---------------------
date_value = get_date_value_ui(get_next_day, get_date_auto, max_entry_attempts=3)
day_name = get_day_name(date_value)
day_time_slots = get_day_time_slots(date_value)
print(f"Will generate a schedule for {day_name}.\n")

# timeslot modificaiton -------------------

if user_decide_modify_times_ui(day_time_slots):
    day_time_slots = modify_schedule_ui(day_time_slots)
else:
    print("Times confirmed.")

# -------- standardize the timeslots
dayTimeSlotsKeysList = list(
    day_time_slots[0].keys()
)  # for when i just want to diplay the keys / dates. will make easier to change stuff later too. BEWARE: Is static tho and does not updates with the acutaly DICT
dayTimeSlotsStandardizedNtS, dayTimeSlotsStandardizedStN = timeSlotStandardizer(dayTimeSlotsKeysList)

# ----------- Employees ---------------------

# Employee Info Input #TODO merge this with availbility UI eventually for cleaner code

employee_manager = EmployeeManager()  # Assuming this is already defined
availability_logic = EmployeeAvailabilityLogic(employee_manager)
availability_ui = EmployeeAvailabilityUI(availability_logic)
employee_manager = instantiate_employees(
    employee_manager, dayTimeSlotsKeysList, employeeNamesList, employeeGenderList
)
availability_ui.user_input_employee_unavailabilities(dayTimeSlotsKeysList, dayTimeSlotsStandardizedStN, dayTimeSlotsStandardizedNtS)

# --------------------------------------- Tasks User Input

# --------------------- Additional Tasks
additional_tasks = user_adds_additonal_tasks_ui() #move into task reccomender (thus before validation but after reccomendation), 
#actually maybe make it a feature in the modification that can add more??
#and rename class to be like task editing etc

task_manager, defaultTasksDictionary, defaultTasksVarNamesList = instantiate_tasks(
    additional_tasks,
    dayTimeSlotsKeysList
    )

task_ui = TaskUI(task_manager)

task_recommender = TaskRecommender(day_name)
task_recommendation_ui = TaskRecommendationUI(task_recommender, dayTimeSlotsKeysList)

task_recommender.recommend_tasks(defaultTasksDictionary)
task_recommendation_ui.edit_selected_tasks(defaultTasksVarNamesList) #maybe change to edit reccomended tasks?? IDK
task_recommender.handle_missing_details(task_recommendation_ui.collect_missing_details)

tasks_dictionary, task_names_list = task_recommender.return_selected_tasks_for_day()
daysTasks = [tasks_dictionary] #keep so can add more stuff if needed

start_algo = time.perf_counter()
# -------------------------------- Scheduling algo
instantiate_and_run_scheduler(
    dayTimeSlotsStandardizedStN, 
    dayTimeSlotsStandardizedNtS, 
    dayTimeSlotsKeysList, 
    daysTasks, 
    tasks_dictionary, 
    task_manager, 
    employee_manager
)

#TODO learn how to use timeit 
# ------------------------------------ Output 
end_algo = time.perf_counter()

start_excel = time.perf_counter()
output_schedule = OutputSchedule(dayTimeSlotsKeysList,employeeNamesList,employee_manager.employees)
output_schedule.excel(employee_manager, task_manager)
end_excel = time.perf_counter()

end_time_log_cap()
algo_res = end_algo-start_algo
excel_res = end_excel-start_excel
print("Algo:", (algo_res))
print("Excel:", (excel_res))
print("Program finished")

profiler.disable()
stats = pstats.Stats(profiler)
profiler.print_stats(sort='cumtime')
stats.dump_stats('profile.prof')