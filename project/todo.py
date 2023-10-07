tasks = []

while True:
    print("Options:\nEnter 'add' to add a task\nEnter 'view' to view tasks\nEnter 'done' to mark a task as done\nEnter 'remove' to remove a task\nEnter 'exit' to exit the program")
    user_input = input(": ")
    if user_input == "exit":
        break
    elif user_input == "add":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
    elif user_input == "view":
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{index}. [{status}] {task['task']}")
    elif user_input == "done":
        index = int(
            input("Enter the task number you want to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    elif user_input == "remove":
        index = int(input("Enter the task number you want to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    else:
        print("Invalid input. Please try again.")
