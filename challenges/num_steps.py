class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            if num%2 > 0:
               num=num-1
               count+=1
            else:
               num=num/2
               count+=1
             
        return count
def main():
    mynum = 123
    if mynum >= 0 and mynum <= 10**6:
       print("number of steps")
       numofsteps = Solution()
       print(numofsteps.numberOfSteps(mynum))
    else:
       print("number constrained 0 <= num <= 10^6") 
if __name__ == "__main__":
    main()
