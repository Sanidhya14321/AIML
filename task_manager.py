# import os

# # File to store tasks
# TASK_FILE = 'tasks.txt'

# # Load tasks from the file
# def load_tasks():
#     tasks={}
#     if os.path.exists(TASK_FILE):
#         with open(TASK_FILE, 'r') as file:
#             for line in file:
#                 task_id, title, status= line.strip().split('|')
#                 tasks[task_id] = {'title': title, 'status': status}
#     return tasks

# # Save tasks to the file
# def save_tasks(tasks):
#     with open(TASK_FILE, 'w') as file:
#         for task_id, task in tasks.items():
#             file.write(f"{task_id}|{task['title']}|{task['status']}\n")

# # Add a new task
# def add_task(tasks):
#     title= input("Enter task title: ")
#     task_id=int(max(tasks.keys(), default=0))+1
#     tasks[task_id] = {'title': title, 'status': 'pending'}
#     print(f"Task {title} added with ID: {task_id}")
#     save_tasks(tasks)
    
# # View all tasks
# def view_tasks(tasks):
#     load_tasks()
#     if not tasks:
#         print("No tasks available.")
#     print("Tasks:")
#     for task_id, task in tasks.items():
#         print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")
        
# # Update a task's status
# def mark_task_complete(tasks):
#     load_tasks()
#     task_id = input("Enter task ID to mark as complete: ")
#     if task_id in tasks:
#         tasks[task_id]['status'] = 'completed'
#         print(f"Task {tasks[task_id]['title']} marked as completed.")
#         save_tasks(tasks)
#     else:
#         print("Task ID not found.")
        
# # Delete a task
# def delete_task(tasks):
#     task_id = input("Enter task ID to delete: ")
#     if task_id in tasks:
#         deleted_task = tasks.pop(task_id)
#         print(f"Task {deleted_task['title']} deleted.")
#         save_tasks(tasks)
#     else:
#         print("Task ID not found.")

# # Main function to run the task manager
# def main():
#     tasks = load_tasks()
#     while True:
#         print("\nTask Manager Menu:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Complete")
#         print("4. Delete Task")
#         print("5. Quit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             mark_task_complete(tasks)
#         elif choice == '4':
#             delete_task(tasks)
#         elif choice == '5':
#             print("Exiting Task Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
            
# if __name__ == "__main__":
#     main()

# # Export tasks to a json file
# import json
# def save_tasks(tasks):
#     with open('tasks.json', 'w') as f:
#         json.dump(tasks, f, indent=4)
# # Load tasks from a json file
# def load_tasks():
#     try:
#         with open('tasks.json', 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
# # Add a new task with json
# def add_task(tasks):
#     title = input("Enter task title: ")
#     task_id = str(max(map(int, tasks.keys()), default=0) + 1)
#     tasks[task_id] = {'title': title, 'status': 'pending'}
#     print(f"Task {title} added with ID: {task_id}")
#     save_tasks(tasks)
# # View all tasks with json
# def view_tasks(tasks):
#     tasks = load_tasks()
#     if not tasks:
#         print("No tasks available.")
#     else:
#         print("Tasks:")
#         for task_id, task in tasks.items():
#             print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")
# # Update a task's status with json
# def mark_task_complete(tasks):
#     tasks = load_tasks()
#     task_id = input("Enter task ID to mark as complete: ")
#     if task_id in tasks:
#         tasks[task_id]['status'] = 'completed'
#         print(f"Task {tasks[task_id]['title']} marked as completed.")
#         save_tasks(tasks)
#     else:
#         print("Task ID not found.")
# # Delete a task with json
# def delete_task(tasks):
#     tasks = load_tasks()
#     task_id = input("Enter task ID to delete: ")
#     if task_id in tasks:
#         deleted_task = tasks.pop(task_id)
#         print(f"Task {deleted_task['title']} deleted.")
#         save_tasks(tasks)
#     else:
#         print("Task ID not found.")
# # Main function to run the task manager with json
# def main():
#     tasks = load_tasks()
#     while True:
#         print("\nTask Manager")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Complete")
#         print("4. Delete Task")
#         print("5. Quit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             mark_task_complete(tasks)
#         elif choice == '4':
#             delete_task(tasks)
#         elif choice == '5':
#             print("Exiting Task Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# if __name__ == "__main__":
#     main()

# Support command-line arguments for quick task management
import sys
import json
import os
# Load tasks from file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    return {}
# Save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)
# Add a new task
def add_task(tasks, title):
    task_id = str(max(map(int, tasks.keys()), default=0) + 1)
    tasks[task_id] = {'title': title, 'status': 'pending'}
    print(f"Task '{title}' added with ID: {task_id}")
    save_tasks(tasks)
# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task_id, task in tasks.items():
            print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")
# Mark a task as complete
def mark_task_complete(tasks, task_id):
    if task_id in tasks:
        tasks[task_id]['status'] = 'completed'
        print(f"Task '{tasks[task_id]['title']}' marked as completed.")
        save_tasks(tasks)
    else:
        print("Task ID not found.")
# Delete a task
def delete_task(tasks, task_id):
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
        save_tasks(tasks)
    else:
        print("Task ID not found.")
# Main function to handle command-line arguments
def main():
    tasks = load_tasks()
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add/view/complete/delete] [args...]")
        return  
    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py add [task title]")
        else:
            title = ' '.join(sys.argv[2:])
            add_task(tasks, title)
    elif command == 'view':
        view_tasks(tasks)
    elif command == 'complete':
        if len(sys.argv) != 3:
            print("Usage: python task_manager.py complete [task ID]")
        else:
            task_id = sys.argv[2]
            mark_task_complete(tasks, task_id)
    elif command == 'delete':
        if len(sys.argv) != 3:
            print("Usage: python task_manager.py delete [task ID]")
        else:
            task_id = sys.argv[2]
            delete_task(tasks, task_id)
    else:
        print("Unknown command. Use 'add', 'view', 'complete', or 'delete'.")

if __name__ == "__main__":
    main()
