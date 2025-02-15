#pytest test_dynamic_queues.py


import datetime
import random
import logging
from typing import Dict

from code_root.backend.core.dynamic_time_slot_queue import DynamicTimeSlotQueue
from code_root.backend.core.tasks import TaskManager
from code_root.backend.core.employees import EmployeeManager
import pytest
import random
import logging

# --- Dummy Classes for Testing ---

class DummyTask:
    def __init__(self, name, start_time, duration, tier, window="No", min_num_people_needed="1", frequency="1"):
        self.task_name = name
        # Ensure start_time is a list (to support multiple possible start times)
        self.start_time = start_time if isinstance(start_time, list) else [start_time]
        self.start_times_iter = 0
        self.duration = duration  # expected as a string convertible to int
        self.tier = tier
        self.window = window
        self.min_num_people_needed = min_num_people_needed
        self.frequency = frequency
        # For recording assignments; keys are time slot strings, values are lists of employee names.
        self.assigned_to = {}

    def assign_employee_to_task(self, time_slots, employee_name):
        if isinstance(time_slots, list):
            for ts in time_slots:
                self.assigned_to.setdefault(ts, []).append(employee_name)
        else:
            self.assigned_to.setdefault(time_slots, []).append(employee_name)

class DummyTaskManager:
    def __init__(self, tasks):
        # tasks is a dict mapping task names to DummyTask instances.
        self.tasks = tasks

    def get_task_gender_reqs(self, task_name):
        # For testing, we assume no gender requirements.
        return {}

    def recalculate_distance_to_deadline(self, task_name, time_slot, time_slot_to_index_map):
        # For testing, assume there is plenty of time remaining.
        return 10

class DummyEmployee:
    def __init__(self, name):
        self.name = name
        self.availability = {}  # Not used in detail for these tests.

    def set_employee_availability(self, time_slots):
        pass

    def assign_task(self, time_slots, task):
        pass

class DummyEmployeeManager:
    def __init__(self, available):
        # available is a list of employee names.
        self.available = available
        self.employees = {name: DummyEmployee(name) for name in available}

    def get_available_employees(self, time_slot):
        # For testing, simply return all available employees.
        return set(self.available)

    def set_employee_availability(self, employee_name, time_slots):
        pass

    def assign_task_to_employee(self, employee_name, task, time_slots):
        pass

class DummySchedule:
    def __init__(self, time_slot_task_queues):
        # time_slot_task_queues is a dict mapping time slot keys to DynamicTimeSlotQueue instances.
        self.time_slot_task_queues = time_slot_task_queues

# --- Pytest Fixtures ---

@pytest.fixture
def time_slot_maps():
    # For example, assume four time slots.
    time_slot_to_index_map = {"9:00": 0, "9:30": 1, "10:00": 2, "10:30": 3}
    index_to_time_slot_map = {v: k for k, v in time_slot_to_index_map.items()}
    return time_slot_to_index_map, index_to_time_slot_map

@pytest.fixture
def dummy_task():
    # Create a dummy task with start_time "9:00", duration "1", tier 1, and non-windowed.
    return DummyTask(name="Task1", start_time="9:00", duration="1", tier=1, window="No", min_num_people_needed="1", frequency="1")

@pytest.fixture
def days_tasks(dummy_task):
    # days_tasks is a list (each element representing a grouping for the day)
    # Here we use one dictionary mapping task keys to task instances.
    return [{"Task1": dummy_task}]

@pytest.fixture
def dyn_queue(time_slot_maps, days_tasks):
    time_slot_to_index_map, _ = time_slot_maps
    # Create a DynamicTimeSlotQueue instance for time slot "9:00"
    return DynamicTimeSlotQueue(time_slot_name="9:00", days_tasks=days_tasks, time_slot_to_index_map=time_slot_to_index_map)

# --- Tests for Internal Methods ---

def test_find_tasks_in_time_slot(days_tasks, dyn_queue, dummy_task):
    """
    Test that _find_tasks_in_time_slot locates tasks whose current start_time matches the search value
    and that it increments the task’s start_times_iter.
    """
    # dummy_task.start_time is ["9:00"] and start_times_iter initially 0.
    result = dyn_queue._find_tasks_in_time_slot(days_tasks, "9:00")
    assert "Task1" in result
    # Check that start_times_iter has been incremented.
    assert dummy_task.start_times_iter == 1

def test_sort_tasks_by_duration(dyn_queue):
    """
    Test that _sort_tasks_by_duration orders task keys in descending order of duration.
    """
    task_a = DummyTask("A", "9:00", duration="3", tier=2)
    task_b = DummyTask("B", "9:00", duration="1", tier=1)
    tasks_list = ["A", "B"]
    tasks_dict = {"A": task_a, "B": task_b}
    sorted_list = dyn_queue._sort_tasks_by_duration(tasks_list, tasks_dict)
    # Expect "A" (duration 3) before "B" (duration 1)
    assert sorted_list == ["A", "B"]

def test_sort_tasks_by_tier(dyn_queue):
    """
    Test that _sort_tasks_by_tier orders task keys in ascending order of tier.
    """
    task_a = DummyTask("A", "9:00", duration="1", tier=2)
    task_b = DummyTask("B", "9:00", duration="1", tier=1)
    tasks_list = ["A", "B"]
    tasks_dict = {"A": task_a, "B": task_b}
    sorted_list = dyn_queue._sort_tasks_by_tier(tasks_list, tasks_dict)
    # Expect "B" (tier 1) before "A" (tier 2)
    assert sorted_list == ["B", "A"]

