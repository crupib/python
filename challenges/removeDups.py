import string
from collections import Counter
nums = [0,0,1,1,1,2,2,3,3,4]
class Solution(object):
   def removeDuplicates(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       retInt = 0
       prevVal = 999
       holdNums = []
       for value in nums:
         if value != prevVal:
           prevVal = value
           holdNums.append(value)
         else:
           prevVal = value   
       for index, value in enumerate(holdNums):
          nums[index] =  value
       for index, value in enumerate(nums):
          if index >= len(holdNums):
             nums[index]='-'
       retInt = len(holdNums)
       return retInt
def main():
  assert len(nums) >= 1 and len(nums) <= 3 * 10**4, "Failed out of range"
  for i in nums:
       assert  i >= -100 and i <= 100, "nums has a value out of range"
  sol = Solution()
  print(sol.removeDuplicates(nums))
  print(nums)

if __name__ == "__main__":
    main()
