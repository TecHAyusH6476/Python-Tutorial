class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_details):
        # for pushing the element to the list ( tasks )
        self.tasks.append(task_details)

    def display_all_tasks(self):
        for task in self.tasks:
            task.display_task_details()

    def mark_task_as_complete(self, title):
        for task in self.tasks:
            if task.title == title and not task.isCompleted:
                task.mark_task_completed()
                print("Task title= ", task.title, " is completed !!")
                return

        print("Task title= ", task.title, " is not found !!")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task title= ", task.title, " is deleted !!")
                return
        print("Task title= ", task.title, " is not found !!")
