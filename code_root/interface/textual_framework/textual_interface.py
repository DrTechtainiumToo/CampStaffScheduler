import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
#python -m devious_fuckin_project_root.interface.textual_framework.textual_interface

from textual.app import App, ComposeResult

# textual_interface.py
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, Input
from textual.screen import Screen
import time
import json


# Import your scheduling logic modules (adjust paths as needed)
from code_root.config.settings import GET_NEXT_DAY, GET_DATE_AUTO, MAX_ENTRY_ATTEMPTS, WEEK_COUNT_START_REF_DAY, UNAVAILABILITY_TASK
from code_root.backend.core.time_processes import get_day_name, get_day_time_slots, timeSlotStandardizer, get_current_week
from code_root.backend.core.process import employee_names, employee_genders
from code_root.backend.core.employees import EmployeeManager, EmployeeAvailabilityLogic, instantiate_employees
from code_root.backend.core.tasks import TaskRecommender, instantiate_tasks
from code_root.backend.core.scheduler import instantiate_and_run_scheduler
from code_root.backend.core.output_schedule import OutputSchedule


# -----------------------------------------------------
# Screen: Welcome Screen
# -----------------------------------------------------
class WelcomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Welcome to the Scheduler App!\n", id="welcome-message")
        yield Button("Start", id="start_button")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start_button":
            self.app.push_screen("date_input")

# -----------------------------------------------------
# Screen: Date Input
# -----------------------------------------------------
class DateInputScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Please enter the date (YYYY-MM-DD):", id="date-label")
        self.date_input = Input(placeholder="YYYY-MM-DD", id="date_input")
        yield self.date_input
        yield Button("Submit", id="submit_date_button")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit_date_button":
            date_value = self.date_input.value.strip()
            # (Add date validation here as needed)
            self.app.date_value = date_value
            self.app.push_screen("timeslot")

# -----------------------------------------------------
# Screen: Timeslot Confirmation / Modification
# -----------------------------------------------------

class TimeslotScreen(Screen):
    def compose(self) -> ComposeResult:
        date_value = self.app.date_value
        print(date_value)
        day_name = get_day_name(date_value)
        self.day_time_slots = get_day_time_slots(date_value)
        yield Static(f"Schedule for {day_name}", id="day-info")
        yield Static("Do you want to modify the default timeslots?", id="modify-query")
        yield Button("Yes", id="modify_yes")
        yield Button("No", id="modify_no")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "modify_yes":
            self.app.push_screen(ModifyTimeslotScreen(self.day_time_slots))        
        elif event.button.id == "modify_no":
            print(self.day_time_slots)
            self.app.day_time_slots = self.day_time_slots
            self.app.push_screen("employee_availability")

# -----------------------------------------------------
# Screen: Modify Timeslots
# -----------------------------------------------------
class ModifyTimeslotScreen(Screen):
    def __init__(self, day_time_slots, **kwargs):
        super().__init__(**kwargs)
        self.day_time_slots = day_time_slots

    def compose(self) -> ComposeResult:
        yield Static("Modify your timeslots below (enter as JSON):", id="modify-label")
        # For demonstration, we assume the user provides a JSON string.
        # (In a more advanced UI, you might build a form with multiple fields.)
        self.timeslot_input = Input(placeholder='e.g., {"08:00": {}, "09:00": {}}', id="timeslot_input")
        yield self.timeslot_input
        yield Button("Submit", id="submit_modified_timeslots")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit_modified_timeslots":
            try:
                modified_ts = json.loads(self.timeslot_input.value.strip())
                self.app.day_time_slots = modified_ts
                self.app.push_screen("employee_availability")
            except Exception as e:
                self.app.push_screen(TaskManagementScreen(time_slot_labels=self.app.message))

# -----------------------------------------------------
# Screen: Employee Availability
# -----------------------------------------------------
class EmployeeAvailabilityScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Employee Availability Setup", id="employee-setup")
        # Here you could add interactive fields to collect availability.
        # For now, we assume default settings.
        yield Static("Using default employee availabilities.", id="employee-info")
        yield Button("Continue", id="continue_employee")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "continue_employee":
            time_slot_labels = self.app.day_time_slots[0].keys()
            employee_manager = EmployeeManager()
            # In a full UI, you'd collect availability details.
            employee_manager = instantiate_employees(employee_manager, time_slot_labels, employee_names, employee_genders)
            self.app.employee_manager = employee_manager
            self.app.push_screen(TaskManagementScreen(time_slot_labels=self.app.day_time_slots)) 

