class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y
def main():
  person1 = Person("Alice", 30)
  person2 = Person("Bob", 25)
  print(person1.name)
  print(person1.age)
  print(person2.name)
  print(person2.age)
  rect = Rectangle(5,3)
  print(rect.area())
  dog = Dog("Buddy")
  cat = Cat("Whiskers")
  print(dog.speak())  #Output: "Woof!"
  print(cat.speak())  #Output: "Meow!"
  bill = BankAccount(1230001,100000)
  print(bill.get_balance())
  bill.deposit(8500)
  print(bill.get_balance())
  bill.withdraw(11044)
  print(bill.get_balance())
  result1 = MathUtils.add(3, 4)
  print(result1)
  result2 = MathUtils.multiply(3, 4)
  print(result2)
if __name__ == "__main__":
    main()
