import string
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        rint = 0
        if needle == "":
          rint = 0
        else:
          rint = haystack.find(needle)
        return rint
def main():
  haystackCase = "aaaaa"
  needleCase = ""
  haystack = haystackCase.lower()
  needle = needleCase.lower()  
  assert len(haystack) >= 1, "Length is < 1"
  assert len(needle) <= 10**4, "Is not less than or = to 10**4"
  sol = Solution()
  print(sol.strStr(haystack,needle))
if __name__ == "__main__":
    main()
