todo_list = []

def show_tasks():
    if not todo_list:
        print("Ga ada task")

    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}.{task}")

def add_task(task):
    todo_list.append(task)
    print("Task ditambahkan")

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index-1)
        print(f"Sudah dihapus: {removed}")
    else:
        print("Invalid task number")

while True:
    print("\n=== To-Do List ===")
    print("1, View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Ayo pilih (1-4): ")

    if choice =='1':
        show_tasks()
    elif choice == '2':
        task = input("Masukin task: ")
        add_task(task)
    elif choice =='3':
        show_tasks()
        try:
            idx = int(input("Masukin task yg mau dihapus: "))
            delete_task(idx)
        except ValueError:
            print("Masukin yg bener")
    elif choice == '4':
        print("dadah!")
        break
    else:
        print("pilihan salah")