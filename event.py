# event.py

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        """Increase the participant count by 1."""
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        """Retrieve the current participant count."""
        return self.participant_count

    def __str__(self):
        """Return a string representation of the event."""
        return f"Event: {self.name}, Date: {self.date}, Participants: {self.participant_count}"
