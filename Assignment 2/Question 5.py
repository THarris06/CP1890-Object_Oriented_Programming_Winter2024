from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """
    A class to represent a task with a name ,description and due date.
    status() - The status of the task.
    """
    task_name: str
    task_description: str
    due_date: datetime

    def status(self):
        if self.due_date < datetime.now():
            return "Pending"
        elif self.due_date >= datetime.now():
            return "Completed"


@dataclass
class Homework(Task):
    """
    A class to represent a Homework task with a name ,description and due date and adding subject as an attribute.
    status() - The status of the task and is override to have a not started and in progress status.
    """
    subject: str

    def __init__(self, task_name, task_description, due_date, subject):
        super().__init__(task_name, task_description, due_date)
        self.subject = subject

    def status(self):
        if self.due_date < datetime.now():
            return "Not Started"
        elif self.due_date >= datetime.now():
            return "Completed"
        else:
            return "In Progress"


@dataclass
class Meeting(Task):
    """
    A class to represent a Meeting task with a name ,description and due date and adding location as an attribute
    status() - The status of the task and is override to have a scheduled and in Happened status
    """
    location: str

    def __init__(self, task_name, task_description, due_date, location):
        super().__init__(task_name, task_description, due_date)
        self.location = location

    def status(self):
        if self.due_date < datetime.now():
            return "Scheduled"
        elif self.due_date >= datetime.now():
            return "Happened"


def main():
    homework = Homework("math homework", 'complete exercises 1-5', datetime(2023, 10, 15), "Math")
    meeting = Meeting("Team meeting", "Discuss project updates", datetime(2023, 9, 20), "Office A")

    print("Homework")
    print("Task Name:", homework.task_name)
    print("Task Description:", homework.task_description)
    print("Due Date:", homework.due_date)
    print("Subject:", homework.subject)
    print("Status:", homework.status())
    print()
    print("Meeting")
    print("Task Name:", meeting.task_name)
    print("Task Description:", meeting.task_description)
    print("Due Date:", meeting.due_date)
    print("Location:", meeting.location)
    print("Status:", meeting.status())


if __name__ == "__main__":
    main()
