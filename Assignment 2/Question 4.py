
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    """
    Class representing events with name, location, start and end dates.
    Duration() - method for calculating length of an event in days.
    """
    name: str
    location: str
    start_date: datetime
    end_date: datetime

    def duration(self):
        return (self.end_date - self.start_date).days


@dataclass
class Conference(Event):
    """
    Class representing a Conference event with name, location, start and end dates and adding attendees.
    duration() - method for calculating length of the conference now outputting in hours instead of days.
    """
    attendees: int

    def __init__(self, name, location, start_date, end_date, attendees):
        super().__init__(name, location, start_date, end_date)
        self.attendees = attendees

    def duration(self):
        return (self.end_date - self.start_date).days * 24


def main():
    event = Event("Birthday Party", "new York", datetime(2023, 8, 25), datetime(2023, 8, 26))
    conference = Conference("Tech Conference", "San francisco", datetime(2023, 9, 15), datetime(2023, 9, 17), 500)

    print("Event:")
    print("Name:", event.name)
    print("Location:", event.location)
    print("Start Date:", event.start_date)
    print("End Date:", event.end_date)
    print("Duration (Days):", event.duration())
    print()
    print("Conference:")
    print("Name:", conference.name)
    print("Location:", conference.location)
    print("Start Date:", conference.start_date)
    print("End Date:", conference.end_date)
    print("Attendees:", conference.attendees)
    print("Duration (Hours):", conference.duration())


if __name__ == "__main__":
    main()
