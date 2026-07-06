
class Dog:
    # Class variable (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, breed, name):
        # Instance variables (unique to each dog)
        self.breed = breed
        self.name = name

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 30)


# Create two Dog objects of different breeds
dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")

# Display their details
dog1.show_details()
dog2.show_details()
