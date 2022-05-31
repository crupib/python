import string
class Solution(object):
   def hasAllCodes(self,s,k):
     if k == 2:
       if s.find('00') != -1 :
          found = True
       elif (s.find('01')) != -1:
          found = True
       elif s.find('10') != -1:
          found = True
       elif s.find('11') != -1:
          found = True
       else:
          found = False
       return found 
     if k == 1:
       if s.find('0') != -1 :
          found = True
       elif (s.find('1')) != -1:
          found = True
       else:
          found = False
       return found 

           
def main():
    s = "0110"
    sol = Solution()
    print(sol.hasAllCodes(s,2))
if __name__ == "__main__":
    main()
