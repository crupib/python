message1 = "Global Variable"
def myFunction():
   print("\nINSIDE THE FUNCTION")
   print(message1)
   message2 = "Local Variable"
   print(message2)
myFunction()
print("\nOUTSIDE THE FUNCTION")
print(message1)
print(message2)
