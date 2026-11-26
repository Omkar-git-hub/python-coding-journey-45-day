class Person:
    """
    A simple Person class demonstrating class and instance attributes.
    
    Class attributes:
        species (str): The species of the person.
        eye_color (str): The default eye color for all persons.
    
    Instance attributes:
        name (str): The name of the person.
        age (int): The age of the person in years.
    """
    
    # Class attributes
    species = "Homo sapiens"
    eye_color = "brown"
    
    def __init__(self, name: str, age: int):
        """
        Initialize a new Person instance with a name and age.
        
        Parameters:
            name (str): The name of the person.
            age (int): The age of the person in years.
        """
        self.name = name
        self.age = age