# main.py
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file("task_data.txt")

    while True:
        print("\n-:Task Management System:-")
        print("1. Add a New Task.")
        print("2. Display all Tasks.")
        print("3. Mark a Task as Completed.")
        print("4. Delete a Task.")
        print("5. Load Tasks from a File.")
        print("6. Save Tasks.")
        print("7. Exit.")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.add_task(name, description)
        elif choice == "2":
            print("\n Current Tasks:")
            task_manager.display_tasks()
        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Enter task number to mark as completed: "))
            task_manager.mark_completed(task_index)
        elif choice == "4":
            task_index=int(input("Enter task number to be deleted: "))
            task_manager.delete_task(task_index)
        elif choice == "5":
            file_name = input("Enter filename(path): ")
            task_index = int(input("Enter task number: "))
            task_manager.load_tasks_from_otherfile(file_name, task_index)
        elif choice == "6":
            task_manager.save_tasks_to_file("task_data.txt")
            print("Tasks saved.")
            break
        elif choice == "7":
            print("Do you want to save the changes you made to Task Manager and then Exit?")
            answer = input("Yes/No: ")
            if ((answer == "Yes") or (answer == "yes")):
                task_manager.save_tasks_to_file("task_data.txt")
                print("Tasks saved. Exiting...")
                break
            else:
                print("Exiting...")
                break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()