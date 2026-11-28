class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def create_calculator(cls, a, b):
        return cls(a, b)

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator.create_calculator(10, 5)
    print(f"Add: {Calculator.add(10, 5)}")
    print(f"Subtract: {Calculator.subtract(10, 5)}")
    print(f"Multiply: {Calculator.multiply(10, 5)}")
    print(f"Divide: {Calculator.divide(10, 5)}")