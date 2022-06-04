import string
class Solution(object):
  def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """   
      prefixtemp = []
      precount = 0
      compre = []
      while precount < len(strs):
        for item in strs:
           prefixtemp.append(item[precount])
        ele = prefixtemp[0]
        chk = False
        for item in prefixtemp:
          if ele != item:
              chk = False
              break;
        if (chk == False) :
           prefixtemp=[]         
        else:
           compre.append(prefixtemp[0])
        precount += 1
      return compre
def main():
  strs = ["flower","flow","flight"]
  sol = Solution()
  print(sol.longestCommonPrefix(strs))
if __name__ == "__main__":
    main()
