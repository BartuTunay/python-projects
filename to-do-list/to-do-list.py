tasks = []

def add_task():
    adding = input("What you like to add?: ").strip()
    if len(adding) == 0:
        print("Please add a actual task")
        return
    tasks.append(adding)
    save_tasks()


def show_task():
    if len(tasks) == 0:
        print("No tasks yet! ")
    else:
        for i, x in enumerate(tasks, start= 1):
            print(f"-- {i}. {x} --")

def delete_task():
    if len(tasks) == 0:
        print("Task no exist")
        return
    try:
        deleting = int(input("Which task would you like to delete? "))
    except ValueError:
        print("Please enter a number of your task")
        return
    if deleting <= 0 or deleting > len(tasks):
        print("Please enter a valid number")
    else:
        deleted_task = tasks.pop(deleting - 1)
        print(f"Deleted: {deleted_task} ")
        save_tasks() 

def load_tasks():
    try:
        with open ("tasks.txt", "r") as f:
            for task in f:
                clean_task = task.strip()
                tasks.append(clean_task)
    except FileNotFoundError:
        pass

def save_tasks():
    with open ("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

load_tasks()

print("----- TO DO LIST -----")

while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    try:
        choice = int(input("Hello Sir, Which option would like to do?: "))
    except ValueError:
        print("Please enter a number for Choose")
        continue

    if choice == 1:
        add_task()
    elif choice == 2:
        show_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        print("Okay, Goodbye!")
        break
    else:
        print("Please enter a valid number!")
        continue    

