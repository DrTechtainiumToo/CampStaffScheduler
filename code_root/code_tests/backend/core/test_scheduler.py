#python -m unittest discover -s tests

import unittest
from typing import Dict

# Import the module under test:
from code_root.backend.core.scheduler import Schedule, instantiate_and_run_scheduler
from code_root.backend.core.dynamic_time_slot_queue import DynamicTimeSlotQueue
from code_root.backend.core.tasks import TaskManager
from code_root.backend.core.employees import EmployeeManager

# --- Dummy Classes for Testing ---

class DummyTask:
    """A simple dummy task with only the attributes required for scheduling."""
    def __init__(self, duration=2, tier=1, window="No", min_num_people_needed="1",
                 frequency=1, due_by="11:00 AM"):
        self.duration = duration              # e.g. 2 periods
        self.tier = tier                      # priority (lower numbers = higher priority)
        self.window = window                  # "Yes" means the task is windowed
        self.min_num_people_needed = min_num_people_needed  # stored as string (e.g., "1")
        self.frequency = frequency            # number of times the task should occur (for windowed tasks)
        self.due_by = due_by                  # a key into the timeslot mapping
        self.assigned_to = {}                 # dictionary (timeslot -> list of employees)
        # For the _find_tasks_in_time_slot method:
        self.start_time = ["9:00 AM"]
        self.start_times_iter = 0

class DummyTaskManager(TaskManager):
    """A dummy TaskManager that simply holds a tasks dictionary."""
    pass

class DummyEmployeeManager(EmployeeManager):
    """A dummy EmployeeManager that simulates a pool of employees."""
    def __init__(self):
        # For testing, we create two dummy employees.
        self.employees = {
            "Alice": type("DummyEmp", (), {"gender": "female", "availability": {}})(),
            "Bob": type("DummyEmp", (), {"gender": "male", "availability": {}})(),
        }
    def get_available_employees(self, time_slot: str) -> set:
        # For simplicity, assume both employees are available for every time slot.
        return {"Alice", "Bob"}
    def set_employee_availability(self, employee_name: str, time_slots: list[str]):
        pass
    def assign_task_to_employee(self, employee_name: str, task_name: str, time_slots: list[str]):
        pass

# --- Unit Tests for Schedule ---

class TestSchedule(unittest.TestCase):

    def setUp(self):
        # Create dummy timeslot mappings.
        self.time_slot_to_index_map = {"9:00 AM": 0, "10:00 AM": 1, "11:00 AM": 2}
        self.index_to_time_slot_map = {v: k for k, v in self.time_slot_to_index_map.items()}
        self.time_slot_labels = ["9:00 AM", "10:00 AM", "11:00 AM"]

        # Create a dummy task and a corresponding days_tasks list.
        dummy_task = DummyTask(duration=2, tier=1, window="No", min_num_people_needed="1",
                               frequency=1, due_by="11:00 AM")
        # For our purposes, we'll assume that the task should be found when searching for "9:00 AM".
        self.days_tasks = [{"task1": dummy_task}]
        self.tasks_dict = {"task1": dummy_task}

        # Create dummy managers.
        self.task_manager = DummyTaskManager(self.tasks_dict)
        self.employee_manager = DummyEmployeeManager()

        # Create a Schedule instance.
        self.schedule = Schedule()

    def test_generate_time_slot_queues(self):
        """Test that generate_time_slot_queues creates a queue for each timeslot and calls populate_queue."""
        self.schedule.generate_time_slot_queues(
            self.time_slot_labels, self.days_tasks, self.tasks_dict, self.time_slot_to_index_map
        )
        # Check that the keys in time_slot_task_queues match the provided timeslot_labels.
        self.assertEqual(set(self.schedule.time_slot_task_queues.keys()), set(self.time_slot_labels))
        # For the "9:00 AM" slot, _find_tasks_in_time_slot should find "task1" and thus populate the queue.
        queue_9 = self.schedule.time_slot_task_queues["9:00 AM"]
        self.assertIn("task1", queue_9.queue)

    def test_generate_schedule_assignments(self):
        """Test that generate_schedule iterates over each queue and updates the schedule accordingly.
           We patch assign_tasks_in_period to return controlled test values."""
        self.schedule.generate_time_slot_queues(
            self.time_slot_labels, self.days_tasks, self.tasks_dict, self.time_slot_to_index_map
        )
        # Patch each queue’s assign_tasks_in_period to return a known tuple.
        # For testing, simulate that each call returns:
        # next_time_slot_key = "10:00 AM", failed_to_schedule = ["failed_task"], remaining_tasks = ["remaining_task"]
        def fake_assign_tasks(*args, **kwargs):
            return ("10:00 AM", ["failed_task"], ["remaining_task"])
        for key, queue in self.schedule.time_slot_task_queues.items():
            queue.assign_tasks_in_period = fake_assign_tasks

        # Call generate_schedule.
        self.schedule.generate_schedule(
            self.time_slot_to_index_map, self.index_to_time_slot_map,
            self.time_slot_labels, self.days_tasks, self.tasks_dict,
            self.task_manager, self.employee_manager, self.schedule
        )
        # Check that failed_to_schedule is updated.
        self.assertIn("failed_task", self.schedule.failed_to_schedule)
        # Check that the queue corresponding to "10:00 AM" has been updated with remaining_tasks.
        queue_10 = self.schedule.time_slot_task_queues["10:00 AM"]
        self.assertIn("remaining_task", queue_10.queue)
        self.assertIn("remaining_task", queue_10.windowed_tasks_list)

    def test_instantiate_and_run_scheduler(self):
        """Test that instantiate_and_run_scheduler runs without error.
           Since this function doesn't return a value, we patch the underlying methods to ensure no exceptions."""
        # Patch DynamicTimeSlotQueue.assign_tasks_in_period so that it returns a tuple.
        def fake_assign_tasks(*args, **kwargs):
            return ("10:00 AM", [], [])
        original_assign = DynamicTimeSlotQueue.assign_tasks_in_period
        DynamicTimeSlotQueue.assign_tasks_in_period = fake_assign_tasks
        try:
            instantiate_and_run_scheduler(
                self.time_slot_to_index_map, self.index_to_time_slot_map, self.time_slot_labels,
                self.days_tasks, self.tasks_dict, self.task_manager, self.employee_manager
            )
        except Exception as e:
            self.fail(f"instantiate_and_run_scheduler raised an exception: {e}")
        finally:
            # Restore the original method.
            DynamicTimeSlotQueue.assign_tasks_in_period = original_assign

if __name__ == '__main__':
    unittest.main()
