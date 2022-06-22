import math
class Solution(object):
    def rev(self,num):
       return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          self.rev(num // 10))
    def isPalindrome(self, num):
        if (num) < 0:
          return False
        if self.rev(num) == num:
          return True
        else:
          return False
def main():
    mynum = 121
    sol = Solution()
    print(sol.isPalindrone(mynum))
    mynum = -121
    print(sol.isPalindrone(mynum))
    mynum = 10
    print(sol.isPalindrone(mynum))
if __name__ == "__main__":
    main()
