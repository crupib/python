from functools import total_ordering

@total_ordering
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Create instances of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1 == person2) # False
print(person1 < person2)  # False
print(person1 <= person2) # False
print(person1 > person2)  # True
print(person1 == person3) # True
