def calculate_grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

calculate_grade(85)  # Output: Grade: B
calculate_grade(72)  # Output: Grade: C
calculate_grade(95)  # Output: Grade: A
calculate_grade(45)  # Output: Grade: F
print('\n\n')
def show_menu():
    print("Menu:")
    print("1. Pizza")
    print("2. Pasta")
    print("3. Salad")
    print("4. Burger")
    print("5. Sandwich")

def order_pizza():
    print("You ordered a pizza.")

def order_pasta():
    print("You ordered pasta.")

def order_salad():
    print("You ordered a salad.")

def order_burger():
    print("You ordered a burger.")

def order_sandwich():
    print("You ordered a sandwich.")

switch = {
    1: order_pizza,
    2: order_pasta,
    3: order_salad,
    4: order_burger,
    5: order_sandwich,
}

def take_order():
    show_menu()
    choice = int(input("Enter your choice (1-5): "))
    func = switch.get(choice)
    if func:
        func()
    else:
        print("Invalid choice.")

take_order()

# Sample Output:
# Menu:
# 1. Pizza
# 2. Pasta
# 3. Salad
# 4. Burger
# 5. Sandwich
# Enter your choice (1-5): 2
# You ordered pasta.
