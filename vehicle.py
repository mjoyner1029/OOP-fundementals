# vehicle.py

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """Update the vehicle's owner."""
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}.")

    def __str__(self):
        """Return a string representation of the vehicle."""
        return f"Vehicle {self.registration_number}: {self.vehicle_type}, Owner: {self.owner}"
