def searchBinary(myList,item):
   first = 0
   last = len(myList)-1
   print("first = ", first)
   print("last = ", last)
   foundFlag = False
   while( first<=last and not foundFlag):
     mid = ( first + last) //2
     print("mid = ",mid)
     if myList[mid] == item:
         foundFlag = True
     else:
         if item < myList[mid]:
             last = mid - 1
             print("last = ", last)
         else:
            first = mid + 1
            print("first = ", first)
   return foundFlag

print(searchBinary([8,9,10,100,1000,2000,3000], 10))
print(searchBinary([8,9,10,100,1000,2000,3000], 5))