# -----------------------------------------------------
# Screen: Task Management
# -----------------------------------------------------
class TaskManagementScreen(Screen):
    def __init__(self, time_slot_labels, **kwargs):
        super().__init__(**kwargs)
        self.time_slot_labels = time_slot_labels

    def compose(self) -> ComposeResult:
        yield Static("Task Management", id="task-management")
        yield Static("Default tasks will be loaded. (You can add additional tasks if desired.)", id="task-info")
        yield Button("Continue", id="continue_tasks")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "continue_tasks":
            additional_tasks: list = []  # Extend this to allow user input for additional tasks.
            task_manager, default_tasks_dict, _ = instantiate_tasks(additional_tasks, self.time_slot_labels)
            self.app.task_manager = task_manager
            # Simplified: auto-select the recommended tasks.
            task_recommender = TaskRecommender(get_day_name(self.app.date_value))
            task_recommender.recommend_tasks(default_tasks_dict)
            self.app.tasks_dictionary = default_tasks_dict
            self.app.push_screen("scheduling")

# -----------------------------------------------------
# Screen: Scheduler Execution
# -----------------------------------------------------
class SchedulingScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Ready to run the scheduling algorithm.", id="scheduling-info")
        yield Button("Run Scheduler", id="run_scheduler")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "run_scheduler":
            time_slot_labels = list(self.app.day_time_slots[0].keys())
            index_to_ts_map, ts_to_index_map = timeSlotStandardizer(time_slot_labels)
            days_tasks = [self.app.tasks_dictionary]
            start_algo = time.perf_counter()
            instantiate_and_run_scheduler(
                ts_to_index_map, 
                index_to_ts_map, 
                time_slot_labels, 
                days_tasks, 
                self.app.tasks_dictionary, 
                self.app.task_manager, 
                self.app.employee_manager
            )
            self.app.algo_run_time = time.perf_counter() - start_algo
            self.app.push_screen("output")

# -----------------------------------------------------
# Screen: Output Generation
# -----------------------------------------------------
class OutputScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Generating schedule output...", id="output-info")
        yield Button("Generate Excel Output", id="generate_excel")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "generate_excel":
            time_slot_labels = list(self.app.day_time_slots[0].keys())
            output_schedule = OutputSchedule(time_slot_labels, employee_names, self.app.employee_manager.employees)
            output_schedule.excel(
                self.app.employee_manager,
                self.app.task_manager, 
                self.app.algo_run_time,
                GET_NEXT_DAY, 
                WEEK_COUNT_START_REF_DAY,
                UNAVAILABILITY_TASK,
            )
            self.app.push_screen("final")

# -----------------------------------------------------
# Screen: Final Screen
# -----------------------------------------------------
class FinalScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Program finished. Thank you!", id="final-message")
        yield Button("Exit", id="exit_button")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit_button":
            self.app.exit()

# -----------------------------------------------------
# Screen: Error Screen (for simple error handling)
# -----------------------------------------------------
class ErrorScreen(Screen):
    def __init__(self, message: str, **kwargs):
        super().__init__(**kwargs)
        self.message = message

    def compose(self) -> ComposeResult:
        yield Static(f"Error: {self.message}", id="error-message")
        yield Button("Back", id="back_button")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back_button":
            self.app.pop_screen()

# -----------------------------------------------------
# Main Textual Application
# -----------------------------------------------------
class SchedulerApp(App):
    CSS_PATH = "scheduler.css"  # Optionally add styling

    def on_mount(self) -> None:
        self.install_screen(WelcomeScreen(), name = "welcome")
        self.install_screen(DateInputScreen(), name = "date_input")
        self.install_screen(TimeslotScreen(), name = "timeslot")
        # ❌ Do NOT register ModifyTimeslotScreen with install_screen() because it needs arguments.
        self.install_screen(EmployeeAvailabilityScreen(), name = "employee_availability")
        self.install_screen(SchedulingScreen(), name = "scheduling")
        self.install_screen(OutputScreen(), name = "output")
        self.install_screen(FinalScreen(), name = "final")
        self.push_screen("welcome")

if __name__ == "__main__":
    SchedulerApp().run()
