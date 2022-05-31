import math
class Solution(object):
    def rev(self,num):
       return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          self.rev(num // 10))
    def ispalindrone(self, num):
        if (num) < 0:
          return 0
        return self.rev(num)
def main():
    mynum = 121
    sol = Solution()
    if (sol.ispalindrone(mynum)) == mynum:
      print(mynum,"is a palindrone")
    else:
      print(mynum, "is not a palindrone")
    mynum = -121
    if (sol.ispalindrone(mynum)) == mynum:
      print(mynum,"is a palindrone")
    else:
      print(mynum, "is not a palindrone")
    mynum = 10
    if (sol.ispalindrone(mynum)) == mynum:
      print(mynum,"is a palindrone")
    else:
      print(mynum, "is not a palindrone")
if __name__ == "__main__":
    main()
