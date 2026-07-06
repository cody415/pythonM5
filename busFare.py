
class Vehicle:
    def __init__(self, name, capacity, fare_per_person):
        # Instance variables
        self.name = name
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def fare(self):
        # Base fare calculation
        return self.capacity * self.fare_per_person


# Bus class inherits from Vehicle
class Bus(Vehicle):
    def fare(self):
        # Add 10% extra charge for maintenance
        total_fare = super().fare()
        return total_fare + (0.10 * total_fare)


# Create a Bus object
school_bus = Bus("School Bus", 50, 20)

# Display details
print("Vehicle Name:", school_bus.name)
print("Capacity:", school_bus.capacity)
print("Fare per Person:", school_bus.fare_per_person)
print("Total Fare:", school_bus.fare())
