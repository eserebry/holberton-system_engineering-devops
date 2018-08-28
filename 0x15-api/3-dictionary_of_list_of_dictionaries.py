#!/usr/bin/python3
''' Using this REST API, for a given employee ID,
export data in the JSON format.'''

import json
import requests
import sys


def todo_json():
    ''' exports data in the JSON format.'''
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    name = user.get("username")
    with open("{}.json".format(user_id), "w") as jsonfile:
        data = {user_id: []}
        for task in todo:
            tasks = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": name}
            data[user_id].append(tasks)
        json.dump(data, jsonfile)

if __name__ == "__main__":
    todo_json()
