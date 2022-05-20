#!/usr/bin/python3
"""Gather data from API"""
from requests import get
from sys import argv, exit
import csv

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

        # export data in the csv file
        with open(id + ".csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=",", quotechar='"',
                quoting=csv.QUOTE_ALL)
            for task in jstodos:
                TASK_COMPLETED_STATUS = task.get("completed")
                TASK_TITLE = task.get("title")
                csv_writer.writerow(
                    [USER_ID, USERNAME,
                     TASK_COMPLETED_STATUS, TASK_TITLE])
