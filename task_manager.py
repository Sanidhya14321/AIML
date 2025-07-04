import os

# File to store tasks
TASK_FILE = 'tasks.txt'

# Load tasks from the file
def load_tasks():
    tasks={}
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task_id, title, status= line.strip().split('|')
                tasks[task_id] = {'title': title, 'status': status}
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}|{task['title']}|{task['status']}\n")

# Add a new task
def add_task(tasks):
    title= input("Enter task title: ")
    task_id=max(tasks.keys(), default=0)+1
    tasks[task_id] = {'title': title, 'status': 'pending'}
    print(f"Task {title} added with ID: {task_id}")
    save_tasks(tasks)
    
# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    print("Tasks:")
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")
        
# Update a task's status
def mark_task_complete(tasks):
    task_id = input("Enter task ID to mark as complete: ")
    if task_id in tasks:
        tasks[task_id]['status'] = 'completed'
        print(f"Task {tasks[task_id]['title']} marked as completed.")
        save_tasks(tasks)
    else:
        print("Task ID not found.")
        
# Delete a task
def delete_task(tasks):
    task_id = input("Enter task ID to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
        save_tasks(tasks)
    else:
        print("Task ID not found.")

# Main function to run the task manager
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
