import time
from io import StringIO
import builtins
import pytest

# Import the functions and variables to test.
from code_root.config.utility import (
    time_block,
    testOutput,
    timer,
    log_to_file,
    xyz_input_auto_completer,
    log_conclusion_text,
)

# --- Helper dummy function for timer decorator tests ---
@timer
def dummy_function(x, y):
    time.sleep(0.1)
    return x + y

# Test that time_block logs the elapsed time with the given label.
def test_time_block_logs_time(monkeypatch):
    fake_file = StringIO()
    # Patch builtins.open so that when time_block calls open(), it returns our fake_file.
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: fake_file)
    
    with time_block("Test Block"):
        time.sleep(0.1)
    
    fake_file.seek(0)
    contents = fake_file.read()
    assert "Test Block:" in contents, "Log should contain the 'Test Block:' label."

# Test that dummy_function (decorated with @timer) returns the correct result and logs run time.
def test_timer_decorator_logs_time(monkeypatch):
    fake_file = StringIO()
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: fake_file)
    
    result = dummy_function(3, 4)
    assert result == 7, "dummy_function should return 7 for inputs 3 and 4."
    
    fake_file.seek(0)
    log_contents = fake_file.read()
    assert "dummy_function run time length:" in log_contents, "Log should contain timing info for dummy_function."

# Test that log_to_file writes the given message.
def test_log_to_file(monkeypatch):
    fake_file = StringIO()
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: fake_file)
    
    log_to_file("Test message", file_path="dummy_log.txt")
    fake_file.seek(0)
    contents = fake_file.read()
    assert "Test message" in contents, "Log should contain the test message."

# Test that xyz_input_auto_completer returns the expected auto-completed input.
def test_xyz_input_auto_completer(monkeypatch):
    monkeypatch.setattr("code_root.config.utility.prompt", lambda prompt_text, completer=None: "TestInput")
    result = xyz_input_auto_completer("Enter value: ", ["TestInput", "Other"])
    assert result == "TestInput", "The auto-completer should return 'TestInput'."


# Test that log_conclusion_text writes an ending message to the log.
def test_log_conclusion_text(monkeypatch):
    fake_file = StringIO()
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: fake_file)
    
    log_conclusion_text()
    fake_file.seek(0)
    contents = fake_file.read()
    assert "-------End of UPDATED Program-------" in contents, "Log should include the end cap message."
