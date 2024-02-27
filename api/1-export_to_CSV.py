import csv
import requests
import sys

def get_tasks_by_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    tasks = response.json()
    return tasks

def export_to_csv(tasks, user_id):
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    csv_filename = f'{user_id}.csv'

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': task['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']).lower(),
                'TASK_TITLE': task['title']
            })

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 1-export_to_CSV.py <user_id>')
        sys.exit(1)

    user_id = sys.argv[1]
    tasks = get_tasks_by_user(user_id)
    export_to_csv(tasks, user_id)
    print(f'CSV file "{user_id}.csv" has been created.')