#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user information
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    user = user_response.json()

    # Get user's todos
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = 0

    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks, total_tasks))

    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
