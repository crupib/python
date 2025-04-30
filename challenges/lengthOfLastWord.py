class Solution(object):
   def lengthOfLastWord(self, s):
      """
      :type nums: List[int]
      :rtype: int
      """
      l = 0
      x = s.strip()
      for i in range(len(x)):
        if x[i] == " ":
          l = 0
        else:
          l += 1
      return l
def main():
  s = "   fly me   to   the moon  "
  ob1 = Solution()
  print(ob1.lengthOfLastWord(s))
  sol = Solution()  
if __name__ == "__main__":
    main()

