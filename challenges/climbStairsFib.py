\
class Solution(object):
   def fib(self,n):
    if n <= 1:
      return n
    return self.fib(n-1) + self.fib(n-2)

   def climbStairs(self,s):
	   return self.fib(s + 1)
        

def main():
  ob1 = Solution()
  print(ob1.climbStairs(45))
if __name__ == "__main__":
    main()