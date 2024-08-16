# demo_vehicle.py
from vehicle import Vehicle

def main():
    # Create instances of Vehicle
    car1 = Vehicle("ABC123", "Sedan", "John Doe")
    car2 = Vehicle("XYZ789", "SUV", "Jane Smith")

    # Print initial details
    print(car1)
    print(car2)

    # Update the owner of car1
    car1.update_owner("Alice Johnson")

    # Print updated details
    print(car1)

if __name__ == "__main__":
    main()
