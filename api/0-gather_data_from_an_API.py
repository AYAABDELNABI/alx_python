import requests
import sys

def getEmployeeAndTodo(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    res = requests.get(url)
    todos = res.json()

    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    res = requests.get(url)
    employee = res.json()

    completed_tasks = sum(1 for todo in todos if todo['completed'])
    all_tasks = len(todos)

    print(f"Employee {employee['name']} is done with tasks({completed_tasks}/{all_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"what is the id: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    id = sys.argv[1]
    getEmployeeAndTodo(id)