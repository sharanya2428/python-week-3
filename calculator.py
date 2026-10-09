class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"


c = Calculator()

print("Addition:", c.add(10, 5))
print("Subtraction:", c.subtract(10, 5))
print("Multiplication:", c.multiply(10, 5))
print("Division:", c.divide(10, 0))
