class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0: 
            return [1]
        if rowIndex == 1: 
            return [1, 1]
        if rowIndex == 2: 
            return [1, 2, 1]
        
        ans = [1] * (rowIndex + 1)
        prev = [1, 2, 1]
        
        for i in range(3, rowIndex + 1):
            for j in range(1, i):
                ans[j] = prev[j] + prev[j - 1]
            prev = ans[:]
            
        return ans
def main():
  obj = Solution()
  retval = obj.getRow(3)
  print(retval)  
if __name__ == "__main__":
    main()
        
