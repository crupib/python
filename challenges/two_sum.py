class Solution(object):
    def twoSum(self, nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for idx, value in enumerate(nums):
            print("values",idx,values)
            print("target-value",idx,target-value)
            if target - value in values:
                print("return",values)
                print("return",idx,target-value)
                return [values[target - value], idx]
            else:
                print("past return",idx,value)
                values[value] = idx
                print(values)
def main():
       nums = [1,4,6,2,7]
       two_sum = Solution()
       target = 9
       print(two_sum.twoSum(nums,target))
if __name__ == "__main__":
    main()
