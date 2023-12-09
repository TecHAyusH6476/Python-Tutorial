from task import Task
from todolist import TodoList


def main():
    todoObj = TodoList()

    while True:
        print("\n ----- Todo List ----- \n")
        print("\n1. Add Task \n")
        print("\n2. Display All task \n")
        print("\n3. Mark task as complete \n")
        print("\n4. Delete task \n")
        print("\n5. End the code!!! \n")

        choice = int(input("Enter your choice!!"))

        if choice == 1:
            title = input("Enter title for task = ")
            description = input("Enter desc for task = ")

            new_task = Task(title=title, desc=description)  # actual parameters
            todoObj.add_task(task_details=new_task)
            print("Task title= ", new_task.title, " is created !!")

        elif choice == 2:
            print("\n All the tasks in TODO list =")
            todoObj.display_all_tasks()

        elif choice == 3:
            title = input("Enter the title of the task to mark as completed = ")
            todoObj.mark_task_as_complete(title=title)
            print("Task title= ", title, " is marked as completed !!")

        elif choice == 4:
            title = input("Enter the title of the task to be deleted = ")
            todoObj.delete_task(title=title)
            print("Task title= ", title, " is deleted !!")

        elif choice == 5:
            print("EXIT!!")
            break

        else:
            print("Invalid Choice !!!! ")


if __name__ == "__main__":
    main()
