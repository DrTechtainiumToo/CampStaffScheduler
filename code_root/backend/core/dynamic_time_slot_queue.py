from code_root.config.utility import timer
import random
import logging
from code_root.backend.core.tasks import TaskManager
from code_root.backend.core.employees import EmployeeManager
from code_root.backend.core.dynamic_time_slot_queue import TaskManager
from typing import Any, Union


class DynamicTimeSlotQueue:
    
    """
    # A queue representing tasks assigned to a specific time slot.
    
    The `DynamicTimeSlotQueue` class manages the assignment of tasks to employees based on various
    criteria such as duration, availability, and task requirements, with the ability to roll over
    unassigned tasks to the next time slot for scheduling.
    """
    
    static_task_count_total = 0 # TODO review if needed Tracks total assigned tasks across instances
    
    def __init__(self, time_slot_name: str, days_tasks: list[dict], time_slot_to_index_map: dict[str, int]) -> None:
        """
        Initializes a dynamic time slot queue.

        Attributes:
        - queue: List of task names assigned to this time slot.
        - days_tasks: Tasks distributed across different days.
        - time_slot: The string identifier for this time slot.
        - time_slot_num: Integer representation of the time slot index.
        - length: Number of tasks in the queue (updated during population).
        - windowed_tasks_list: List of tasks with flexible scheduling.
        - remaining_tasks: List of tasks that need to be rescheduled.
        - failed_to_schedule: List of tasks that could not be assigned.
        - next_time_slot_key: The next time slot key for rolling over tasks.
        """
        
        self.queue: list[str] = []
        self.days_tasks: list[dict] = days_tasks
        self.time_slot: str = time_slot_name
        self.time_slot_num: int = time_slot_to_index_map[time_slot_name]
        self.length: int = 0 # num tasks in queue #updated at qeue population
        self.windowed_tasks_list: list[str] = []
        self.remaining_tasks: list[str] = []
        self.failed_to_schedule: list[str] = []
        self.next_time_slot_key: Union[str, None] = None
    
    def _find_tasks_in_time_slot(self, days_tasks: list[dict], searchVal: str) -> list[str]:
        """Identifies tasks that fall within the current time slot. Only dicts inside the input list!"""
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
    
    def _sort_tasks_by_duration(self, tasks: list[str], tasks_dict: dict[str, TaskManager.Task]) -> list[str]:
        """Sorts tasks by their duration, prioritizing longer tasks."""
        tasks.sort(key=lambda task: tasks_dict[task].duration, reverse=True)
        return tasks
    
    def _sort_tasks_by_tier(self, tasks: list[str], tasks_dict: dict[str, TaskManager.Task]) -> list[str]:
        """Sorts tasks by their tier, prioritizing higher-importance tasks."""
        tasks.sort(key=lambda task: tasks_dict[task].tier)
        return tasks
    
    def _collect_windowed_tasks(self, tasks: list[str], tasks_dict: dict[str, TaskManager.Task]) -> None:  
        # NOTE shortcoming - wut if optinal tasks have greater duration???????? if duration longer than optinal window then no longer an optional task?, really less optional task & more like windowedTask
        # assume since already sorted by duration, that if resort all the optional ones to back of list, the long duration ones should still be sorted first, and this put at the front of the list
        # of optional tasks, thus no need to sort the optionals by duration again
        # maybe make if not due in this period then move to end - more for assignment-if was due in this period during the population stage would just be a normal task then, eh? or if no due this period than can leave, only optimize if need to????
        for task in tasks:
            if "Yes" == getattr(tasks_dict[task], "window"):
                self.windowed_tasks_list.append(task)
                
    @timer
    def populate_queue(self, tasks_dict: dict[str, TaskManager.Task]):  # maybe change to generate later idk, semantics

        tasks_matching_start_time = self._find_tasks_in_time_slot(self.days_tasks, self.time_slot)
        # PROBLEM, what if the duration or num of people is dynamically generated at assignment bc it depends on what other things have been added. in part what tier is for too
        tasks_by_duration = self._sort_tasks_by_duration(tasks_matching_start_time, tasks_dict)
        # Sort by tier last, bc some large tasks may have to be scheduled last but by dur they wouldn't
        tasks_by_tier = self._sort_tasks_by_tier(tasks_by_duration, tasks_dict)
        self._collect_windowed_tasks(tasks_by_tier, tasks_dict)
        self.queue = tasks_by_tier
        
        queue = set(self.queue)
        windowed_tasks = set(self.windowed_tasks_list)
        current: int = DynamicTimeSlotQueue.static_task_count_total
        DynamicTimeSlotQueue.static_task_count_total = current + len(list(queue - windowed_tasks))
        

    def _calc_time_slots_for_duration(self, task_name: str, task_manager, index_to_time_slot_map: dict[int, str]) -> list[str]:
        """Returns a list of time slot identifiers based on the duration of a task"""
        duration = int(task_manager.tasks[task_name].duration)
        # WHY - Convert to int so can use in range() in list comprehension, also so can compare to integers
        
        if duration > 1:

            # Calculate numeric timekey values for the duration of the task
            duration_slots_numeric: list[int] = [self.time_slot_num + i for i in range(duration)]

            # Convert numeric values back to string representations
            duration_slots_strings: list[str] = [
                index_to_time_slot_map[num]
                for num in duration_slots_numeric
                if num in index_to_time_slot_map
            ]

            return duration_slots_strings
        else:
            # If duration is 1, return the current time slot in a list. Assumes duration is 1
            
            #TODO update why a list? bc converter only takes lists?
            return [self.time_slot]      
  
    #WIP              
    def _generate_assignment_probabilities(self, removeLater):
        """LITERALLY JUST FIGURING OUT ASSIGNMENT ORDER, also responsible for randomization"""
        
        #task reqs mock: 
        # Task: 'swimming'
        # (Attr) certs: {'lifeguard' : 2, 'ropes: 4'}  ('cert': num needed)

        #General List
        #List Construction
        
        def _create_list_critical_employees():
            pass
            
        def _create_list_generic_employees():
            pass
            
        #Function for List Creation:   
        def _create_employee_assignment_list() -> tuple[list[str],list[str]]:
            
            generic_emp = _create_list_generic_employees()
            certified_emp = _create_list_critical_employees()
            
            return certified_emp, generic_emp
        
        certified_emp, generic_emp = _create_employee_assignment_list()
        
        def _reorder_employee_by_preferences(certified_emp: list[str], generic_emp: list[str]): 
            certified_emp
            generic_emp
            
            #get pref and the somehow reorder
            
            #Reordering Based on Preferences
            #Preference Scoring & Sorting
            #got position maybe????? of enjoyment??? idk 
        
        #randomize first, then do by pref - thus all assignment funciton all has to do it go through the list
        #seperate reorder by pref and making sure its random, how do i not unessecarily reorder it more times than I need to?
        
        final_list = _reorder_employee_by_preferences()
        #Random Selection within Bands
        #To maintain fairness and inject some level of randomness (while still meeting task requirements):
        #Random Selection within Bands: Within groups of similarly-preferred employees, you could randomize assignments to avoid any deterministic bias. This could be done using random shuffling within subgroups who have the same preference score.

        #what if instead of probabilites jsut do list. 
        # Bc cant leave it up to chance that a lifegaurd gets assigned to a water activity (now which lifegaurd can be randomized for fairness)
        #and then reorganized by the preferences of the people for the activites, such as if activity in prefs then +1 position in queue? (assuming not in no1 spot already)
        #maybe resort among ppl who have certs and thus nessecary to task and people who don't. 
        # so two seperate lists thus can resort each list by pref of indvidual person for activity once you have the correct ordering of ppl you need for the task
        # need think how to make this modular
        
        # get_personnel_with_task_critical_traits
        # get who is available first -- do this first or get qualified people??? hmmm, This first cus have to search multiple for qualis and better to have to search less
        # then do the rest of these if nessecary
        # Then do normal people, skip if amount from special has been filled alread
        
        return removeLater

    #TODO WIP 
    def _generate_list_of_eligible_employees(
        self,
        avail_employees_in_period: set[str],
        time_slots_for_task: list[str],
        task_manager: TaskManager,
        employee_manager: EmployeeManager,
        task_name: str
        ) -> set[str]:  
        """Generates a list of employees eligible for task assignment."""
        #Uses and returns sets for fast membership checks during assignment.
        #Gets the ppl with right certs, right availbilites etc, gets the eligible ppl for the task
        #NOTE wouldn't it jsut be faster, besides duration maybe. it would be faster to determine all the combinable reqs and then all() that way we only use one for loop. Plus the all() is in c so very fast
        #TODO for future optimization, first figure out how to get all the different constraints indvidually then can figure out how to optimize and package most effectivley from there
        
        #Set default set to reference for filter operations
        filtered_emp: set[str]= avail_employees_in_period

        #FILTER 0.5 - Filter for gender if it's a requirement
        gender_reqs: dict[str] = task_manager.get_task_gender_reqs(task_name)
        if 'gender' in gender_reqs: #NOTE another reason why i should make the csv sheet values and headers standardized etc, so can easily change condiitonals like this from highlevel in program and thus dont have to go through all the statements 
            gender_desired = gender_reqs['gender']
            filtered_for_gender = {employee for employee in filtered_emp
            if employee_manager.employees[employee].gender == gender_desired}
            del gender_reqs['gender'] # Clean up the requirements for subsequent processing
            
            filtered_emp: set[str] = filtered_for_gender
            # WHY: Reassigning to the original list ensures consistency in subsequent references.
            # Avoids potential issues with modifying a list being iterated over.
        
        #FILTER 1 - If multi-duration task, check and filter to see who is available for the whole task duration
        if len(time_slots_for_task) > 1:
            emp_filtered_duration = {
                employee for employee in filtered_emp 
                if all(employee_manager.employees[employee].availability.get(time_slot, False) 
                    for time_slot in time_slots_for_task
                    )
            }
            filtered_emp = emp_filtered_duration
        
        #IGNORE for now bc could limit ppl who i draft for certs
        # Anti CO task coninciding / concurrent scheduling filter, or anti CO  
        if task_manager.tasks[task_name].anti_co_concurrent:
            pass #TODO finish
            #Filter out one co counsler per pair, on tasks must / can have only one co counsler and the other needs to do something else
            #For example, resthour or night off #TODO DOUBLE Check logic and filter is what i mean it to be
            #TODO make a get_co method                  
                    
        # ANTI sequential feature  
        #NOTE anti sequential and at_least_once logic implementation very similar/  maybe can merge?
        if task_manager.tasks[task_name].anti_sequential: #make setting CONST
            #Filter out person who has had task assigned last period. So person cannot get task two periods in a row (aka sequentially)
            emp_already_assigned = {employee for employee in task_manager.tasks[task_name].assigned_to[self.time_slot]}
            for employee in emp_already_assigned:
                filtered_emp.discard(employee)
        
        #Filter 1.5 - #If is a task that everyone must be assigned once.
        #BUG #ISSUE #NOTE problem how many people to assign in period? can have problem if just fills up the rest? or gives everyone offs at the beginning of the day
        #Needs to be generally well distibuted
        #TODO finish
        if task_manager.tasks[task_name].at_least_once_per_person:
            # TODO prob need to make so at top of every windowed tasks list that rolled over (relative importance?)
            #Filter available people who haven't had the task assigned yet AT ANY TIME
            ppl_yet_to_get_task = set(filtered_emp) - set(task_manager.tasks[task_name].assigned_to.values())
                # WHY: Using set subtraction to filter unassigned employees is more efficient than iterating through each employee’s assignments.                
            filtered_emp = ppl_yet_to_get_task
        
        return filtered_emp

    
        """"
        #FILTER 2 - by certs 
        #TODO add certs req datapoint in database, then modify the task processing funcitons (while at it get new database and make it so that one for each day?)
        #then modify the get task reqs thing
        task_cert_reqs = task_manasldkffldsf;lkl;k;kger.get_task_cert_reqs
        #Mock: "{'Ropes': 1, 'Lifeguard' : 3, 'Target': 2}
        if task_cert_reqs:
            certs_names = list(task_cert_reqs.keys())
            certified_employees = {
                certs_name : {employee for employee in filtered_emp 
                                if employee_manager} #TODO Finish
                for certs_name in certs_names
            }
        
        #SHIT TODO still need to look ahead to not use up too many of the thing on generic   
        #exclude from generics anything that might be used later
        
            
        # So if two certs req filter
            #Get people who meet the first req
            # then get people who meet the 2nd 
            
            #if need a person with multiple certs we can do this Cert AND Cert : num needed 
                # vs Cert:ppl, Cert:ppl
        #NOTE may need to modify how funciton returns task_employee_reqs
            #NOTE may need to make a function so can return lists of cert type for x amount
            #maybe output into a tuple, thus can not have to worry about it
                        
        #WAY 1 - So basically that way the assignment ordering function can then see oh i have 4 unuiqe task reqs employees with these set of reqs, these sets of reqs, and then general
        #then it can order those, AT THE END, that way okay so for the selection system obv assignment is just for ordering but
        #can either be like for each list reps a req so take x people off the list then that req is filled, lists can come in the same order as task reqs (in eligbility they are generated in order of task reqs thus ordering remains the same)
        # WAY 2 - can just put all of them into one giant set at the end, then have it randomly select people on while loop that is conditional on each tasks req until they all filled
        # WAY 3 - can loop through list and use all() and find person with all reqs or atleast for each type of req - so that not have to worry about seperate lists
        
        
        def get_lists_of_employees_with_certs():
                
            
            #TODO make lookahead thing here, then implement that into filtering logic
            if task_employee_reqs:
                #Use eligible employees to decrease the num of people that have to search through to find task reqs
                employees_with_req_traits = employee_manager.get_employees_in_pool_with_traits(filtered_emp, **task_employee_reqs)
            else:  
                employees_with_req_traits = filtered_emp # then no employees with special traits needed, can pick any
            
            return employees_with_req_traits
        """
        #TODO note maybe note that maybe, i should check if can schedule task here bc have all the shit, if not then skip to the next one, so move all that checking logic
        #TODO should unit test these so they all don't fail if trip certain shit



    def _update_data(
        self,
        task_name: str,
        employee_name: str,
        time_slots: list[str],
        employee_manager: EmployeeManager,
        task_manager: TaskManager,
        avail_employees_in_period: set[str],
        employees_with_req_traits: set[str],
        assigned_people: set[str]
        ) -> None:
        """Updates task and employee data after assignment"""
        
        assigned_people.add(employee_name)
        
        # for multi duration tasks - rethink how to efficently implement this later.
        employee_manager.set_employee_availability(
            employee_name, time_slots
        )
        employee_manager.assign_task_to_employee(
            employee_name, task_name, time_slots
        ) 
        task_manager.tasks[task_name].assign_employee_to_task(
            time_slots, employee_name
        )
        avail_employees_in_period.discard(employee_name)
    
    def _assign_employees_to_task(
        self,
        employees_with_req_traits: Any,
        task_name: str,
        time_slots: list[str],
        task_manager: TaskManager,
        employee_manager: EmployeeManager,
        assigned_people: set[str],
        avail_employees_in_period: set[str],
    ) -> None:
        '''CHOOSE WHICH EMPLOYEES ARE ASSIGNED AND HOW MANY'''
        
        #note actual assignment process
        #DynamicTimeSlotQueue.static_task_count_total
        #if task_manager.tasks[task_name].anti_co_concurrent:

        #TODO NOTE IMPORTANT BUG need to make sure we reassign the value that it modifies - bc im pretty sure not modifying sets outisde of funciton
        
        # TODO write logic for TASKS THAT ARE DEPENDENT ON NUMBER OF EMPLOYEES BASED ON OTHER TASKS
        # TODO once get code for how many certs to assign, then make it count until it has fulfilled it.

        # first assign special trait employees first
        def choose1() -> str:
            chosen_name_local = random.choice( #TODO can later replace with prob logic
                list(employees_with_req_traits)
            )
            return chosen_name_local
            
        # also interesting, a suggestion by GPT4 - employees_with_req_traits = set(employees_with_req_traits_local.keys()) & set(avail_employees_in_period.keys()) - set(assigned_people.keys())
        #BUG #TODO REDO THIS GARBAGE
        
        #TODO redo this, not working right now
        if employees_with_req_traits:  # check if already assigned or unavailable
            while True:
                chosen_name = choose1() # find someone who isn't been assigned or unavailable
                if chosen_name not in assigned_people:  # use all??
                    break  # Break the loop if a suitable / available employee is found, #TODO implent find someone with right reqs???
            self._update_data(task_name, chosen_name, time_slots, employee_manager, task_manager, avail_employees_in_period, employees_with_req_traits, assigned_people)

        else:
            attribute = getattr(task_manager.tasks[task_name], "min_num_people_needed")
            if attribute == "unassigned_employees":
                attribute = len(avail_employees_in_period)
            ppl_needed: int = int(attribute)  # need to check if an if or not
            while (ppl_needed > 0):
                while True:
                    # callback? cant add more so maybe have accept its short, or have it retrace and be able to merge some tasks??
                    try:  # NOTE temporary solution
                        chosen_name = random.choice(list(avail_employees_in_period))
                    except:
                        # error handle logic here?
                        continue
                    if chosen_name not in assigned_people:
                        self._update_data(task_name, chosen_name, time_slots, employee_manager, task_manager, avail_employees_in_period, employees_with_req_traits, assigned_people)
                        ppl_needed -= 1
                        break

                    # HMM this is also an interesting implementation: available_candidates = set(avail_employees_in_period.keys()) - set(assigned_people.keys())
                    # check if already assigned or unavailable
                    # update with anti-cert-use-up code later
                    # normal random assignment
                # then do the normal
                # check if in avail employees for period, would slow down if didnt have to but dict means fast look up.
                # temp prinout to see if assigning to tasks:
    @timer
    def _assign_single_task(
        self, 
        task_name: str,
        index_to_time_slot_map: dict[int, str],
        avail_employees_in_period: set[str],
        task_manager: TaskManager,
        employee_manager: EmployeeManager,
        schedule
        ):
        
        assigned_people: set[str] = set()
        #TODO how to initalize without getting yelled at that its a dicitionary
        #NOTE if BUG it will be here
        
        time_slots_for_task = self._calc_time_slots_for_duration(
            task_name, 
            task_manager, 
            index_to_time_slot_map
        ) #Time slot range for task
        
        employees_with_req_traits = self._generate_list_of_eligible_employees(
            avail_employees_in_period,
            time_slots_for_task,
            task_manager,
            employee_manager,
            task_name
        )
        self._assign_employees_to_task(
            employees_with_req_traits,
            task_name,
            time_slots_for_task,
            task_manager,
            employee_manager,
            assigned_people,
            avail_employees_in_period
        )
        
        #special process for windowed tasks -> moves task to next queue acc to freq attr
        #TODO see if make this a function - much later tho fine for now.
        #NOTE Moved out of update data bc otherwise ever person assigned goes thru this and adds a duplicate to next queue
        if task_name in self.windowed_tasks_list:
            required_assignments = int(task_manager.tasks[task_name].frequency) 
            current_assignments = sum(1 for people in task_manager.tasks[task_name].assigned_to.values() if people) #GPT had to help me on this one
            if current_assignments < required_assignments:
                next_queue_key = index_to_time_slot_map[self.time_slot_num + 1]
                #FIX - schedule.time_slot_task_queues[next_queue_key].windowed_tasks_list.append(task_name) #BUG not referencing schedule properly
                schedule.time_slot_task_queues[next_queue_key].queue.append(task_name)
                
        #else just stays in this queue like normal, doesn't go to next stage
  
    def _roll_over_tasks(self, task: str, index_to_time_slot_map: dict[int, str]):
        #tuple[None | str, list[str], list[str]]
        """#Only rolls over the windowed tasks NOT the STATIC ones"""
        
        #easier to check here, than keeping lists, and removing any STATIC or non windowed tasks
        task_index = self.queue.index(task)
        
        #DONE what if there is a windowed that was due this period but didn't get shceduled?? how do I filter it out?
        filtered = [task for task in self.queue[task_index:] if task in self.windowed_tasks_list] #NOTE-1 to be inclusive of task
        self.remaining_tasks = filtered
        next_time_slot_index: int = self.time_slot_num + 1
        try:
            self.next_time_slot_key = index_to_time_slot_map[next_time_slot_index]
        except KeyError:
            logging.warning(f"At {self.time_slot}: Next time slot does not exist in the current_schedule. Adding {self.remaining_tasks} to failed tasks.")
            self.failed_to_schedule.extend(self.remaining_tasks)
            self.next_time_slot_key = None
               
    @timer
    def assign_tasks_in_period(
        self,
        time_slot_to_index_map: dict[str, int],
        index_to_time_slot_map: dict[int, str],
        task_manager: TaskManager,
        employee_manager: EmployeeManager,
        schedule: Any
        ) -> tuple[Union[str, None], list[str], list[str]]:
        """
        Args:
            time_slot_to_index_map (dict[str, int]): [description]
            index_to_time_slot_map (dict[int, str]): [description]
            task_manager (TaskManager): [description]
            employee_manager (EmployeeManager): [description]
            schedule (Any): [description]

        Returns:
            tuple[Union[str, None], list[str], list[str]]: 
            self.next_time_slot_key, self.failed_to_schedule, self.remaining_tasks, 
        """
        avail_employees_in_period = employee_manager.get_available_employees(self.time_slot)
        
        #TODO Functionize this??
        #prob slowest part of code, well second, after i add in the probbabilites
        for task in self.queue: #NOTE Shortcoming -what if task that trips this reqs 4, but next one reqs 2, and there are two employees avail, but when populating queue tasks are sorted by duration from max->min
            if avail_employees_in_period: 
                ppl_needed = task_manager.tasks[task].min_num_people_needed
                if ppl_needed.isdigit():
                    if (len(avail_employees_in_period)+1 >= int(ppl_needed)): 
                        if getattr(task_manager.tasks[task], "window", None) != "Yes": #if Non windowed task,
                            #and maybe eventally the attr names themselves
                            self._assign_single_task(task, index_to_time_slot_map, avail_employees_in_period, task_manager, employee_manager, schedule)
                        elif "Yes" == getattr(task_manager.tasks[task], "window") and ((int(task_manager.tasks[task].duration)) <= task_manager.recalculate_distance_to_deadline(task, self.time_slot, time_slot_to_index_map)): #IF statement before to prevent non windowed from getting distance calced (error)                                
                            self._assign_single_task(task, index_to_time_slot_map, avail_employees_in_period, task_manager, employee_manager, schedule)
                        else:
                            logging.warning(f"At {self.time_slot}: Not enough time remaining to current_schedule {task} because duration would put it past it's deadline. Adding to failed tasks. Or a STATIC task got thru somehow")
                            self.failed_to_schedule.append(task)
                            continue
                    elif task_manager.tasks[task].window: #Only rolls over the windowed tasks NOT the STATIC ones, 
                        self._roll_over_tasks(task, index_to_time_slot_map)
                    else: #Non windowed task just get ignored, makes sure any remaining widowed get caught before break
                        self._roll_over_tasks(task, index_to_time_slot_map)
                else:
                    self._assign_single_task(task, index_to_time_slot_map, avail_employees_in_period, task_manager, employee_manager, schedule) # for uncalulated var / non int attrs
            else: #Default
                self._roll_over_tasks(task, index_to_time_slot_map) #make sure rest gets captured, before break
                break
        return self.next_time_slot_key, self.failed_to_schedule, self.remaining_tasks
