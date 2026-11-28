import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_attributes import Dog


def test_class_attribute_exists():
    assert hasattr(Dog, "species")


def test_class_attribute_value():
    assert Dog.species == "Canine"


def test_instance_accesses_class_attribute():
    dog = Dog("Rex", "Labrador")
    assert dog.species == "Canine"


def test_describe_includes_species():
    dog = Dog("Rex", "Labrador")
    assert "Canine" in dog.describe()


def test_describe_includes_name_and_breed():
    dog = Dog("Buddy", "Poodle")
    assert "Buddy" in dog.describe()
    assert "Poodle" in dog.describe()