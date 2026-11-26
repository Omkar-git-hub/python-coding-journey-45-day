"""
basic_class.py

A simple example of a Python class demonstrating basic object-oriented programming concepts.
"""

class BasicClass:
    """
    A basic class that holds a name and an age, and provides methods to interact with these attributes.
    """

    def __init__(self, name: str, age: int = 0):
        """
        Initialize a new instance of BasicClass.

        Parameters:
            name (str): The name of the instance.
            age (int, optional): The age of the instance. Defaults to 0.
        """
        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        Return a greeting string that includes the instance's name.

        Returns:
            str: A greeting message.
        """
        return f"Hello, my name is {self.name}."

    def have_birthday(self) -> None:
        """
        Increment the age of the instance by one year.
        """
        self.age += 1

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the instance.

        Returns:
            str: The representation string.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the instance.

        Returns:
            str: The readable string.
        """
        return f"{self.name} is {self.age} years old."