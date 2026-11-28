class BasicClass:
    """
    A simple class demonstrating the use of the `self` keyword.
    It stores a name and an age, and provides methods to set and retrieve these attributes.
    """

    def __init__(self, name: str = "", age: int = 0) -> None:
        """
        Initialize a new instance of BasicClass.

        :param name: The name associated with the instance.
        :param age: The age associated with the instance.
        """
        self.name = name
        self.age = age

    def set_details(self, name: str, age: int) -> None:
        """
        Set the name and age for the instance.

        :param name: The new name.
        :param age: The new age.
        """
        self.name = name
        self.age = age

    def get_details(self) -> str:
        """
        Retrieve a formatted string containing the instance's details.

        :return: A string in the format "<name> is <age> years old".
        """
        return f"{self.name} is {self.age} years old"

    def increment_age(self, years: int = 1) -> None:
        """
        Increment the stored age by a given number of years.

        :param years: Number of years to add to the current age (default is 1).
        """
        self.age += years

    def __repr__(self) -> str:
        """
        Official string representation of the object.
        """
        return f"BasicClass(name={self.name!r}, age={self.age!r})"