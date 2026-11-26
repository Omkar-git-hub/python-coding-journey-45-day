class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed} and belongs to the {self.species} species."


dog = Dog("Rex", "Labrador")
print(dog.describe())
print(f"Species: {Dog.species}")