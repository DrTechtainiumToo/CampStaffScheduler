from code_root.config.utility import timer
from code_root.backend.core.tasks import TaskManager
from code_root.backend.core.employees import EmployeeManager
from code_root.backend.core.dynamic_time_slot_queue import DynamicTimeSlotQueue
from typing import Any, Self
import logging

class Schedule:
    def __init__(self) -> None:
        """
        Attributes:
        - time_slot_task_queues: Stores queues for each time slot.
        - failed_to_schedule: Tracks tasks that could not be scheduled.
        """
        self.time_slot_task_queues: dict[str, DynamicTimeSlotQueue] = {}
        self.failed_to_schedule: list[str] = []
        #TODO #REFACTOR #REVIEW #IDEA for later: wut if just used a class attr for tasks_dict and set it for all the queues to ref?
        
    def generate_time_slot_queues(self,
        time_slot_labels: list[str], 
        days_tasks: list[dict], 
        tasks_dict: dict[str, Any],
        time_slot_to_index_map: dict[str, int]) -> None:
        """Creates each time-slot queue and populates it with tasks .
            Args:
                time_slot_labels (list[str]): Labels for each time slot.
                days_tasks (list[dict]): Tasks assigned for each day.
                tasks_dict (dict[str, Any]): A dictionary mapping task IDs to task objects.
                time_slot_to_index_map (dict[str, int]): Mapping of time slot labels to indices.
        """
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
        Drives the generation of the schedule and orchestrates scheduling across all queues.
        
        Args:
            time_slot_to_index_map (dict[str, int]): Mapping of time slot labels to indices.
            index_to_time_slot_map (dict[int, str]): Reverse mapping of indices to time slot labels.
            time_slot_labels (list[str]): Labels for each time slot.
            days_tasks (list[dict]): Tasks assigned for each day.
            tasks_dict (dict[str, TaskManager.Task]): Mapping of task IDs to Task objects.
            task_manager (TaskManager): Manages task execution.
            employee_manager (EmployeeManager): Manages employees for task allocation.
            schedule (Self): The schedule instance driving the scheduling process.

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
    """
    Instantiates a Schedule object and generates a schedule.
    Aka calls Schedule.generate_schedule with required inputs.
    
    Args:
        time_slot_to_index_map (dict[str, int]): Mapping of time slot labels to indices.
        index_to_time_slot_map (dict[int, str]): Reverse mapping of indices to time slot labels.
        time_slot_labels (list[str]): Labels for each time slot.
        days_tasks (list[dict]): Tasks assigned for each day.
        tasks_dict (dict[str, TaskManager.Task]): Mapping of task IDs to Task objects.
        task_manager (TaskManager): Manages task execution.
        employee_manager (EmployeeManager): Manages employees for task allocation.
    """
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
