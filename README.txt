Project Setup & Running Instructions

🚀 Quick Start (Mac Users)
This project was developed on macOS, so all instructions assume you’re using a Mac.

git clone <your-repo-url>
cd SomeDeviousProject
poetry install  # Install dependencies
poetry run python main.py  # Run the program
🔧 Advanced Setup & Configuration
1️⃣ Install Poetry (Dependency Management)

If you haven’t installed Poetry yet, run:

curl -sSL https://install.python-poetry.org | python3 -
poetry --version  # Verify installation
2️⃣ Initialize Poetry (Only If Needed)

Navigate to the project folder:

cd /path/to/your/project
poetry init  # First-time setup (only if pyproject.toml is missing)
3️⃣ Running the Project

poetry run python main.py
📌 Notes for Future Me (In Case I Forget)

📦 Updating Dependencies
If you add new packages or update dependencies, inside the Poetry virtual environment, run:

pip freeze > requirements.txt
To install the dependencies in another environment:

pip install -r requirements.txt
To check installed packages in the current environment:

pip list
🛠 Git Workflow Cheatsheet

📌 Setting Up a Git Repository

git clone <repo-url>  # Clone a repo
cd <repo-folder>  # Move into the repo folder
📝 Making Changes & Pushing to GitHub

git status  # See what changed
git add .  # Stage all changed files
git commit -m "Your commit message"  # Commit changes
git push origin main  # Push changes to GitHub
🔄 Pulling Changes (If Working in a Team)

git pull origin main  # Pull the latest changes
🔍 Type Checking (Add Notes Later)

Add instructions for pytype and mypy here when needed.
🛠 Converting Pip-Based Dependencies to Poetry

If you need to scan through files for dependencies and convert them to Poetry:

pip uninstall pipreqs  # Uninstall pipreqs if needed
pipreqs . --force  # Generate requirements.txt
cat requirements.txt | xargs poetry add  # Convert dependencies to Poetry
🔄 Ensuring Reproducibility with Poetry

poetry lock  # Lock dependencies for reproducibility
🐍 Managing Python Versions in Poetry
Poetry defaults to using system Python, but you can force it to use your pyenv version:

poetry env use $(pyenv which python)
If that doesn’t work, manually specify:

poetry env use /Users/yourname/.pyenv/versions/<desired_version>/bin/python
To make sure all environments use pyenv, run:

poetry config virtualenvs.prefer-active-python true

Helpful notes on poetry
also TOML requires boolean values to be lowercase.
By default, if you don’t set an upper bound in your project’s pyproject.toml, Poetry might assume a broader range (possibly including Python 4.0.0)
to run evneryhtin inside a vienv in poetry: poetry shell



For me: 
textual docs: https://textual.textualize.io
Additonally im using Black for formatting so: 
# for formatting, black {source_file_or_directory}

To run mypy:
mypy .

python -m cProfile -s time your_script.py
This runs your script with Python’s built-in profiler, cProfile, sorting the output by execution time (the -s time option). It shows you which functions take the most time, so you can identify bottlenecks.

snakeviz profile.prof
After saving your profiling results (for example, by redirecting cProfile output to profile.prof), you can run this command to launch Snakeviz—a graphical, web-based viewer that makes it easier to explore the profiling data visually.


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
