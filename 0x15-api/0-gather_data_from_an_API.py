#!/usr/bin/python3
"""Gather data from API"""
from requests import get
from sys import argv

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
        EMPLOYEE_NAME = jsuser[0].get("name")
        NUMBER_OF_DONE_TASKS = 0
        for task in jstodos:
            if task.get("completed") is True:
                TOTAL_NUMBER_OF_TASKS = len(jstodos)

        # Print first line
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))
        # Second and N lines
        for doing in jstodos:
            TASK_TITLE = doing.get("title")
            if doing.get("completed") is True:
                print("\t {}".format(TASK_TITLE))
