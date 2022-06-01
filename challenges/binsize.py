import string
class Solution(object):
   def binstr(self,k,k2sq):
     getBinary = lambda x, n: format(x, 'b').zfill(n)
     binaryList = []
     for i in range(k2sq):
       binaryList.append(getBinary(i,k))
     return binaryList 
   def hasAllCodes(self,s,k,k2sq):
       found = 0
       binList = self.binstr(k,k2sq)
       for item in binList:
          found = s.find(item)
          if found == -1:
            return False
       return True    
def main():
    sol = Solution()
    k = 2
    s = "00110110"
    k2sq = 2**k
    print(sol.hasAllCodes(s,k,k2sq))
    s = "0110"
    k = 1
    k2sq = 2**k
    print(sol.hasAllCodes(s,k,k2sq))
    s = "0110"
    k = 2
    k2sq = 2**k
    print(sol.hasAllCodes(s,k,k2sq))
if __name__ == "__main__":
    main()
