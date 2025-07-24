#!/usr/bin/python3
""" ToDo list """

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_url = "https://jsonplaceholder\
.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder\
.typicode.com/users/{}/todos".format(employee_id)

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']

    todo_data = requests.get(todo_url).json()

    num_completed_tasks = 0
    for task in todo_data:
        if task['completed']:
            num_completed_tasks += 1

    total_num_tasks = len(todo_data)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_num_tasks))

    for task in todo_data:
        if task['completed']:
            print("\t {}".format(task['title']))
