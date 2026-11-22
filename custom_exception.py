"""
Custom Exception Class

This module demonstrates how to create and use custom exception classes in Python.
Custom exceptions allow you to define your own error types with specific messages
and behaviors, making your code more expressive and easier to debug.
"""


class CustomError(Exception):
    """
    Base custom exception class.

    This serves as the foundation for all custom exceptions in this module.
    It extends the built-in Exception class and provides a default message.
    """

    def __init__(self, message="A custom error occurred", *args):
        self.message = message
        super().__init__(self.message, *args)

    def __str__(self):
        return self.message


class ValidationError(CustomError):
    """
    Exception raised when input validation fails.

    Attributes:
        field (str): The name of the field that failed validation.
        value: The invalid value that was provided.
    """

    def __init__(self, field, value, message=None):
        self.field = field
        self.value = value
        if message is None:
            message = f"Validation failed for field '{field}': value '{value}' is invalid"
        super().__init__(message)

    def __str__(self):
        return f"[ValidationError] {self.message} (field={self.field}, value={self.value})"


class DataNotFoundError(CustomError):
    """
    Exception raised when requested data is not found.

    Attributes:
        key: The key or identifier of the missing data.
    """

    def __init__(self, key, message=None):
        self.key = key
        if message is None:
            message = f"Data not found for key: '{key}'"
        super().__init__(message)

    def __str__(self):
        return f"[DataNotFoundError] {self.message} (key={self.key})"


class PermissionDeniedError(CustomError):
    """
    Exception raised when a user does not have permission to perform an action.

    Attributes:
        user (str): The username or identifier of the user.
        action (str): The action that was denied.
    """

    def __init__(self, user, action, message=None):
        self.user = user
        self.action = action
        if message is None:
            message = f"Permission denied for user '{user}' to perform action '{action}'"
        super().__init__(message)

    def __str__(self):
        return f"[PermissionDeniedError] {self.message} (user={self.user}, action={self.action})"


def validate_age(age):
    """
    Validate that an age is a positive integer.

    Args:
        age: The age value to validate.

    Returns:
        int: The validated age.

    Raises:
        ValidationError: If the age is not a positive integer.
    """
    if not isinstance(age, int):
        raise ValidationError(field="age", value=age, message="Age must be an integer")
    if age < 0:
        raise ValidationError(field="age", value=age, message="Age cannot be negative")
    if age > 150:
        raise ValidationError(field="age", value=age, message="Age is unrealistically high")
    return age


def find_user(users, user_id):
    """
    Find a user by their ID in a list of user dictionaries.

    Args:
        users (list): A list of user dictionaries, each with an 'id' key.
        user_id: The ID of the user to find.

    Returns:
        dict: The user dictionary if found.

    Raises:
        DataNotFoundError: If no user with the given ID exists.
    """
    for user in users:
        if user.get("id") == user_id:
            return user
    raise DataNotFoundError(key=user_id)


def perform_action(user, action, permissions):
    """
    Check if a user has permission to perform an action.

    Args:
        user (str): The username.
        action (str): The action to perform.
        permissions (dict): A dictionary mapping usernames to lists of allowed actions.

    Returns:
        str: A confirmation message if the action is permitted.

    Raises:
        PermissionDeniedError: If the user does not have permission for the action.
    """
    user_permissions = permissions.get(user, [])
    if action not in user_permissions:
        raise PermissionDeniedError(user=user, action=action)
    return f"User '{user}' successfully performed action '{action}'"


def main():
    """Demonstrate the usage of custom exception classes."""
    print("=" * 60)
    print("Custom Exception Classes Demonstration")
    print("=" * 60)

    # Demonstrate ValidationError
    print("\n1. Demonstrating ValidationError:")
    try:
        validate_age(-5)
    except ValidationError as e:
        print(f"   Caught: {e}")
        print(f"   Field: {e.field}, Value: {e.value}")

    try:
        validate_age("twenty")
    except ValidationError as e:
        print(f"   Caught: {e}")
        print(f"   Field: {e.field}, Value: {e.value}")

    # Demonstrate DataNotFoundError
    print("\n2. Demonstrating DataNotFoundError:")
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]

    try:
        user = find_user(users, 2)
        print(f"   Found user: {user['name']}")
    except DataNotFoundError as e:
        print(f"   Caught: {e}")

    try:
        user = find_user(users, 99)
    except DataNotFoundError as e:
        print(f"   Caught: {e}")
        print(f"   Key: {e.key}")

    # Demonstrate PermissionDeniedError
    print("\n3. Demonstrating PermissionDeniedError:")
    permissions = {
        "admin": ["read", "write", "delete"],
        "editor": ["read", "write"],
        "viewer": ["read"],
    }

    try:
        result = perform_action("admin", "delete", permissions)
        print(f"   {result}")
    except PermissionDeniedError as e:
        print(f"   Caught: {e}")

    try:
        result = perform_action("viewer", "write", permissions)
    except PermissionDeniedError as e:
        print(f"   Caught: {e}")
        print(f"   User: {e.user}, Action: {e.action}")

    # Demonstrate catching the base CustomError
    print("\n4. Demonstrating base CustomError:")
    try:
        raise CustomError("Something went wrong")
    except CustomError as e:
        print(f"   Caught: {e}")

    print("\n" + "=" * 60)
    print("All demonstrations completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()