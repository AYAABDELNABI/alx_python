import json
import requests
import sys

def get_employee_info(employee_id):
    """
    Retrieves employee information and exports their TODO list in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Get employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Create JSON data
    json_data = {str(employee_id): []}
    for todo in todo_data:
        json_data[str(employee_id)].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_name
        })

    # Export JSON data to file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"TODO list exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
    
    import json
import requests
import sys

def get_employee_info(employee_id):
    """
    Retrieves employee information and exports their TODO list in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Get employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Create JSON data
    json_data = {str(employee_id): []}
    for todo in todo_data:
        json_data[str(employee_id)].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_name
        })

    # Export JSON data to file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"TODO list exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)