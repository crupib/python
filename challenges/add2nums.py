class Solution(object):
    def twoSum(self, nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retlist = []
        for index, value in enumerate(nums):
          for jndex, jvalue in enumerate(nums):
             sum = value+jvalue
             if sum == target:
                retlist.append(index)
        return retlist
def main():
       nums = [2,7,11,15]
       two_sum = Solution()
       target = 13
       print(two_sum.twoSum(nums,target))
if __name__ == "__main__":
    main()
