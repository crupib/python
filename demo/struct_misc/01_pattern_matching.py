def process_data(data):
    match data:
        case 0:
            print("Received zero")
        case [x, y]:
            print(f"Received a list: {x}, {y}")
        case {"name": name, "age": age}:
            print(f"Received a dictionary: {name}, {age}")
        case _:
            print("Received something else")
 
process_data(0)                           # Output: Received zero
process_data([1, 2])                       # Output: Received a list: 1, 2
process_data({"name": "John", "age": 25}) # Output: Received a dictionary: John, 25
process_data("Hello")                     # Output: Received something else
