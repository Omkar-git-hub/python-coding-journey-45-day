class Person:
    """
    A simple Person class demonstrating instance methods and a class attribute.

    Attributes
    ----------
    name : str
        The name of the person.
    age : int
        The age of the person.

    Class Attributes
    ----------------
    species : str
        Species of all Person instances.
    """

    species = "Homo sapiens"

    def __init__(self, name: str, age: int):
        """
        Initialize a new Person instance.

        Parameters
        ----------
        name : str
            The person's name.
        age : int
            The person's age.
        """
        self.name = name
        self.age = age

    # Instance methods for accessing and modifying attributes
    def get_name(self) -> str:
        """Return the person's name."""
        return self.name

    def set_name(self, new_name: str) -> None:
        """Set a new name for the person."""
        self.name = new_name

    def get_age(self) -> int:
        """Return the person's age."""
        return self.age

    def set_age(self, new_age: int) -> None:
        """Set a new age for the person."""
        self.age = new_age

    def display_info(self) -> str:
        """
        Return a formatted string containing the person's details.

        Returns
        -------
        str
            Formatted information string.
        """
        return f"{self.name} is {self.age} years old and belongs to the species {self.species}."