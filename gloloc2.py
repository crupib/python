message1 = "Global Variable (shares same name as a local variable"
def myFunction():
   message1 = "Local Variable (shares the same name as a global variable)"
   print("\nINSIDE THE FUNCTION")
   print(message1)
myFunction()
print("\nOUTSIDE THE FUNCTION")
print(message1)
