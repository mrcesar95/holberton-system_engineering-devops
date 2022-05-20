#!/usr/bin/python3
"""Gather data from API"""

from requests import get
from sys import argv, exit
import json

if __name__ == "__main__":
    try:
        id = argv[1]
        is_integer = int(id)
    except Exception:
        exit()

    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users?id=" + id
    url_todos = url + "todos?userId=" + id

    request_user = get(url_user)
    request_todos = get(url_todos)
    # Connection and have an access to the json
    try:
        jsuser = request_user.json()
        jstodos = request_todos.json()
    except ValueError:
        print("No Json")

    # Assing values
    if jsuser and jstodos:
        USER_ID = id
        USERNAME = jsuser[0].get("username")

        # create the value of the dict f the final json file
        jslist = []
        for task in jstodos:
            TASK_TITLE = task.get("title")
            TASK_COMPLETED_STATUS = task.get("completed")
            # write the internal dict
            taskdict = {"task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": USERNAME}
            jslist.append(taskdict)

        # create the final dictionary
        jsresult = {USER_ID: jslist}

        # generate the json file
        with open(id + ".json", "w", newline="") as jsonfile:
            json.dump(jsresult, jsonfile)
