import json
import requests
import sys

def get_tasks_by_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    tasks = response.json()
    return tasks

def export_to_json(tasks, user_id):
    data = {user_id: []}

    for task in tasks:
        data[user_id].append({
            'task': task['title'],
            'completed': task['completed'],
            'username': task['username']
        })

    json_filename = f'{user_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 2-export_to_JSON.py <user_id>')
        sys.exit(1)

    user_id = sys.argv[1]
    tasks = get_tasks_by_user(user_id)
    export_to_json(tasks, user_id)
    print(f'JSON file "{user_id}.json" has been created.')