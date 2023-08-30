from pprint import pprint
from collections import defaultdict
def main():
    print("Python Short cuts")
    pprint("List Comprehensions")
    numbers = [x for x in range(10)]
    pprint(numbers) 
    squares = {x: x*x for x in range(5)}
    pprint("Dictionary Comprehensions")
    pprint(squares)
    pprint("Multiple Assignment")
    a, b = 10, 20
    print("a = ", a)
    print("b = ",b)
    pprint("Swapping values")
    a,b = b,a
    print("a = ", a)
    print("b = ",b)
    pprint("Conditional Assignment")
    x = -5
    value = x if x > 0 else 0 
    print("value = ", value)
    print("String Formatting")
    name = '"My Boy Blue"'
    age = 67
    message = f"My Name is {name} and I am {age} years old."
    print(message)
    print("Unpacking Iterables")
    numbers = [1,2,3]
    a,b,c = numbers
    message = f"a = {a}, b = {b}, c = {c}"
    print(message)
    print("Enumerate")
    my_list = [4,9,11,3,42,26]
    for index, value in enumerate(my_list):
       print(f"Index: {index}, Value: {value}")
    print("Zip")
    names = ["Jeremy", "WillL","WillE", "Red", "Anthony", "James", "Mike", "Bill"]
    ages = [30,35,35,32,26,26,35,67]
    for name, age in zip(names,ages):
       print(f"Name: {name}, Age: {age}")
    counts = defaultdict(int)
    counts["apples"] += 1
    pprint(counts)
if __name__ == "__main__":
    main()
