# for formatting, black {source_file_or_directory}


from code_root.config.settings import (
    GET_NEXT_DAY,
    GET_DATE_AUTO,
    MAX_ENTRY_ATTEMPTS,
    WEEK_COUNT_START_REF_DAY,
    UNAVAILABILITY_TASK,
)
from code_root.config.utility import (
    end_time_log_cap, 
    timer
)
from code_root.backend.core.time_processes import (
    get_day_name,
    get_day_time_slots,
    timeSlotStandardizer,
    get_current_week
)
from code_root.backend.core.process import (
    employee_names, 
    employee_genders
)
from code_root.backend.core.employees import (
    EmployeeManager,
    EmployeeAvailabilityLogic,
    instantiate_employees,
)
from code_root.backend.core.tasks import (
    TaskRecommender,
    instantiate_tasks,
)
from code_root.interface.terminal.terminal_ui_logic import (
    TaskUI,
    user_adds_additonal_tasks_ui,
    TaskRecommendationUI,
    get_date_value_ui,
    modify_schedule_ui,
    user_decide_modify_times_ui,
    EmployeeAvailabilityUI,
)
from code_root.backend.core.scheduler import instantiate_and_run_scheduler
from code_root.backend.core.output_schedule import OutputSchedule
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

printIntroSequence()

# Get day ---------------------
date_value = get_date_value_ui(get_date_auto=GET_DATE_AUTO, get_next_day=GET_NEXT_DAY, max_entry_attempts=MAX_ENTRY_ATTEMPTS)
day_name = get_day_name(date_value)
day_time_slots = get_day_time_slots(date_value)
print(f"Will generate a schedule for {day_name}.\n")

#Get week - For knowing when to load certain employees (counsler mode?)
camp_week = get_current_week(WEEK_COUNT_START_REF_DAY, GET_NEXT_DAY)

# timeslot modificaiton -------------------

if user_decide_modify_times_ui(day_time_slots):
    day_time_slots = modify_schedule_ui(day_time_slots)
else:
    print("Times confirmed.")

# -------- standardize the timeslots
time_slot_labels = list(
    day_time_slots[0].keys()
)
index_to_time_slot_map, time_slot_to_index_map = timeSlotStandardizer(time_slot_labels)

# ----------- Employees ---------------------

# Employee Info Input #TODO merge this with availbility UI eventually for cleaner code

employee_manager = EmployeeManager()  # Assuming this is already defined
availability_logic = EmployeeAvailabilityLogic(employee_manager)
availability_ui = EmployeeAvailabilityUI(availability_logic)
employee_manager = instantiate_employees(
    employee_manager, 
    time_slot_labels, 
    employee_names, 
    employee_genders
)
availability_ui.user_input_employee_unavailabilities(time_slot_labels, time_slot_to_index_map, index_to_time_slot_map)

# --------------------------------------- Tasks User Input

# --------------------- Additional Tasks
additional_tasks = user_adds_additonal_tasks_ui() #move into task reccomender (thus before validation but after reccomendation), 
#actually maybe make it a feature in the modification that can add more??
#and rename class to be like task editing etc

task_manager, default_tasks_dictionary, defaultTasksVarNamesList = instantiate_tasks(
    additional_tasks,
    time_slot_labels
    )

task_ui = TaskUI(task_manager)

task_recommender = TaskRecommender(day_name)
task_recommendation_ui = TaskRecommendationUI(task_recommender, time_slot_labels)

task_recommender.recommend_tasks(default_tasks_dictionary)
task_recommendation_ui.edit_selected_tasks(defaultTasksVarNamesList) #maybe change to edit reccomended tasks?? IDK
task_recommender.handle_missing_details(task_recommendation_ui.collect_missing_details)

tasks_dictionary, task_names_list = task_recommender.return_selected_tasks_for_day()
days_tasks = [tasks_dictionary] #keep so can add more stuff if needed

start_algo = time.perf_counter()
# -------------------------------- Scheduling algo
instantiate_and_run_scheduler(
    time_slot_to_index_map, 
    index_to_time_slot_map, 
    time_slot_labels, 
    days_tasks, 
    tasks_dictionary, 
    task_manager, 
    employee_manager
)

#TODO learn how to use timeit 
# ------------------------------------ Output 
end_algo = time.perf_counter()
algo_run_time = end_algo-start_algo
start_excel = time.perf_counter()

output_schedule = OutputSchedule(time_slot_labels, employee_names, employee_manager.employees)
output_schedule.excel(
    employee_manager,
    task_manager, 
    algo_run_time,
    GET_NEXT_DAY, 
    WEEK_COUNT_START_REF_DAY,
    UNAVAILABILITY_TASK,
)

end_excel = time.perf_counter()

end_time_log_cap()
excel_res = end_excel-start_excel
print("Algo:", (algo_run_time))
print("Excel:", (excel_res))
print("Program finished")

profiler.disable()
stats = pstats.Stats(profiler)
#profiler.print_stats(sort='cumtime')
stats.dump_stats('profile.prof')