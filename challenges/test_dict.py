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
                print(values)
def main():
       nums = [1,4,6,2,7]
       two_sum = Solution()
       target = 9
       print(two_sum.twoSum(nums,target))
       junk = {}
       for x, num in enumerate(nums):
           junk[num] = x
           print(junk)
if __name__ == "__main__":
    main()
