#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    total_tasks = len(todos)
    done_tasks = 0

    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
