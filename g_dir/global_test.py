message1 = "Global Variable"
def myFunction():
  message2 ="Local Varible"
  message1 ="Global Local Varible"
  print("\nINSIDE THE FUNCTION")
  print(message1)
  print(message2)
def main():
   myFunction()
   print("\nOUTSIDE THE FUNCTION")
   print(message1)
   try:
     print(message2)
   except NameError:
     error = False
   print("OkieDokie")
if __name__ == '__main__':
   main()

