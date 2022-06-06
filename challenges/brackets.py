import string
from collections import Counter
class Solution(object):
  def allEqual(self, prefixtemp):
        ele = prefixtemp[0]
        chk = True
        for item in prefixtemp:
          if ele != item:
              chk = False
              break
        return chk
  def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        braces = Counter(s)
        lcurly = (braces['{'])
        rcurly = (braces['}'])   
        lbrace = (braces[')'])
        rbrace = (braces['('])   
        lbracket = (braces['['])
        rbracket = (braces[']'])                
        if lcurly != rcurly :
            print("Fail on curly braces")
            rbool = False
        elif lbrace != rbrace :
            print("Fail on normal braces")
            rbool = False
        elif lbrace != rbrace :
            print("Fail on normal braces")
            rbool = False
        else:
            rbool = True
       
        
        return rbool
def main():
  s = "(["
  sol = Solution()
  print(sol.isValid(sorted(s)))


if __name__ == "__main__":
    main()
