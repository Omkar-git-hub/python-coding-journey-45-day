class BasicClass:
    """
    A simple class demonstrating constructor usage.
    """

    def __init__(self, name: str = "John Doe", age: int = 30):
        """
        Initialize a new BasicClass instance.

        Parameters:
            name (str): The name of the person. Defaults to "John Doe".
            age (int): The age of the person. Defaults to 30.
        """
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"