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
    filename = "todo_all_employees.json"
    all_dict = {}
    user_dict = {}

    with open(filename, "w") as jsonfile:
        data = {user_id: []}
        for us in user:
            us = {us_id = user.get("id")
                  all_us[us_id] = []
                  user_dic[us_id] = us.get("username")}
        for task in todo:
            tasks = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": name}
            data[user_id].append(tasks)
        json.dump(data, jsonfile)

if __name__ == "__main__":
    todo_json()
