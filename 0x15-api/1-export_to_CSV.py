#!/usr/bin/python3
"""
Exports task #0 into CSV format,
lists all tasks owned by a specified user id
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    USER_ID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(USER_ID)).json()
    USERNAME = user.get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(USER_ID)).json()

    with open("{}.csv".format(USER_ID), mode='w') as f:
        fh = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            fh.writerow([USER_ID, USERNAME, task.get("completed"),
                         task.get("title")])
