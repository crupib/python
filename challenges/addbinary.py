class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        # Initialize the result
        result = ''
        # Initialize the carry
        carry = 0        
        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
        
            # Compute the carry.
            carry = 0 if r < 2 else 1
        
        if carry != 0:
            result = '1' + result
        
        return result.zfill(max_len)
def main():
  a = "11"
  b = "1"
  ob1 = Solution()
  print(ob1.addBinary(a,b))
if __name__ == "__main__":
    main()