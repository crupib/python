
class Solution(object):
   def plusOne(self,digits):
      """
       :type digits: List[int]
       :rtype: List[int]
      """
      num = ""
      for i in digits:
         num +=str(i)
      num = int(num)
      num+=1
      num = str(num)
      ans = []
      for i in num:
         ans.append(int(i))
      return ans
def main():
  #digits=[1,2,3]
  digits=[9,9]
  ob1 = Solution()
  print(ob1.plusOne(digits))
  sol = Solution()  
if __name__ == "__main__":
    main()
