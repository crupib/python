class Solution(object):
    def twoSum(self, nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx
def main():
       nums = [3,3]
       two_sum = Solution()
       target = 6
       print(two_sum.twoSum(nums,target))
if __name__ == "__main__":
    main()
