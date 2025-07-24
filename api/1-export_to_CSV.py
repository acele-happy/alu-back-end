#!/usr/bin/python3
"""export csv"""

import csv
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

    csv_data = [["{}".format(i["userId"]),
                 employee["username"],
                 "{}".format(i["completed"]), i["title"]] for i in todo_data]

    with open("{}.csv".format(employee["id"]), 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(csv_data)
