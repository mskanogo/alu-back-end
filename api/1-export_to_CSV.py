#!/usr/bin/python3

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    user = user_response.json()

    # Get todos
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )
    todos = todos_response.json()

    filename = "{}.csv".format(user_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                user_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])
