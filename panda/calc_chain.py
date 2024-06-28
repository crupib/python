class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self  # Return self to allow chaining

    def multiply(self, factor):
        self.value *= factor
        return self

    def subtract(self, amount):
        self.value -= amount
        return self


# Using the class with method chaining
result = Calculator(10).add(5).multiply(2).subtract(3).value
result2 = Calculator(4).add(3).multiply(4).subtract(2).value
print(result)
print(result2)
# 27
