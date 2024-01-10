employees = [
    {"name": "matt", "manager": None},
    {"name": "alice", "manager": "fred"},
    {"name": "fred", "manager": "matt"},
]

def sort_employees(employees):
    """Sorts a list of employees so that managers appear before their subordinates."""

    dependencies = {}  # Map employee names to their managers
    for employee in employees:
        manager = employee.get("manager")
        if manager:
            dependencies.setdefault(manager, []).append(employee["name"])

    sorted_employees = []
    ready = [employee for employee in employees if employee["manager"] is None]
    while ready:
        employee = ready.pop(0)
        sorted_employees.append(employee)
        subordinates = dependencies.pop(employee["name"], [])
        ready.extend(
            employee
            for employee in employees
            if employee["name"] in subordinates and dependencies.get(employee["name"])
        )
        ready.extend(
            employee
            for employee in employees
            if employee["name"] in subordinates and not dependencies.get(employee["name"])
        )

    return sorted_employees

sorted_employees = sort_employees(employees)
print(f"Sorted list of employees: {[employee['name'] for employee in sorted_employees]}")