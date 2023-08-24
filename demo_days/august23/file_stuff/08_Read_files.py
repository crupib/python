import os
with open("target_folder/hello.txt", 'r') as file:
     print(file.read())
with open("target_folder/hello.txt", 'r') as file:
    for i, line in enumerate(file, 1):
        print(f"* Reading line #{i}: {line}") 
