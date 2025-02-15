from code_root.config.utility import timer
from code_root.backend.core.tasks import TaskManager
from code_root.backend.core.employees import EmployeeManager
from code_root.backend.core.dynamic_time_slot_queue import DynamicTimeSlotQueue
from typing import Any, Self
import logging

class Schedule:
    def __init__(self) -> None:
        self.time_slot_task_queues: dict[str, DynamicTimeSlotQueue] = {}
        self.failed_to_schedule: list[str] = []
        #TODO for later: wut if just used a class attr for tasks_dict and set it for all the queues to ref?
        
    def generate_time_slot_queues(self,
        time_slot_labels: list[str], 
        days_tasks: list[dict], 
        tasks_dict: dict[str, Any],
        time_slot_to_index_map: dict[str, int]) -> None:
        """ Create and populate each time-slot queue."""
        
        for time_slot in time_slot_labels:
            new_queue = DynamicTimeSlotQueue(
                time_slot, days_tasks,
                time_slot_to_index_map
            )
            new_queue.populate_queue(tasks_dict)
            self.time_slot_task_queues[time_slot] = new_queue
      
    def generate_schedule(self,
        time_slot_to_index_map: dict[str, int], 
        index_to_time_slot_map: dict[int, str], 
        time_slot_labels: list[str], 
        days_tasks: list[dict],
        tasks_dict: dict[str, TaskManager.Task], 
        task_manager: TaskManager, 
        employee_manager: EmployeeManager,
        schedule: Self) -> None:
        """
        Drives the generation of the schedule.
        """
        #TODO im confused between days_tasks and tasks_dict, why do i need dif ones? simplify IDK
        
        # 1) Create all the time slot queues
        self.generate_time_slot_queues(time_slot_labels, days_tasks, tasks_dict, time_slot_to_index_map)
        
        # 2) Assign tasks in each queue
        for queue in self.time_slot_task_queues:
            next_time_slot_key, failed_to_schedule, remaining_tasks = self.time_slot_task_queues[queue].assign_tasks_in_period(
                time_slot_to_index_map,
                index_to_time_slot_map,
                task_manager,
                employee_manager,
                schedule
            )
            
            self.failed_to_schedule.extend(failed_to_schedule)
            #$FAILURE POINT FIXME keyerror: none
            self.time_slot_task_queues[next_time_slot_key].queue.extend(remaining_tasks)
            self.time_slot_task_queues[next_time_slot_key].windowed_tasks_list.extend(remaining_tasks)
        
                  
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
    
    schedule = Schedule()
    schedule.generate_schedule(
        time_slot_to_index_map,
        index_to_time_slot_map,
        time_slot_labels,
        days_tasks,
        tasks_dict,
        task_manager,
        employee_manager,
        schedule
    )
