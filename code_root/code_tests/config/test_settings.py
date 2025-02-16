import pytest
import json
import importlib
from pathlib import Path
from io import StringIO
import builtins

# --- Dummy JSON Data for Testing ---

dummy_settings_config = {
    "settings": {
        "scheduler_mode": "TEST_MODE",
        "interface_type": "web",
        "max_entry_attempts": 5,
        "get_next_day": True,
        "get_date_auto": False,
        "week_count_start_ref_day": "1/1",
        "unavailability_task": "Unavailable"
    },
    "paths": {
        "project_root": "dummy_root",
        "backend_folder": "backend",
        "core": "core",
        "data_folder": "data",
        "interface_folder": "interface",
        "config_folder": "config",
        "csv_data_folder": "csv",
        "files": {
            "swat_night_chores_info_csv": "night.csv",
            "swat_scheduler_special_tasks_list_csv": "special.csv",
            "swat_employee_info_csv": "employee.csv",
            "swat_basic_tasks_list_for_scheduler_csv": "basic.csv"
        }
    },
    "responses": {
        "yes_answers": ["yes", "y"],
        "no_answers": ["no", "n"],
        "male_answers": ["male"],
        "female_answers": ["female"]
    },
    "days": {"Monday": 1, "Tuesday": 2},
    "days_key_value_inverse": {"1": "Monday", "2": "Tuesday"},
    "time_slots": {
        "normal_day_time_slots": [{"9:00 AM": True}, {"10:00 AM": True}]
    },
    "time_slots_by_day": {},
    "misc": {"dumb_meme_1": "This is a meme"}
}

dummy_excel_config = {
    "excel_text_values_settings": {"header": "TestHeader"},
    "excel_formatting_settings": {"format": "TestFormat"},
    "task_format": {"task": "TestTaskFormat"}
}

# --- Dummy File-Like Object ---
class DummyFile(StringIO):
    def __init__(self, data):
        # data should be a string (e.g. JSON dump)
        super().__init__(data)
    # __enter__ and __exit__ are inherited from StringIO.

# --- Pytest Fixture to Patch File I/O in the Settings Module ---
@pytest.fixture(autouse=True)
def patch_settings(monkeypatch):
    """
    Patch the open() calls in the settings module so that it uses our dummy JSON data.
    For all other files use the original open.
    Also patch CONFIG_PATH and EXCEL_CONFIG_PATH. 
    """
    # Save the original open function.
    original_open = builtins.open
    
    # Define a fake open() that returns the appropriate dummy data based on the file path.
    def fake_open(file, mode="r", *args, **kwargs):
        file_str = str(file)
        if "settings_config.json" in file_str:
            return DummyFile(json.dumps(dummy_settings_config))
        elif "excel_output_settings.json" in file_str:
            return DummyFile(json.dumps(dummy_excel_config))
        else:
            return original_open(file, mode, *args, **kwargs)

    # Patch open in the settings module's namespace.
    monkeypatch.setattr(builtins, "open", fake_open)

    # Patch the CONFIG_PATH and EXCEL_CONFIG_PATH to dummy paths.
    fake_config_path = Path("dummy_settings_config.json")
    fake_excel_config_path = Path("dummy_excel_output_settings.json")
    monkeypatch.setattr("code_root.config.settings.CONFIG_PATH", fake_config_path)
    monkeypatch.setattr("code_root.config.settings.EXCEL_CONFIG_PATH", fake_excel_config_path)

    # Reload the settings module so it uses our patched open() and paths.
    import code_root.config.settings as settings
    importlib.reload(settings)
    return settings

# --- Test Functions ---

def test_application_settings(patch_settings):
    settings = patch_settings
    # Test that application behavior settings are loaded as expected.
    assert isinstance(settings.SCHEDULER_MODE, str)
    assert settings.SCHEDULER_MODE == "TEST_MODE"
    assert isinstance(settings.INTERFACE_TYPE, str)
    assert isinstance(settings.MAX_ENTRY_ATTEMPTS, int)
    assert settings.MAX_ENTRY_ATTEMPTS >= 0
    assert isinstance(settings.GET_NEXT_DAY, bool)
    assert settings.GET_NEXT_DAY is True or False
    assert isinstance(settings.GET_DATE_AUTO, bool)
    assert settings.GET_DATE_AUTO is True or False
    assert isinstance(settings.WEEK_COUNT_START_REF_DAY, str)
    assert settings.WEEK_COUNT_START_REF_DAY == "1/1"
    assert isinstance(settings.UNAVAILABILITY_TASK, str)
    assert not isinstance(settings.UNAVAILABILITY_TASK, int)
    assert settings.UNAVAILABILITY_TASK == "Unavailable"

def test_paths_settings(patch_settings):
    settings = patch_settings
    # Build the expected file path for one CSV file.
    expected_night_csv = Path("dummy_root") / "backend" / "data" / "csv" / "night.csv"
    # Compare the string representation.
    assert str(settings.SWAT_NIGHT_CHORES_INFO_CSV) == str(expected_night_csv)

def test_responses_settings(patch_settings):
    settings = patch_settings
    assert settings.YES_ANSWERS == ["yes", "y"]
    assert settings.NO_ANSWERS == ["no", "n"]
    assert settings.MALE_ANSWERS == ["male"]
    assert settings.FEMALE_ANSWERS == ["female"]

def test_days_settings(patch_settings):
    settings = patch_settings
    assert settings.DAYS == {"Monday": 1, "Tuesday": 2}
    # Note: The DAYS_KEY_VALUE_INVERSE is loaded from the JSON.
    # If your JSON contains string keys, they will remain strings.
    assert settings.DAYS_KEY_VALUE_INVERSE == {"1": "Monday", "2": "Tuesday"}

def test_time_slots_settings(patch_settings):
    settings = patch_settings
    # Check that the time_slots_data dictionary contains the normal_day_time_slots key.
    assert "normal_day_time_slots" in settings.time_slots_data
    # And that time_slots_by_day is an empty dictionary (per our dummy config).
    assert settings.time_slots_by_day == {}

def test_misc_and_excel_settings(patch_settings):
    settings = patch_settings
    # Test misc value.
    assert settings.DUMB_MEME_1 == "This is a meme"
    # Test Excel configurations.
    assert settings.excel_text_values_settings == {"header": "TestHeader"}
    assert settings.excel_formatting_settings == {"format": "TestFormat"}
    assert settings.task_format_dict == {"task": "TestTaskFormat"}
