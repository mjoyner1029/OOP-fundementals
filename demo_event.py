# demo_event.py
from event import Event

def main():
    # Create an instance of Event
    seminar = Event("Tech Conference", "2024-09-30")

    # Print initial event details
    print(seminar)

    # Add participants
    seminar.add_participant()
    seminar.add_participant()

    # Print updated event details
    print(seminar)

    # Get participant count
    count = seminar.get_participant_count()
    print(f"Total participants: {count}")

if __name__ == "__main__":
    main()
