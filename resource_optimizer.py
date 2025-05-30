import numpy as np
from ortools.linear_solver import pywraplp

# Machine hours and task time matrix
machine_capacity = [8, 10, 12]
task_time = [
    [2, 3, 1],   # Task 1
    [3, 2, 4],   # Task 2
    [4, 3, 2]    # Task 3
]

solver = pywraplp.Solver.CreateSolver('SCIP')
x = []

# Create variables
for i in range(len(task_time)):
    x.append([])
    for j in range(len(task_time[0])):
        x[i].append(solver.IntVar(0, 1, f'x[{i}][{j}]'))

# Constraints
for i in range(len(task_time)):
    solver.Add(sum(x[i][j] for j in range(len(task_time[0]))) == 1)

for j in range(len(task_time[0])):
    solver.Add(sum(x[i][j] * task_time[i][j] for i in range(len(task_time))) <= machine_capacity[j])

# Objective
solver.Maximize(sum(x[i][j] for i in range(len(task_time)) for j in range(len(task_time[0]))))

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Optimized task allocation:")
    for i in range(len(task_time)):
        for j in range(len(task_time[0])):
            if x[i][j].solution_value() > 0:
                print(f"Task {i+1} → Machine {j+1}")
