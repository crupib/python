def addNumbers(*num):
   sum = 0
   for i in num:
      sum = sum + i
   print(sum)

def printMemberAge(**age):
   for i, j in age.items():
     print("Name = %s, Age = %s" %(i,j))

def main():
   addNumbers(1,2,3,4,5,6,7,8)
   printMemberAge(Peter=5,John=7)
   printMemberAge(Peter=5,John=7,Yvonne=10)
if __name__ == '__main__':
   main()

