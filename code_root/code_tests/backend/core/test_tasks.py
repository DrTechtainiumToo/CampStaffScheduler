
import io
import csv
import re
import pytest
from pathlib import Path

# Import functions and classes from your module.
# (Adjust the import path if your file is named differently.)
from code_root.backend.core.tasks  import (
    try_convert_to_int,
    TaskManager,
    TaskDataConverter,
    user_adds_additonal_tasks,
    TaskRecommender,
    instantiate_tasks,
)

#############################
# Tests for try_convert_to_int
#############################
def test_try_convert_to_int_valid():
    assert try_convert_to_int("123") == 123

def test_try_convert_to_int_invalid():
    # Should return 0 if conversion fails.
    assert try_convert_to_int("abc") == 0

def test_try_convert_to_int_empty():
    assert try_convert_to_int("") == 0

####################################
# Tests for TaskManager basic methods
####################################
@pytest.fixture
def dummy_task_dict():
    # Provide a dummy task instance.
    # Before instantiating a Task, we must define the default timeslots so that
    # Task.__init__ can create the "assigned_to" dictionary.
    # We set them to a simple list.
    TaskManager.Task.define_default_assigned_to_times(['09:00', '10:00'])
    # Create a dummy task instance using the inner Task class.
    # We supply the required positional arguments and also minimal kwargs for start_time2..start_time7.
    dummy_task = TaskManager.Task(
        task_name="Dummy Task",
        task_frequency="2",
        start_time="09:00",
        duration="1",
        min_num_people_needed="1",
        importance="High",
        pre_assigned_to="Alice, Bob",
        certs_required="Gold1",
        gender_required="male2",
        task_tier="1",
        # Provide empty values for additional start times:
        start_time2="",
        start_time3="",
        start_time4="",
        start_time5="",
        start_time6="",
        start_time7="",
        # Also supply a due_by attribute so we can test deadline calculations.
        due_by="10:00"
    )
    return {"DummyTask": dummy_task}

def test_task_manager_init_add_delete(dummy_task_dict):
    # Create a TaskManager with an initial dictionary.
    tm = TaskManager(dummy_task_dict)
    # Initially, total tasks equals the number of keys.
    assert tm.total_tasks_for_today() == len(dummy_task_dict)
    # Add a new dummy task.
    tm.add_task("ExtraTask", dummy_task_dict["DummyTask"])
    assert "ExtraTask" in tm.tasks
    # Delete a task.
    tm.delete_task("DummyTask")
    assert "DummyTask" not in tm.tasks

def test_recalculate_distance_to_deadline(dummy_task_dict):
    # Use the dummy task from the fixture.
    tm = TaskManager(dummy_task_dict)
    # Prepare a dummy timeslot mapping.
    # For example, suppose "09:00" maps to 1 and "10:00" maps to 2.
    timeslot_map = {"09:00": 1, "10:00": 2}
    # Calculate distance for "DummyTask". It uses the task’s due_by attribute.
    distance = tm.recalculate_distance_to_deadline("DummyTask", "09:00", timeslot_map)
    # Expect 2 - 1 = 1.
    assert distance == 1

##########################################
# Tests for TaskDataConverter (CSV import)
##########################################
# A dummy CSV string with a header and one row.
DUMMY_CSV_CONTENT = (
    "TaskName,Frequency,StartTime,TaskDuration,MinNumPeopleNeeded,Importance,PreassignedTo,"
    "CertificationsRequired,GenderReq,TaskCost,WillSpawnTodayChosen,Tier,Window,TimePreferred,"
    "EarliestStart,DueBy,StartTime2,StartTime3,StartTime4,StartTime5,StartTime6,StartTime7,"
    "ScheduledOccurance,OccursEveryNDays,SpawnSunday,SpawnMonday,SpawnTuesday,SpawnWensday,"
    "SpawnThursday,SpawnFriday,SpawnSaturday,TaskVariableName,TaskVariableName2,Category,"
    "AutoSchedule,AntiCoCounselorConcurrent,AntiSequential,AtLeastOncePerPerson\n"
    "Task A,2,09:00,1,1,High,,Gold1,male2,0,Yes,1,,None,None,10:00,,,,,,,,No,Yes,No,No,No,No,No,VAR_A,VAR_A,CategoryA,Yes,No,No,No\n"
)

@pytest.fixture
def fake_open_csv(monkeypatch):
    # Fake open() so that when TaskDataConverter calls open() for a given file,
    # it returns a StringIO with our dummy CSV content.
    def fake_open(filename, mode='r', newline=None, encoding=None):
        # You can check filename if needed.
        return io.StringIO(DUMMY_CSV_CONTENT)
    monkeypatch.setattr("task.open", fake_open)
    return fake_open

def test_add_tasks_from_csv(fake_open_csv):
    converter = TaskDataConverter()
    # Call add_tasks_from_csv with a fake filename (the content is provided by fake_open_csv).
    converter.add_tasks_from_csv("dummy_tasks.csv")
    # Our CSV row uses "VAR_A" as the key.
    assert "VAR_A" in converter.tasks_dict
    task_obj = converter.tasks_dict["VAR_A"]
    # Check that some attributes were set from the CSV.
    assert task_obj.task_name == "Task A"
    # Note: In the Task __init__, additional start time fields are provided via kwargs,
    # so start_time becomes a list with the provided "09:00" and empty strings.
    assert isinstance(task_obj.start_time, list)
    # Also, check that the task_variable_name was taken from TaskVariableName2 column.
    # (It may be None or "VAR_A" depending on your CSV—here we expect "VAR_A".)
    # You can adjust the test as needed.
    assert getattr(task_obj, "task_variable_name", None) == "VAR_A"

