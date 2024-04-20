from ortools.sat.python import cp_model

"""Import the required libraries,
Declare the solver,
Create the variables,
Define the constraints,
Define the objective function,
Invoke the solver and
Display the results."""


def main():
    # Create the model
    model = cp_model.CpModel()

    # Create the variables
    x = {} # x[task_id, employee_id, time_slot] = model.NewBoolVar('x[%i,%i,%i]' % (task_id, employee_id, time_slot))
    # x[task_id, employee_id, time_slot] = model.NewBoolVar('x[%i,%i,%i]' % (task_id, employee_id, time_slot))
     
    # Create the constraints


    # Tasks must not overlap
    model.AddNoOverlap([model.NewIntervalVar(tasks[i], durations[i], tasks_end[i], f'interval_{i}') for i in range(num_tasks)])
    
    # Tasks must be assigned to an available employee
    # Tasks must be assigned to qualified person
        #Cert
        #Gender
    # Tasks req people must not take people with skills needed for other tasks in the same period that have yet to be scheduled and would leave it short of people
    # Tasks must try to fill the min num of people req
    # Some tasks must occur at x time
    # Some tasks must occur for x time periods in a day
    # Some tasks can occur between x and y
        #some tasks must occur between x and y and be assigned to someone so there is no gap of the task not being done btwn periods
    # For windowed tasks, task can not be assigned so that its duration streches over its limit
    # Some Tasks must be consequitive
    # Some tasks cannot be assigned to the same person twice in a row
    # Some tasks must occur for a person ATLEAST once a day
    #S ome tasks can be merged
   
   
    #Availbility and qualification
    for task in tasks:
        for employee in employees:
            if not employee.is_available(task.time) or not employee.is_qualified(task): #TODO create is_qualified var
                model.Add(x[task.id, employee.id, task.time] == 0)

    #Min Staffing reqs
    for task in tasks:
        model.Add(sum(x[task.id, emp.id, task.time] for emp in employees) >= task.min_staff)

    
    #Time specific tasks (static)
    for task in tasks:
        if task.has_specific_time():
            model.Add(x[task.id, emp.id, task.specific_time] == 1 for emp in employees)

    #Consequtive tasks
    for task in tasks:
        for t in range(start_time, end_time - task.duration + 1):
            model.Add(sum(x[task.id, emp.id, t + dt] for dt in range(task.duration)) == task.duration for emp in employees)


    #Non-repetition and Distribution #TODO make so ok if get twice in day, but not back to back
    for employee in employees:
        for t in range(1, total_time_slots):
            model.Add(x[task.id, employee.id, t - 1] + x[task.id, employee.id, t] <= 1)

    #Windowed and Constrained Duration Tasks
    for task in tasks:
        if task.is_windowed:
            model.Add(sum(x[task.id, emp.id, t] for t in range(task.start_window, task.end_window + 1)) == task.duration for emp in employees)

    #Task Merging???? hwo would tell what is what with using only ints to rep
    # Example to conceptualize, implementation would depend on specific merge rules
    for task1, task2 in possible_merges:
        for t in time_slots:
            model.Add(x[task1.id, emp.id, t] + x[task2.id, emp.id, t] <= 1)

    
    
    
    # Define the objective (optional, e.g., minimize the latest end time)
    #model.Minimize(max(tasks_end))

    # Solve the problem
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Minimum end time: {solver.ObjectiveValue()}')
        print("Solution found!")
        for i in range(num_tasks):
            start = solver.Value(tasks[i])
            end = solver.Value(tasks_end[i])
            print(f'Task {i} starts at {start} and ends at {end}')
    else:
        print("No solution found.")

