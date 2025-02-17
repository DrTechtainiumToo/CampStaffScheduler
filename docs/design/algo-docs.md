
# Scheduling Algorithm Overview

## Basic Scheduling Process Overview

```markdown
Start
|
|--> Initialize Schedule
|     |--> Create Time Slot Queues
|
|--> Populate Queues with Tasks
|     |--> Find Tasks for Each Time Slot
|     |--> Sort Tasks by Duration
|     |--> Sort Tasks by Tier
|     |--> Collect Windowed Tasks
|
|--> Assign Tasks For Each Time Period
      |--> Calculate Available Employees In Period
      |--> For Each Task in Queue:
            |--> Check if employees are available
                  |--> Calculate Time Slots Needed
                  |--> Select Employees
                  |--> Assign Employees to Task
                  |--> Update Task and Employee Data
            |
      |--> Roll over remaining windowed tasks to next period
      |--> Log unscheduled non-windowed tasks
| --> Notify user if any tasks could not be scheduled
End
```

# Task Population and Sorting

## Populating the Queue

1. **Finding Tasks**: Identify tasks that match the current time slot.
2. **Sorting Tasks**:
   - By **duration** (longest tasks first).
   - By **tier** (prioritizing high-importance tasks).
3. **Handling Special Tasks**:
   - Collect windowed tasks separately.
   - Allow flexible scheduling when applicable.

---

# Constraint Logic for Scheduling

## Features
- **General Availability**: Is the employee available during the required times?
- **Basic Skill Match**: Does the employee have the basic skills for the task?

## Individual Screening Function
- Screens individuals based on required certifications and other criteria.
- Handles edge cases efficiently.

## Probabilistic Assignment Table
- Generates probability tables for assignment.
- Adjusts based on availability and future task needs.

## Global Requirement Assessment
- Ensures feasibility before assigning tasks.
- Prioritizes personnel where they are most needed.

## Handling Tasks with No Initial Requirements
- Prevents over-assigning certified employees to unnecessary tasks.

## Dynamic Task References
- Ensures task names are dynamic to prevent broken references.
- Implements auto-updating and deletion mechanisms when tasks change.

## Preferences and Assignments
- Reads and applies employee preferences stored in key-value format.
- Ensures the assignment process respects these preferences when possible.

---

# Task Loop Overview

## Process:
1. **Check for Available Employees**.
2. **Determine Required Personnel**.
3. **Assign Employees Based on Task Type**:
   - **Non-windowed tasks** → Assign directly.
   - **Windowed tasks** → Assign if feasible within time limits.
4. **Handle Unscheduled Tasks**:
   - Log warnings for unscheduled tasks.
   - Roll over windowed tasks to the next period.

## Key Considerations:
- **`break` Statement**: Stops processing when no employees are available.
- **Rollover Handling**: Ensures unfinished tasks are carried over.
---

### 🚀 **Next Steps**
See [Todo List and Road Map](/docs/roadmap/todos-and-roadmap.md)