import datetime
from datetime import timezone
import pytest



# Import the class under test.
from code_root.backend.core.output_schedule import OutputSchedule

# --- Dummy Settings for Testing ---
dummy_etvs = {
    "date_output": True,
    "quote_of_day": "Inspire Quote",
    "file_title": "Test Schedule",
    "schedule_title": "Test Schedule Title"
}
dummy_excel_formatting_settings = {
    "date_label_format": {"bold": True},
    "corner_gap_fill_format": {"italic": True},
    "time_slot_format": {"bg_color": "#FFFF00"},
    "employee_format": {"bg_color": "#00FF00"},
    "title_format": {"bold": True},
    "quote_format": {"italic": True},
    "credit_note_format": {"underline": True}
}
dummy_task_format_dict = {
    "Unavailable": {"bg_color": "#FF0000"},
    "Default": {"bg_color": "#FFFFFF"}
}

# --- Dummy Workbook/Worksheet Classes ---
class DummyWorksheet:
    def __init__(self):
        self.written = []
        self.merged = []
        self.landscape = False
        self.columns_set = []
    def write(self, row, col, data, fmt=None):
        self.written.append((row, col, data, fmt))
    def merge_range(self, first_row, first_col, last_row, last_col, data, fmt=None):
        self.merged.append((first_row, first_col, last_row, last_col, data, fmt))
    def set_landscape(self):
        self.landscape = True
    def set_column(self, first_col, last_col, width):
        self.columns_set.append((first_col, last_col, width))

class DummyWorkbook:
    def __init__(self, file_title):
        self.file_title = file_title
        self.format_calls = []
        self.worksheets = []
        self.worksheet_name = None
        self.closed = False
    def add_format(self, fmt_settings):
        self.format_calls.append(fmt_settings)
        # For testing purposes, simply return the settings.
        return fmt_settings
    def add_worksheet(self, name):
        ws = DummyWorksheet()
        self.worksheets.append(ws)
        self.worksheet_name = name
        return ws
    def close(self):
        self.closed = True

# --- Dummy Manager Classes ---
class DummyEmployee:
    def __init__(self, name, assigned_to):
        self.name = name
        self.assigned_to = assigned_to  # e.g., a dict mapping time slots to tasks

class DummyEmployeeManager:
    def __init__(self):
        # For simplicity, one employee with assignments for each time slot.
        self.employees = {
            "Alice": DummyEmployee("Alice", {
                "9:00am": "Task1",
                "10:00am": "Unavailable",
                "11:00am": ""
            })
        }

class DummyTask:
    def __init__(self, duration):
        self.duration = duration  # string (e.g. "1")
        self.assigned_to = {}

class DummyTaskManager:
    def __init__(self):
        self.tasks = {
            "Task1": DummyTask("1")
        }

# --- Test for the excel() Method ---

def test_excel_method(monkeypatch):
    import code_root.backend.core.output_schedule as output_schedule
    monkeypatch.setattr(output_schedule, "xlsxwriter", type("DummyXlsxWriter", (), {"Workbook": dummy_workbook_factory}))

    # --- Patch get_current_week so that it returns a fixed value.
    monkeypatch.setattr(
        "code_root.backend.core.time_processes.get_current_week",
        lambda ref_day, next_day: "Week 5"
    )

    # --- Patch the settings imported in the excel() method.
    import code_root.config.settings as settings
    settings.excel_text_values_settings = dummy_etvs
    settings.excel_formatting_settings = dummy_excel_formatting_settings
    settings.task_format_dict = dummy_task_format_dict
    settings.WEEK_COUNT_START_REF_DAY = "01/01"  # dummy value

    # --- Patch xlsxwriter.Workbook so that it returns a DummyWorkbook.
    # Because the excel() method does "import xlsxwriter" locally, we patch it in the utility module.
    import code_root.config.utility as util
    created_workbook = None

    def dummy_workbook_factory(file_title):
        nonlocal created_workbook
        created_workbook = DummyWorkbook(file_title)
        return created_workbook

    monkeypatch.setattr(util, "xlsxwriter", type("DummyXlsxWriter", (), {"Workbook": dummy_workbook_factory}))

    # --- Create dummy inputs for OutputSchedule.
    day_time_slots_list = ["9:00am", "10:00am", "11:00am"]
    employee_list = ["Alice"]
    employee_instances = None  # not used in this context

    output_schedule = OutputSchedule(day_time_slots_list, employee_list, employee_instances)

    dummy_emp_manager = DummyEmployeeManager()
    dummy_task_manager = DummyTaskManager()

    algo_run_time = 0.123
    GET_NEXT_DAY = False
    WEEK_COUNT_START_REF_DAY = "01/01"
    UNAVAILABILITY_TASK = "Unavailable"

    # --- Call the excel() method.
    output_schedule.excel(dummy_emp_manager, dummy_task_manager, algo_run_time, GET_NEXT_DAY, WEEK_COUNT_START_REF_DAY, UNAVAILABILITY_TASK)

    # --- Determine expected values.
    expected_day = datetime.datetime.now(timezone.utc).astimezone().strftime("%A")
    week_number_day = "Week 5 " + expected_day
    expected_file_title = f"{dummy_etvs.get('file_title', 'SWAT Schedule')} {week_number_day}.xlsx"
    expected_ws_name = f"{dummy_etvs.get('schedule_title', 'SWAT Schedule')}{week_number_day}"

    # --- Assertions:
    assert created_workbook is not None, "A workbook should have been created."
    assert created_workbook.file_title == expected_file_title, "File title should match expected format."
    assert created_workbook.worksheet_name == expected_ws_name, "Worksheet name should match expected value."
    assert created_workbook.closed, "Workbook should be closed after excel() is called."

    # Optionally, you can check that certain writes occurred in the worksheet.
    # For example, verify that the date label was written at cell (0, 0) in uppercase.
    ws = created_workbook.worksheets[0]
    # Find a write call at row 0, col 0.
    writes_at_0_0 = [entry for entry in ws.written if entry[0] == 0 and entry[1] == 0]
    assert writes_at_0_0, "There should be a write at cell (0, 0)."
    # Check that the written data equals week_number_day.upper()
    written_data = writes_at_0_0[0][2]
    assert written_data == week_number_day.upper(), "The date label should be written in uppercase."
