from tabulate import tabulate


# Define the structure of your schedule
schedule = {
    "7:00": {"Task A": 3, "Task B": 1},
    "8:00": {"Task C": 2},
    # Add as many time slots and tasks as needed...
    "Windowed": [("Task D", "9:00-11:00", 2)]  # (Task, Time Window, People)
}

# Function to print the schedule
def print_schedule(schedule):
    # Find the longest task list to determine column width
    max_tasks = max(len(tasks) for tasks in schedule.values() if isinstance(tasks, dict))
    
    # Print the header
    print("Time", end="")
    for i in range(max_tasks):
        print(f"\tTask {i+1}\tPeople", end="")
    print("\n" + "-" * 80)
    
    # Print the tasks for each time slot
    for time, tasks in schedule.items():
        if time != "Windowed":
            print(time, end="")
            if isinstance(tasks, dict):
                for task, people in tasks.items():
                    print(f"\t{task}\t{people}", end="")
            print()
    
    # Print windowed tasks
    print("\nWindowed Tasks:")
    for task, window, people in schedule["Windowed"]:
        print(f"{task} can occur between {window} for {people} people")
        
# Call the function to print the schedule
print_schedule(schedule)


# Let's say you have a list of tasks, each task is a dictionary with its details
tasks = [
    {"Time": "7:00", "Task": "Task A", "Assigned People": 3, "Total Periods": 2, "Window": "7:00-9:00"},
    {"Time": "8:00", "Task": "Task B", "Assigned People": 2, "Total Periods": 1, "Window": "-"},
    # ... other tasks
]

# Convert the list of dictionaries to a list of lists for tabulate
table = [[task["Time"], task["Task"], task["Assigned People"], task["Total Periods"], task["Window"]] for task in tasks]

# Print the table
print(tabulate(table, headers=["Time", "Task", "Assigned People", "Total Periods", "Window"], tablefmt="grid"))
