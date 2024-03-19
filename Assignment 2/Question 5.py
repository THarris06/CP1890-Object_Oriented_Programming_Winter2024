# Question 5
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    task_name: str
    task_description: str
    due_date: datetime

    def status(self) -> str:
        if self.due_date > datetime.now():
            return "Pending"
        elif self.due_date <= datetime.now():
            return "Completed"


@dataclass
class Homework(Task):
    subject: str

    def __init__(self, task_name: str, task_description: str, due_date: datetime, subject: str):
        super().__init__(task_name, task_description, due_date)
        self.subject = subject

    def status(self) -> str:
        if self.due_date > datetime.now():
            return "Not Started"
        elif self.due_date < datetime.now():
            return "Completed"
        else:
            return "In progress"


@dataclass
class Meeting(Task):
    location: str

    def __init__(self, task_name: str, task_description: str, due_date: datetime, location: str):
        super().__init__(task_name, task_description, due_date)
        self.location = location

    def status(self) -> str:
        if self.due_date > datetime.now():
            return "Scheduled"
        elif self.due_date <= datetime.now():
            return "Happened"


def main():
    homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2023, 10, 15), "Math")
    meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2023, 9, 20), "Office A")

    print("Homework:")
    print("Task Name:", homework.task_name)
    print("Task Description:", homework.task_description)
    print("Due Date:", homework.due_date)
    print("Subject:", homework.subject)
    print("Status:", homework.status())

    print("\n")

    print("Meeting:")
    print("Task Name:", meeting.task_name)
    print("Task Description:", meeting.task_description)
    print("Due Date:", meeting.due_date)
    print("Location:", meeting.location)
    print("Status:", meeting.status())


if __name__ == "__main__":
    main()
