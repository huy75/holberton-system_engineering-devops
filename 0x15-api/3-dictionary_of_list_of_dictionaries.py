#!/usr/bin/python3
"""
Exports all tasks into the JSON format,
"""

if __name__ == "__main__":
    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    json_dict = {}

    for user in users:
        todo_list = []
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id'))).json()
        for task in todos:
            todo = {}
            todo["task"] = task.get("title")
            todo["completed"] = task.get("completed")
            todo["username"] = user.get("username")
            todo_list.append(todo)
        json_dict[user.get('id')] = todo_list

    with open('todo_all_employees.json', mode='w') as jsonfile:
        json.dump(json_dict, jsonfile)
