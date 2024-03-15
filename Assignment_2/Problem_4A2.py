from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def get_duration(self):
        return self.end_date.day - self.start_date.day


@dataclass
class Conference(Event):
    def __init__(self, name, location, start_date, end_date, attendees):
        super().__init__(name, location, start_date, end_date)
        self.attendees = attendees

    def get_duration(self):
        return (self.end_date.day - self.start_date.day) * 24


def main():
    event = Event("Birthday Party", "New York", datetime(2023, 8, 25), datetime(2023, 8, 26))
    conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9, 15), datetime(2023, 9, 17), 500)
    print("Event:")
    print("Name:", event.name)
    print("Location:", event.location)
    print("Start Date:", event.start_date)
    print("End Date:", event.end_date)
    print("Duration (days):", event.get_duration())
    print("\n")
    print("Conference:")
    print("Name:", conference.name)
    print("Location:", conference.location)
    print("Start Date:", conference.start_date)
    print("End Date:", conference.end_date)
    print("Attendees:", conference.attendees)
    print("Duration (hours):", conference.get_duration())


if __name__ == "__main__":
    main()
