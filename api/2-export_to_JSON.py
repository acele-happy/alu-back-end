#!/usr/bin/python3
"""export Json"""


import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_url = "https://jsonplaceholder\
.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder\
.typicode.com/users/{}/todos".format(employee_id)

    employee = requests.get(employee_url).json()
    employee_name = employee['name']

    todo_data = requests.get(todo_url).json()
    data = [{"task": i["title"],
             "completed": i["completed"],
             "username": employee["username"]} for i in todo_data]
    json_data = json.dumps({"{}".format(employee["id"]): data})
    with open("{}.json".format(employee["id"]), 'w', encoding='utf-8') as f:
        f.write(json_data)
