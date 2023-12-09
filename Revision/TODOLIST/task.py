# title desc completed


class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.isCompleted = False

    def display_task_details(self):
        print(
            "Title = ",
            self.title,
            "\n Description = ",
            self.desc,
            "\n Completed = ",
            self.isCompleted,
        )

    def mark_task_completed(self):
        self.isCompleted = True
