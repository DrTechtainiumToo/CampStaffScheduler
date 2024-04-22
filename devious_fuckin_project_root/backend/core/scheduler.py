from config.utility import timer
import random
from backend.core.tasks import TaskManager
from backend.core.employees import EmployeeManager, Employee
import logging
from typing import Any

class Schedule:  # hmm learning concpet diff between ref blueprint and inst obj if inst then will refer to inst? what if multiple
    def __init__(self) -> None:
        self.time_slot_task_queues: dict[str, Schedule.DynamicTimeSlotQueue] = {}
        self.failed_to_schedule: list[str] = []
        # wut if just used a class attr for tasks_dict and set it for all the queues to ref?

    def generate_schedule(self,
        time_slot_to_index_map: dict[str, int], 
        index_to_time_slot_map: dict[int, str], 
        time_slot_labels: list[str], 
        days_tasks: list[dict], 
        tasks_dict: dict[str, TaskManager.Task], 
        task_manager: TaskManager, 
        employee_manager: EmployeeManager,
        current_schedule: Any) -> None:
        # would having length of day be predefined actually give notacible improv???? no
        self.generate_time_slot_queues(time_slot_labels, days_tasks, tasks_dict, time_slot_to_index_map)
        
        for queue in self.time_slot_task_queues:
            self.time_slot_task_queues[queue].assign_tasks(
                time_slot_to_index_map,
                index_to_time_slot_map,
                task_manager,
                employee_manager,
                current_schedule
            )
        # run all the queues until finished

    def generate_time_slot_queues(self, 
        time_slot_labels: list[str], 
        days_tasks: list[dict], 
        tasks_dict: dict[str, Any],
        time_slot_to_index_map: dict[str, int]) -> None:
        
        # original generation of timeslots and assign to dict, plus populating the queues, #INITALIZATION OF VALUES
        for time_slot in time_slot_labels:
            self.time_slot_task_queues[time_slot] = Schedule.DynamicTimeSlotQueue(time_slot, days_tasks, time_slot_to_index_map)
            self.time_slot_task_queues[time_slot].populate_queue(tasks_dict)

    class DynamicTimeSlotQueue:
        def __init__(self, time_slot_name: str, days_tasks: list[dict], time_slot_to_index_map: dict[str, int]) -> None:
            self.queue: list[str] = []
            self.days_tasks: list[dict] = days_tasks
            self.time_slot: str = time_slot_name
            self.time_slot_num: int = time_slot_to_index_map[time_slot_name]
            self.length: int = 0 # num tasks in queue #updated at qeue population
            self.windowed_tasks_list: list[str] = [] #TODO figure out what to do with this, also add old tasks to front, refactor by due? date??
            self.remaining_tasks: list[str] = []
            
            
        @timer
        def populate_queue(self, tasks_dict: dict[str, TaskManager.Task]):  # maybe change to generate later idk, semantics
            def find_tasks_in_time_slot(days_tasks: list[dict], searchVal: str) -> list[str]:
                """Only dicts inside the input list!"""
                tasks_with_start_time: list[str] = []
                for iterable in days_tasks:  # takes care of facts that the days_tasks is a list and tasks are in [0], aka days_tasks = [tasks to acess]
                    for key, instance in iterable.items(): #NOTE why is key constant? 
                        # Assuming each value has a 'start_time' list and a 'start_times_iter' attribute bc iter is assigned 0 for all objs, and startime should be filled, esp since validated all task details earlier in program.
                        if (instance.start_time and 0 <= instance.start_times_iter < len(instance.start_time)):  #NOTE even needed, literally just doing an abstract version of code below. #to account for the fact that there may be multiple start times and are comparing to the right startime.
                            # Compare searchVal with the current start_time value
                            if (searchVal == instance.start_time[instance.start_times_iter]):
                                instance.start_times_iter += 1
                                tasks_with_start_time.append(key)
                            #else: logging.warning(f"ERROR | {searchVal} not in {key}'s startime: {instance.start_time[instance.start_times_iter]}")
                        #else: logging.warning(f"ERROR | len instance.start_times_iter: {instance.start_times_iter}")
                    #else: logging.warning(f"ERROR | prob an empty list or startime is out of bounds at: for key, instance in dataGrouping.items()")
                return tasks_with_start_time
            
            # PROBLEM, what if the duration or num of people is dynamically generated at assignment bc it depends on what other things have been added. in part what tier is for too
            def sort_tasks_by_duration(tasks: list[str]) -> list[str]:
                tasks.sort(key=lambda task: tasks_dict[task].duration, reverse=True)
                return tasks
            
            # Sort by tier last, bc some large tasks may have to be scheduled last but by dur they wouldn't
            def sort_tasks_by_tier(tasks: list[str]) -> list[str]:
                tasks.sort(key=lambda task: tasks_dict[task].tier)
                return tasks

            # TODO this will prob need quite a bit of work
            def collect_windowed_tasks(tasks: list[str]) -> None:  
                # NOTE shortcoming - wut if optinal tasks have greater duration???????? if duration longer than optinal window then no longer an optional task?, really less optional task & more like windowedTask
                # assume since already sorted by duration, that if resort all the optional ones to back of list, the long duration ones should still be sorted first, and this put at the front of the list
                # of optional tasks, thus no need to sort the optionals by duration again
                # maybe make if not due in this period then move to end - more for assignment-if was due in this period during the population stage would just be a normal task then, eh? or if no due this period than can leave, only optimize if need to????
                for task in tasks:
                    if "Yes" == getattr(tasks_dict[task], "window"):
                        self.windowed_tasks_list.append(task)

            tasks_matching_start_time = find_tasks_in_time_slot(self.days_tasks, self.time_slot)
            tasks_by_duration = sort_tasks_by_duration(tasks_matching_start_time)
            tasks_by_tier = sort_tasks_by_tier(tasks_by_duration)
            collect_windowed_tasks(tasks_by_tier)
            self.queue = tasks_by_tier

        @timer
        def assign_tasks(
            self,
            time_slot_to_index_map: dict[str, int],
            index_to_time_slot_map: dict[int, str],
            task_manager: TaskManager,
            employee_manager: EmployeeManager,
            Schedule: Any,
            employee_info=None,
            ) -> None:
            avail_employees_in_period = employee_manager.get_available_employees(self.time_slot)

            @timer
            def assign_task(task_name: str, index_to_time_slot_map):
                assigned_people: dict[str, Any] = {}
                # TODO evantually redo this and figure out how to implement how many certs you need. Also maybe make a table with prelisted number of people with certs, might be faster

                def generate_list_of_eligible_employees() -> Any:  # need to rename this
                    task_reqs = task_manager.tasks[task_name].get_task_requirements()  # should be *task employee req
                    # TODO FOR NOW - justs assigns all the min number of people with things that meet reqs, even after reqs have technically been filled
                    if (task_reqs):  # truthy if contain at least one item, Falsey if empty. If checks if true.
                        employees_with_req_traits = employee_manager.get_employees_with_traits(**task_reqs)  # WHY & LEANRING CONCEPT **unpack dictionary into keyword arguments bc function expects them
                    else:  # then no employees with special traits needed, can pick any
                        employees_with_req_traits = {}
                    # get_personnel_with_task_critical_traits
                    # get who is available first -- do this first or get qualified people??? hmmm, This first cus have to search multiple for qualis and better to have to search less
                    # then do the rest of these if nessecary
                    # Then do normal people, skip if amount from special has been filled alread]
                    return employees_with_req_traits

                def generate_assignment_probabilities(removeLater):
                    assignment_probbability = (
                        {}
                    )  # employee | base prob value | modifiers ??? how implement???
                    # Figure shit out later
                    # should return employee chosen
                    # lower probbs if certs in other things and tasks with those certs are needed in the period
                    return removeLater

                def update_data(name: str, time_slots: list[str]) -> None:
                    # assigned_people[name] = None #TODO fix #POTENTIAL TO  CAUSE BUG hmm is this working right? so doesn't assing same people twice?? #ok if do this first, but then do total unavail. Proab could optimize here
                    # for multi duration tasks - rethink how to efficently implement this later.
                    employee_manager.set_employee_availability(
                        name, time_slots
                    )
                    employee_manager.assign_task_to_employee(
                        name, task_name, time_slots
                    )  # TODO see if can take list like for employee availability, for multi duration args???
                    task_manager.tasks[task_name].assign_employee_to_task(
                        time_slots, name
                    )
                    del avail_employees_in_period[name]
                    if (employees_with_req_traits):  # bc otherwise will delete an empty dict and cause an error
                        del employees_with_req_traits[name]

                def calculate_time_slots_for_duration(task_name: str) -> list[str]:
                    """Returns a list of time slot identifiers based on the duration of a task"""
                    duration = int(task_manager.tasks[task_name].duration) 
                    # WHY int - Ensure duration is an integer bc dictionary to convert value will onyl take integer
                    #also if put back string, it would compare # characters in if function below.
                    
                    if duration > 1:
                        # Check the duration of the task

                        # Calculate numeric timekey values for the duration of the task
                        duration_slots_numeric: list[int] = [self.time_slot_num + i for i in range(duration)] # good list comprehension

                        # Convert numeric values back to string representations
                        duration_slots_strings: list[str] = [
                            index_to_time_slot_map[num]
                            for num in duration_slots_numeric
                            if num in index_to_time_slot_map
                        ]

                        return duration_slots_strings
                    else:
                        # If duration is 1, return the current time slot in a list 
                        # #TODO update why a list? bc converter only takes lists?
                        return [self.time_slot]

                def assign_employees_to_task(
                    employees_with_req_traits: Any,
                    task_name: str,
                    time_slots: list[str],
                ) -> None:
                    # TODO write logic for TASKS THAT ARE DEPENDENT ON NUMBER OF EMPLOYEES BASED ON OTHER TASKS
                    # TODO once get code for how many certs to assign, then make it count until it has fulfilled it.

                    # first assign special trait employees first
                    def choose1() -> str:
                        chosen_name_local = random.choice( #TODO can later replace with prob logic
                            list(employees_with_req_traits.keys())
                        )
                        return chosen_name_local
                        
                    # also interesting, a suggestion by GPT4 - employees_with_req_traits = set(employees_with_req_traits_local.keys()) & set(avail_employees_in_period.keys()) - set(assigned_people.keys())

                    if employees_with_req_traits:  # check if already assigned or unavailable
                        while True:
                            chosen_name = (choose1()) # find someone who isn't been assigned or unavailable
                            if (
                                chosen_name not in assigned_people
                                and chosen_name not in avail_employees_in_period
                            ):  # use all??
                                break  # Break the loop if a suitable / available employee is found, #TODO implent find someone with right reqs???
                        update_data(chosen_name, time_slots)

                    else:
                        attribute = getattr(task_manager.tasks[task_name], "min_num_people_needed")
                        if attribute == "unassigned_employees":
                            attribute = len(avail_employees_in_period)
                        ppl_needed: int = int(attribute)  # need to check if an if or not
                        while (ppl_needed > 0):
                            while True:
                                # callback? cant add more so maybe have accept its short, or have it retrace and be able to merge some tasks??
                                try:  # NOTE temporary solution
                                    chosen_name = random.choice(list(avail_employees_in_period.keys()))
                                except:
                                    # error handle logic here?
                                    continue
                                if chosen_name not in assigned_people:
                                    update_data(chosen_name, time_slots)
                                    ppl_needed -= 1
                                    break

                        # HMM this is also an interesting implementation: available_candidates = set(avail_employees_in_period.keys()) - set(assigned_people.keys())
                        # check if already assigned or unavailable
                        # update with anti-cert-use-up code later
                        # normal random assignment
                    # then do the normal
                    # check if in avail employees for period, would slow down if didnt have to but dict means fast look up.
                    # temp prinout to see if assigning to tasks:
                
                
                time_slots_for_task = calculate_time_slots_for_duration(task_name) #Time slot range for task
                employees_with_req_traits = generate_list_of_eligible_employees()
                assign_employees_to_task(
                    employees_with_req_traits, task_name, time_slots_for_task
                )
                
                #special process for windowed tasks -> moves task to next queue acc to freq attr
                if task_name in self.windowed_tasks_list:
                    required_assignments = int(task_manager.tasks[task_name].frequency) 
                    current_assignments = sum(1 for people in task_manager.tasks[task_name].assigned_to.values() if people) #GPT had to help me on this one
                    if current_assignments < required_assignments:
                        next_queue_key = index_to_time_slot_map[self.time_slot_num + 1]
                        Schedule.time_slot_task_queues[next_queue_key].windowed_tasks_list.append(task_name)
                        Schedule.time_slot_task_queues[next_queue_key].queue.append(task_name)
                        
                    #else just stays in this queue like normal, doesn't go to next stage
                    #NOTE Moved out of update data bc otherwise ever person assigned goes thru this and adds a duplicate to next queue
            
            def roll_over_tasks(task: str) -> None:
                """roll over remaining windowed tasks"""
                
                #easier to check here, than keeping lists, and removing any STATIC or non windowed tasks
                start_index = self.queue.index(task)
                
                #TODO what if there is a windowed that was due this period but didn't get shceduled?? how do I filter it out?
                filtered = [task for task in self.queue[start_index:] if task in self.windowed_tasks_list] #-1 to be inclusive of task
                self.remaining_tasks = filtered
                next_time_slot_index: int = self.time_slot_num + 1
                try:
                    next_time_slot_key: str = index_to_time_slot_map[next_time_slot_index]
                    Schedule.time_slot_task_queues[next_time_slot_key].queue.extend(self.remaining_tasks)
                    Schedule.time_slot_task_queues[next_time_slot_key].windowed_tasks_list.extend(self.remaining_tasks)
                except KeyError:
                    logging.warning(f"At {self.time_slot}: Next time slot does not exist in the current_schedule. Adding {self.remaining_tasks} to failed tasks.")
                    Schedule.failed_to_schedule.extend(self.remaining_tasks)
                    
            #prob slowest part of code, well second, after i add in the probbabilites
            for task in self.queue: #NOTE Shortcoming -what if task that trips this reqs 4, but next one reqs 2, and there are two employees avail, but when populating queue tasks are sorted by duration from max->min
                if avail_employees_in_period: 
                    ppl_needed = task_manager.tasks[task].min_num_people_needed
                    if ppl_needed.isdigit():
                        if (len(avail_employees_in_period)+1 >= int(ppl_needed)): 
                            if getattr(task_manager.tasks[task], "window", None) != "Yes": #if Non windowed task #TODO make constants for all csv values so can easy change,
                                #and maybe eventally the attr names themselves
                                assign_task(task, index_to_time_slot_map)
                            elif "Yes" == getattr(task_manager.tasks[task], "window") and ((int(task_manager.tasks[task].duration)) <= task_manager.recalculate_distance_to_deadline(task, self.time_slot, time_slot_to_index_map)): #IF statement before to prevent non windowed from getting distance calced (error)                                
                                assign_task(task, index_to_time_slot_map)
                            else:
                                logging.warning(f"At {self.time_slot}: Not enough time remaining to current_schedule {task} because duration would put it past it's deadline. Adding to failed tasks. Or a STATIC task got thru somehow")
                                Schedule.failed_to_schedule.append(task) #TODO deal with later
                                continue
                        elif task_manager.tasks[task].window: #Only rolls over the windowed tasks NOT the STATIC ones, 
                            roll_over_tasks(task)
                        else: #Non windowed task just get ignored, goes to
                            roll_over_tasks(task) #make sure rest gets captured, before break
                            break
                    else:
                        assign_task(task, index_to_time_slot_map) # for uncalulated var / non int attrs
                else: #Default
                    roll_over_tasks(task) #make sure rest gets captured, before break
                    break
            


# need to then reorder selected tasks by TIER and duration, how to make sure stuff does not get overwritten twice???????
# Then go to next criteria or assign to people and set durations. once done set all other durations to blank???? idk
# recursive function to look through all the lists and shit in the days_tasks and find those that start at time, next duration, then do by tiers


@timer
def instantiate_and_run_scheduler(
    time_slot_to_index_map: dict[str, int],
    index_to_time_slot_map: dict[int, str],
    time_slot_labels: list[str],
    days_tasks: list[dict],
    tasks_dict: dict[str, TaskManager.Task],
    task_manager: TaskManager,
    employee_manager: EmployeeManager,
) -> None:
    
    current_schedule = Schedule()
    current_schedule.generate_schedule(
        time_slot_to_index_map,
        index_to_time_slot_map,
        time_slot_labels,
        days_tasks,
        tasks_dict,
        task_manager,
        employee_manager,
        current_schedule
    )

