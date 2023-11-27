def gcd_without_mod(a, b):
    while b:
        a, b = b, a - (a // b) * b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd_without_mod(num1, num2)

print(f"The GCD of {num1} and {num2} is {result}")
