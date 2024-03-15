from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Task:
    def __init__(self, task_name: str = '', task_description: str = '', due_date: datetime = None):
        self.task_name = task_name
        self.task_description = task_description
        self.due_date = due_date

    def status(self):
        if self.due_date < datetime.now():
            return "Completed"
        elif self.due_date > datetime.now():
            return "Pending"


@dataclass
class Homework(Task):
    def __init__(self, task_name: str = '', task_description: str = '', due_date: datetime = None, subject: str = ''):
        super().__init__(task_name, task_description, due_date)
        self.subject = subject

    def status(self):
        if self.due_date > datetime.now() + timedelta(weeks=4):
            return "Not Started"
        elif self.due_date > datetime.now():
            return "Pending"
        elif self.due_date < datetime.now():
            return "Completed"


@dataclass
class Meeting(Task):
    def __init__(self, task_name: str = '', task_description: str = '', due_date: datetime = None, location: str = ''):
        super().__init__(task_name, task_description, due_date)
        self.location = location

    def status(self):
        if self.due_date > datetime.now():
            return "Scheduled"
        elif self.due_date < datetime.now():
            return "Happened"


def main():
    homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2024,
                                                                            3, 20), "Math")
    meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2024,
                                                                          9, 20), "Office A")
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
