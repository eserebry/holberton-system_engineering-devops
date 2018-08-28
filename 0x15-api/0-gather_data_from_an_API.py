#!/usr/bin/python3
''' Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''

import requests
import sys


def todo():
    ''' returns information about user TODO list progress'''
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    tr = "https://jsonplaceholder.typicode.com/todos?userId={}&&completed=true"
    todo_true = requests.get(tr.format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    name = user.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todo_true), len(todo)))
    for task in todo:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))

if __name__ == "__main__":
    todo()
