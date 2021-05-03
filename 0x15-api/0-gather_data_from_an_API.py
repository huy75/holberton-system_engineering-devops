#!/usr/bin/python3
"""
for a given employee ID, returns information about
his/her TODO list progress
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for task in todo:
        if task.get("completed"):
            TASK_TITLE.append(task.get("title"))
            NUMBER_OF_DONE_TASKS += 1

    EMPLOYEE_NAME = user.get("name")
    TOTAL_NUMBER_OF_TASKS = len(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print('\t {}'.format(task))
