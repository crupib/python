from wsgiref.simple_server import WSGIRequestHandler


class Solution(object):
   def climbStairs(self,n):
        
    if n == 1 or n == 2:
        return n
    
    prevPrev = 1
    prev = 2
    current = 0
    
    for step in range(3, n+1):
        # Calculate Number of Ways to Reach Current Step
        current = prevPrev + prev
        # Update Pointers for Next Step
        prevPrev = prev
        prev = current
    return current

def main():
  ob1 = Solution()
  print(ob1.climbStairs(45))
if __name__ == "__main__":
    main()