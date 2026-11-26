class Person:
    """
    Simple Person class with name and age attributes.
    Provides a greeting method and a readable representation.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a friendly greeting."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


def create_person(name: str, age: int) -> Person:
    """
    Factory function that creates and returns a Person instance.

    Args:
        name: The person's name.
        age: The person's age.

    Returns:
        An instance of Person with the provided name and age.
    """
    return Person(name, age)