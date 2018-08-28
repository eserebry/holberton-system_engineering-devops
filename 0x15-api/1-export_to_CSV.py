#!/usr/bin/python3
''' using  REST API, for a given employee ID
export data in the CSV format'''

import csv
import requests
import sys


def todo_csv():
    ''' exports data in the CSV format'''
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    name = user.get("name")
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            file.writerow([user_id, user.get("username"),
                           task.get("completed"), task.get("title")])

if __name__ == "__main__":
    todo_csv()
