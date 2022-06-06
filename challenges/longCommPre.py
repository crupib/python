import string
class Solution(object):
  def allEqual(self, prefixtemp):
        ele = prefixtemp[0]
        chk = True
        for item in prefixtemp:
          if ele != item:
              chk = False
              break
        return chk
  def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """   
      prefixtemp = []
      precount = 0
      compre = []
      numberOfStrings = len(strs)
      while precount < numberOfStrings:
        for item in strs:
           prefixtemp.append(item[precount])
        allEqual = self.allEqual(prefixtemp)
        if allEqual == True: 
           compre.append(prefixtemp[0])
           prefixtemp = []
        else:
           prefixtemp = []
        precount += 1
      return compre
def main():
  strs = ["flower","flow","flight"]
  sol = Solution()
  print(sol.longestCommonPrefix(strs))
  strs = ["dog","racecar","car"]
  print(sol.longestCommonPrefix(strs))
  
if __name__ == "__main__":
    main()
