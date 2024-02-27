import json
import requests

def get_tasks_by_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    tasks = response.json()
    return tasks

def export_to_json():
    tasks_by_user = {}
    user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for user_id in user_ids:
        tasks = get_tasks_by_user(user_id)
        tasks_by_user[user_id] = [
            {"username": task["user"]["username"], "task": task["title"], "completed": task["completed"]}
            for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(tasks_by_user, f, indent=4)

if __name__ == '__main__':
    export_to_json()