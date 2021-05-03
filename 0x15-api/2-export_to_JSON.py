#!/usr/bin/python3
"""
Exports task #0 into the JSON format,
lists all tasks owned by a specified user id
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    USER_ID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(USER_ID)).json()
    USERNAME = user.get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(USER_ID)).json()

    json_dict = {}
    json_dict[USER_ID] = [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": USERNAME} for task in tasks]

    with open('{}.json'.format(user.get("id")), mode='w') as jsonfile:
        json.dump(json_dict, jsonfile)
