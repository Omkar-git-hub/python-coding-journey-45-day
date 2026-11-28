"""
This module demonstrates the use of static methods in Python.
Static methods belong to a class but do not have access to the instance (`self`) or class (`cls`) objects.
They are useful for utility functions that logically belong to the class but do not need to modify class or instance state.
"""

class MathOperations:
    """
    A simple utility class that provides basic arithmetic operations as static methods.
    """

    @staticmethod
    def add(a, b):
        """
        Return the sum of two numbers.

        Parameters:
            a (int | float): The first operand.
            b (int | float): The second operand.

        Returns:
            int | float: The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Return the difference between two numbers.

        Parameters:
            a (int | float): The first operand.
            b (int | float): The second operand.

        Returns:
            int | float: The result of a minus b.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Return the product of two numbers.

        Parameters:
            a (int | float): The first operand.
            b (int | float): The second operand.

        Returns:
            int | float: The product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Return the quotient of two numbers.

        Parameters:
            a (int | float): The dividend.
            b (int | float): The divisor.

        Raises:
            ValueError: If the divisor is zero.

        Returns:
            float: The result of a divided by b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(base, exponent):
        """
        Return the result of raising a base to a given exponent.

        Parameters:
            base (int | float): The base value.
            exponent (int | float): The exponent value.

        Returns:
            int | float: The result of base ** exponent.
        """
        return base ** exponent

    @staticmethod
    def square(number):
        """
        Return the square of a number.

        Parameters:
            number (int | float): The number to square.

        Returns:
            int | float: The square of the number.
        """
        return number * number

    @staticmethod
    def cube(number):
        """
        Return the cube of a number.

        Parameters:
            number (int | float): The number to cube.

        Returns:
            int | float: The cube of the number.
        """
        return number * number * number

    @staticmethod
    def factorial(n):
        """
        Return the factorial of a non-negative integer.

        Parameters:
            n (int): The number to compute the factorial of.

        Raises:
            ValueError: If n is negative.

        Returns:
            int: The factorial of n.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative integers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def is_even(number):
        """
        Check if a number is even.

        Parameters:
            number (int): The number to check.

        Returns:
            bool: True if number is even, False otherwise.
        """
        return number % 2 == 0

    @staticmethod
    def is_odd(number):
        """
        Check if a number is odd.

        Parameters:
            number (int): The number to check.

        Returns:
            bool: True if number is odd, False otherwise.
        """
        return number % 2 != 0