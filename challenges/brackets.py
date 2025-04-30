import string
class Solution(object):
        def isValid(self, str1):          
            stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
            for parenthese in str1:
                if parenthese in pchar:
                    stack.append(parenthese)
                elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                    return False
            return len(stack) == 0
def main():
  s = "[]"
  assert len(s) >= 1 and len(s) <= 10**4, "Failed out of range"
  sol = Solution()
  print(sol.isValid(s))
if __name__ == "__main__":
    main()
