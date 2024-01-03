import os
with open("hello3.txt", 'w') as file:
     text_to_write = "Hello Files From Writing"
     file.write(text_to_write)
with open("hello3.txt", 'a') as file:
     text_to_write = "\nHello Files From Appending"
     file.write(text_to_write)
with open("hello3.txt") as file:
     print(file.read())
