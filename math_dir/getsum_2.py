def getSum(myList):
   sum=0
   for row in myList:
      for item in row:
        sum += item
   return sum

print(getSum([[1,2],[3,4],[5,6]]))
print(getSum([[1,2,3],[4,5,6],[3,9,1]]))
