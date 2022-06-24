class Solution(object):
    # Python3 program to
# remove duplicates
# Function to remove
# duplicate elements

# This function returns
# new size of modified
# array.
    def removeDuplicates(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      if len(nums) == 0:
         return 0
      length = 1
      previous = nums[0]
      index = 1
      for i in range(1,len(nums)):
         if nums[i] != previous:
            length += 1
            previous = nums[i]
            nums[index] = nums[i]
            index+=1
      return length
   
def main():
    count = 0
    nums = [1,1]
    sol = Solution()
    count = sol.removeDuplicates(nums)
    print(nums[0:count])

if __name__ == "__main__":
        main()
