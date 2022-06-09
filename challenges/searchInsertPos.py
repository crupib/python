import string
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rint = 0
        insertSpot = 0
        for idx, ele in enumerate(nums):
           if ele < target :
              insertSpot += 1
              rint = insertSpot
              continue
           elif ele == target:
              rint = idx
              break
           elif ele > target:
              rint = insertSpot
        return rint
def main():
  sol = Solution()
  nums = [1, 3, 5, 6]
  target = 5
  print(sol.searchInsert(nums,target))
  nums = [1, 3, 5, 6]
  target = 2
  print(sol.searchInsert(nums,target))
  nums = [1, 3, 5, 6]
  target = 7
  print(sol.searchInsert(nums,target))
if __name__ == "__main__":
    main()
