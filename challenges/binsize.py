import string
class Solution(object):
   k2sq = 0
   def binstr(self,k,k2sq):
     getBinary = lambda x, n: format(x, 'b').zfill(n)
     binaryList = []
     for i in range(k2sq):
       binaryList.append(getBinary(i,k))
     return binaryList 
   def hasAllCodes(self,s,k):
       found = 0
       binList = self.binstr(k,self.k2sq)
       for item in binList:
          found = s.find(item)
          if found == -1:
            return False
       return True    
def main():
    sol = Solution()
    k = 2
    s = "00110110"
    sol.k2sq = 2**k
    print(sol.hasAllCodes(s,k))
    s = "0110"
    k = 1
    sol.k2sq = 2**k
    print(sol.hasAllCodes(s,k))
    s = "0110"
    k = 2
    sol.k2sq = 2**k
    print(sol.hasAllCodes(s,k))
    s = "000001010100101110011111"
    k = 3
    print(sol.hasAllCodes(s,k))
    s = "00011111"
    k = 3
    print(sol.hasAllCodes(s,k))

if __name__ == "__main__":
    main()
