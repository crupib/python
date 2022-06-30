class Solution(object):
   def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
def main():
       nums1 = [1,2,3,0,0,0]
       nums2 =  [2,5,6]
       m = 3
       n = 3
       mergeArrays = Solution()
       mergeArrays.merge(nums1, m, nums2, n)
       print(nums1)
       
if __name__ == "__main__":
    main()
        
