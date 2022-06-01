import string
class Solution(object):
   def hasAllCodes(self,s,k):
     counter = 0
     if k == 2:
       found0 = s.find('00') 
       if found0 == -1
         found = False
       found1 = s.find('01')
       if found1 == -1
         found = False
       found2 = s.find('10')
       if found2 == -1
         found = False
       found3 = s.find('11')
       if found3 == -1
         found = False
        
       return found 
     counter = 0
     if k == 1:
       if s.find('0') != -1 :
          counter += 1
          found = True
       elif (s.find('1')) != -1:
          counter += 1
          found = True
       else:
          found = False
       if counter < 4:
          found = False
       return found 
           
def main():
    s = "001101100"
    sol = Solution()
    print(sol.hasAllCodes(s,2))
if __name__ == "__main__":
    main()
