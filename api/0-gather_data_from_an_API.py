#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of a given employee
from the JSONPlaceholder API (https://jsonplaceholder.typicode.com/).

It accepts one command-line argument:
    - An integer representing the employee ID.

It then retrieves the user's name and their list of tasks, printing the
number of completed tasks versus total tasks, followed by the titles of
completed tasks in a formatted output.

Example usage:
    python3 0-gather_data_from_an_API.py 2

Expected output format:
    Employee <NAME> is done with tasks(<#done>/<#total>):
         <Task Title 1>
         <Task Title 2>
         ...

Author: acele happy
Date: 2025-07-20
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), total_tasks
        )
    )
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
