
class BMW:
    def __init__(self, model):
        self.model = model

    def speed(self):
        return f"{self.model} (BMW) has a top speed of 250 km/h."

    def fuel_type(self):
        return f"{self.model} (BMW) uses petrol."


class Ferrari:
    def __init__(self, model):
        self.model = model

    def speed(self):
        return f"{self.model} (Ferrari) has a top speed of 350 km/h."

    def fuel_type(self):
        return f"{self.model} (Ferrari) uses premium petrol."


# Function to demonstrate polymorphism
def car_details(car):
    print(car.speed())
    print(car.fuel_type())
    print("-" * 40)


# Create objects
bmw_car = BMW("BMW X5")
ferrari_car = Ferrari("Ferrari F8")

# Call the same function with different objects
car_details(bmw_car)
car_details(ferrari_car)