def test_collect_windowed_tasks(dyn_queue):
    """
    Test that _collect_windowed_tasks collects tasks whose 'window' attribute is "Yes".
    """
    task_a = DummyTask("A", "9:00", duration="1", tier=1, window="Yes")
    task_b = DummyTask("B", "9:00", duration="1", tier=1, window="No")
    tasks_list = ["A", "B"]
    tasks_dict = {"A": task_a, "B": task_b}
    dyn_queue.windowed_tasks_list = []
    dyn_queue._collect_windowed_tasks(tasks_list, tasks_dict)
    assert "A" in dyn_queue.windowed_tasks_list
    assert "B" not in dyn_queue.windowed_tasks_list

def test_populate_queue(dyn_queue, dummy_task):
    """
    Test that populate_queue uses the helper methods to set self.queue and update the static task count.
    """
    tasks_dict = {"Task1": dummy_task}
    # Reset the class-level static task count.
    DynamicTimeSlotQueue.static_task_count_total = 0
    dyn_queue.populate_queue(tasks_dict)
    # Since dummy_task.start_time ("9:00") matches the queue’s time slot, it should be included.
    assert "Task1" in dyn_queue.queue
    # As the task is not windowed, it should not appear in windowed_tasks_list.
    assert "Task1" not in dyn_queue.windowed_tasks_list
    # The static count is updated by adding the number of non-windowed tasks.
    expected_count = len(set(dyn_queue.queue) - set(dyn_queue.windowed_tasks_list))
    assert DynamicTimeSlotQueue.static_task_count_total == expected_count

def test_calc_time_slots_for_duration(dyn_queue, dummy_task, time_slot_maps):
    """
    Test that _calc_time_slots_for_duration returns a list of time slot identifiers based on the task's duration.
    """
    # Set duration to "2" (so task occupies two consecutive slots)
    dummy_task.duration = "2"
    dummy_task_manager = DummyTaskManager({"Task1": dummy_task})
    _, index_to_time_slot_map = time_slot_maps
    result = dyn_queue._calc_time_slots_for_duration("Task1", dummy_task_manager, index_to_time_slot_map)
    # With dyn_queue.time_slot "9:00" (index 0), expect ["9:00", "9:30"]
    assert result == ["9:00", "9:30"]

    # If duration is "1", it should return just [self.time_slot]
    dummy_task.duration = "1"
    result = dyn_queue._calc_time_slots_for_duration("Task1", dummy_task_manager, index_to_time_slot_map)
    assert result == ["9:00"]

def test_roll_over_tasks(dyn_queue, time_slot_maps):
    """
    Test that _roll_over_tasks correctly identifies windowed tasks remaining in the queue and sets the next time slot.
    """
    # Set up a dummy queue and mark some tasks as windowed.
    dyn_queue.queue = ["Task1", "Task2", "Task3"]
    dyn_queue.windowed_tasks_list = ["Task2", "Task3"]
    time_slot_to_index_map, index_to_time_slot_map = time_slot_maps
    # Set the current time slot number to 0 ("9:00")
    dyn_queue.time_slot_num = 0
    dyn_queue._roll_over_tasks("Task1", index_to_time_slot_map)
    # Expect that remaining_tasks contains tasks from the queue (from Task1 onward) that are windowed.
    # In this case, Task2 and Task3.
    assert dyn_queue.remaining_tasks == ["Task2", "Task3"]
    # The next time slot key should be index 1 (i.e. "9:30").
    assert dyn_queue.next_time_slot_key == index_to_time_slot_map[1]

# --- Tests for the Overall Assignment Function ---

def test_assign_tasks_in_period(dyn_queue, time_slot_maps, dummy_task):
    """
    Test assign_tasks_in_period in a scenario with one non-windowed task and one available employee.
    The dummy task should receive an assignment.
    """
    # Prepare the queue with one task.
    dyn_queue.queue = ["Task1"]
    # Ensure the dummy task has the proper attributes.
    dummy_task.duration = "1"
    dummy_task.window = "No"
    dummy_task.min_num_people_needed = "1"
    # Create a dummy task manager with the dummy task.
    dummy_task_manager = DummyTaskManager({"Task1": dummy_task})
    # Create a dummy employee manager that always returns one available employee.
    dummy_employee_manager = DummyEmployeeManager(["Alice"])
    # Prepare a dummy schedule with a next time slot queue (even if not used for a non-windowed task).
    time_slot_to_index_map, index_to_time_slot_map = time_slot_maps
    dummy_next_queue = DynamicTimeSlotQueue("9:30", [], {"9:30": 1})
    dummy_schedule = DummySchedule(time_slot_task_queues={"9:30": dummy_next_queue})
    # Reset the static task count.
    DynamicTimeSlotQueue.static_task_count_total = 0
    # Call the assignment method.
    result = dyn_queue.assign_tasks_in_period(time_slot_to_index_map, index_to_time_slot_map, dummy_task_manager, dummy_employee_manager, dummy_schedule)
    # The _assign_single_task process (via _update_data) should result in "Alice" being assigned to "9:00" for Task1.
    assert "9:00" in dummy_task.assigned_to
    assert "Alice" in dummy_task.assigned_to["9:00"]
    # For a task that is successfully assigned, no rollover occurs:
    next_key, failed, remaining = result
    assert next_key is None
    assert failed == []
    assert remaining == []