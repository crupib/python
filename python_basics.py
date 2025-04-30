def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Test the function with different inputs
divide_numbers(10, 2)  # This should work fine
divide_numbers(10, 0)  # This will raise a ZeroDivisionError

x = -100
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
if x > 0:
    print("x is positive")
else:
    print("x is negative")
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
numbers = list(range(5))
print(numbers)
# Test the function with different inputs
divide_numbers(10, 2)  # This should work fine
divide_numbers(10, 0)  # This will raise a ZeroDivisionError