#######################################
# Test for user_adds_additional_tasks
#######################################
def test_user_adds_additional_tasks(monkeypatch):
    # For this test, we need to ensure that the global name "Task" used in the function
    # refers to TaskManager.Task. (Your module code uses "Task(...)" without qualification.)
    from task import TaskDataConverter  # just to force module load if needed
    # Patch the module's global "Task" to be TaskManager.Task.
    monkeypatch.setattr("task.Task", TaskManager.Task)
    
    # Prepare an empty dictionary.
    tasks_dict = {}
    # Call user_adds_additional_tasks with dummy parameters.
    # For minimal parameters, we supply also the extra start_time2..start_time7 in keyword args.
    result = user_adds_additional_tasks(
        taskDictLocal=tasks_dict,
        userTaskVariableName="VAR_USER",
        userTaskName="User Task",
        userFrequency="3",
        userStartTime="08:00",
        userDuration="2",
        userMinManpower="2",
        userImportance="Medium",
        userGenderSpecific="female1",
        userAssignees="Carol, Dave",
        user_windowed_task="No",
        userTimePreferred="08:30",
        user_earliest_start="08:00",
        user_due_by="09:00",
        task_tier=1
    )
    # The new task should be added to tasks_dict with key equal to userTaskName.
    assert "User Task" in result
    task_obj = result["User Task"]
    # Verify that some attributes are correctly set.
    assert task_obj.task_name == "User Task"
    assert task_obj.min_num_people_needed == "2"
    # Check that the pre_assigned_to list was generated.
    assert task_obj.pre_assigned_to == ["Carol", "Dave"]

##########################################
# Tests for TaskRecommender
##########################################
def create_dummy_task_for_recommender(spawn_value, extra_kwargs=None):
    """Helper to create a dummy task instance with a given spawn value for a day.
    We need to supply the spawn attribute for the day. For example, if dayName is 'Monday',
    the attribute name will be 'spawn_monday'."""
    extra_kwargs = extra_kwargs or {}
    # Ensure default timeslots are defined.
    TaskManager.Task.define_default_assigned_to_times(['09:00', '10:00'])
    # Create a dummy task.
    return TaskManager.Task(
        task_name="Dummy",
        task_frequency="1",
        start_time="09:00",
        duration="1",
        min_num_people_needed="1",
        importance="Low",
        pre_assigned_to="",
        certs_required="",
        gender_required="",
        task_tier="1",
        start_time2="",
        start_time3="",
        start_time4="",
        start_time5="",
        start_time6="",
        start_time7="",
        **extra_kwargs,
        # Set the spawn attribute for Monday (for example).
        spawn_monday=spawn_value
    )

def test_recommend_tasks():
    # Create two dummy tasks: one that should spawn on Monday and one that should not.
    task_yes = create_dummy_task_for_recommender("Yes")
    task_no = create_dummy_task_for_recommender("No")
    master_dict = {
        "TaskYes": task_yes,
        "TaskNo": task_no,
    }
    # Instantiate a TaskRecommender for "Monday"
    recommender = TaskRecommender("Monday")
    recommender.recommend_tasks(master_dict)
    # Only the task with spawn_monday == "Yes" should be selected.
    selected, names = recommender.return_selected_tasks_for_day()
    assert "TaskYes" in selected
    assert "TaskNo" not in selected
    # The list of variable names should contain only "TaskYes".
    assert names == ["TaskYes"]

##############################################
# Test for instantiate_tasks (merging CSV & additional tasks)
##############################################
# We will monkeypatch open() so that both CSV files return our dummy CSV content.
@pytest.fixture
def fake_open_for_instantiate(monkeypatch):
    def fake_open(filename, mode='r', newline=None, encoding=None):
        # Check if the filename corresponds to either CSV file.
        # (SWAT_BASIC_TASKS_LIST_FOR_SCHEDULER_CSV and SWAT_NIGHT_CHORES_INFO_CSV are imported in your module.)
        if "basic" in filename.lower() or "night" in filename.lower():
            return io.StringIO(DUMMY_CSV_CONTENT)
        return io.StringIO("")
    monkeypatch.setattr("task.open", fake_open)
    return fake_open

def test_instantiate_tasks(fake_open_for_instantiate):
    # Prepare an additional tasks dictionary.
    # For simplicity, create one additional task using the inner Task class.
    TaskManager.Task.define_default_assigned_to_times(['09:00', '10:00'])
    extra_task = TaskManager.Task(
        task_name="Extra Task",
        task_frequency="1",
        start_time="09:00",
        duration="1",
        min_num_people_needed="1",
        importance="Extra",
        pre_assigned_to="",
        certs_required="",
        gender_required="",
        task_tier="1",
        start_time2="",
        start_time3="",
        start_time4="",
        start_time5="",
        start_time6="",
        start_time7="",
        due_by="10:00"
    )
    additional_tasks = {"ExtraTask": extra_task}
    # Provide a dummy dayTimeSlotsKeysList.
    day_slots = ['09:00', '10:00']
    task_manager, merged_dict, var_names = instantiate_tasks(additional_tasks, day_slots)
    # Check that the additional task is present.
    assert "ExtraTask" in merged_dict
    # And that var_names includes keys from both CSV files and extra tasks.
    # (Since our fake CSV returns one row with key "VAR_A", we expect that and the extra task.)
    assert "VAR_A" in merged_dict
    assert "ExtraTask" in merged_dict
    # Also, task_manager.tasks should equal merged_dict.
    assert task_manager.tasks == merged_dict
