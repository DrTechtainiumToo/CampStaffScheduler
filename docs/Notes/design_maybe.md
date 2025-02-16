

PROJECT EXPLINATION:

## 5. Program Overview

### Data Loading:
- Load default info, employee gender & nickname, basic tasks & durations, timeslots, and night chore details.

### User Input & Task Generation:
- Ask for special tasks and determine recurring special events based on date.
- Generate total tasks.
- Identify people available (and handle partial availabilities).

### Time Slot Scheduling:
- For each timeslot:
  - Determine tasks due and required personnel.
  - Rank tasks by importance.
  - Check available personnel vs. required tasks (throw exception if shortages occur).
  - Assign tasks using a loop until either all tasks are filled or no further assignments can be made.
  - Consider task deadlines and multi-period tasks.

### Assignment Considerations:
- Factor in employee task preferences (weighted probability).
- Handle gender-dependent tasks (e.g., special events, specific chores).
- Randomly select employees based on calculated probabilities.
- Log any unassigned tasks or scheduling issues for final reporting.

### Output:
- Print final schedule and error logs to the console.
- Write results to CSV for manual modification or Excel/Google Sheets processing.

## 6. Modularization Steps

### Core Logic:
- Isolate business rules and scheduling algorithms from I/O code.
- Functions should handle task management, scheduling, and data manipulation.

### Data Access Layer:
- Create a module (e.g., `database.py` or `file_manager.py`) to handle all data interactions.

### User Interfaces:
#### Terminal Interface:
- Develop a CLI (e.g., `terminal_ui.py`) for command-line interactions.

#### Web Interface:
- Set up a web server (e.g., using Flask in `web_server.py`) for HTTP requests/responses.

### Configuration & Initialization:
- Implement a configuration system (e.g., `settings.py`) to manage which UI to launch and set dependencies.
- Use dependency injection to allow flexibility (swap mock databases, alternate UIs, etc.).

### File Structure Suggestions:
- `task_manager.py` & `scheduler.py` – Core business logic.
- `database.py` & `file_manager.py` – Data storage and retrieval.
- `terminal_ui.py` – Command line interface.
- `web_server.py` – Web routes and handlers.
- `settings.py` – Configuration management.
- `main.py` – Entry point: reads configuration, initializes UI, and starts the app.

## 7. Problem I Overcame

### Task Scheduling Boundaries:
- Issue: Confusing start/end time inclusivity led to bugs.
- Solution: Changed terminology to `starts_from` and `due_by` (both inclusive).
- Result: Clarified scheduling parameters, making the system more intuitive for both users and developers.

PROJECT HISTORY:
for when i merge with mian that has an updated readme
