import time


# Import the functions and variables to test.
from code_root.config.utility import (
\
    xyz_input_auto_completer,

)


# --- Helper dummy function for timer decorator tests ---
def dummy_function(x, y):
    time.sleep(0.1)
    return x + y

# Test that xyz_input_auto_completer returns the expected auto-completed input.
def test_xyz_input_auto_completer(monkeypatch):
    monkeypatch.setattr(
        "code_root.config.utility.prompt",
        lambda prompt_text, completer=None: "TestInput",
    )
    result = xyz_input_auto_completer("Enter value: ", ["TestInput", "Other"])
    assert result == "TestInput", "The auto-completer should return 'TestInput'."
