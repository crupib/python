# Predefined username and password
correct_username = "admin"
correct_password = "password123"

# Function to validate login
def login_system():
    # Get username and password from user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if both username and password are correct
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login system function
login_system()
