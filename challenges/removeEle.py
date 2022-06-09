import string
from collections import Counter
#nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [0,1,2,2,3,0,4,2]
nums = [3,2,2,3]
class Solution(object):
   def removeElement(self, nums, val):
       """
       :type nums: List[int]
       :rtype: int
       """
       retInt = 0
       counter = 0
       for index, value in enumerate(nums):
          try: 
             idx = nums.index(val)
             nums[idx] = 999
             counter+=1
          except ValueError:
             break
       retInt = len(nums)-counter
       nums.sort()
       return retInt

def main():
  assert len(nums) >= 0 and len(nums) <= 100, "Failed out of range"
  for i in nums:
       assert  i >= 0 and i <= 50, "nums has a value out of range"
 # val = 2
  val = 3
  assert val >= 0 and val <= 100, "value out of range"
  sol = Solution()
  numelms= sol.removeElement(nums,val)
  print(nums[0:numelms])
if __name__ == "__main__":
    main()
