def main():
  userInput = input('Enter 1 or 2: ') 
  if userInput == "1":
     print("Hello World")
     print("How are you?")
  elif userInput == "2":
     print("Python Rocks!")
     print("I love Python")
  else:
    print("you fucked up!")
  num1 = 12 if userInput=="1" else 13
  print(num1)
  print("This is task A" if userInput == "1" else "This is task B")
if __name__ == '__main__':
   main()
